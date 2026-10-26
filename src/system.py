import math
import traceback
from datetime import datetime
 
from car import Car, CarType
from car_manager import car_manager
from console import console
from utils.logger import logger
 
# ---------------------------------------------------------------------------
# 주차 요금 규칙 (아직 확정 전이라 가정한 값. 바꾸려면 여기 숫자만 고치면 된다.)
#   - 외부 차량만 요금을 낸다. (입주민/특수 차량은 무료)
#   - 10분 단위로 올림해서, 10분당 260원  (화면 설계의 5시간 = 7,800원에 맞춘 값)
#   - 무료 시간은 0분
# ---------------------------------------------------------------------------
FEE_UNIT_MINUTES = 10
FEE_PER_UNIT = 260
FREE_MINUTES = 0
 
 
class System:
    def __init__(self):
        self._loaded = False  # 저장 파일을 불러왔는지
        self._load_ok = False  # 불러오기가 성공했는지 (실패했다면 종료할 때 덮어쓰지 않는다)
        self._running = False  # 프로그램이 실행 중인지


 
    def seq_start(self):
        """프로그램 시작: 저장된 차량을 불러오고, 종료할 때까지 시작 메뉴를 반복한다."""
        if not self._loaded:
            self.seq_load()
 
        self._running = True
        while self._running:
            try:
                console.show_start_menu()
                user_input = input().strip()
 
                if not (user_input.isascii() and user_input.isdecimal()):
                    console.clear()  # 글자, 빈 입력, 음수, 소수 모두 여기로 온다.
                    print("[Error] 숫자를 입력해주십시오.")
                    continue
                if int(user_input) > 3:
                    console.clear()
                    print("[Error] 0 ~ 3 사이의 정수를 입력해주십시오.")
                    continue
 
                match int(user_input):
                    case 0:
                        self.seq_end()
                    case 1:
                        console.clear()
                        self.seq_test_view()
                    case 2:
                        console.clear()
                        self.seq_manage()
                    case 3:
                        console.clear()
                        self.seq_calc()
            except (EOFError, KeyboardInterrupt):
                # Ctrl+C / Ctrl+D 로 입력이 끊긴 경우 -> 정상 종료 처리
                print()
                logger.log("입력 중 종료 신호를 받았습니다.", logger.Level.INFO)
                self.seq_end()
            except Exception as error:  # 예상하지 못한 오류로 프로그램이 꺼지지 않게 한다.
                logger.log(
                    f"예상하지 못한 오류: {error!r}\n{traceback.format_exc()}",
                    logger.Level.ERROR,
                )
                console.clear()
                print("[Error] 알 수 없는 오류가 발생했습니다. 다시 시도해주십시오.")

 
    def seq_load(self):
        """저장 파일(JSON)을 읽어서 차량 정보를 불러온다."""
        self._loaded = True
        self._load_ok = car_manager.load()
        if car_manager.last_error:
            print(f"[Error] {car_manager.last_error}")
        if car_manager.data:
            print(f"저장된 차량 {len(car_manager.data)}대를 불러왔습니다.")

 
    def seq_end(self):
        """프로그램 종료"""
        console.clear()
        if self._load_ok and not car_manager.save():
            print(f"[Error] {car_manager.last_error}")
        print("프로그램을 종료합니다.")
        logger.log("프로그램 종료", logger.Level.INFO)
        self._running = False
 
    def seq_calc(self):
        """주차 요금 계산: 차량 번호를 입력받아 최근 주차 기간과 요금을 보여준다."""
        while True:
            user_input = input().strip()
 
            if user_input == "0":
                console.clear()
                return
 
            number = "".join(user_input.split())  # 공백 제거
            if not Car.validate_number(number):
                console.clear()
                print("[Error] 차량 번호를 정확히 입력해주십시오. (예: 서울12가3456)")
                continue
 
            car = car_manager.data.get(number)
            if car is None:
                console.clear()
                print("[Error] 등록되지 않은 차량입니다.")
                continue
 
            if not car.park_in:
                console.clear()
                print("[Error] 입차 기록이 없는 차량입니다.")
                continue
 
            # 가장 최근 주차 기간: 마지막 입차 ~ (출차 또는 현재)
            start = datetime.strptime(car.park_in[-1]["time"], Car.TIME_FORMAT)
            if car.parking:
                end = datetime.now()
            else:
                end = datetime.strptime(car.park_out[-1], Car.TIME_FORMAT)
 
            seconds = (end - start).total_seconds()
            if seconds < 0:
                console.clear()
                print("[Error] 입차 시각이 현재 시각보다 늦어 계산할 수 없습니다.")
                continue
 
            total_minutes = math.ceil(seconds / 60)
            if car.type is CarType.GUEST:
                units = math.ceil(max(0, total_minutes - FREE_MINUTES) / FEE_UNIT_MINUTES)
                fee = units * FEE_PER_UNIT
            else:
                fee = 0
 
            hours, minutes = divmod(total_minutes, 60)
            if hours and minutes:
                duration_text = f"{hours}시간 {minutes}분"
            elif hours:
                duration_text = f"{hours}시간"
            else:
                duration_text = f"{minutes}분"
            if car.parking:
                duration_text += ", 주차 중"
            end_text = "현재" if car.parking else end.strftime("%Y-%m-%d %H:%M")

            
            console.clear()
            print(" ")
            print("차량 관리 시스템 - (주차 요금 계산)")
            print(" ")
            print(f"    대상: {car.number} ({car.type.value})")
            print(f"주차기간: {start.strftime('%Y-%m-%d %H:%M')} ~ {end_text} ({duration_text})")
            if car.type is CarType.GUEST:
                print(f"    요금: {fee:,}원")
            else:
                print("    요금: 무료 (외부 차량만 요금이 부과됩니다)")
            logger.log(f"요금 계산 [{car.number}] {fee}원", logger.Level.DEBUG)
            return
 

 
system = System()

import math
import re
import traceback
from datetime import datetime
 
from car import Car, CarType
from car_manager import car_manager
from console import console
from utils.logger import logger
 

 
 
class System:
    def __init__(self):

        pass


 
    def seq_start(self):
        """프로그램 시작: 저장된 차량을 불러오고, 종료할 때까지 시작 메뉴를 반복한다."""
            
 
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
        """저장 파일(JSON)을 읽어서 차량 정보를 불러옴."""
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

 
  
system = System()

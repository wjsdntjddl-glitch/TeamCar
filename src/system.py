import re
import json
from car import Car, CarType
from datetime import datetime
from car_manager import car_manager
from console import console


class System:
    def __init__(self):
        pass


###############
# 프로그램 실행 #
###############
    def seq_start(self):
        console.show_start_menu()
        user_input = input() # 문자열로 입력 받음(1,2,3도 문자열로인식)

        try:
            if not user_input.isnumeric(): # 문자열이 아니면 typeerror 발생
                raise (TypeError)

            int_input = int(user_input) # 입력값을 정수로 변환 
            if int_input < 0 or int_input > 3:
                raise (ValueError)
        
        # type에러 발생시
        except TypeError:
            console.clear()
            print("[Error] 숫자를 입력해주십시오.")
            return self.seq_start()
        
        # value에러 발생시
        except ValueError:
            console.clear()
            print("[Error] 0 ~ 3 사이의 정수를 입력해주십시오.")
            return self.seq_start()

        match int_input:
            case 0:
                console.clear()
            case 1:
                self.seq_test_view()
            case 2:
                console.clear()
                self.seq_manage()
            case 3:
                pass

################
# 주차 요금 계산 #
################
    def seq_calc(self, car):
        console.show_calc() # console.py의 어떤함수를 호출?

        # 입주민 차량과 특수 차량은 무료
        if car.car_type in (CarType.RESIDENT, CarType.SPECIAL):
            print("주차 요금이 부과되지 않습니다.")
            return

        # 입차 및 출차 기록 확인###################################굳이?
        if not car.park_in or not car.park_out:
            print("입차 또는 출차 기록이 없습니다.")
            return

        # 가장 최근 입차 및 출차 시간 사용
        park_in_time = datetime.strptime(
            car.park_in[-1]["time"], "%Y-%m-%d %H:%M:%S"
        )
        park_out_time = datetime.strptime(
            car.park_out[-1], "%Y-%m-%d %H:%M:%S"
        )


        # 총 주차 시간(분) 계산
        total_seconds = (park_out_time - park_in_time).total_seconds()
        total_minutes = int(total_seconds // 60)


        # 최초 30분 무료, 이후 5분당 300원
        if total_minutes <= 30:
            fee = 0
            print("최초 30분은 무료입니다.")
        else:
            paid_seconds = total_seconds - 30 * 60
            units = int((paid_seconds + 5 * 60 - 1) // (5 * 60))
            fee = units * 300

        print(f"총 주차 시간: {int(total_minutes)}분")
        print(f"주차요금: {fee:,}원")

        return fee


################
# 프로그램 종료 #
################
    def seq_end(self):
        console.show_end_menu()
        user_input = input()

        try:
            if not user_input.isnumeric():
                raise (TypeError)

            int_input = int(user_input)
            if int_input < 0 or int_input > 1:
                raise (ValueError)

        except TypeError:
            console.clear()
            print("[Error] 숫자를 입력해주십시오.")
            return self.seq_end()
        except ValueError:
            console.clear()
            print("[Error] 0 또는 1을 입력해주십시오.")
            return self.seq_end()

        match int_input:
            case 0:
                console.clear()
                return self.seq_start()
            case 1:
                console.clear()
                print("프로그램을 종료합니다.")


#################
# 데이터 불러오기 #
#################
    def seq_load(self):
        car_manager.load()
        print("JSON 파일을 성공적으로 불러왔습니다.")



if __name__ == "__main__":
    system = System()
    system.seq_start()

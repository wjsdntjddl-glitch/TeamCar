import json
import os

from car_manager import car_manager
from console import console


class System:
    def __init__(self):
        pass
        

    def seq_load(self):
        
        car_manager.load()

    def seq_start(self):
        # 콘솔 객체를 불러 시작 메뉴를 콘솔 화면에 출력
        # Figma - MiniProject - 화면설계서 - 시작 메뉴
        console.show_start_menu()

        # 사용자 입력 받기
        # 단, 여기서 사용자 입력을 받을때 예외 처리 필요
        # 0~3 사이 정수만 입력받아야 하며 그외 모든
        # 값들은 예외
        print("\n> ", end="")
        user_input = int(input())

        match user_input:
            case 0:  # 프로그램 종료
                return
            case 1:  # 조회 메뉴
                self.seq_view()
            case 2:  # 관리 메뉴
                self.seq_manage()
            case 3:  # 주차 요금 계산
                self.seq_calc()

    def seq_view(self):
        pass

    def seq_manage(self):  # 차량 관리
        console.show_manage_menu()
        choice = input("\n> ", end="")
            
        if choice == '1':
            self.show_manage_register()
        elif choice == '2':
            self.show_manage_modify()
        elif choice == '3':
            self.show_manage_remove()
        elif choice == '0':
            self.seq_start()
        else:
            print("올바른 번호를 입력해 주세요.")


    def seq_manage_register(self):  # 차량 정보 등록
        console.show_manage_register_1()
        car_number = input("\n> ", end="")

        if not isinstance(car_number,str) or car_number.strip():
            return print("")

        console.show_manage_register_2()
        console.show_manage_register_3()
        console.show_manage_register_4()
        console.show_manage_register_5()
        console.show_manage_register_6()

        return car_manager.save()

    def seq_manage_modify(self):  # 차량 정보 수정
        console.show_manage_modify_1()
        number1 = input("\n> ", end="")

        for car in car_manager.data:
            if car.number == number1:
                console.show_manage_modify_2(car)

                number2 = input("\n> ", end="")
                match number2:
                    case 0:  # 뒤로
                        return self.seq_manage()
                    case 1:  # 번호
                        # TODO
                        console.show_manage_modify_2_1()
                        try:
                            car.number = input("\n> ", end="")
                            print("번호 수정이 완료되었습니다.")
                        except ValueError as e:
                            print(e)

                    case 2:  # 이름
                        self.seq_manage_modify()
                    case 3:  # 연락처
                        self.seq_manage_remove()
                    case 4:  # 차종
                        self.seq_manage_remove()
                    case 5:  # 색상
                        self.seq_manage_remove()




    def seq_manage_remove(self):  # 차량 정보 삭제
        console.show_manage_remove_1()
        number = input()
        if number.strip() is not None:
            print("공백을 입력하셨습니다. 다시 입력하세요.")

        for car in car_manager.data:
            if car.number == number:
                car_manager.data.remove(car)
                print(f"[{car}] 등록 정보를 삭제 했습니다.")

                car_manager.save()

        print("차량 정보를 찾지 못했습니다.")

    def seq_calc(self):
        pass


system = System()

def main():
    pass


if __name__ == "__main__":
    main()

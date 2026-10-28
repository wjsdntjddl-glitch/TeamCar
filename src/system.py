from car import Car
from car_manager import car_manager
from console import console
from utils.logger import logger


class System:
    def __init__(self) -> None:
        pass

    @classmethod
    def get_menu_input(cls, start: int, end: int) -> int:
        """사용자 입력을 받아 정수로 변환하여 반환"""
        user_input = input()
        try:
            if not user_input.isnumeric():
                raise (TypeError)

            int_input = int(user_input)
            if int_input < start or int_input > end:
                raise (ValueError)

        except TypeError:
            return -1
        except ValueError:
            return -1

        return int_input

    def seq_load(self) -> None:
        car_manager.load()

    def seq_start(self) -> None:
        console.show_start_menu()
        input = System.get_menu_input(0, 3)

        match input:
            case -1:
                console.clear()
                print("[Error] 다시 입력하십시오.")
                self.seq_start()
            case 0:
                console.clear()
                self.seq_end()
            case 1:
                console.clear()
                self.seq_view()
            case 2:
                console.clear()
                self.seq_manage()

    def seq_end(self):
        """프로그램 종료"""
        logger.log("프로그램 종료")
        console.clear()
        print("프로그램을 종료합니다.")

    def seq_view(self):  # 차량 조회 메뉴
        console.show_view_menu()
        print("\n> ", end="")
        user_input = int(input())

        match user_input:
            case 0:  # 뒤로
                console.clear()
                self.seq_start()
            case 1:  # 차량 목록 조회
                console.clear()
                self.seq_view_all()
            case 2:  # 차량 상세 조회
                console.clear()
                self.seq_view_detail()
            case 3:  # 차량 제조회사 기준 조회
                console.clear()
                self.seq_view_by_model()
            case 4:  # 차주 이름으로 차량 조회
                console.clear()
                self.seq_view_by_name()

    def seq_view_all(self):  # 차량 목록 조회
        console.show_view_all()
        self.seq_view()

    def seq_view_detail(self):  # 차량 상세 조회
        console.show_view_detail()
        self.seq_view()

    def seq_view_by_model(self):  # 차량 제조회사 기준 조회
        console.show_view_by_model()
        self.seq_view()

    def seq_view_by_name(self):  # 차주 이름으로 차량 조회
        console.show_view_by_name()
        self.seq_view()

    def seq_manage(self):
        console.show_manage_menu()
        input = System.get_menu_input(0, 3)

        match input:
            case -1:
                console.clear()
                print("[Error] 다시 입력하십시오.")
                self.seq_manage()
            case 0:
                console.clear()
                self.seq_start()
            case 1:
                console.clear()
                self.seq_manage_register()
            case 2:
                console.clear()
                self.seq_manage_modifiy()
            case 3:
                console.clear()
                self.seq_manage_remove()

    def seq_manage_register(self) -> None:
        screen = 1
        car = Car()

        while True:
            if screen == 1:
                console.show_manage_register(1)
                try:
                    car.number = input()
                    screen = 2
                except ValueError as e:
                    console.clear()
                    print(e)

            elif screen == 2:
                console.show_manage_register(2)
                try:
                    car.name = input()
                    screen = 3
                except ValueError as e:
                    screen = 2
                    console.clear()
                    print(e)

            elif screen == 3:
                console.show_manage_register(3)
                try:
                    car.phone = input()
                    screen = 4
                except ValueError as e:
                    screen = 3
                    console.clear()
                    print(e)

            elif screen == 4:
                console.show_manage_register(4)
                try:
                    car.model = input()
                    screen = 5
                except ValueError as e:
                    screen = 4
                    console.clear()
                    print(e)

            elif screen == 5:
                console.show_manage_register(5)
                try:
                    car.color = input()
                except ValueError as e:
                    screen = 5
                    console.clear()
                    print(e)

                break

        car_manager.data.append(car)
        car_manager.save()
        console.clear()
        print("등록이 완료됐습니다.")
        self.seq_manage()

    def seq_manage_modifiy(self) -> None:
        console.show_manage_modifiy(1)
        number = input()
        car = None
        for item in car_manager.data:
            if number == item.number:
                car = item
                break

        if car is None:
            console.clear()
            print("[Error] 입력한 번호와 일치하는 차량이 없습니다.")
            self.seq_manage()
            return

        console.clear()
        console.show_manage_modifiy(2, car)
        user_input = input()
        
        print("\n수정사항을 입력하세요.\n\n> ", end="")
        while True:
            try:
                match user_input:
                    case "1":
                        car.number = input()
                    case "2":
                        car.name = input()
                    case "3":
                        car.phone = input()
                    case "4":
                        car.model = input()
                    case "5":
                        car.color = input()

                break
            except ValueError as e:
                print(e)

        car_manager.save()
        console.clear()
        print("수정이 완료됐습니다.")
        self.seq_manage()

    def seq_manage_remove(self):
        console.show_manage_remove()
        number = input()

        for car in car_manager.data:
            if car.number == number:
                car_manager.data.remove(car)
                car_manager.save()
                print(f"[{number}] 차량 등록 정보를 삭제 했습니다.")
                return


        console.clear()
        print("차량 정보를 찾지 못했습니다.")

        self.seq_manage()

system = System()
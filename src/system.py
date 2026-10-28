from car import Car
from car_manager import car_manager
from console import console


class System:
    def __init__(self):
        pass

    @classmethod
    def get_menu_input(cls, start: int, end: int) -> int:
        """
        사용자 입력을 받아 정수로 변환하여 반환
        Returns:
            int:
            -1: 범위에서 벗어나는 값 입력시 반환
        """
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
                # self.seq_manage()

    def seq_end(self):
        """프로그램 종료"""
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


system = System()

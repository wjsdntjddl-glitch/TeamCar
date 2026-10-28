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
                # self.seq_view()
            case 2:
                console.clear()
                # self.seq_manage()

    def seq_end(self):
        """프로그램 종료"""
        console.clear()
        print("프로그램을 종료합니다.")


system = System()

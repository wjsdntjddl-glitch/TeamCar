import re
from car import Car
import car_manager

from console import console
import src


class System:
    def __init__(self):
        pass

    def seq_start(self):
        console.show_start_menu()
        user_input = input()

        try:
            if not user_input.isnumeric():
                raise (TypeError)

            int_input = int(user_input)
            if int_input < 0 or int_input > 3:
                raise (ValueError)

        except TypeError:
            console.clear()
            print("[Error] 숫자를 입력해주십시오.")
            self.seq_start()
        except ValueError:
            console.clear()
            print("[Error] 0 ~ 3 사이의 정수를 입력해주십시오.")
            self.seq_start()

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

    def seq_manage(self):
        console.show_manage_menu()
        user_input = input()

        try:
            if not user_input.isnumeric():
                raise (TypeError)

            int_input = int(user_input)
            if int_input < 0 or int_input > 3:
                raise (ValueError)

        except TypeError:
            console.clear()
            print("[Error] 숫자를 입력해주십시오.")
            self.seq_manage()
        except ValueError:
            console.clear()
            print("[Error] 0 ~ 3 사이의 정수를 입력해주십시오.")
            self.seq_manage()

        match int_input:
            case 0:
                console.clear()
                self.seq_start()
            case 1:
                console.clear()
                self.seq_manage_register()
            case 2:
                pass
            case 3:
                pass

    def seq_manage_register(self) -> None:
        console.show_manage_register()
        user_input = input()
        trimmed_input = user_input.replace(" ", "")
        pattern = r"[가-힣]{2}\d{2}\d?[가-힣]\d{4}$"
        if re.fullmatch(pattern, trimmed_input) is None:
            console.clear()
            print("[Error] 차량 번호를 정확히 입력해주십시오.")
            self.seq_manage_register()

        car_manager.data[trimmed_input] = Car("이상무")
        car_manager.save()

    def seq_test_view(self):
        car_manager.load()
        print(car_manager.data["경기12나3456"].name)


if __name__ == "__main__":
    src()

system = System()
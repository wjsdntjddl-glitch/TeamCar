from car import Car
from car_manager import car_manager
from console import console
from utils.logger import logger


class System:
    def __init__(self) -> None:
        pass

    @classmethod
    def get_menu_input(cls, start: int, end: int) -> int:
        """
        사용자 입력을 받아 정수로 변환하여 반환
        Returns:
            int:
        **-1:** TypeError, ValueError <br>
        **-2:** EOFError <br>
        **-3:** KeyboardInterrupt
        """
        try:
            user_input = input()
            if not user_input.isnumeric():
                raise TypeError

            int_input = int(user_input)
            if int_input < start or int_input > end:
                raise ValueError

        except (TypeError, ValueError):
            return -1
        except EOFError:
            return -2
        except KeyboardInterrupt:
            return -3

        return int_input

    def seq_load(self) -> None:
        """JSON 파일 불러오기"""
        car_manager.load()

    def seq_start(self) -> None:
        console.show_start_menu()
        input = System.get_menu_input(0, 2)

        match input:
            case -3:
                console.clear()
                self.seq_end()
            case -1 | -2:
                console.clear()
                print(f"{console.get_fmt_err()}\n다시 입력하십시오.")
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

    def seq_end(self) -> None:
        """프로그램 종료"""
        console.clear()
        print(console.get_fmt_end())
        print("프로그램을 종료합니다.")

    def seq_view(self) -> None:
        """차량 조회 메뉴"""
        console.show_view_menu()
        print("\n> ", end="")
        input = System.get_menu_input(0, 4)

        match input:
            case -3:
                console.clear()
                self.seq_end()
            case -2:
                console.clear()
                self.seq_start()
            case -1: # 잘못된 입력
                console.clear()
                print(console.get_fmt_err() + "\n다시 입력하십시오.")
                self.seq_view()
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
                self.seq_view_by_brand()
            case 4:  # 차주 이름으로 차량 조회
                console.clear()
                self.seq_view_by_name()

    def seq_view_all(self) -> None:
        """전체 차량 목록 조회"""
        console.show_view_all()
        self.seq_view()

    def seq_view_detail(self) -> None:
        """차량 상세 조회"""
        console.show_view_detail()
        self.seq_view()

    def seq_view_by_brand(self) -> None:
        """제조 회사 입력으로 차량 조회"""
        console.show_view_by_brand()
        self.seq_view()

    def seq_view_by_name(self) -> None:
        """차주 이름으로 차량 조회"""
        console.show_view_by_name()
        self.seq_view()

    def seq_manage(self) -> None:
        """차량 관리 메뉴"""
        console.show_manage_menu()
        input = System.get_menu_input(0, 3)

        match input:
            case -3:
                console.clear()
                self.seq_end()
            case -2:
                console.clear()
                self.seq_start()
            case -1:
                console.clear()
                print(f"{console.get_fmt_err()}\n다시 입력하십시오.")
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
        """차량 등록"""
        screen = 1
        car = Car()

        while True:
            if screen == 1:
                console.show_manage_register(1)
                try:
                    number = input()
                    screen = 2
                    if car_manager.is_duplicated(number):
                        screen = 1
                        console.clear()
                        print(f"{console.get_fmt_err()}\n중복된 차량 번호 입니다.")
                        continue

                    car.number = number

                except ValueError as e:
                    screen = 1
                    console.clear()
                    print(e)
                except EOFError:
                    console.clear()
                    self.seq_manage()
                    return
                except KeyboardInterrupt:
                    console.clear()
                    self.seq_end()
                    return

            elif screen == 2:
                console.show_manage_register(2)
                try:
                    car.name = input()
                    screen = 3
                except ValueError as e:
                    screen = 2
                    console.clear()
                    print(e)
                except EOFError:
                    console.clear()
                    self.seq_manage()
                    return
                except KeyboardInterrupt:
                    console.clear()
                    self.seq_end()
                    return

            elif screen == 3:
                console.show_manage_register(3)
                try:
                    car.phone = input()
                    screen = 4
                except ValueError as e:
                    screen = 3
                    console.clear()
                    print(e)
                except EOFError:
                    console.clear()
                    self.seq_manage()
                    return
                except KeyboardInterrupt:
                    console.clear()
                    self.seq_end()
                    return

            elif screen == 4:
                console.show_manage_register(4)
                try:
                    car.brand = input()
                    screen = 5
                except ValueError as e:
                    screen = 4
                    console.clear()
                    print(e)
                except EOFError:
                    console.clear()
                    self.seq_manage()
                    return
                except KeyboardInterrupt:
                    console.clear()
                    self.seq_end()
                    return

            elif screen == 5:
                console.show_manage_register(5)
                try:
                    car.color = input()
                except ValueError as e:
                    screen = 5
                    console.clear()
                    print(e)
                except EOFError:
                    console.clear()
                    self.seq_manage()
                    return
                except KeyboardInterrupt:
                    console.clear()
                    self.seq_end()
                    return

                break

        car_manager.data.append(car)
        car_manager.save()
        console.clear()
        print(console.get_fmt_cpl())
        print("등록이 완료됐습니다.")
        logger.info(f"[{car.number}] 차량 등록 완료")
        self.seq_manage()

    def seq_manage_modifiy(self) -> None:
        """등록된 차량 요소 수정"""
        console.show_manage_modifiy(1)
        try:
            number = input()
        except EOFError:
            console.clear()
            self.seq_manage()
            return
        except KeyboardInterrupt:
            console.clear()
            self.seq_end()
            return
        
        car = None
        for item in car_manager.data:
            if number == item.number:
                car = item
                break

        if car is None:
            console.clear()
            print(f"{console.get_fmt_err()}\n입력한 번호와 일치하는 차량이 없습니다.")
            self.seq_manage()
            return

        console.clear()
        console.show_manage_modifiy(2, car)
        try:
            user_input = input()
        except EOFError:
            console.clear()
            self.seq_manage()
            return
        except KeyboardInterrupt:
            console.clear()
            self.seq_end()
            return


        match user_input:
            case "0":
                console.clear()
                self.seq_manage()
                return
            case "1" | "2" | "3" | "4" | "5":
                print("\n수정사항을 입력하세요.\n\n> ", end="")
                try:
                    new_value = input()
                except EOFError:
                    console.clear()
                    self.seq_manage()
                    return
                except KeyboardInterrupt:
                    console.clear()
                    self.seq_end()
                    return
            case _:
                print("[Error] 잘못된 입력입니다.")
                console.clear()
                self.seq_manage()
                return

        try:
            match user_input:
                case "1":
                    if car_manager.is_duplicated(new_value):
                        raise ValueError(f"{console.get_fmt_err()}\n중복된 차량 번호 입니다.")

                    old = car.number
                    car.number = new_value
                case "2":
                    old = car.name
                    car.name = new_value
                case "3":
                    old = car.phone
                    car.phone = new_value
                case "4":
                    old = car.brand
                    car.brand = new_value
                case "5":
                    old = car.color
                    car.color = new_value
        except ValueError as e:
            print(e)
            self.seq_manage()
            return

        car_manager.save()
        console.clear()
        print(console.get_fmt_cpl())
        print(f"* 이전: {old}")
        print(f"* 이후: {new_value}")
        print("[-] 수정이 완료됐습니다.\n")
        logger.info(f"'{old}' -> '{new_value}' 수정 완료")
        self.seq_manage()

    def seq_manage_remove(self) -> None:
        """등록된 차량 삭제"""
        console.show_manage_remove()
        try:
            number = input()
        except EOFError:
            console.clear()
            self.seq_manage()
            return
        except KeyboardInterrupt:
            console.clear()
            self.seq_end()
            return

        for car in car_manager.data:
            if car.number == number:
                car_manager.data.remove(car)
                car_manager.save()
                print(console.get_fmt_cpl())
                print(f"[{number}] 차량 정보를 삭제 했습니다.\n")
                logger.info(f"[{number}] 차량 정보 삭제")
                self.seq_manage()
                return

        console.clear()
        print(console.get_fmt_err())
        print("[Error] 차량 정보를 찾지 못했습니다.\n")

        self.seq_manage()


system = System()

import subprocess
import time
import msvcrt

from wcwidth import wcswidth

from car import Car
from car_manager import car_manager


class Console:
    def __init__(self):
        self.page = 1  # 현재 페이지
        self.page_size = 10  # 한 페이지에 출력할 차량 수
        self.headers = ["번호", "이름", "연락처", "차종", "색상"]
        self.widths = [
            wcswidth(header) for header in self.headers
        ]  # 각 헤더의 가로 길이

    @classmethod
    def format_phone(cls, phone: str | None) -> str | None:
        """연락처를 번호 문법에 맞춰 대시(-) 삽입"""
        if phone is not None and len(phone) == 11 and phone.isdigit():
            return f"{phone[:3]}-{phone[3:7]}-{phone[7:]}"

        return phone

    @classmethod
    def align_text(cls, text: str, width: int) -> str:
        """문자열을 유니코드 문자열의 길이에 맞춰 정렬"""
        text = str(text)
        return text + " " * max(0, width - wcswidth(text))

    def update_widths(self, cars: list[Car]) -> None:
        """헤더의 크기를 데이터의 최대 길이에 맞춰 변경"""
        for car in cars:
            values = [
                car.number,
                car.name,
                Console.format_phone(car.phone),
                car.brand,
                car.color,
            ]

            for i, value in enumerate(values):
                self.widths[i] = max(self.widths[i], wcswidth(str(value)))

    def print_row(self, values) -> None:
        """열 단위 문자열 출력"""
        self.update_widths(car_manager.data)
        result = "|"

        for i in range(len(values)):
            result += " " + self.align_text(values[i], self.widths[i]) + " |"

        print(result)

    def show_start_menu(self) -> None:
        """시작 화면"""
        print(self.get_fmt_start())
        print("차량 관리 시스템")
        print("도움말: 숫자를 입력해 메뉴에 접근합니다. ex) 조회시 1 입력")
        print(" ")
        print("0. 프로그램 종료")
        print("1. 조회")
        print("2. 관리")
        print("\n> ", end="")

    def show_view_menu(self) -> None:
        """조회 메뉴 화면"""
        print(self.get_fmt_look())
        print(" ")
        print("차량 조회 시스템")
        print("도움말: 숫자를 입력해 메뉴에 접근합니다. ex) 조회시 1 입력")
        print("0. 뒤로")
        print("1. 차량 목록 조회")
        print("2. 차량 상세 조회")
        print("3. 차량 브랜드명 기준 조회")
        print("4. 차주 이름으로 차량 조회")
        print(" ")

    def show_view_all(self) -> None:
        """전체 조회 화면"""
        self.clear()
        self.update_widths(car_manager.data)
        total = len(car_manager.data)

        total_pages = max(1, (total + self.page_size - 1) // self.page_size)

        table_width = sum(self.widths) + 3 * len(self.widths) + 1

        self.page = 1

        while True:
            print("차량 관리 시스템 - (차량 목록 조회)")
            print(f"총 {total}대 조회")
            print()

            headers = ["번호", "이름", "연락처", "브랜드", "색상"]

            self.print_row(headers)

            start = (self.page - 1) * self.page_size
            end = start + self.page_size

            page_cars = car_manager.data[start:end]

            for car in page_cars:
                values = [
                    car.number,
                    car.name,
                    self.format_phone(car.phone),
                    car.brand,
                    car.color,
                ]

                self.print_row(values)

            print()

            page_text = f"{self.page} / {total_pages} 페이지"
            space = table_width - wcswidth(page_text)
            print(" " * max(0, space) + page_text)

            print()
            print("0. 뒤로")
            print("1. 이전 페이지")
            print("2. 다음 페이지")
            print()

            try:
                choice = input("선택: ")
            except EOFError:
                self.clear()
                return
            except KeyboardInterrupt:
                self.clear()
                return
            self.clear()

            if choice == "0":
                break

            elif choice == "1":
                if self.page > 1:
                    self.page -= 1
                else:
                    print("첫 페이지입니다.")

            elif choice == "2":
                if self.page < total_pages:
                    self.page += 1
                else:
                    print("마지막 페이지입니다.")

            else:
                print(f"{self.get_fmt_err()}\n0~2 사이의 숫자만 입력할 수 있습니다.")
                time.sleep(1.5)
                self.clear()
                

    def show_view_detail(self):  # 상세 조회 화면
        print()
        print("차량 관리 시스템 - (차량 상세 조회)")
        print("도움말: 차량 번호를 입력하세요.")
        print("0. 뒤로")
        print()

        try:
            number = input("> ").strip()
        except EOFError:
            self.clear()
            return
        except KeyboardInterrupt:
            self.clear()
            return

        self.clear()

        if number == "0":
            return

        for car in car_manager.data:
            if car.number == number:
                print()
                print('-'*30)
                print(f"차량 번호 : {car.number}")
                print(f"이름      : {car.name}")
                print(f"연락처    : {self.format_phone(car.phone)}")
                print(f"차종      : {car.brand}")
                print(f"색상      : {car.color}")
                print('-'*30)
                print("\n이전으로 돌아가려면 아무키나 누르십시오.")
                msvcrt.getch()
                self.clear()
                return

        print()
        print(f"{self.get_fmt_err()}\n해당 차량 번호를 찾을 수 없습니다.")
        time.sleep(1.5)
        self.clear()

    def show_view_by_brand(self):  # 차량 브랜드명 기준 조회 화면
        print()
        print("차량 관리 시스템 - (차량 브랜드 기준 조회)")
        print("도움말: 조회할 차량 브랜드명을 입력하세요.")
        print("0. 뒤로")
        print()

        try:
            brand = input("> ").strip()
        except EOFError:
            self.clear()
            return
        except KeyboardInterrupt:
            self.clear()
            return
        self.clear()

        if brand == "0":
            return

        result = []

        for car in car_manager.data:
            if car.brand == brand:
                result.append(car)

        print()
        print(f"총 {len(result)}대 조회")
        print()

        if len(result) == 0:
            print(f"{self.get_fmt_err()}해당 브랜드의 차량이 없습니다.")
            time.sleep(1.5)
            self.clear()
            return

        headers = ["번호", "이름", "연락처", "차종", "색상"]

        self.print_row(headers)

        for car in result:
            values = [
                car.number,
                car.name,
                self.format_phone(car.phone),
                car.brand,
                car.color,
            ]

            self.print_row(values)

        print("\n이전으로 돌아가려면 아무키나 누르십시오.")
        msvcrt.getch()
        self.clear()


    def show_view_by_name(self):  # 차주 이름으로 차량 조회 화면
        print()
        print("차량 관리 시스템 - (차주 이름으로 차량 조회)")
        print("도움말: 조회할 차주 이름을 입력하세요.")
        print("0. 뒤로")
        print()

        try:
            name = input("> ").strip()
        except EOFError:
            self.clear()
            return
        except KeyboardInterrupt:
            self.clear()
            return
        self.clear()

        if name == "0":
            return

        result = []

        for car in car_manager.data:
            if car.name == name:
                result.append(car)

        print()
        print(f"총 {len(result)}대 조회")
        print()

        if len(result) == 0:
            print(f"{self.get_fmt_err()}\n해당 이름의 차주가 없습니다.")
            time.sleep(1.5)
            self.clear()
            return

        headers = ["번호", "이름", "연락처", "차종", "색상"]

        self.print_row(headers)

        for car in result:
            values = [
                car.number,
                car.name,
                self.format_phone(car.phone),
                car.brand,
                car.color,
            ]

            self.print_row(values)

        print("\n이전으로 돌아가려면 아무키나 누르십시오.")
        msvcrt.getch()
        self.clear()

    def clear(self) -> None:
        """콘솔 화면 초기화"""
        subprocess.run("cls", shell=True, check=False)

    def show_manage_menu(self) -> None:
        print(self.get_fmt_mgt())
        print(" ")
        print("차량 관리 시스템 - (관리)")
        print("도움말: 숫자를 입력해 메뉴에 접근합니다. ex) 차량 정보 등록시 1 입력")
        print(" ")
        print("0. 뒤로")
        print("1. 차량 정보 등록")
        print("2. 차량 정보 수정")
        print("3. 차량 정보 삭제")
        print("\n> ", end="")

    def show_manage_register(self, screen: int) -> None:
        match screen:
            case 1:
                print(" ")
                print("차량 관리 시스템 - (차량 정보 등록)")
                print("도움말: 차량 번호를 입력하세요")
                print(" ")
                print("\n> ", end="")
            case 2:
                print(" ")
                print("차량 관리 시스템 - (차량 정보 등록)")
                print("도움말: 차량 소유자 이름을 입력하세요")
                print(" ")
                print("\n> ", end="")
            case 3:
                print(" ")
                print("차량 관리 시스템 - (차량 정보 등록)")
                print("도움말: 연락처를 입력하세요")
                print(" ")
                print("> ", end="")
            case 4:
                print(" ")
                print("차량 관리 시스템 - (차량 정보 등록)")
                print("도움말: 차량 브랜드명을 입력하세요")
                print(" ")
                print("> ", end="")
            case 5:
                print(" ")
                print("차량 관리 시스템 - (차량 정보 등록)")
                print("도움말: 차량 색상을 입력하세요")
                print(" ")
                print("> ", end="")

    def show_manage_modifiy(self, screen: int, car: Car | None = None) -> None:
        if screen == 1:
            print(" ")
            print("차량 관리 시스템 - (차량 정보 수정)")
            print("도움말: 차량 번호를 입력하세요")
            print(" ")
            print("\n> ", end="")
        elif screen == 2:
            print(" ")
            print("차량 관리 시스템 - (차량 정보 수정)")
            print("도움말: 숫자를 입력해 수정할 사항을 선택하세요")
            print(" ")
            print("0. 뒤로")
            print("1. 번호")
            print("2. 이름")
            print("3. 연락처")
            print("4. 차종")
            print("5. 색상")
            print("\n> ", end="")

    def show_manage_remove(self):
        """차량 정보 삭제 화면"""
        print("\n차량 관리 시스템 - (차량 정보 삭제)")
        print("도움말: 차량 번호를 입력하세요")
        print("\n> ", end="")

    def get_fmt_err(self) -> str:
        """Formatted Error 문자열 리터럴 반환"""
        return r"""
  ______ 
 |  ____|
 | |__   _ __ _ __ ___  _ __ 
 |  __| | '__| '__/ _ \| '__|
 | |____| |  | | | (_) | |   
 |______|_|  |_|  \___/|_|
"""

    def get_fmt_cpl(self) -> str:
        """Formatted Completed 문자열 리터럴 반환"""
        return r"""
   _____                      _      _       _ 
  / ____|                    | |    | |     | |
 | |     ___  _ __ ___  _ __ | | ___| |_ ___| |
 | |    / _ \| '_ ` _ \| '_ \| |/ _ \ __/ _ \ |
 | |___| (_) | | | | | | |_) | |  __/ ||  __/_|
  \_____\___/|_| |_| |_| .__/|_|\___|\__\___(_)
                       | |                     
                       |_|                     
"""

    def get_fmt_mgt(self) -> str:
        """Formatted Management 문자열 리터럴 반환"""
        return r"""
 /$$      /$$                                                                                       /$$
| $$$    /$$$                                                                                      | $$
| $$$$  /$$$$  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$$$$$$  /$$$$$$
| $$ $$/$$ $$ |____  $$| $$__  $$ |____  $$ /$$__  $$ /$$__  $$| $$_  $$_  $$ /$$__  $$| $$__  $$|_  $$_/
| $$  $$$| $$  /$$$$$$$| $$  \ $$  /$$$$$$$| $$  \ $$| $$$$$$$$| $$ \ $$ \ $$| $$$$$$$$| $$  \ $$  | $$
| $$\  $ | $$ /$$__  $$| $$  | $$ /$$__  $$| $$  | $$| $$_____/| $$ | $$ | $$| $$_____/| $$  | $$  | $$ /$$
| $$ \/  | $$|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$| $$  | $$  |  $$$$/
|__/     |__/ \_______/|__/  |__/ \_______/ \____  $$ \_______/|__/ |__/ |__/ \_______/|__/  |__/   \___/ 
                                            /$$  \ $$
                                           |  $$$$$$/
                                            \______/
"""

    def get_fmt_look(self) -> str:
        """Formatted Lookup To Car 문자열 리터럴 반환"""
        return r"""
 /$$                           /$$                                   /$$                      /$$$$$$
| $$                          | $$                                  | $$                     /$$__  $$
| $$        /$$$$$$   /$$$$$$ | $$   /$$ /$$   /$$  /$$$$$$        /$$$$$$    /$$$$$$       | $$  \__/  /$$$$$$   /$$$$$$
| $$       /$$__  $$ /$$__  $$| $$  /$$/| $$  | $$ /$$__  $$      |_  $$_/   /$$__  $$      | $$       |____  $$ /$$__  $$
| $$      | $$  \ $$| $$  \ $$| $$$$$$/ | $$  | $$| $$  \ $$        | $$    | $$  \ $$      | $$        /$$$$$$$| $$  \__/
| $$      | $$  | $$| $$  | $$| $$_  $$ | $$  | $$| $$  | $$        | $$ /$$| $$  | $$      | $$    $$ /$$__  $$| $$
| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$ \  $$|  $$$$$$/| $$$$$$$/        |  $$$$/|  $$$$$$/      |  $$$$$$/|  $$$$$$$| $$
|________/ \______/  \______/ |__/  \__/ \______/ | $$____/          \___/   \______/        \______/  \_______/|__/
                                                  | $$
                                                  | $$
                                                  |__/
"""

    def get_fmt_start(self) -> str:
        """Formatted CarNumberPlz 문자열 리터럴 반환"""
        return r"""
  /$$$$$$                            /$$   /$$                         /$$                                 /$$$$$$$  /$$
 /$$__  $$                          | $$$ | $$                        | $$                                | $$__  $$| $$
| $$  \__/  /$$$$$$   /$$$$$$       | $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$       | $$  \ $$| $$ /$$$$$$$$
| $$       |____  $$ /$$__  $$      | $$ $$ $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$      | $$$$$$$/| $$|____ /$$/
| $$        /$$$$$$$| $$  \__/      | $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/      | $$____/ | $$   /$$$$/
| $$    $$ /$$__  $$| $$            | $$\  $$$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$            | $$      | $$  /$$__/
|  $$$$$$/|  $$$$$$$| $$            | $$ \  $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$            | $$      | $$ /$$$$$$$$
 \______/  \_______/|__/            |__/  \__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/            |__/      |__/|________/
"""

    def get_fmt_end(self) -> str:
        """Formatted ThankYou SeeYouLater 문자열 리터럴 반환"""
        return r"""
    _______ _                 _
   |__   __| |               | |
      | |  | |__   __ _ _ __ | | __   _   _  ___  _   _
      | |  | '_ \ / _` | '_ \| |/ /  | | | |/ _ \| | | |
      | |  | | | | (_| | | | |   <   | |_| | (_) | |_| |
      |_|  |_| |_|\__,_|_| |_|_|\_\   \__, |\___/ \__,_|
   _____                               __/ |       _
  / ____|                             |___/ |     | |
 | (___   ___  ___    _   _  ___  _   _   | | __ _| |_ ___ _ __
  \___ \ / _ \/ _ \  | | | |/ _ \| | | |  | |/ _` | __/ _ \ '__|
  ____) |  __/  __/  | |_| | (_) | |_| |  | | (_| | ||  __/ |
 |_____/ \___|\___|   \__, |\___/ \__,_|  |_|\__,_|\__\___|_|
                       __/ |
                      |___/
"""


console = Console()

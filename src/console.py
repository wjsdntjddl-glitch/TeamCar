import subprocess

from wcwidth import wcswidth

from car import Car
from car_manager import car_manager


class Console:
    def __init__(self):
        self.page = 1  # 현재 페이지
        self.page_size = 10  # 한 페이지에 출력할 차량 수
        self.widths = [4, 4, 6, 4, 4]

    def update_widths(self):
        headers = ["번호", "이름", "연락처", "차종", "색상"]

        self.widths = [wcswidth(header) for header in headers]

        for car in car_manager.data:
            values = [car.number, car.name, self.format_phone(car.phone), car.brand, car.color]

            for i, value in enumerate(values):
                self.widths[i] = max(self.widths[i], wcswidth(str(value)))

    def format_phone(self,phone):
        phone = str(phone).replace('-','')

        if len(phone) == 11 and phone.isdigit():
            return f'{phone[:3]}-{phone[3:7]}-{phone[7:]}'

        return phone

    def align_text(self, text, width):
        text = str(text)
        return text + " " * max(0, width - wcswidth(text))

    def print_row(self, values):
        self.update_widths()
        result = "|"

        for i in range(len(values)):
            result += " " + self.align_text(values[i], self.widths[i]) + " |"

        print(result)

    def show_start_menu(self) -> None:
        """시작 화면"""
        print(" ")
        print("차량 관리 시스템")
        print("도움말: 숫자를 입력해 메뉴에 접근합니다. ex) 조회시 1 입력")
        print(" ")
        print("0. 프로그램 종료")
        print("1. 조회")
        print("2. 관리")
        print("\n> ", end="")

    def show_view_menu(self):  # 조회 메뉴 화면
        print(" ")
        print("차량 관리 시스템")
        print("도움말: 숫자를 입력해 메뉴에 접근합니다. ex) 조회시 1 입력")
        print("0. 뒤로")
        print("1. 차량 목록 조회")
        print("2. 차량 상세 조회")
        print("3. 차량 제조회사 기준 조회")
        print("4. 차주 이름으로 차량 조회")
        print(" ")

    def show_view_all(self):  # 전체 조회 화면
        self.clear()
        self.update_widths()
        total = len(car_manager.data)

        total_pages = max(1, (total + self.page_size - 1) // self.page_size)

        table_width = sum(self.widths) + 3 * len(self.widths) + 1

        self.page = 1

        while True:
            print("차량 관리 시스템 - (차량 목록 조회)")
            print(f"총 {total}대 조회")
            print()

            headers = ["번호", "이름", "연락처", "차종", "색상"]

            self.print_row(headers)

            start = (self.page - 1) * self.page_size
            end = start + self.page_size

            page_cars = car_manager.data[start:end]

            for car in page_cars:
                values = [car.number, car.name, self.format_phone(car.phone), car.brand, car.color]

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

            choice = input("선택: ")
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
                print("잘못된 입력입니다.")

    def show_view_detail(self):  # 상세 조회 화면
        print()
        print("차량 관리 시스템 - (차량 상세 조회)")
        print("도움말: 차량 번호를 입력하세요.")
        print("0. 뒤로")
        print()

        number = input("> ").strip()
        console.clear()

        if number == "0":
            return

        for car in car_manager.data:
            if car.number == number:
                print()
                print(f"차량 번호 : {car.number}")
                print(f"이름      : {car.name}")
                print(f"연락처    : {self.format_phone(car.phone)}")
                print(f"차종      : {car.brand}")
                print(f"색상      : {car.color}")
                print()
                return

        print()
        print("해당 차량 번호를 찾을 수 없습니다.")

    def show_view_by_brand(self):  # 차량 제조회사 기준 조회 화면
        print()
        print("차량 관리 시스템 - (차량 제조회사 기준 조회)")
        print("도움말: 조회할 차량 제조회사를 입력하세요.")
        print("0. 뒤로")
        print()

        brand = input("> ").strip()
        console.clear()

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
            print("해당 제조회사의 차량이 없습니다.")
            return

        headers = ["번호", "이름", "연락처", "차종", "색상"]

        self.print_row(headers)

        for car in result:
            values = [car.number, car.name, self.format_phone(car.phone), car.brand, car.color]

            self.print_row(values)

    def show_view_by_name(self):  # 차주 이름으로 차량 조회 화면
        print()
        print("차량 관리 시스템 - (차주 이름으로 차량 조회)")
        print("도움말: 조회할 차주 이름을 입력하세요.")
        print("0. 뒤로")
        print()

        name = input("> ").strip()
        console.clear()

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
            print("해당 이름의 차주가 없습니다.")
            return

        headers = ["번호", "이름", "연락처", "차종", "색상"]

        self.print_row(headers)

        for car in result:
            values = [car.number, car.name, self.format_phone(car.phone), car.brand, car.color]

            self.print_row(values)

    def clear(self) -> None:
        """콘솔 화면 초기화"""
        subprocess.run("cls", shell=True, check=False)

    def show_manage_menu(self) -> None:
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
                print("도움말: 차량 제조 회사를 입력하세요")
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


console = Console()

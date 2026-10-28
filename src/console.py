
from wcwidth import wcswidth

class Console:
    def __init__(self):

        # JSON 데이터를 Car 객체로 변환
        self.cars = []

        self.page = 1  # 현재 페이지
        self.page_size = 3  # 한 페이지에 출력할 차량 수
        self.widths = [4, 4, 6, 4, 4]
    def update_widths(self):
        headers = ["번호", "이름", "연락처", "차종", "색상"]

        self.widths = [wcswidth(header) for header in headers]

        for car in self.cars:
            values = [
                car.number,
                car.name,
                car.phone,
                car.model,
                car.color
            ]

            for i, value in enumerate(values):
                self.widths[i] = max(
                    self.widths[i],
                    wcswidth(str(value))
                )

    def align_text(self, text, width):
        text = str(text)
        return text + " " * max(0, width - wcswidth(text))

    def print_row(self, values):
        self.update_widths()
        result = "|"

        for i in range(len(values)):
            result += " " + self.align_text(
                values[i], self.widths[i]
            ) + " |"

        print(result)
    
    def show_start_menu(self):
        print(" ")
        print("차량 관리 시스템")
        print("도움말: 숫자를 입력해 메뉴에 접근합니다. ex) 조회시 1 입력")
        print(" ")
        print("0. 프로그램 종료")
        print("1. 조회")
        print("2. 관리")
        print("3. 계산")

    def show_view_menu(self): # 조회 메뉴 화면
        print(" ")
        print("차량 관리 시스템")
        print("도움말: 숫자를 입력해 메뉴에 접근합니다. ex) 조회시 1 입력")
        print("0. 뒤로")
        print("1. 차량 목록 조회")
        print("2. 차량 상세 조회")
        print("3. 차량 제조회사 기준 조회")
        print("4. 차주 이름으로 차량 조회")
        # print("5. 입차 차량 조회 (시간별)")
        print(" ")

    def show_view_all(self): # 전체 조회 화면
        self.update_widths()
        total = len(self.cars)

        total_pages = max(
            1, (total + self.page_size - 1) // self.page_size
        )

        table_width = sum(self.widths) + 3 * len(self.widths) + 1

        self.page = 1

        while True:
            print("\n" * 2)
            print("차량 관리 시스템 - (차량 목록 조회)")
            print(f"총 {total}대 조회")
            print()

            headers = [
                "번호", "이름", "연락처", "차종",
                "색상" #, "상태", "외부 차량"
            ]

            self.print_row(headers)

            start = (self.page - 1) * self.page_size
            end = start + self.page_size

            page_cars = self.cars[start:end]

            for car in page_cars:
                values = [
                    car.number,
                    car.name,
                    car.phone,
                    car.model,
                    car.color,
                    # "입차" if car.parking else "출차",
                    # "N" if car.type == "입주민" else "Y"
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

            choice = input("선택: ")

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


    def show_view_detail(self): # 상세 조회 화면
        print()
        print("차량 관리 시스템 - (차량 상세 조회)")
        print("도움말: 차량 번호를 입력하세요.")
        print("0. 뒤로")
        print()

        number = input("> ").strip()

        if number == "0":
            return

        for car in self.cars:
            if car.number == number:
                print()
                print(f"차량 번호 : {car.number}")
                print(f"이름      : {car.name}")
                print(f"연락처    : {car.phone}")
                print(f"차종      : {car.model}")
                print(f"색상      : {car.color}")
                # print(f"상태      : {'입차' if car.parking else '출차'}")
                # print(f"외부 차량 : {'N' if car.type == '입주민' else 'Y'}")
                # print(f"차량 구분 : {car.type}")
                # print(f"입차 시간 : {car.park_in}")
                # print(f"출차 시간 : {car.park_out if car.park_out else '-'}")
                print()
                return

        print()
        print("해당 차량 번호를 찾을 수 없습니다.")

    def show_view_by_model(self): # 차량 제조회사 기준 조회 화면
        print()
        print("차량 관리 시스템 - (차량 제조회사 기준 조회)")
        print("도움말: 조회할 차량 제조회사를 입력하세요.")
        print("0. 뒤로")
        print()

        model = input("> ").strip()

        if model == "0":
            return

        result = []

        for car in self.cars:
            if car.model == model:
                result.append(car)

        print()
        print(f"총 {len(result)}대 조회")
        print()

        if len(result) == 0:
            print("해당 제조회사의 차량이 없습니다.")
            return

        headers = [
            "번호", "이름", "연락처", "차종",
            "색상" #, "상태", "외부 차량"
        ]

        self.print_row(headers)

        for car in result:
            values = [
                car.number,
                car.name,
                car.phone,
                car.model,
                car.color,
                # "입차" if car.parking else "출차",
                # "N" if car.type == "입주민" else "Y"
            ]

            self.print_row(values)

    def show_view_by_name(self): # 차주 이름으로 차량 조회 화면
        print()
        print("차량 관리 시스템 - (차주 이름으로 차량 조회)")
        print("도움말: 조회할 차주 이름을 입력하세요.")
        print("0. 뒤로")
        print()

        name = input("> ").strip()

        if name == "0":
            return

        result = []

        for car in self.cars:
            if car.name == name:
                result.append(car)

        print()
        print(f"총 {len(result)}대 조회")
        print()

        if len(result) == 0:
            print("해당 이름의 차주가 없습니다.")
            return

        headers = [
            "번호", "이름", "연락처", "차종",
            "색상" #, "상태", "외부 차량"
        ]

        self.print_row(headers)

        for car in result:
            values = [
                car.number,
                car.name,
                car.phone,
                car.model,
                car.color,
                # "입차" if car.parking else "출차",
                # "N" if car.type == "입주민" else "Y"
            ]

            self.print_row(values)


    
    
    # def show_view_entered_between(self): # 입차 차량 조회 화면
    #     from datetime import datetime

    #     print()
    #     print("차량 관리 시스템 - (입차/출차 시간별 조회)")
    #     print("도움말: 조회할 시작 시간과 종료 시간을 입력하세요.")
    #     print("입력 형식: YYYY-MM-DD HH:MM")
    #     print("0. 뒤로")
    #     print()

    #     start_input = input("시작 시간 > ").strip()

    #     if start_input == "0":
    #         return

    #     end_input = input("종료 시간 > ").strip()

    #     if end_input == "0":
    #         return

    #     try:
    #         start_time = datetime.strptime(
    #             start_input, "%Y-%m-%d %H:%M"
    #         )
    #         end_time = datetime.strptime(
    #             end_input, "%Y-%m-%d %H:%M"
    #         )
    #     except ValueError:
    #         print("시간 형식이 올바르지 않습니다.")
    #         input("엔터를 누르면 돌아갑니다.")
    #         return

    #     if start_time > end_time:
    #         print("시작 시간이 종료 시간보다 늦을 수 없습니다.")
    #         input("엔터를 누르면 돌아갑니다.")
    #         return

    #     result = []

    #     for car in cars:
    #         # 입차 시간 확인
    #         if car.park_in:
    #             park_in_time = datetime.strptime(
    #                 car.park_in, "%Y-%m-%d %H:%M"
    #             )

    #             if start_time <= park_in_time <= end_time:
    #                 result.append((park_in_time, "입차", car))

    #         # 출차 시간 확인
    #         if car.park_out:
    #             park_out_time = datetime.strptime(
    #                 car.park_out, "%Y-%m-%d %H:%M"
    #             )

    #             if start_time <= park_out_time <= end_time:
    #                 result.append((park_out_time, "출차", car))

    #     # 발생 시간순 정렬
    #     result.sort(key=lambda item: item[0])

    #     print()
    #     print("차량 관리 시스템 - (입차/출차 시간별 조회)")
    #     print(f"조회 기간: {start_input} ~ {end_input}")
    #     print(f"총 {len(result)}건 조회")
    #     print()

    #     if len(result) == 0:
    #         print("해당 시간대의 입차/출차 기록이 없습니다.")
    #     else:
    #         for event_time, event_type, car in result:
    #             print(
    #                 f"[{event_type}] "
    #                 f"{event_time.strftime('%Y-%m-%d %H:%M')} "
    #                 f"| {car.number} "
    #                 f"| {car.name} "
    #                 f"| {car.model}"
    #             )

    #     print()
    #     input("엔터를 누르면 조회 메뉴로 돌아갑니다.")
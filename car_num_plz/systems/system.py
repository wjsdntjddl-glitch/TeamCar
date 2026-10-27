from models.manager import CarManager
from views.console import Console


class System:
    """전체 흐름을 제어하는 시스템 클래스"""

    def __init__(self):
        self.manager = CarManager()

    def run(self):
        """메인 실행 루프"""
        while True:
            choice = Console.show_main_menu()

            if choice == "1":  # 조회 분기
                self.handle_search()
            elif choice == "2":  # 관리 분기
                self.handle_manage()
            elif choice == "3":  # 요금 계산 분기
                car_no = input("요금을 계산할 차량 번호를 입력하세요: ").strip()
                success, msg = self.manager.calculate_fee(car_no)
                Console.display_message(success, msg)
            elif choice == "4":  # 프로그램 종료
                print("\n프로그램을 종료합니다.")
                break
            else:
                Console.display_message(False, "올바른 메뉴 번호를 입력해주세요.")

    def handle_search(self):
        """조회 하위 메뉴 처리"""
        while True:
            sub_choice = Console.show_search_menu()
            if sub_choice == "1":
                cars = self.manager.get_all_cars()
                Console.display_car_list(cars)
            elif sub_choice == "2":
                num = input("조회할 차량 번호: ").strip()
                car = self.manager.get_car_detail(num)
                Console.display_car_list([car] if car else [])
            elif sub_choice == "3":
                brand = input("조회할 제조회사(예: 현대): ").strip()
                cars = self.manager.get_cars_by_brand(brand)
                Console.display_car_list(cars)
            elif sub_choice == "4":
                owner = input("조회할 차주 이름: ").strip()
                cars = self.manager.get_cars_by_owner(owner)
                Console.display_car_list(cars)
            elif sub_choice == "5":
                try:
                    start = int(input("시작 시간 (0~23시): "))
                    end = int(input("종료 시간 (0~23시): "))
                    cars = self.manager.get_cars_by_time(start, end)
                    Console.display_car_list(cars)
                except ValueError:
                    Console.display_message(False, "숫자로 정확히 입력해주세요.")
            elif sub_choice == "0":
                break
            else:
                Console.display_message(False, "잘못된 선택입니다.")

    def handle_manage(self):
        """관리 하위 메뉴 처리"""
        while True:
            sub_choice = Console.show_manage_menu()
            if sub_choice == "1":
                num = input("차량 번호: ").strip()
                owner = input("차주 이름: ").strip()
                brand = input("제조회사: ").strip()
                success, msg = self.manager.register_car(num, owner, brand)
                Console.display_message(success, msg)
            elif sub_choice == "2":
                num = input("수정할 차량 번호: ").strip()
                owner = input("새로운 차주 이름: ").strip()
                brand = input("새로운 제조회사: ").strip()
                success, msg = self.manager.update_car(num, owner, brand)
                Console.display_message(success, msg)
            elif sub_choice == "3":
                num = input("삭제(출차)할 차량 번호: ").strip()
                success, msg = self.manager.delete_car(num)
                Console.display_message(success, msg)
            elif sub_choice == "0":
                break
            else:
                Console.display_message(False, "잘못된 선택입니다.")

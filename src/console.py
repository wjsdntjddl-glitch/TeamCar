
class Console:
    def __init__(self, system_instance):
        self.system = system_instance  # System 객체와 연결

    def show_start_menu(self):
        """시작 화면"""
        while True:
            print("\n차량 관리 시스템")
            print("도움말: 숫자를 입력해 메뉴에 접근합니다. ex) 조회시 1 입력")
            print("\n0. 프로그램 종료")
            print("1. 조회")
            print("2. 관리")
            print("3. 계산")
            
            choice = input("\n> ", end="")
            if choice == '1':
                self.show_view_menu()
            elif choice == '2':
                self.show_manage_menu()
            elif choice == '3':
                self.show_calc()
            elif choice == '0':
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 선택해 주세요.")

    def show_manage_menu(self):
        """관리 메뉴 화면"""
        while True:
            print("\n차량 관리 시스템 - (관리)")
            print("도움말: 숫자를 입력해 메뉴에 접근합니다. ex) 차량 정보 등록시 1 입력")
            print("\n0. 뒤로")
            print("1. 차량 정보 등록")
            print("2. 차량 정보 수정")
            print("3. 차량 정보 삭제")
            
            choice = input("\n> ", end="")
            
            if choice == '1':
                self.show_manage_register()
            elif choice == '2':
                self.show_manage_modify()
            elif choice == '3':
                self.show_manage_remove()
            elif choice == '0':
                self.show_start_menu()
                break
            else:
                print("올바른 번호를 입력해 주세요.")

    def show_manage_register(self):
        """차량 등록 화면"""
        print("\n차량 관리 시스템 - (차량 정보 등록)")
        number = input(
            "도움말: 차량 번호를 입력하세요"
            "\n> ", end=""
        )
        name = input(
            "도움말: 차량 소유자 이름을 입력하세요"
            "\n> ", end=""
        )
        phone = input(
            "도움말: 연락처를 입력하세요"
            "\n> ", end=""
        )
        model = input(
            "도움말: 차량 제조회사를 입력하세요"
            "\n> ", end=""
        )
        color = input(
            "도움말: 색상을 입력하세요"
            "\n> ", end=""
        )
        
        # System 클래스에 등록 요청 전달
        self.system.register_car(number, name, phone, model, color)

    def show_manage_modify(self):
        """차량 정보 수정 화면"""
        print("\n차량 관리 시스템 - (차량 정보 수정)")
        print("도움말: 차량 번호를 입력하세요")
        
        car_number = input("> ")
        
        # 1. 시스템을 통해 해당 차량 정보 검색 (없을 경우 예외 처리 가능)
        car_data = self.system.find_car_by_number(car_number)

        if not car_data:
            print(f"[오류] '{car_number}'에 해당하는 차량 정보를 찾을 수 없습니다.")
            return

        while True:
            print("\n차량 관리 시스템 - (차량 정보 수정)")
            print("도움말: 숫자를 입력해 수정할 사항을 선택하세요")
            
            # 차량 정보 표 형태 출력
            print(f"\n|   번호   |   이름   |      연락처      |   차종   |   색상   |   상태   | 외부 차량 |")
            print(f"| {car_data['number']} | {car_data['name']} | {car_data['phone']} | {car_data['model']} | {car_data['color']} | {car_data['status']} |     {car_data['is_external']}     |")
            print("\n0. 뒤로")
            print("1. 번호")
            print("2. 이름")
            print("3. 연락처")
            print("4. 차종")
            print("5. 색상")
            
            choice = input("선택: ")
            
            if choice == '0':
                print("이전 메뉴로 돌아갑니다.")
                break
            elif choice == '1':
                new_val = input("수정할 번호 입력: ")
                self.system.seq_manage_modify(car_number, field="number", value=new_val)
                car_data['number'] = new_val  # 화면 갱신용
            elif choice == '2':
                new_val = input("수정할 이름 입력: ")
                self.system.seq_manage_modify(car_number, field="name", value=new_val)
                car_data['name'] = new_val
            elif choice == '3':
                new_val = input("수정할 연락처 입력: ")
                self.system.seq_manage_modify(car_number, field="phone", value=new_val)
                car_data['phone'] = new_val
            elif choice == '4':
                new_val = input("수정할 차종 입력: ")
                self.system.seq_manage_modify(car_number, field="model", value=new_val)
                car_data['model'] = new_val
            elif choice == '5':
                new_val = input("수정할 색상 입력: ")
                self.system.seq_manage_modify(car_number, field="color", value=new_val)
                car_data['color'] = new_val
            else:
                print("잘못된 입력입니다. 올바른 번호를 선택해 주세요.")

    def show_manage_remove(self):
        """차량 정보 삭제 화면"""
        print("\n차량 관리 시스템 - (차량 정보 삭제)")
        number = input(
            "도움말: 차량 번호를 입력하세요"
            "\n> ", end=""
        )
        
        self.system.remove_car(number)

    def show_calc(self):
        pass

    def show_view_menu(self):
        """조회 메뉴 화면 (다른 팀원분 영역과 연동되는 부분 예시)"""
        # 예시 구현
        print("\n[조회 메뉴로 이동합니다...]")
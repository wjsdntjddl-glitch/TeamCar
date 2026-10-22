class Console:
    def __init__(self):
        pass

    def show_start_menu(self):
        print(" ")
        print("차량 관리 시스템")
        print("도움말: 숫자를 입력해 메뉴에 접근합니다. ex) 조회시 1 입력")
        print(" ")
        print("0. 프로그램 종료")
        print("1. 조회")
        print("2. 관리")
        print("3. 계산")

    def show_manage_menu(self): # 관리 메뉴 화면
        print(" ")
        print("차량 관리 시스템 - (관리)")
        print("도움말: 숫자를 입력해 메뉴에 접근합니다. ex) 차량 정보 등록시 1 입력")
        print(" ")
        print("0. 뒤로")
        print("1. 차량 정보 등록")
        print("2. 차량 정보 수정")
        print("3. 차량 정보 삭제")

    def show_manage_register(self): # 입주 차량 등록 화면
        print(" ")
        print("차량 관리 시스템 - (차량 정보 등록)")
        print("도움말: 차량 번호를 입력하세요")
        print("\n> ", end="")
        self.number = input()
        print(" ")
        print("차량 관리 시스템 - (차량 정보 등록)")
        print("도움말: 차량 소유자 이름을 입력하세요")
        print("\n> ", end="")
        self.name = input()
        print(" ")
        print("차량 관리 시스템 - (차량 정보 등록)")
        print("도움말: 연락처를 입력하세요")
        print("\n> ", end="")
        self.phone = input()
        print(" ")
        print("차량 관리 시스템 - (차량 정보 등록)")
        print("도움말: 차량 제조회사를 입력하세요")
        print("\n> ", end="")
        self.model = input()
        print(" ")
        print("차량 관리 시스템 - (차량 정보 등록)")
        print("도움말: 색상을 입력하세요")
        print("\n> ", end="")
        self.color = input()
        print(" ")
        print("차량 등록 완료")

    def show_manage_modify(self): # 차량 정보 수정 화면
        print(" ")
        print("차량 관리 시스템 - (차량 정보 수정)")
        print("도움말: 차량 번호를 입력하세요")
        print("\n> ", end="")
        self.number = input()

    def show_manage_remove(self): # 차량 정보 삭제 화면
        print(" ")
        print("차량 관리 시스템 - (차량 정보 삭제)")
        print("도움말: 차량 번호를 입력하세요")
        print("\n> ", end="")
        self.number = input()
        print(" ")
        print(f"[{self.number}] 등록 정보를 삭제 했습니다.")

console = Console()

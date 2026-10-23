import subprocess


class Console:
    def __init__(self) -> None:
        pass

    def clear(self) -> None:
        subprocess.run("cls", shell=True, check=False)

    def show_start_menu(self) -> None:
        print(" ")
        print("차량 관리 시스템")
        print("도움말: 숫자를 입력해 메뉴에 접근합니다. ex) 조회시 1 입력")
        print(" ")
        print("0. 프로그램 종료")
        print("1. 조회")
        print("2. 관리")
        print("3. 계산")
        print("\n> ", end="")

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

    def show_manager_register_1(self) -> None:
        print("> 서울12바3456")
        print(" ")
        print("차량 관리 시스템 - (차량 정보 등록)")
        print("도움말: 차량 소유자 이름을 입력하세요")
        print(" ")
        print("> 이상무")

    def show_manage_register(self) -> None:
        print(" ")
        print("차량 관리 시스템 - (차량 정보 등록)")
        print("도움말: 차량 번호를 입력하세요")
        print(" ")
        print("\n> ", end="")
        # print(" ")
        # print("차량 관리 시스템 - (차량 정보 등록)")
        # print("도움말: 연락처를 입력하세요")
        # print(" ")
        # print("> 010-0000-0000")
        # print(" ")
        # print("차량 관리 시스템 - (차량 정보 등록)")
        # print("도움말: 차량 모델을 입력하세요")
        # print(" ")
        # print("> 그랜저")
        # print(" ")
        # print("차량 관리 시스템 - (차량 정보 등록)")
        # print("도움말: 색상을 입력하세요")
        # print(" ")
        # print("> 흰색")
        # print(" ")
        # print("차량 등록 완료")


console = Console()

import subprocess


class Console:
    def __init__(self):
        pass

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

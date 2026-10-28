import subprocess


class Console:
    def __init__(self) -> None:
        pass

    def clear(self) -> None:
        subprocess.run("cls", shell=True, check=False)

    ############
    # 시작 화면 #
    ############
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


console = Console()

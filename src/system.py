from car_manager import car_manager
from console import console


class System:
    def __init__(self):
        pass

    def seq_load(self):
        # JSON 파일을 불러와 Python 데이터 형식으로 변환
        car_manager.load()

    def seq_start(self):
        # 콘솔 객체를 불러 시작 메뉴를 콘솔 화면에 출력
        # Figma - MiniProject - 화면설계서 - 시작 메뉴
        console.show_start_menu()

        # 사용자 입력 받기
        # 단, 여기서 사용자 입력을 받을때 예외 처리 필요
        # 0~3 사이 정수만 입력받아야 하며 그외 모든
        # 값들은 예외
        print("\n> ", end="")
        user_input = int(input())

        match user_input:
            case 0:  # 프로그램 종료
                return
            case 1:  # 조회 메뉴
                self.seq_view()
            case 2:  # 관리 메뉴
                self.seq_manage()
            case 3:  # 주차 요금 계산
                self.seq_calc()


    def seq_view(self):
        pass

    def seq_manage(self):  # 차량 관리
        console.show_manage_menu()
        print("\n> ", end="")
        user_input = int(input())

        match user_input:
            case 0:  # 뒤로
                return self.seq_start()
            case 1:  # 차량 정보 등록
                self.seq_manage_register()
            case 2:  # 차량 정보 수정
                self.seq_manage_modify()
            case 3:  # 차량 정보 삭제
                self.seq_manage_remove()

    def seq_manage_register(self):  # 차량 정보 등록
        console.show_manage_register()     
        return system.seq_start()

    def seq_manage_modify(self):  # 차량 정보 수정
        console.show_manage_modify()
        return system.seq_start()

    def seq_manage_remove(self):  # 차량 정보 삭제
        console.show_manage_remove()
        return system.seq_start()

    def seq_calc(self):
        pass


system = System()

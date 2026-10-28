from car_manager import car_manager
from console import console
from car import Car


class System:
    def __init__(self):
        pass

    def seq_load(self):
        pass

    def seq_start(self):
        pass

    def seq_view(self):  # 차량 조회 메뉴
        console.show_view_menu()
        print("\n> ", end="")
        user_input = int(input())

        match user_input:
            case 0:  # 뒤로
                return self.seq_start()
            case 1:  # 차량 목록 조회
                self.seq_view_all()
            case 2:  # 차량 상세 조회
                self.seq_view_detail()
            case 3:  # 차량 제조회사 기준 조회
                self.seq_view_by_model()
            case 4:  # 차주 이름으로 차량 조회
                self.seq_view_by_name()

    def seq_view_all(self):  # 차량 목록 조회
        console.show_view_all()
        return self.seq_view()

    def seq_view_detail(self):  # 차량 상세 조회
        console.show_view_detail()
        return self.seq_view()

    def seq_view_by_model(self):  # 차량 제조회사 기준 조회
        console.show_view_by_model()
        return self.seq_view()

    def seq_view_by_name(self):  # 차주 이름으로 차량 조회
        console.show_view_by_name()
        return self.seq_view()


system = System()

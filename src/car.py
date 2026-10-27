class Car:
    def __init__(
        self, number, name, phone, model, color, parking, type, park_in, park_out
    ):
        self.number = number  # 차량 번호
        self.name = name  # 이름
        self.phone = phone  # 연락처
        self.model = model  # 차 회사
        self.color = color  # 차 색상
        self.parking = parking  # 주차된 차량
        self.type = type  # 입주민/외부/특수
        self.park_in = park_in  # 입차
        self.park_out = park_out  # 출차

from enum import Enum


# 차량 유형을 정의하는 클래스
class CarType(Enum): 
    RESIDENT = "입주민 차량"
    EXTERNAL = "외부 차량"
    SPECIAL = "특수 차량"


class Car:
    def __init__(
        self,
        number,
        name,
        phone,
        model,
        color,
        parking,
        car_type,
    ):
        self.number = number      # 차량 번호
        self.name = name          # 차주 성함
        self.phone = phone        # 차주 연락처
        self.model = model        # 차량 회사
        self.color = color        # 차량 색상
        self.parking = parking    # 주차 여부 (True 또는 False)
        self.car_type = car_type  # 방문 유형


        self.park_in = []
        self.park_out = []


    # 외부 차량인 경우에만 reason받기
    def add_park_in(self, time, reason=None):
        if self.car_type in (CarType.RESIDENT, CarType.SPECIAL):
            reason = None

        elif self.car_type == CarType.EXTERNAL:
            
            if not isinstance(reason, str):
                raise TypeError("한글 또는 영어로 입력해 주세요.")

            if reason is None or not reason.strip():
                raise ValueError("방문 사유를 입력해 주세요.")


        self.park_in.append({
            "time": time,
            "reason": reason,
        })


    def add_out(self, time):
        self.out.append(time)

    @staticmethod
    def json_default(obj):
        if isinstance(obj, Car):
            return {
                "name": obj.name,
                "phone": obj.phone,
                "model": obj.model,
                "color": obj.color,
                "parking": obj.parking,
                "car_type": obj.car_type.value,
                "park_in": obj.park_in,
                "park_out": obj.park_out,
            }
from enum import Enum


class CarType(Enum):
    RESIDENT = "입주민 차량"
    EXTERNAL = "외부 차량"
    SPECIAL = "특수 차량"


class Car:
    def __init__(self, number, name, phone, model, color, parking, type, park_in = None, out = None):
        self.number = number      # 차량 번호
        self.name = name          # 차주 성함
        self.phone = phone        # 차주 연락처
        self.model = model        # 차량 회사
        self.color = color        # 차량 색상
        self.parking = parking    # 주차 여부 (True 또는 False)
        
        # 외부에서 "입주민 차량"이라는 글자가 들어오면, 위에서 만든 CarType(Enum)으로 변환해 저장합니다.
        if isinstance(type, str):
            self.type = CarType(type)
        else:
            self.type = type

        

        self.park_in = park_in if park_in is not None else []
        self.out = out if out is not None else []


##############
# 입출차 기록 #
##############

    # 입차 기록을 딕셔너리 형태로 배열에 추가
    def add_park_in_record(self, time_str, reason_str=None):
        
        # 입주민 차량일 경우 사유(reason)를 강제로 None 처리
        if self.type == CarType.RESIDENT:
            final_reason = None
        else:
            final_reason = reason_str
            
        self.park_in.append({
            "time": time_str,
            "reason": final_reason
        })

    # 출차 기록(문자열)을 배열에 추가
    def add_out_record(self, time_str):
        self.out.append(time_str)
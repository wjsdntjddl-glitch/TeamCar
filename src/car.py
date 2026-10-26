class Car:

    def __init__(
        self, number, name, phone, model, color, parking, type, park_in, park_out
    ):
        self.number = number # 차량 번호
        self.name = name # 이름
        self.phone = phone # 연락처
        self.model = model # 차 회사
        self.color = color # 차 색상
        self.parking = parking # 주차된 차량
        self.type = type # 입주민/외부/특수
        self.park_in = park_in # 입차
        self.park_out = park_out # 출차

    # 차량 1 - 입주민 차량 (현재 주차 중)
car1 = Car(
    "12가3456",
    "김철수",
    "010-1234-5678",
    "현대",
    "흰색",
    True,
    "입주민",
    "2026-10-26 08:30",
    None
)

# 차량 2 - 외부 차량 (출차 완료)
car2 = Car(
    "34나5678",
    "이영희",
    "010-2345-6789",
    "기아",
    "검정",
    False,
    "외부",
    "2026-10-26 09:15",
    "2026-10-26 11:20"
)

# 차량 3 - 특수 차량 (현재 주차 중)
car3 = Car(
    "56다7890",
    "박민수",
    "010-3456-7890",
    "벤츠",
    "회색",
    True,
    "특수",
    "2026-10-26 10:00",
    None
)

# 차량 4 - 입주민 차량
car4 = Car(
    "78라1234", "최민준", "010-4567-8901",
    "현대", "검정", True, "입주민",
    "2026-10-26 07:45", None
)

# 차량 5 - 외부 차량
car5 = Car(
    "90마5678", "정수빈", "010-5678-9012",
    "기아", "흰색", False, "외부",
    "2026-10-26 08:20", "2026-10-26 10:30"
)

# 차량 6 - 입주민 차량
car6 = Car(
    "23바9012", "한지우", "010-6789-0123",
    "BMW", "파랑", True, "입주민",
    "2026-10-26 09:10", None
)

# 차량 7 - 특수 차량
car7 = Car(
    "45사3456", "오세훈", "010-7890-1234",
    "벤츠", "검정", True, "특수",
    "2026-10-26 09:40", None
)

# 차량 8 - 외부 차량
car8 = Car(
    "67아7890", "윤서연", "010-8901-2345",
    "쉐보레", "빨강", False, "외부",
    "2026-10-26 10:15", "2026-10-26 12:00"
)

# 차량 9 - 입주민 차량
car9 = Car(
    "89자2345", "임도윤", "010-9012-3456",
    "제네시스", "회색", True, "입주민",
    "2026-10-26 11:00", None
)

# 차량 10 - 외부 차량
car10 = Car(
    "11차6789", "강하린", "010-0123-4567",
    "테슬라", "흰색", True, "외부",
    "2026-10-26 11:30", None
)



# 차량 객체를 리스트에 저장
cars = [
    car1, car2, car3, car4, car5,
    car6, car7, car8, car9, car10
]

for car in cars:
    print("차량번호:", car.number)
    print("차주 이름:", car.name)
    print("차량 제조사:", car.model)
    print("주차 여부:", car.parking)
    print("차량 구분:", car.type)
    print("입차 시간:", car.park_in)
    print("출차 시간:", car.park_out)
    print("----------------------")
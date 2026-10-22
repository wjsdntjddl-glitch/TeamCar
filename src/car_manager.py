from car import Car


class CarManager:
    def __init__(self):
        self.data = {}

    def load(self):
        # 불러올 파일에 담긴 내용 예시
        file_string = """ 
        {
            "서울12가3456" : {
                "name" : "이상무",
                "phone" : "010-0000-0000",
                "model": "현대",
                "color": "하얀색",
                "parking": true,
                "resident": false,
                "park_in" : [
                    {"time" : "2026-10-19 09:25:00", "reason": "세탁기 고장 AS 방문"},
                    {"time" : "2026-10-19 15:00:00", "reason": "식기세척기 고장 AS 방문"}
                ],
                "park_out" : [
                    "2026-10-19 11:35:00"
                ]
            }
        }
        """

        # 불러와진 데이터 예시
        number = "서울12가3456"
        name = "이상무"
        phone = "010-0000-0000"
        model = "현대"
        color = "하얀색"
        parking = True
        resident = False
        park_in = [
            {"time": "2026-10-19 09:25:00", "reason": "세탁기 고장 AS 방문"},
            {"time": "2026-10-19 15:00:00", "reason": "식기세척기 고장 AS 방문"},
        ]
        park_out = ["2026-10-19 11:35:00"]

        # self.data 딕셔너리에 Car 클래스의 객체를
        # 차량 번호를 key로 하여 추가
        self.data[number] = Car(
            number, name, phone, model, color, parking, resident, park_in, park_out
        )


car_manager = CarManager()

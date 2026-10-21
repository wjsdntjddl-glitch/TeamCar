class Car:
    def __init__(
        self, number, name, phone, model, color, parking, resident, park_in, park_out
    ):       
        self.number = number
        self.name = name
        self.phone = phone
        self.model = model
        self.color = color
        self.parking = parking
        self.resident = resident
        self.park_in = park_in
        self.park_out = park_out

    def show_info(self):
        print(f'{self.number}/{self.name}')


def main():
    car1 = Car("12가 3456","전우성","010-1234-5678","포터","흰색",True,False,[{"time":"2026-10-21 17:00:00","reason":"세탁기고장as"}],["2026-10-22 18:00:00"])

    car1.show_info()
if __name__ == "__main__":
    main()

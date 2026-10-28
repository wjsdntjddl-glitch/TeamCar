from datetime import datetime
import re


class Car:
    """개별 차량의 정보를 담는 클래스"""

    def __init__(
        self,
        number: str,
        name: str,
        phone: str,
        model: str,
        color: str,
        parking: bool,
        type: str,
        park_in: str | None = None,
        park_out: str | None = None,
    ):
        self.__number = number
        self.__name = name
        self.__phone = phone
        self.__model = model
        self.__color = color
        self.__parking = parking
        self.__type = type
        self.__park_in = (
            datetime.now().strftime("%Y/%m/%d %H:%M:%S") if park_in is None else park_in
        )
        self.__park_out = (
            datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            if park_out is None
            else park_out
        )

    @property
    def number(self):
        return self.__number

    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone

    @property
    def model(self):
        return self.__model

    @property
    def color(self):
        return self.__color

    @property
    def parking(self):
        return self.__parking

    @property
    def type(self):
        return self.__type

    @property
    def park_in(self):
        return self.__park_in

    @property
    def park_out(self):
        return self.__park_out

    # setter
    @number.setter
    def number(self, value: str) -> None:
        if not self.validate_number(value):
            raise ValueError("차량 번호는 필수입니다.")

        self.__number = value

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("이름은 필수입니다.")

        self.__name = value

    @phone.setter
    def phone(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("연락처를 확인하세요.")

        new_value = value.replace("-", "")

        if not new_value.isnumeric():
            raise ValueError("잘못된 입력입니다.")

        if not len(new_value) == 11:
            raise ValueError("올바르지 않은 형식입니다.")

        self.__phone = value

    @model.setter
    def model(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("잘못된 입력입니다.")

        self.__model = value

    @color.setter
    def color(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("잘못된 입력입니다.")
        
        self.__color = value

    @parking.setter
    def parking(self, value: bool):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("잘못된 입력입니다.")

        if not (value == "Y" | "N"):
            raise ValueError("Y 또는 N 으로 입력해주세요.")

        if value == "Y":
            self.parking = True

        if value == "N":
            self.parking = False

        self.__parking = value

    @type.setter
    def type(self, value):
        if not (value == "입주민" or value == "외부" or value == "특수"):
            raise ValueError("입주민/외부/특수 중 하나로 입력하세요.")

        self.type = value

    @park_in.setter
    def park_in(self, value):
        self.__park_in = (
            datetime.now().strftime("%Y/%m/%d %H:%M:%S") if value is None else value
        )

    @park_out.setter
    def park_out(self, value):
        
        self.__park_out = (
            datetime.now().strftime("%Y/%m/%d %H:%M:%S") if value is None else value
        )

    @staticmethod
    def validate_number(number):
        """차량 번호 확인"""
        if not isinstance(number, str):
            return False

        pattern = r"^[가-힣]{2}[0-9]{2}[0-9]?[가-힣][0-9]{4}$"

        return re.fullmatch(pattern, number) is not None

    def to_dict(self) -> dict:
        """Member객체를 딕셔너리로 변환"""
        return {
            "number": self.number,
            "name": self.name,
            "phone": self.phone,
            "model": self.model,
            "color": self.color,
            "pariking": self.parking,
            "type": self.type,
            "park_in": self.park_in,
            "park_out": self.park_out,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Car":
        """dict데이터를 Car 객체로 변환"""
        car = cls(
            number=data["number"],
            name=data["name"],
            phone=data["phone"],
            model=data["model"],
            color=data["color"],
            parking=data["parking"],
            type=data["type"],
            park_in=data["park_in"],
            park_out=data["park_out"],
        )
        # print("car:",car)
        return car

    def __repr__(self) -> str:
        return (
            f"Car(number={self.__number!r},"
            f"name={self.__name!r},"
            f"phone={self.__phone!r},"
            f"model={self.__model!r},"
            f"color={self.__color!r},"
            f"parking={self.__parking!r},"
            f"type={self.__type!r},"
            f"park_in={self.__park_in!r},"
            f"park_out={self.__park_out!r},"
            f")"
        )


def main():
    member = Car("12가3456", "전우성", "010-3141-6057", "현대", "흰색", "Y", "입주민")

    print(member)


if __name__ == "__main__":
    main()

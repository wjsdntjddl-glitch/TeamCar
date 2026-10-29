import re


class Car:
    def __init__(
        self,
        number: str | None = None,
        name: str | None = None,
        phone: str | None = None,
        brand: str | None = None,
        color: str | None = None,
    ) -> None:
        self.__number = number
        self.__name = name
        self.__phone = phone
        self.__brand = brand
        self.__color = color

    @classmethod
    def is_empty_str(cls, value: str) -> bool:
        return not value.strip()

    @property
    def number(self) -> str | None:
        return self.__number if self.__number is not None else None

    @number.setter
    def number(self, value: str) -> None:
        if Car.is_empty_str(value):
            raise ValueError("[Error] 필수 입력사항입니다.")
        
        number = value.replace(" ", "")
        pattern = r"\d{2}\d?[가-힣]\d{4}$"
        if re.fullmatch(pattern, number) is None:
            raise ValueError("[Error] 차량 번호를 정확히 입력하십시오.")

        self.__number = number

    @property
    def name(self) -> str | None:
        return self.__name if self.__name is not None else None

    @name.setter
    def name(self, value: str) -> None:
        if Car.is_empty_str(value):
            raise ValueError("[Error] 필수 입력사항입니다.")
        
        self.__name = value

    @property
    def phone(self) -> str | None:
        return self.__phone if self.__phone is not None else None

    @phone.setter
    def phone(self, value: str) -> None:
        if Car.is_empty_str(value):
            raise ValueError("[Error] 필수 입력사항입니다.")
        
        phone = value.replace("-", "")
        if not phone.isnumeric() or len(phone) != 11:
            raise ValueError("[Error] 연락처를 정확히 입력하십시오.")

        self.__phone = phone

    @property
    def brand(self) -> str | None:
        return self.__brand if self.__brand is not None else None

    @brand.setter
    def brand(self, value: str) -> None:
        if Car.is_empty_str(value):
            raise ValueError("[Error] 필수 입력사항입니다.")
        
        self.__brand = value

    @property
    def color(self) -> str | None:
        return self.__color if self.__color is not None else None

    @color.setter
    def color(self, value: str) -> None:
        if Car.is_empty_str(value):
            raise ValueError("[Error] 필수 입력사항입니다.")
        
        self.__color = value

    @staticmethod
    def to_obj(from_dict: dict[str, str]) -> "Car":
        if not isinstance(from_dict, dict):
            raise TypeError("dict 타입이 아닙니다.")

        return Car(
            number=from_dict["number"],
            name=from_dict["name"],
            phone=from_dict["phone"],
            brand=from_dict["brand"],
            color=from_dict["color"],
        )

    @staticmethod
    def to_dict(from_obj: "Car") -> dict[str, str]:
        if not isinstance(from_obj, Car):
            raise TypeError("Car 타입이 아닙니다.")

        if (
            from_obj.__number is None
            or from_obj.__name is None
            or from_obj.__phone is None
            or from_obj.__brand is None
            or from_obj.__color is None
        ):
            raise TypeError("Car 객체의 데이터 멤버에 None이 포함되어 있습니다.")

        return {
            "number": from_obj.__number,
            "name": from_obj.__name,
            "phone": from_obj.__phone,
            "brand": from_obj.__brand,
            "color": from_obj.__color,
        }

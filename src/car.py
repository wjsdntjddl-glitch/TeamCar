import re


class Car:
    def __init__(
        self,
        number: str | None = None,
        name: str | None = None,
        phone: str | None = None,
        model: str | None = None,
        color: str | None = None,
    ) -> None:
        self.__number = number
        self.__name = name
        self.__phone = phone
        self.__model = model
        self.__color = color

    @property
    def number(self) -> str | None:
        return self.__number if self.__number is not None else None

    @number.setter
    def number(self, value: str) -> None:
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
        self.__name = value

    @property
    def phone(self) -> str | None:
        return self.__phone if self.__phone is not None else None

    @phone.setter
    def phone(self, value: str) -> None:
        phone = value.replace("-", "")
        if not phone.isnumeric() and len(phone) != 11:
            raise ValueError("[Error] 연락처를 정확히 입력하십시오.")

        self.__phone = value

    @property
    def model(self) -> str | None:
        return self.__model if self.__model is not None else None

    @model.setter
    def model(self, value: str) -> None:
        self.__model = value

    @property
    def color(self) -> str | None:
        return self.__color if self.__color is not None else None

    @color.setter
    def color(self, value: str) -> None:
        self.__color = value

    @staticmethod
    def to_obj(from_dict: dict[str, str]) -> "Car":
        if not isinstance(from_dict, dict):
            raise TypeError("dict 타입이 아닙니다.")

        return Car(
            number=from_dict["number"],
            name=from_dict["name"],
            phone=from_dict["phone"],
            model=from_dict["model"],
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
            or from_obj.__model is None
            or from_obj.__color is None
        ):
            raise TypeError("Car 객체의 데이터 멤버에 None이 포함되어 있습니다.")

        return {
            "number": from_obj.__number,
            "name": from_obj.__name,
            "phone": from_obj.__phone,
            "model": from_obj.__model,
            "color": from_obj.__color,
        }

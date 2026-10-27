import re
from datetime import datetime

 
class Car:
 
    TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
 
    def __init__(
        self,
        number: str,
        name: str,
        phone: str,
        model: str,
        color: str) -> None:
 

        self.number = number
        self.name = name
        self.phone = phone
        self.model = model
        self.color = color


    ####################
    # Getter: 읽기 전용 #
    ####################
    @property
    def number(self) -> str:
        """차량 번호 (예: 서울12가3456)"""
        return self.__number
 
    @property
    def name(self) -> str:
        """차주 성함"""
        return self.__name
 
    @property
    def phone(self) -> str:
        """차주 연락처 (010-0000-0000)"""
        return self.__phone
 
    @property
    def model(self) -> str:
        """차량 회사(제조사)"""
        return self.__model
 
    @property
    def color(self) -> str:
        """차량 색상"""
        return self.__color
 

 
    #####################
    # Setter: 속성값 변경 #
    #####################
    @number.setter
    def number(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("차량 번호를 정확히 입력해주십시오.(예: 12가3456)")
        self.__number = value

 ####### 보완 ######
    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("이름은 한글, 영문, 숫자 2~20자로 입력해주십시오.")
        self.__name = value
 
    @phone.setter
    def phone(self, value: str) -> None:
        if isinstance(value, str):
            value = value.replace("-", "").replace(" ", "")  # 숫자만 남긴다
        if not Car.validate_phone(value):
            raise ValueError("연락처를 정확히 입력해주십시오. (예: 010-1234-5678)")
        if len(value) == 11:
            value = value[:3] + "-" + value[3:7] + "-" + value[7:]
        else:
            value = value[:3] + "-" + value[3:6] + "-" + value[6:]
        self.__phone = value

    @model.setter
    def model(self, value: str) -> None:
        if isinstance(value, str):
            value = value.strip()
        if not Car.validate_model(value):
            raise ValueError("차량 회사는 1~30자로 입력해주십시오.")
        self.__model = value
 
    @color.setter
    def color(self, value: str) -> None:
        if isinstance(value, str):
            value = value.strip()
        if not Car.validate_color(value):
            raise ValueError("색상은 한글 또는 영문 10자 이하로 입력해주십시오.")
        self.__color = value


    
    ##############
    # 값 검사 함수 #
    ##############
    @staticmethod
    def validate_number(number) -> bool:
        """차량 번호 검증: 지역 2글자 + 숫자 2~3자리 + 한글 1글자 + 숫자 4자리"""
        pattern = r"[가-힣]{2}\d{2}\d?[가-힣]\d{4}"
        return isinstance(number, str) and re.fullmatch(pattern, number, re.ASCII) is not None
 
    @staticmethod
    def validate_name(name) -> bool:
        """이름 검증: 한글/영문/숫자 2~20자"""
        return isinstance(name, str) and re.fullmatch(r"[가-힣A-Za-z0-9 ]{2,20}", name) is not None
 
    @staticmethod
    def validate_phone(phone) -> bool:
        """연락처 검증: 숫자만 10~11자리 (010, 011, 016, 017, 018, 019로 시작)"""
        return isinstance(phone, str) and re.fullmatch(r"01[016789]\d{7,8}", phone, re.ASCII) is not None
 
    @staticmethod
    def validate_model(model) -> bool:
        """차량 회사 검증: 1~30자"""
        return isinstance(model, str) and 1 <= len(model) <= 30
 
    @staticmethod
    def validate_color(color) -> bool: # len()
        """색상 검증: 한글/영문 1~10자"""
        return isinstance(color, str) and re.fullmatch(r"[가-힣A-Za-z]{1,10}", color) is not None
 
 
    ##################
    # JSON 변환 / 출력 #
    ##################
    def to_dict(self) -> dict:
        """Car 객체를 JSON에 저장할 딕셔너리로 반환 (차량 번호는 JSON의 이름표라서 빠진다)"""
        return {
            "number": self.number, 
            "name": self.name,  
            "phone": self.phone,
            "model": self.model,
            "color": self.color
        }
 
    @classmethod
    def from_dict(cls, number, data: dict) -> "Car":
        """dict 데이터를 Car 객체로 변환"""
        if not isinstance(data, dict):
            raise ValueError("차량 정보 형식이 올바르지 않습니다.")
        
        for key in ("number","name", "phone", "model", "color"):
            if key not in data:
                raise ValueError(f"데이터가 누락되었습니다: {key}")
        return cls(
            number=data["number"],
            name=data["name"],
            phone=data["phone"],
            model=data["model"],
            color=data["color"]
        )
 
    @staticmethod
    def json_default(obj):
        """json.dump(default=...)에 넘기는 변환기."""
        if isinstance(obj, Car):
            return obj.to_dict()
        raise TypeError(f"JSON으로 저장할 수 없는 값입니다: {type(obj).__name__}")
 
    def __repr__(self) -> str:
        return (
            f"Car(number={self.__number!r}, "
            f"name={self.__name!r}, "
            f"phone={self.__phone!r}, "
            f"model={self.__model!r}, "
            f"color={self.__color!r}, "
        )
 
 ### 이부분은 src.py에
# def main():
#     car = Car("서울12가3456", "이상무", "010-0000-0000", "현대", "하얀색")
#     print(car)
#     print(car.to_dict())
 
#     try:
#         car.phone = "abc"
#     except ValueError as error:
#         print("잘못된 연락처:", error)
 
 
# if __name__ == "__main__":
#     main()
 

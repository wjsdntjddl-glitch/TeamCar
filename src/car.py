import re
from datetime import datetime
from enum import Enum
 
 
class CarType(Enum):
    RESIDENT = "입주민 차량"
    GUEST = "외부 차량"
    SPECIAL = "특수 차량"
 
 
class Car:
 
    TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
 
    def __init__(
        self,
        number: str,
        name: str,
        phone: str,
        model: str,
        color: str,
        type: CarType | str = CarType.RESIDENT,
        park_in: list | None = None,
        park_out: list | None = None,
    ) -> None:
 

        self.number = number
        self.name = name
        self.phone = phone
        self.model = model
        self.color = color
        self.type = type  
        self.__park_in = [] # Car 클래스 밖에서 접근 불가
        self.__park_out = [] #setter를 통해서만 바꿀 수 있음.
        
        # park_in에 값이 없으면 빈 리스트로 초기화
        self.park_in = [] if park_in is None else park_in  # park_out보다 먼저 넣는다.
        self.park_out = [] if park_out is None else park_out
        # 출차 시각이 입차 시각보다 빠르면 ValueError가 발생한다.


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
        if isinstance(value, str):
            value = "".join(value.split())  # 공백 제거
        if not Car.validate_number(value):
            raise ValueError("차량 번호를 다시 입력해주십시오.(예: 서울12가3456)")
        self.__number = value
 
    @name.setter
    def name(self, value: str) -> None:
        if isinstance(value, str):
            value = value.strip()
        if not Car.validate_name(value):
            raise ValueError("이름은 한글, 영문, 숫자 2~20자로 입력해주십시오.")
        self.__name = value
 
    @phone.setter
    def phone(self, value: str) -> None:
        if isinstance(value, str):
            value = value.replace("-", "").replace(" ", "")  # 숫자만 남긴다
        if not Car.validate_phone(value):
            raise ValueError("연락처를 정확히 입력해주십시오. (예: 010-1234-5678)")
        if len(value) == 11:
            value = f"{value[:3]}-{value[3:7]}-{value[7:]}"
        else:
            value = f"{value[:3]}-{value[3:6]}-{value[6:]}"
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

 ########## 논의해서 수정 ########
    @type.setter
    def type(self, value: CarType | str) -> None:
        if isinstance(value, str):  # "입주민 차량" / "입주민차량" 둘 다 받는다
            for car_type in CarType:
                if car_type.value.replace(" ", "") == value.replace(" ", ""):
                    value = car_type
                    break
        if not isinstance(value, CarType):
            raise ValueError("차량 종류는 입주민 차량, 외부 차량, 특수 차량 중 하나여야 합니다.")
        self.__type = value
 
    
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
    def validate_color(color) -> bool:
        """색상 검증: 한글/영문 1~10자"""
        return isinstance(color, str) and re.fullmatch(r"[가-힣A-Za-z]{1,10}", color) is not None
 
    @staticmethod
    def validate_time(time) -> bool:
        """시각 검증: '2026-10-19 09:25:00' 또는 '2026-10-19 09:25' (실제로 있는 날짜/시각만)"""
        if not isinstance(time, str):
            return False
        time = time.strip()
        if re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}(:[0-5]\d)?", time, re.ASCII) is None:
            return False
        try:
            datetime.strptime(time[:16], "%Y-%m-%d %H:%M")  # 13월, 25시 같은 값을 걸러낸다
        except ValueError:
            return False
        return True
 
    @staticmethod
    def _check_order(in_times: list, out_times: list) -> None:
        """입차/출차 시각이 '입차 -> 출차 -> 입차 -> ...' 순서와 개수에 맞는지 검사한다."""
        if len(out_times) > len(in_times):
            raise ValueError("출차 기록이 입차 기록보다 많습니다.")
        previous = ""
        for index, in_time in enumerate(in_times):
            if in_time < previous:
                raise ValueError("입차 시각이 직전 기록보다 빠릅니다.")
            previous = in_time
            if index < len(out_times):
                if out_times[index] < previous:
                    raise ValueError("출차 시각이 입차 시각보다 빠릅니다.")
                previous = out_times[index]
 
    ##################
    # JSON 변환 / 출력 #
    ##################
    def to_dict(self) -> dict:
        """Car 객체를 JSON에 저장할 딕셔너리로 반환 (차량 번호는 JSON의 이름표라서 빠진다)"""
        return {
            "name": self.name,  
            "phone": self.phone,
            "model": self.model,
            "color": self.color,
            "parking": "입차" if self.parking else "출차",
            "type": self.type.value,
            "park_in": self.park_in,
            "park_out": self.park_out,
        }
 
    @classmethod
    def from_dict(cls, number, data: dict) -> "Car":
        """dict 데이터를 Car 객체로 변환. 'parking'은 기록에서 계산하므로 무시한다."""
        if not isinstance(data, dict):
            raise ValueError("차량 정보 형식이 올바르지 않습니다.")
        for key in ("name", "phone", "model", "color", "type"):
            if key not in data:
                raise ValueError(f"필수 항목이 없습니다: {key}")
        return cls(
            number=number,
            name=data["name"],
            phone=data["phone"],
            model=data["model"],
            color=data["color"],
            type=data["type"],
            park_in=data.get("park_in"),
            park_out=data.get("park_out"),
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
            f"type={self.__type.value!r}, "
            f"parking={self.parking!r})"
        )
 
 
def main():
    car = Car("서울12가3456", "이상무", "010-0000-0000", "현대", "하얀색")
    car.park_in = [{"time": "2026-10-19 09:25:00", "reason": None}]
    print(car)
    print(car.to_dict())
 
    try:
        car.phone = "abc"
    except ValueError as error:
        print("잘못된 연락처:", error)
 
 
if __name__ == "__main__":
    main()
 

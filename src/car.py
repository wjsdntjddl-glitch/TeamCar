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


            # member.py

# from datetime import datetime
# import re


# class Member:
#     """회원 정보를 관리하는 모델 클래스 캡슐화 적용"""

#     def __init__(
#         self,
#         member_id: str,
#         name: str,
#         email: str,
#         password: str,
#         role: str = "USER",
#         reg_date: str | None = None,
#     ) -> None:

#         self.__member_id = member_id
#         self.__name = name
#         self.__email = email
#         self.__password = password
#         self.__role = role
#         # 삼항 연산자(3.1) 사용
#         self.__reg_date = (
#             datetime.now().strftime("%Y/%m/%d %H:%M:%S")
#             if reg_date is None
#             else reg_date
#         )

#     # @property를 사용해 __member_id, __name, __email등을 읽음

#     ##########
#     # Getter #
#     ##########
#     @property
#     def member_id(self) -> str:
#         """회원ID 읽기 전용"""
#         return self.__member_id

#     @property
#     def name(self) -> str:
#         """이름"""
#         return self.__name

#     @property
#     def email(self) -> str:
#         """이메일"""
#         return self.__email

#     @property
#     def password(self) -> str:
#         """비밀번호: 평문"""
#         return self.__password

#     @property
#     def role(self) -> str:
#         """권한"""
#         return self.__role

#     @property
#     def reg_date(self) -> str:
#         """등록일"""
#         return self.__reg_date

#     ###################################
#     # Setter: 속성값을 변경하는 기능 추가 #
#     ###################################
#     @member_id.setter
#     def member_id(self, value: str) -> None:
#         if not isinstance(value, str) or not value.strip():
#             raise ValueError("회원ID는 필수 문자열입니다.")
#         self.password = value


#     @name.setter
#     def name(self, value: str) -> None:  # setter는 return값이 없음(None)
#         if not isinstance(value, str) or not value.strip():
#             # str이 아니거나 빈 문자열이면
#             raise ValueError("이름은 필수 문자열 입니다.")

#         self.__name = value


#     # email : re
#     @email.setter
#     def email(self, value: str) -> None:
#         if not self.validate_email(value):
#             raise ValueError("이메일 형식을 고려하세요.")

#         self.__email = value


#     # 비번
#     @password.setter
#     def password(self, value: str) -> None:
#         if not self.validate_password(value):
#             raise ValueError("비밀번호를 확인하세요.")
#         self.password = str


#     @role.setter
#     def role(self, value: str) -> None:
#         """ 권한 setter """
#         if not isinstance(value, str) or value not in ["USER", "ADMIN"]:
#             raise ValueError("권한은 USER 또는 ADMIN이어야 합니다.")

#         self.__role = value


#     @reg_date.setter
#     def reg_date(self, value: str) -> None:
#         """등록일 setter"""
#         self.__reg_date = (
#             datetime.now().strftime("%Y/%m/%d %H:%M:%S") if value is None else value
#         )


#     @staticmethod
#     def validate_password(password):

#         if not isinstance(password, str):
#             return False

#         if len(password) < 8:
#             return False

#         # 알파벳 있는지
#         # any() : 여러 조건중 하나라도 True이면 True
#         has_alpha = any(ch.isalpha() for ch in password)
#         has_digit = any(ch.isdigit() for ch in password)

#         return has_alpha and has_digit


#     @staticmethod
#     def validate_email(email: str) -> bool:
#         """이메일 검증"""
#         if not isinstance(email, str):
#             return False

#         # jamesol@naver.com                             # \. : 문자 그대로 해석
#         pattern = r"^[A-Za-z0-9._%+-] + @[A-Za-z0-9._-] + \.[A-Za-z]{2,}$"
#         # 한 개 이상       # 한 개 이상      # 두 개 이상

#         return re.fullmatch(pattern, email) is not None


#      # Member 객체를 딕셔너리로 반환
#     def to_dict(self) -> dict:
#         """ Member 객체를 딕셔너리로 반환 """
#         return  {
#     "member_id": self.member_id,  # getter로 불러오기
#     "name": self.name,
#     "email": self.email,
#     "reg_date": self.reg_date,
#     "role": self.role,
#     "password": self.password
#   }


    
#     # dict 데이터를 Member 객체로 변환
#     @classmethod
#     def from_dict(cls, data:dict) -> "Member":
#         """ dict 데이터를 Member 객체로 변환""" 
#         member = cls(
#             member_id = data["member_id"],
#             name = data['name'],
#             email = data['email'],
#             password = data['password'],
#             role = data['role'],
#             reg_date = data['reg_date']
#         )
#         # print('member:', member)
#         return member

#     # member_id = "user01"
#     def __repr__(self) -> str:
#         return (
#             f"Member(  member_id={self.__member_id!r}, "
#             f"name={self.__name!r}, "
#             f"email={self.__email!r}, "
#             f"password={self.__password!r}, "
#             f"role={self.__role!r}, "
#             f"reg_date={self.__reg_date!r} "
#             f")"
#         )  # !r :


# def main():
#     member = Member("user01", "이상무", "jamesol@naver.com",  "a12345678", "USER")

#     print(member)


# if __name__ == "__main__":
#     main()

# # WORKSPACE 위치에서 실행시, 아래 명령어 입력
# # python -m member.model.member
# # (모듈로 실행해야 된대)

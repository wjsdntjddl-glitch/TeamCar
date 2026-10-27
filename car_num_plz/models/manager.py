import json
import os
import tempfile
from pathlib import Path

from car_num_plz.models.car import Car


class CarManager:
    def __init__(self, file_path: str | Path | None = None) -> None:

        # __file__ : 현재 실행 중인 Python 모듈 파일의 경로
        if file_path is None:
            file_path = Path(__file__).resolve().parent.parent / "out" / "data.json"

        # 회원 경로
        self.file_path = file_path

        # 회원 목록
        self.cars: list[Car] = []

        # JSON파일에서 회원정보 읽기
        self.load_json()

    def do_update(self, car: Car) -> int:

        for index, current_car in enumerate(self.cars):
            if current_car.number == car.number:
                self.cars[index] = car

                try:
                    self.save_json()
                except Exception:
                    self.cars[index] = current_car
                    raise
                return 1

        return 0

    def do_retrieve(self) -> list[Car]:
        return self.cars.copy()

    def do_delete(self, number: str) -> int:

        car = self.do_select_one(number)
        if car is None:
            return 0

        index = self.cars.index(car)
        self.cars.pop(index)

        try:
            self.save_json()
        except Exception:
            self.cars.insert(index, car)

        return 1

    def do_select_one(self, number: str) -> Car:
        for car in self.cars:
            if car.number == number:
                return car

        return None

    def do_save(self, car: Car) -> int:
        if self.do_select_one(number=car.number) is not None:
            return 0

        self.cars.append(car)

        try:
            self.save_json()
        except Exception:
            self.cars.remove(car)

        return 1

    def load_json(self) -> None:
        if not self.file_path.exists():
            self.cars = []
            return

        with self.file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("회원 JSON 데이터는 리스트여야 합니다.")

        self.cars = [Car.from_dict(item) for item in data]

    def save_json(self) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        data = [car.to_dict() for car in self.cars]

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    cm = CarManager()

    car_user01 = Car(
        number= "12가3456",
        name= "전우성",
        phone= "010-3141-6057",
        model= "현대",
        color= "흰색",
        parking= "Y",
        type= "입주민")

    print("=== 회원 수정 ===")
    car_user = cm.do_select_one("12가3456")

    if car_user:
        car_user.name = "이순희-U"
        car_user.phone = "010-1234-5678"
        car_user.model = "기아"
        car_user.parking = "N"

        flag = cm.do_update(car_user)

        if flag == 1:
            print("수정 성공")
        else:
            print("수정 실패1")

    else:
        print("수정 실패2")


    # print("=== 전체 회원 조회 ===")
    # members = cm.do_retrieve()

    # for member in members:
    #     print(f"- {member}")

    
    # print("=== 회원 저장 ===")

    # flag = cm.do_save(car_user)

    # if flag == 1:
    #     print("회원 등록 성공")
    # else:
    #     print("회원 등록 실패")


    # print("=== 회원 단건 조회 ===")
    # member = cm.do_select_one("pcwk98")

    # if member:
    #     print(f"회원 조회 성공:\n {member}")
    # else:
    #     print("회원 조회 실패")
        
    
    # print("=== 회원 삭제 ===")
    # flag = cm.do_delete(car_user.number)

    # if flag == 1:
    #     print("삭제 성공")
    # else:
    #     print("삭제 실패")



if __name__ == "__main__":
    main()

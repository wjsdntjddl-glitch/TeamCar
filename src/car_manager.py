import json
from pathlib import Path

from car import Car
from utils.logger import logger


class CarManager:
    def __init__(self) -> None:
        self.data: list[Car] = []
        self.data_path = Path("out") / "data.json"

    def save(self) -> None:
        if not self.data_path.parent.exists():
            self.data_path.parent.mkdir(parents=True, exist_ok=True)

        with self.data_path.open("w", encoding="utf-8") as file:
            json.dump(
                self.data,
                file,
                default=Car.to_dict,
                indent=4,
                ensure_ascii=False,
            )

    def load(self) -> None:
        if not self.data_path.exists():
            logger.warn("JSON 파일을 경로 탐색 실패 / 경로: " + str(self.data_path.absolute()))
            print("경고! JSON 파일이 없습니다.")
            print(f"> {self.data_path.absolute()}")
            return

        with self.data_path.open("r", encoding="utf-8") as file:
            json_data: list[dict[str, str]] = json.load(file)
            for data in json_data:
                car = Car(
                    number=data["number"],
                    name=data["name"],
                    phone=data["phone"],
                    brand=data["brand"],
                    color=data["color"],
                )
                self.data.append(car)

    def is_duplicated(self, number: str) -> bool:
        """동일한 차량 번호 중복 검사"""
        for car in self.data:
            if car.number == number:
                return True

        return False

car_manager = CarManager()
import json
from pathlib import Path

from car import Car

data_path = Path("out") / "data.json"


class CarManager:
    def __init__(self) -> None:
        self.data: list[Car] = []

    def save(self) -> None:
        if not data_path.parent.exists():
            data_path.parent.mkdir(parents=True, exist_ok=True)

        with data_path.open("w", encoding="utf-8") as file:
            json.dump(
                self.data,
                file,
                default=Car.to_dict,
                indent=4,
                ensure_ascii=False,
            )

    def load(self) -> None:
        if not data_path.exists():
            print("JSON 파일이 없습니다.")
            return

        with data_path.open("r", encoding="utf-8") as file:
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

car_manager = CarManager()
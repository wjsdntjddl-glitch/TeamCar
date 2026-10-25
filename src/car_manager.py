from pathlib import Path
from car import Car, CarType
import json

data_path = Path("out") / "data.json"


class CarManager:
    def __init__(self) -> None:
        self.data = {}

    def save(self) -> None:
        # if not data_path.parent.exists():
        data_path.parent.mkdir(parents=True, exist_ok=True)

        json_data = {}

        for number, car in self.data.items():
            json_data[number] = Car.json_default(car)

        with data_path.open("w", encoding="utf-8") as file:
            json.dump(
                json_data,
                file,
                indent=4,
                ensure_ascii=False,
            )

    def load(self) -> None:
        if not data_path.exists():
            self.data = {}
            return

        with data_path.open("r", encoding="utf-8") as file:
            json_data = json.load(file)

        self.data = {}

        for number, data in json_data.items():
            car = Car(
                number=number,
                name=data["name"],
                phone=data["phone"],
                model=data["model"],
                color=data["color"],
                parking=data["parking"],
                car_type=CarType(data["car_type"]),
            )

            car.park_in = data["park_in"]
            car.out = data["out"]

            self.data[number] = car

    def is_duplicated(self, car: Car) -> bool:
        return car.number in self.data


car_manager = CarManager()
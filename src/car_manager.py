from pathlib import Path
from car import Car
import json

data_path = Path("out") / "data.json"


class CarManager:
    def __init__(self) -> None:
        self.data = {}

    def save(self) -> None:
        if not data_path.parent.exists():
            data_path.parent.mkdir(parents=True, exist_ok=True)

        if not data_path.exists():
            with data_path.open("w", encoding="utf-8") as file:
                json.dump(
                    self.data,
                    file,
                    default=Car.json_default,
                    indent=4,
                    ensure_ascii=False,
                )

    def load(self) -> None:
        with data_path.open("r", encoding="utf-8") as file:
            json_data = json.load(file)
            print(json_data)
            for key in json_data:
                data = json_data[key]
                name = data["name"]

                self.data[key] = Car(name)
    
    def is_duplicated(self, car: Car) -> bool:
        return car.number in self.data


car_manager = CarManager()
from pathlib import Path
from car import Car, CarType
import json

data_path = Path("out") / "data.json"


class CarManager:
    def __init__(self) -> None:
        # 저장된 차량 정보
        self.data = {}


################
# 차량 정보 저장 #
################
    def save(self) -> None:
        try:
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
        except (OSError, TypeError, ValueError) as e:
            print(f"[Error] JSON 파일 저장 중 오류가 발생했습니다.: {e}")


###################
# 차량 정보 불러오기 #
###################    
    def load(self) -> None:
        if not data_path.exists():
            self.data = {}
            print('저장된 JSON 파일이 없습니다.')
            return

        try:
            with data_path.open("r", encoding="utf-8") as file:
                json_data = json.load(file)

            if not isinstance(json_data, dict):
                raise ValueError("JSON의 최상위 데이터는 객체여야 합니다.")

            loaded_data = {}

            for number, data in json_data.items():
                if not isinstance(data, dict):
                    raise ValueError(
                        f"{number} 차량의 데이터 형식이 올바르지 않습니다."
                    )
                
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
                car.park_out = data["park_out"]

                loaded_data[number] = car

            self.data = loaded_data
            print("JSON 파일을 성공적으로 불러왔습니다.")

        except json.JSONDecodeError as e:
            print(f"JSON 파일의 형식이 잘못되었습니다: {e}")

        except KeyError as e:
            print(f"차량 데이터에 필수 항목이 없습니다: {e}")

        except ValueError as e:
            print(f"차량 데이터가 올바르지 않습니다: {e}")

        except OSError as e:
            print(f"JSON 파일을 읽는 중 오류가 발생했습니다: {e}")

        except TypeError as e:
            print(f"차량 데이터의 자료형이 올바르지 않습니다: {e}")


##############
# 중복된 차량 #
##############
    def is_duplicated(self, car: Car) -> bool:
        return car.number in self.data


car_manager = CarManager()

if __name__ == "__main__":
    car_manager.load()
    car_manager.save()
    print("JSON 파일 저장 완료")
    print(car_manager.data)
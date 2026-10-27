import json
import os
from pathlib import Path
from car import Car

 
# 프로젝트 맨 위 폴더(TeamCar)의 out/data.json
# 파일 위치를 기준으로 잡았기 때문에 어느 폴더에서 실행해도 같은 곳에 저장된다.
data_path = Path(__file__).resolve().parent.parent / "out" / "data.json"
 
 
class CarManager:
    def __init__(self) -> None:
        self.data = []

    # def is_duplicated(self, car: Car) -> bool:
    #     """이미 등록된 차량 번호면 True."""
    #     return car.number in self.data
 
    def save(self) -> bool:
        """data.json에 저장 (성공하면 True, 실패하면 False)"""
        self.last_error = ""
        
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
        # out 폴더가 없으면 만들어줌./파일이 들어갈 폴더/이미 있어도 에러안남

            # 이 블록이 끝나면 파일을 자동으로 닫아줌.
            with self.path.open("w", encoding="utf-8") as file:
                json.dump(       # 기존에 있던 data.json을 덮어씀.
                    self.data,
                    file,
                    default=Car.json_default,
                    indent=4,
                    ensure_ascii=False,
                )
        except (OSError, TypeError):
            self.last_error = "차량 정보를 저장하지 못했습니다."
           
            return False

        return True
         
 
    def load(self) -> bool:
        DATA_FILE = Path("out") /"data.json"
        
        with DATA_FILE.open("r", encoding="utf-8") as file:
            json_data = json.load(file)
            print(json_data)

            for key in json_data:
                car_data = json_data[key]
                car = Car.from_dict(key, car_data)
                self.data.append(car)
 
car_manager = CarManager()

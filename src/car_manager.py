import json
import os
import shutil
from pathlib import Path
 
from car import Car
from utils.logger import logger
 
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
        """data.json에 저장한다. 성공하면 True, 실패하면 False(원인은 last_error)."""
        self.last_error = ""
        temp_path = self.path.with_name(self.path.name + ".tmp")
        try:
            for key, car in self.data.items():
                if not isinstance(car, Car) or key != car.number:
                    raise ValueError(f"저장할 수 없는 항목입니다: {key}")
 
            self.path.parent.mkdir(parents=True, exist_ok=True)
            # 임시 파일에 먼저 쓰고, 끝까지 성공하면 진짜 파일과 바꾼다.
            # (쓰다가 실패해도 기존 data.json이 망가지지 않는다.)
            with temp_path.open("w", encoding="utf-8") as file:
                json.dump(
                    self.data,
                    file,
                    default=Car.json_default,
                    indent=4,
                    ensure_ascii=False,
                )
            os.replace(temp_path, self.path)
        except (OSError, TypeError, ValueError) as error:
            try:
                temp_path.unlink(missing_ok=True)
            except OSError:
                pass
            self.last_error = (
                "차량 정보를 저장하지 못했습니다. 파일 접근 권한과 저장 공간을 확인해주십시오."
            )
            logger.log(f"JSON 저장 오류: {error!r}", logger.Level.ERROR)
            return False
 
        logger.log(f"차량 정보 저장 완료 ({len(self.data)}대)", logger.Level.DEBUG)
        return True
 
    def load(self) -> bool:
        DATA_FILE = Path("out") /"data  .json"
        
        with DATA_FILE.open("r", encoding="utf-8") as file:
            pass
 
car_manager = CarManager()

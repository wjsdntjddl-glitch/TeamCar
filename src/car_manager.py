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
    def __init__(self, path=None) -> None:
        self.data: dict[str, Car] = {}  # {차량 번호: Car}
        self.path = Path(path) if path is not None else data_path
        # 가장 최근 save/load에서 문제가 있었다면 사용자에게 보여줄 문장이 들어간다.
        self.last_error = ""
 
    def is_duplicated(self, car: Car) -> bool:
        """이미 등록된 차량 번호면 True."""
        return car.number in self.data
 
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
        """data.json을 읽어 data를 채운다.
 
        - 파일이 아직 없으면(처음 실행) 빈 상태로 시작하고 True.
        - 파일이 깨졌으면 원본을 .bak로 보관하고 빈 상태로 시작하고 False.
        - 일부 차량만 잘못됐으면 그 차량만 빼고 불러오고 True (last_error에 안내).
        """
        self.last_error = ""
        self.data = {}
 
        if not self.path.exists():
            logger.log("저장 파일이 없어 빈 상태로 시작합니다.", logger.Level.INFO)
            return True
 
        try:
            text = self.path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as error:
            self.last_error = "저장 파일을 읽지 못했습니다. 파일 접근 권한을 확인해주십시오."
            logger.log(f"JSON 읽기 오류: {error!r}", logger.Level.ERROR)
            return False
 
        broken = False  # 파일 전체가 깨졌는지
        skipped = 0  # 일부 차량만 잘못됐을 때, 제외한 차량 수
        try:
            raw = json.loads(text)
            if not isinstance(raw, dict):
                raise ValueError("최상위 형식이 올바르지 않습니다.")
        except ValueError as error:  # json.JSONDecodeError도 ValueError의 한 종류
            broken = True
            logger.log(f"JSON 형식 오류: {error!r}", logger.Level.ERROR)
        else:
            for number, info in raw.items():
                try:
                    car = Car.from_dict(number, info)
                    if car.number != number:
                        raise ValueError("차량 번호 표기가 올바르지 않습니다.")
                    self.data[number] = car
                except ValueError as error:
                    skipped += 1
                    logger.log(
                        f"차량 정보 불러오기 건너뜀 [{number}]: {error}",
                        logger.Level.WARNING,
                    )
 
        if broken or skipped:
            # 문제가 있는 원본은 .bak로 복사해 둔다. (이후 저장으로 덮어써져도 남아 있도록)
            backup_name = self.path.name + ".bak"
            try:
                shutil.copy2(self.path, self.path.with_name(backup_name))
            except OSError as error:
                logger.log(f"백업 실패: {error!r}", logger.Level.ERROR)
            if broken:
                self.last_error = (
                    "저장 파일이 손상되어 빈 상태로 시작합니다. "
                    f"원본은 {backup_name} 에 보관했습니다."
                )
            else:
                self.last_error = (
                    f"{skipped}대의 차량 정보가 올바르지 않아 제외했습니다. "
                    f"원본은 {backup_name} 에 보관했습니다."
                )
 
        logger.log(f"차량 정보 불러오기 완료 ({len(self.data)}대)", logger.Level.DEBUG)
        return not broken
 
 
car_manager = CarManager()

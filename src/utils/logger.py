import configparser
from datetime import datetime
from enum import IntEnum
from pathlib import Path


class Logger:
    # 로그 레벨을 나타내는 클래스
    class Level(IntEnum):
        """로그 레벨 클래스"""

        DEBUG = 0
        INFO = 1
        WARNING = 2
        ERROR = 3

    _log_level = Level.INFO
    _log_path = Path("out") / "TeamCar.log"
    _config_path = Path("out") / "Config.ini"

    def __init__(self) -> None:
        # ../out/ 디렉터리 존재 여부 확인
        if not Logger._config_path.parent.exists():
            Logger._config_path.parent.mkdir(parents=True, exist_ok=True)

        # ../out/Config.ini 파일 존재 여부 확인
        if not Logger._config_path.exists():
            with Logger._config_path.open("w", encoding="utf-8") as file:
                text = """[Config]
Log_Level=1

# 0: Debug
# 1: Info
# 2: Warning
# 3: Error
"""
                file.write(text)

        else:
            # ../out/Config.ini 파일 읽기 후 _log_level 대입
            config = configparser.ConfigParser()
            config.read(self._config_path, encoding="utf-8")
            self._log_level = config.get(
                "Config", "Log_Level", fallback=self._log_level
            )

    def log(self, description: str, level: Level = Level.INFO) -> None:
        """로그 작성 함수"""

        # Config의 로그 레벨보다 낮을 경우 로그 작성 취소
        if level < int(self._log_level):
            return

        # ../out/ 디렉터리 존재 여부 확인
        if not Logger._log_path.parent.exists():
            Logger._log_path.parent.mkdir(parents=True, exist_ok=True)

        # ../out/TeamCar.log 파일 존재 여부 확인 후
        # 쓰기 모드 or 이어 쓰기 권한 명시
        if Logger._log_path.exists():
            permission = "a"
        else:
            permission = "w"

        # 로그 파일 오픈후 로그 작성
        with Logger._log_path.open(permission, encoding="utf-8") as file:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            match level:
                case Logger.Level.DEBUG:
                    level_str = "Debug"
                case Logger.Level.INFO:
                    level_str = "Info"
                case Logger.Level.WARNING:
                    level_str = "Warning"
                case Logger.Level.ERROR:
                    level_str = "Error"

            result = f"[{level_str}] [{time}] {description}\n"
            file.write(result)


logger = Logger()
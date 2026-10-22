from datetime import datetime
from pathlib import Path


class Logger:
    _lpath = Path("out") / "TeamCar.log"

    def __init__(self) -> None:
        pass

    @staticmethod
    def log(description: str, level: int = 0) -> None:
        """
        로그 작성
        """
        if not Logger._lpath.parent.exists():
            Logger._lpath.parent.mkdir(parents=True, exist_ok=True)

        if Logger._lpath.exists():
            permission = "a"
        else:
            permission = "w"

        with Logger._lpath.open(permission, encoding="utf-8") as file:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = f"[Info] [{time}] {description}\n"
            file.write(result)

        print()


logger = Logger()
from system import system
from utils.logger import logger


# 프로그램 시작
def main():
    logger.info("프로그램 시작")
    system.seq_load()
    system.seq_start()
    logger.info("프로그램 종료")


if __name__ == "__main__":
    main()

from system import system
from utils.logger import logger


def main():
    logger.log("프로그램 시작", logger.Level.DEBUG)
    system.seq_start()


if __name__ == "__main__":
    main()
# ctrl + shift + p -> open keyboard JSON
# from system import system
# from utils.logger import logger


# 프로그램 시작
def main():
    # JSON 파일을 불러오는 프로세스 호출
    system.seq_load()

    # 시작 프로세스 호출
    system.seq_start()

    # 프로그램 종료
    return  print("프로그램을 종료합니다.")

if __name__ == "__main__":
    main()

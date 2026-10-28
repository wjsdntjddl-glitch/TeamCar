from system import system


# 프로그램 시작
def main():
    # JSON 파일을 불러오는 프로세스 호출
    system.seq_load()

    # 시작 프로세스 호출
    system.seq_start()


if __name__ == "__main__":
    main()

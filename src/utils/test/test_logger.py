import os
import configparser

from .. import logger


def reset_config_file():
    if logger.Logger._config_path.exists():
        os.remove(logger.Logger._config_path)

def reset_log_file():
    if logger.Logger._log_path.exists():
        os.remove(logger.Logger._log_path)

def test_logger_init():
    reset_config_file()
    logger.Logger()
    # 테스트 #1: ./out/TeamCar.log 로그 파일 존재 여부 확인
    assert logger.Logger._config_path.exists()

    config = configparser.ConfigParser()
    config.read(logger.Logger._config_path, encoding="utf-8")

    # 테스트 #2: Config 섹션 존재 여부 확인
    assert config.has_section("Config")

    # 테스트 #3: Log_Level 옵션 존재 여부 확인
    assert config.has_option("Config", "Log_Level")

def test_logger_write():
    reset_config_file()

    logger.Logger()
    logger.logger.log("테스트", logger.Logger.Level.INFO)

    # 테스트 #1: 로그 파일 생성 여부 확인
    assert logger.Logger._log_path.exists()

    # 테스트 이후 파일 삭제
    reset_log_file()
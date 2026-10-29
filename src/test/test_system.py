import json
from pathlib import Path

from car import Car
from car_manager import car_manager
from system import system


def test_get_menu_input(monkeypatch) -> None:
    """메뉴 입력 테스트"""
    # Case #1 - 입력 타입 검증
    monkeypatch.setattr("builtins.input", lambda: "테스트")
    assert system.get_menu_input(0, 3) == -1

    # Case #2 - 입력 범위 검증
    monkeypatch.setattr("builtins.input", lambda: "5")
    assert system.get_menu_input(0, 3) == -1

    # Case #3 - 정상 입력 검증
    monkeypatch.setattr("builtins.input", lambda: "1")
    assert system.get_menu_input(0, 3) == 1


def test_seq_manage_register(monkeypatch) -> None:
    """등록 테스트"""
    # Case #1 - 정상 등록 검증
    inputs = iter(["00가0000", "이상무", "000-1111-2222", "현대", "하얀색"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    try:
        system.seq_manage_register()
    except StopIteration:
        pass

    assert car_manager.data[0].number == "00가0000"
    assert car_manager.data[0].name == "이상무"
    assert car_manager.data[0].phone == "00011112222"
    assert car_manager.data[0].brand == "현대"
    assert car_manager.data[0].color == "하얀색"

def test_seq_manage_modifiy(monkeypatch) -> None:
    """수정 테스트"""
    # Case #1 - 정상 수정 검증
    car_manager.data = [
        Car(
            number="12가3456",
            name="이상무",
            phone="01012345678",
            brand="현대",
            color="진주색",
        )
    ]

    inputs = iter(["12가3456", "2", "무상이"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    try:
        system.seq_manage_modifiy()
    except StopIteration:
        pass

    assert car_manager.data[0].name == "무상이"

def test_seq_manage_remove(monkeypatch) -> None:
    """삭제 테스트"""
    # Case #1 - 정상 삭제 검증
    car_manager.data = [
        Car(
            number="12가3456",
            name="이상무",
            phone="01012345678",
            brand="현대",
            color="진주색",
        )
    ]

    inputs = iter(["12가3456"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    try:
        system.seq_manage_remove()
    except StopIteration:
        pass

    assert len(car_manager.data) == 0
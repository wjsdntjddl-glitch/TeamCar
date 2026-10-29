from system import system
from car_manager import car_manager


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

def test_seq_load() -> None:
    """JSON 파일 불러오기 통합 검증"""
    
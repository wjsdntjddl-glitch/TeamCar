from wcwidth import wcswidth

from car import Car
from console import console


def test_format_phone() -> None:
    """연락처 대시(-) 삽입 검증"""

    # Case #1 - 변환 검증
    phone = "00022224444"
    assert console.format_phone(phone) == "000-2222-4444"

def test_align_text() -> None:
    """문자열 정렬 검증"""

    # Case #1 - 정렬 검증
    text = "테스트 문자열"
    assert console.align_text(text, 15) == "테스트 문자열  "

def test_update_widths() -> None:
    """데이터의 최대 길이에 맞춰 열 크기 변경 검증"""
    console.headers = ["번호", "이름", "연락처", "차종", "색상"]
    cars = [
        Car(
            number="12가3456",
            name="이상무",
            phone="01012345678",
            brand="현대",
            color="진주색"
        )
    ]

    console.update_widths(cars)
    # Case #1 - 길이 검증
    assert console.widths[0] == wcswidth("12가3456")
    assert console.widths[1] == wcswidth("이상무")
    assert console.widths[2] == wcswidth("010-1234-5678")
    assert console.widths[3] == wcswidth("차종")
    assert console.widths[4] == wcswidth("진주색")
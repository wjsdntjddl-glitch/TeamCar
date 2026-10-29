import json
from pathlib import Path

from car import Car
from car_manager import car_manager


def test_save() -> None:
    car_manager.data_path = Path("src/test/out") / "test_data.json"

    car_manager.data = [
        Car(
            number="12가3456",
            name="이상무",
            phone="01012345678",
            brand="현대",
            color="진주색",
        )
    ]

    car_manager.save()

    assert car_manager.data_path.exists()

    with car_manager.data_path.open("r", encoding="utf-8") as file:
        json_data: list[dict[str, str]] = json.load(file)
        assert car_manager.data[0].number == json_data[0]["number"]
        assert car_manager.data[0].name == json_data[0]["name"]
        assert car_manager.data[0].phone == json_data[0]["phone"]
        assert car_manager.data[0].brand == json_data[0]["brand"]
        assert car_manager.data[0].color == json_data[0]["color"]


def test_load() -> None:
    car_manager.data_path = Path("src/test/out") / "test_data.json"
    car_manager.data = []
    json_text = """[
    {
        "number": "12가3456",
        "name": "이상무",
        "phone": "01012345678",
        "brand": "현대",
        "color": "진주색"
    }
]
"""

    if not car_manager.data_path.parent.exists():
        car_manager.data_path.parent.mkdir(parents=True, exist_ok=True)

    with car_manager.data_path.open("w", encoding="utf-8") as file:
        file.write(json_text)

    car_manager.load()

    assert car_manager.data[0].number == "12가3456"
    assert car_manager.data[0].name == "이상무"
    assert car_manager.data[0].phone == "01012345678"
    assert car_manager.data[0].brand == "현대"
    assert car_manager.data[0].color == "진주색"


def test_is_duplicated() -> None:
    car_manager.data = [
        Car(
            number="12가3456",
            name="이상무",
            phone="01012345678",
            brand="현대",
            color="진주색",
        )
    ]

    assert car_manager.is_duplicated("12가3456")

    car_manager.data = []

    assert not car_manager.is_duplicated("12가3456")

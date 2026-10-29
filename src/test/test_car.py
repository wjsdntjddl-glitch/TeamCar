import pytest

from car import Car


def test_number_setter():
    """car.number 할당 테스트"""
    car = Car()

    # Case #1 - 차량 번호 앞 2~3 자리 검증
    with pytest.raises(ValueError):
        car.number = "1가0000"

    with pytest.raises(ValueError):
        car.number = "1234가0000"

    # Case #2 - 차량 번호 앞 2~3 자리 숫자 이후
    # 한글 한글자가 포함되었는지 검증
    with pytest.raises(ValueError):
        car.number = "12*0000"

    with pytest.raises(ValueError):
        car.number = "12A0000"

    # Case #3 - 차량 번호 마지막 4자리가 숫자인지 검증
    with pytest.raises(ValueError):
        car.number = "12가****"

    with pytest.raises(ValueError):
        car.number = "12가12345"

    # Case #4 - 정상 입력 검증
    car.number = "12가3456"
    assert car.number == "12가3456"

def test_phone_setter():
    """car.phone 할당 테스트"""
    car = Car()

    # Case #1 - 연락처 11자리 검증
    with pytest.raises(ValueError):
        car.phone = "000022224444"

    with pytest.raises(ValueError):
        car.phone = "0022224444"

    # Case #2 - 정상 입력 검증
    car.phone = "00022224444"
    assert car.phone == "00022224444"

def test_to_obj():
    """dict -> car 타입 변환 테스트"""
    dict_car = {
        "number": "12가3456",
        "name": "이상무",
        "phone": "01012345678",
        "brand": "현대",
        "color": "진주색",
    }

    obj_car = Car.to_obj(dict_car)

    # Case #1 - 타입 변환 검증
    assert isinstance(obj_car, Car)

    # Case #2 - 타입 변환 내용 검증
    assert obj_car.number == "12가3456"
    assert obj_car.name == "이상무"
    assert obj_car.phone == "01012345678"
    assert obj_car.brand == "현대"
    assert obj_car.color == "진주색"

def test_to_dict():
    """ car -> dict 타입 변환 테스트"""
    obj_car = Car(
        number="12가3456",
        name="이상무",
        phone="01012345678",
        brand="현대",
        color="진주색"
    )

    dict_car = Car.to_dict(obj_car)

    # Case #1 - 타입 변환 검증
    assert isinstance(dict_car, dict)

    # Case #2 - 타입 변환 내용 검증
    assert dict_car["number"] == "12가3456"
    assert dict_car["name"] == "이상무"
    assert dict_car["phone"] == "01012345678"
    assert dict_car["brand"] == "현대"
    assert dict_car["color"] == "진주색"
import pytest
from storm_slime import StormSlime


def test_create_slime():

    slime = StormSlime(
        "S1",
        "Thunder",
        5,
        10,
        1
    )

    assert slime.id == "S1"


def test_size_property():

    slime = StormSlime(
        "S1",
        "Thunder",
        5,
        10,
        1
    )

    assert slime.size == 5.0


def test_invalid_size():

    with pytest.raises(ValueError):

        StormSlime(
            "S1",
            "Thunder",
            -1,
            10,
            1
        )


def test_empty_name():

    with pytest.raises(ValueError):

        StormSlime(
            "S1",
            "",
            5,
            10,
            1
        )


def test_calculate_power_returns_number():

    slime = StormSlime(
        "S1",
        "Thunder",
        5,
        10,
        1
    )

    power = slime.calculate_power()

    assert isinstance(power, float)

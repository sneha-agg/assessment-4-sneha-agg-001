import pytest
from storm_slime import StormSlime


def test_storm_creation():

    slime = StormSlime(
        "1",
        "Storm",
        5,
        10,
        1
    )

    assert slime.id == "1"


def test_charge():

    slime = StormSlime(
        "1",
        "Storm",
        5,
        10,
        1
    )

    slime.charge_storm()

    assert slime.lightning_charge == 20


def test_release_lightning():

    slime = StormSlime(
        "1",
        "Storm",
        5,
        15,
        1
    )

    damage = slime.release_lightning()

    assert damage == 15
    assert slime.lightning_charge == 0


def test_get_slime_type():

    slime = StormSlime(
        "1",
        "Storm",
        5,
        10,
        1
    )

    assert slime.get_slime_type() == "Storm Slime"


def test_negative_charge():

    with pytest.raises(ValueError):

        StormSlime(
            "1",
            "Storm",
            5,
            -1,
            1
        )

import pytest

from laboratory import Laboratory
from storm_slime import StormSlime


def test_add_slime():

    lab = Laboratory()

    slime = StormSlime(
        "1",
        "Storm",
        5,
        10,
        1
    )

    lab.add_slime(slime)

    assert "1" in lab.slimes


def test_remove_slime():

    lab = Laboratory()

    slime = StormSlime(
        "1",
        "Storm",
        5,
        10,
        1
    )

    lab.add_slime(slime)

    lab.remove_slime("1")

    assert "1" not in lab.slimes


def test_remove_missing_slime():

    lab = Laboratory()

    with pytest.raises(KeyError):
        lab.remove_slime("UNKNOWN")


def test_add_none():

    lab = Laboratory()

    with pytest.raises(ValueError):
        lab.add_slime(None)


def test_combine_invalid_id():

    lab = Laboratory()

    with pytest.raises(KeyError):
        lab.combine_slimes(
            "A",
            "B"
        )

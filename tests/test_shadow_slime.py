import pytest
from shadow_slime import ShadowSlime


def test_shadow_creation():

    slime = ShadowSlime(
        "1",
        "Shadow",
        5,
        10,
        True
    )

    assert slime.id == "1"


def test_hide():

    slime = ShadowSlime(
        "1",
        "Shadow",
        5,
        10,
        False
    )

    slime.hide()

    assert slime.stealth_mode is True


def test_reveal():

    slime = ShadowSlime(
        "1",
        "Shadow",
        5,
        10,
        True
    )

    slime.reveal()

    assert slime.stealth_mode is False


def test_get_slime_type():

    slime = ShadowSlime(
        "1",
        "Shadow",
        5,
        10,
        True
    )

    assert slime.get_slime_type() == "Shadow Slime"


def test_negative_density():

    with pytest.raises(ValueError):

        ShadowSlime(
            "1",
            "Shadow",
            5,
            -1,
            True
        )

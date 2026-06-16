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
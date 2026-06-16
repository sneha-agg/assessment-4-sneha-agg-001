from storm_slime import StormSlime


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
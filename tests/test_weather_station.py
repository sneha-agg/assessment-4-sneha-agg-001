import pytest

from weather_station import WeatherStation
from storm_slime import StormSlime


def test_weather_creation():

    station = WeatherStation(
        70,
        1013
    )

    assert station.humidity == 70


def test_boost_storm():

    station = WeatherStation(
        70,
        1013
    )

    slime = StormSlime(
        "1",
        "Storm",
        5,
        10,
        1
    )

    station.boost_storm(slime)

    assert slime.lightning_charge == 15


def test_monitor_conditions():

    station = WeatherStation(
        70,
        1013
    )

    result = station.monitor_conditions()

    assert "Humidity" in result


def test_invalid_humidity():

    with pytest.raises(ValueError):

        WeatherStation(
            150,
            1013
        )

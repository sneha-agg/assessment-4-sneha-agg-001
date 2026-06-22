"""
Integration demonstration for the
Slime Laboratory Management System.

This file demonstrates interactions
between all project classes.
"""

from shadow_slime import ShadowSlime
from storm_slime import StormSlime
from weather_station import WeatherStation
from laboratory import Laboratory


def main():

    print("\n=== SHADOW SLIME ===")

    shadow = ShadowSlime(
        "S001",
        "Darky",
        5,
        8,
        True
    )

    shadow.calculate_power()

    print(shadow)

    print("\n=== STORM SLIME ===")

    storm = StormSlime(
        "ST001",
        "Thunder",
        7,
        20,
        4.5
    )

    storm.calculate_power()

    print(storm)

    print("\n=== WEATHER STATION ===")

    station = WeatherStation(
        humidity=70,
        air_pressure=1013
    )

    station.boost_storm(storm)

    storm.calculate_power()

    print(storm)

    print(
        station.monitor_conditions()
    )

    print("\n=== LABORATORY ===")

    lab = Laboratory()

    lab.add_slime(shadow)
    lab.add_slime(storm)

    print(lab)

    print("\n=== COMBINE SLIMES ===")

    result = lab.combine_slimes(
        shadow.id,
        storm.id
    )

    print(result)

    print(lab)


if __name__ == "__main__":
    main()

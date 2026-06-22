class WeatherStation:
    """
    Simulates environmental conditions
    that affect StormSlime objects.
    """

    def __init__(self, humidity, air_pressure):

        if humidity < 0 or humidity > 100:
            raise ValueError(
                "Humidity must be between 0 and 100."
            )

        self.humidity = humidity
        self.air_pressure = air_pressure

    def boost_storm(self, storm_slime):
        """
        Enhances a StormSlime using
        environmental conditions.
        """

        if storm_slime is None:
            raise ValueError(
                "Storm slime cannot be None."
            )

        storm_slime.lightning_charge += 5
        storm_slime.rain_intensity += 1

    def monitor_conditions(self):
        """
        Return current weather conditions.
        """

        return (
            f"Humidity: {self.humidity}, "
            f"Pressure: {self.air_pressure}"
        )

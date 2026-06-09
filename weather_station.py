class WeatherStation:

    def __init__(self, humidity, air_pressure):
        self.humidity = humidity
        self.air_pressure = air_pressure

    def boost_storm(self, storm_slime):
        storm_slime.lightning_charge += 5
        storm_slime.rain_intensity += 1

    def monitor_conditions(self):
        return (
            f"Humidity: {self.humidity}, "
            f"Pressure: {self.air_pressure}"
        )
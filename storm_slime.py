from slime import Slime


class StormSlime(Slime):

    def __init__(
            self,
            slime_id,
            name,
            size,
            lightning_charge,
            rain_intensity
    ):
        super().__init__(
            slime_id,
            name,
            size,
            base_power=10.0
        )

        self.lightning_charge = lightning_charge
        self.rain_intensity = rain_intensity

    def charge_storm(self):
        self.lightning_charge += 10

    def release_lightning(self):
        damage = self.lightning_charge
        self.lightning_charge = 0
        return damage

    def get_slime_type(self):
        return "Storm Slime"

    def get_special_attributes(self):
        return {
            "lightning_charge": self.lightning_charge,
            "rain_intensity": self.rain_intensity
        }
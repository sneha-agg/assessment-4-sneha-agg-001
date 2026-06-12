from slime import Slime


class ShadowSlime(Slime):

    def __init__(
            self,
            slime_id,
            name,
            size,
            shadow_density,
            stealth_mode
    ):
        super().__init__(
            slime_id,
            name,
            size,
            base_power=8.0
        )

        self.shadow_density = shadow_density
        self.stealth_mode = stealth_mode

    def hide(self):
        self.stealth_mode = True

    def reveal(self):
        self.stealth_mode = False

    def get_slime_type(self):
        return "Shadow Slime"

    def get_special_attributes(self):
        return {
            "shadow_density": self.shadow_density,
            "stealth_mode": self.stealth_mode
        }
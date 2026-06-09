import random
import copy


class Laboratory:

    def __init__(self):
        self.slimes = {}

    def add_slime(self, slime):
        self.slimes[slime.id] = slime

    def remove_slime(self, slime_id):
        self.slimes.pop(slime_id, None)

    def combine_slimes(self, id1, id2):

        if id1 not in self.slimes:
            return None

        if id2 not in self.slimes:
            return None

        slime1 = self.slimes[id1]
        slime2 = self.slimes[id2]

        explosion_chance = (
            slime1.volatility +
            slime2.volatility
        ) / 20

        if random.random() < explosion_chance:

            del self.slimes[id1]
            del self.slimes[id2]

            return "EXPLOSION"

        parent = random.choice([slime1, slime2])

        child = copy.deepcopy(parent)

        child.id = f"{parent.id}_COPY"

        self.slimes[child.id] = child

        return child

    def __str__(self):

        output = "\n=== LABORATORY ===\n"

        for slime in self.slimes.values():

            output += (
                f"{slime.get_slime_type()} "
                f"-> {slime.id}\n"
            )

        return output
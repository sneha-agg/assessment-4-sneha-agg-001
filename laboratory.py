import random
import copy


class Laboratory:
    """
    Stores and manages slime objects.

    Supports adding, removing and
    combining slimes.
    """

    def __init__(self):
        self.slimes = {}

    def add_slime(self, slime):
        """
        Add a slime to the laboratory.
        """

        if slime is None:
            raise ValueError(
                "Cannot add a null slime."
            )

        self.slimes[slime.id] = slime

    def remove_slime(self, slime_id):
        """
        Remove a slime from the laboratory.
        """

        if slime_id not in self.slimes:
            raise KeyError(
                f"Slime {slime_id} does not exist."
            )

        del self.slimes[slime_id]

    def combine_slimes(self, id1, id2):
        """
        Combine two slimes together.

        A combination may result in an
        explosion or a cloned offspring.
        """

        if id1 not in self.slimes:
            raise KeyError(
                f"Slime {id1} not found."
            )

        if id2 not in self.slimes:
            raise KeyError(
                f"Slime {id2} not found."
            )

        slime1 = self.slimes[id1]
        slime2 = self.slimes[id2]

        # Calculate probability of explosion
        explosion_chance = (
            slime1.volatility +
            slime2.volatility
        ) / 20

        if random.random() < explosion_chance:

            del self.slimes[id1]
            del self.slimes[id2]

            return "EXPLOSION"

        parent = random.choice(
            [slime1, slime2]
        )

        # Create offspring slime
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

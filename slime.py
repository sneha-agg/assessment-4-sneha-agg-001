from abc import ABC, abstractmethod
import random
import math


class Slime(ABC):
    """
    Abstract base class representing a slime.

    Provides common attributes and behaviour shared
    by all slime types in the laboratory.
    """

    def __init__(self, slime_id, name, size, base_power=5.0):

        self.id = str(slime_id)

        if not name:
            raise ValueError("Name cannot be empty.")

        self.name = name

        if float(size) <= 0:
            raise ValueError("Size must be greater than zero.")

        self.size = float(size)

        self.volatility = random.randint(0, 10)

        self.base_power = float(base_power)
        self.power = self.base_power

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, str):
            raise TypeError("ID must be a string")
        self._id = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Size must be numeric")

        if value <= 0:
            raise ValueError("Size must be greater than zero.")

        self._size = float(value)

    @abstractmethod
    def get_slime_type(self):
        """Return the slime type."""
        pass

    @abstractmethod
    def get_special_attributes(self):
        """Return slime-specific attributes."""
        pass

    def calculate_power(self):
        """
        Calculates the slime's power based on
        its attributes and special properties.
        """

        power = self.base_power

        attributes = self.get_special_attributes()

        numeric_total = 0
        string_values = []
        bool_values = []

        all_values = [
            self.name,
            self.size,
            self.volatility,
            *attributes.values()
        ]

        for value in all_values:

            if isinstance(value, bool):
                bool_values.append(value)

            elif isinstance(value, (int, float)):
                numeric_total += value

            elif isinstance(value, str):
                string_values.append(
                    sum(ord(char) for char in value)
                )

        power += numeric_total

        if string_values:
            power += (
                sum(string_values) /
                len(string_values)
            ) * math.pi

        for value in bool_values:
            if value:
                power *= 2
            else:
                power /= 2

        self.power = round(power, 2)

        return self.power

    def __str__(self):
        return (
            f"{self.get_slime_type()} "
            f"[ID={self.id}] "
            f"{self.name} "
            f"Power={self.power}"
        )

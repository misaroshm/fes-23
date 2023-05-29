from dataclasses import dataclass

@dataclass
class PersonalInfo:
    """A class representing personal information of an individual."""

    id: int
    _name: str
    address: str
    phone_number: str
    email: str
    position: str
    year: int

    @property
    def name(self):
        """Get the full name of the individual."""
        first_name, second_name = self._name.split("_")
        return first_name, second_name

    @name.setter
    def name(self, value):
        """Set the name of the individual.

        Args:
            value (str): The name to be set.

        Raises:
            ValueError: If the name is not a string.
        """
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

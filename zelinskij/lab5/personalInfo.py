from dataclasses import dataclass

@dataclass
class PersonalInfo:
  

    id: int
    _name: str
    address: str
    phone_number: str
    email: str
    position: str
    year: int

    @property
    def name(self):
        
        first_name, second_name = self._name.split("_")
        return first_name, second_name

    @name.setter
    def name(self, value):
        
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

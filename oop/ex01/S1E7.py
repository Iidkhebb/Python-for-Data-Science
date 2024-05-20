from abc import ABC, abstractmethod
from S1E9 import Character

class Baratheon(Character):
    """
    A class representing a member of House Baratheon, inheriting from Character.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
    
    family_name = "Baratheon"
    eyes = "brown"
    hairs = "dark"

    def die(self):
        """
        Change the health state of the character to False.
        """
        self.is_alive = False

    def __str__(self):
        """
        Return a string representation of the character.
        """
        return f"{self.first_name} {self.family_name} with {self.eyes} eyes and {self.hairs} hair"

    def __repr__(self):
        """
        Return a string representation of the character.
        """
        return f"Baratheon('{self.first_name}', is_alive={self.is_alive})"


class Lannister(Character):
    """
    A class representing a member of House Lannister, inheriting from Character.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """
        Change the health state of the character to False.
        """
        self.is_alive = False

    def __str__(self):
        """
        Return a string representation of the character.
        """
        return f"{self.first_name} {self.family_name} with {self.eyes} eyes and {self.hairs} hair"

    def __repr__(self):
        """
        Return a string representation of the character.
        """
        return f"Lannister('{self.first_name}', is_alive={self.is_alive})"

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """
        Class method to create a Lannister character.
        
        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): The health state of the character. Defaults to True.

        Returns:
            Lannister: A new instance of the Lannister class.
        """
        return cls(first_name, is_alive)

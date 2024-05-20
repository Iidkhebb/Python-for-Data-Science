from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract base class representing a character.

    Attributes:
        first_name (str): The first name of the character.
        is_alive (bool): The health state of the character.
        Defaults to True.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize the character with a first name and
        an optional health state.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): The health state of the
            character. Defaults to True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Method to change the health state of the character to False.
        """
        pass


class Stark(Character):
    """
    A class representing a member of House Stark, inheriting from Character.
    """

    def die(self):
        """
        Change the health state of the character to False.
        """
        self.is_alive = False

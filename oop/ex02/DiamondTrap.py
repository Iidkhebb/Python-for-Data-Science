from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    @property
    def eyes(self):
        return self._eyes
    
    @eyes.setter
    def eyes(self, value):
        self._eyes = value
    
    @property
    def hairs(self):
        return self._hairs
    
    @hairs.setter
    def hairs(self, value):
        self._hairs = value

    def set_eyes(self, color):
        self._eyes = color
    
    def get_eyes(self):
        return self._eyes
    
    def set_hairs(self, color):
        self._hairs = color
    
    def get_hairs(self):
        return self._hairs

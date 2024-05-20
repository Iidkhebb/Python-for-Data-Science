class calculator:
    def __init__(self, vector):
        self.vector = vector
    
    def set_vector(self, new_vector):
        self.vector = new_vector

    def __add__(self, scalar):
        result = [x + scalar for x in self.vector]
        self.set_vector(result)
        print(result)
        return result

    def __mul__(self, scalar):
        result = [x * scalar for x in self.vector]
        self.set_vector(result)
        print(result)
        return result

    def __sub__(self, scalar):
        result = [x - scalar for x in self.vector]
        self.set_vector(result)
        print(result)
        return result

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError("Division by zero")
        result = [x / scalar for x in self.vector]
        self.set_vector(result)
        print(result)
        return result
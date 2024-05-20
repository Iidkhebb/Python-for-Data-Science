class calculator:
    @staticmethod
    def dotproduct(V1, V2):
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {result}")
        return result

    @staticmethod
    def add_vec(V1, V2):
        result = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is: {result}")
        return result

    @staticmethod
    def sous_vec(V1, V2):
        result = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
        return result
class Vector:
    def __init__(self, values=None, size=0, initial_value=0) -> None:
        if values is not None:
            self.values = values
            self.present = [True for _ in values]
        else:
            self.values = [initial_value for _ in range(size)]
            self.present = [False for _ in range(size)]


    def __repr__(self) -> str:
        return f'Vector(values={self.values})'

    def __getitem__(self, index):
        return self.values[index]
    
    def __setitem__(self, index, value):
        self.values[index] = value
        self.present[index] = True

    def multiply(self, value):
        n = 0
        while n < len(self.values):
            self.values[n] *= value
            n += 1
    
    def add(self, other_vector):
        if len(self.values) == len(other_vector.values):
            for index in range(len(self.values)):
                self.values[index] += other_vector.values[index]
        else:
            raise RuntimeError(f'Vectors must be same size to add them.')
    
    def isPresent(self, index):
        return self.present[index]
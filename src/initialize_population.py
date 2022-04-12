
from random import sample


class Population:

    def __init__(self, matrix, n):
        self.matrix = matrix
        self.n = n

    def initialize_population(self) -> [[]]:

        population = []
        m = []

        for value in range(len(self.matrix)):
            m.append(value)

        for individual in range(self.n):
            population.append(sample(m, len(m)))

        return population

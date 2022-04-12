from random import random, sample


class Mutation:
    def __init__(self, population, mutation_rate):
        self.population = population
        self.mutation_rate = mutation_rate

        # This is an exchange mutation

    def mutation(self) -> [[]]:
        mutated_pop = []
        for individual in self.population:
            if random() <= self.mutation_rate:
                x, y = sample(range(len(individual)), 2)
                individual[x], individual[y] = individual[y], individual[x]

            mutated_pop.append(individual)

        return mutated_pop

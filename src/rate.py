

class Rate:

    def __init__(self, population, matrix):
        self.population = population
        self.matrix = matrix

    def rate(self) -> [[], ]:
        rates = []
        for costs in self.population:
            temp_rate = []
            i = 0
            for cost in costs:
                try:
                    temp_rate.append(self.matrix[costs[i]][costs[i + 1]])
                    i += 1
                except IndexError:  # return route
                    temp_rate.append(self.matrix[costs[-1]][costs[0]])
            rates.append(sum(temp_rate))

        return [[self.population[individual], rates[individual]]
                for individual in range(len(self.population))]


from random import sample, choice


class Selection:

    def __init__(self, number_of_tournaments: int, k: int, population: []):
        self.k = k
        self.number_of_tournaments = number_of_tournaments
        self.population = population

    def flatten(self, list_of_lists):
        if len(list_of_lists) == 0:
            return list_of_lists
        if isinstance(list_of_lists[0], list):
            return self.flatten(list_of_lists[0]) + self.flatten(list_of_lists[1:])
        return list_of_lists[:1] + self.flatten(list_of_lists[1:])

    def select(self) -> [[]]:

        # This is a tournament selection

        tournaments = []
        [tournaments.append(sample(self.population, self.k)) for t in range(self.number_of_tournaments)]

        winners = []
        for bracket in tournaments:
            bracket_rates = []
            [bracket_rates.append(x[1]) for x in bracket]
            bracket_winner = []
            for individual, rate in enumerate(bracket_rates):
                if rate == min(bracket_rates):
                    bracket_winner.append(bracket[individual])
                else:
                    continue
            if len(bracket_winner) > 1:
                bracket_winner = [choice(bracket_winner)]
            winners.append(bracket_winner)

        return [x[0] for x in [item for sublist in winners for item in sublist]]

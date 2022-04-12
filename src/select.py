
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
        for t in range(self.number_of_tournaments):
            bracket = sample(self.population, self.k)
            tournaments.append(bracket)

        winners = []
        for bracket in tournaments:
            score = []
            [score.append(x[1]) for x in bracket]
            winner = []
            for index, x in enumerate(score):
                if x == min(score):
                    winner.append(bracket[index])
                else:
                    continue
            if len(winner) != 1:
                winner = [choice(winner)]
            winners.append(winner)

        return [x[0] for x in [item for sublist in winners for item in sublist]]

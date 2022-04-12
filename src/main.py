
from initialize_population import Population
from create_matrix_from_file import Matrix
from rate import Rate
from select import Selection
from crossover import OX
from mutate import Mutation


def main():

    file_path = "C:/Users/Jan/zsi_tsp/data/berlin52.txt"  # absolute path to the text file
    starting_matrix = Matrix(file_path).create_matrix()

    n = 10  # the number of individuals of the starting population - parameter
    starting_population = Population(starting_matrix, n).initialize_population()
    pop_rates = Rate(starting_population, starting_matrix).rate()

    number_of_generations = 1000  # number of generations - parameter

    number_of_tournaments = 50  # tournament selection parameters
    k = 2

    crossover_chance = 0.6  # OX crossover chance - parameter
    mutation_chance = 0.01  # mutation chance - parameter

    min_routes = []
    best_individuals = []

    t = 0  # number of temp population

    while not t == number_of_generations:
        pop = Selection(number_of_tournaments, k, pop_rates).select()
        pop = OX(pop, crossover_chance).crossover()
        pop = Mutation(pop, mutation_chance).mutation()
        pop_rates = Rate(pop, starting_matrix).rate()

        rates = []
        for individual in pop_rates:
            rates.append(individual[1])

        min_routes.append(min(rates))
        if min(min_routes) >= min(rates):
            for index, rate in enumerate(rates):
                if rate == min(rates):
                    if pop_rates[index] not in best_individuals:
                        best_individuals.append(pop_rates[index])

        t += 1

    best_individual = []
    rates = []
    for individual in best_individuals:
        rates.append(individual[1])

    for index, rate in enumerate(rates):
        if rate == min(rates):
            best_individual = best_individuals[index]

    print("-".join(map(str, best_individual[0])), best_individual[1])


if __name__ == "__main__":
    main()

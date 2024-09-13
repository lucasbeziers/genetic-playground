import random
from individual import Individual

# Class Population
class Population:
    def __init__(self, population_size, genome_size, mutation_rate, max_generations):
        self.population_size = population_size
        self.genome_size = genome_size
        self.mutation_rate = mutation_rate
        self.max_generations = max_generations
        self.optimal_generation = max_generations
        self.population = self.create_population()

    # Creates an initial random population
    def create_population(self):
        return [Individual([random.randint(0, 1) for _ in range(self.genome_size)]) for _ in range(self.population_size)]

    # Selects two parents using a tournament selection
    def selection(self):
        participants = random.sample(self.population, 3)
        parents = sorted(participants, key=lambda indiv: indiv.fitness, reverse=True)[:2]
        return parents

    # Crossover between two parents
    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, self.genome_size - 1)
        child1_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
        child2_genes = parent2.genes[:crossover_point] + parent1.genes[crossover_point:]
        return Individual(child1_genes), Individual(child2_genes)

    # Random mutation on an individual
    def mutation(self, individual):
        for i in range(len(individual.genes)):
            if random.random() < self.mutation_rate:
                individual.genes[i] = 1 - individual.genes[i]

    # Evolves the population over multiple generations
    def evolve(self):
        for generation in range(self.max_generations):
            print(f'Generation {generation}')
            # Calculate fitness for each individual
            for individual in self.population:
                individual.calculate_fitness()

            # Sort the population by fitness
            self.population.sort(key=lambda x: x.fitness, reverse=True)
            print(f'Best fitness is {self.population[0].fitness} by {self.population[0].genes}')

            # If the optimal solution is found (e.g., max sum of genes)
            if self.population[0].fitness == self.genome_size:
                print(f'Optimal solution found at generation {generation}!')
                self.optimal_generation = generation
                break

            # Selection, crossover, and mutation to create the next generation
            new_population = []
            while len(new_population) < self.population_size:
                parent1, parent2 = self.selection()
                child1, child2 = self.crossover(parent1, parent2)
                self.mutation(child1)
                self.mutation(child2)
                new_population.append(child1)
                new_population.append(child2)

            # Replace the current population
            self.population = new_population[:self.population_size]

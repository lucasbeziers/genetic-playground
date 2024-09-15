import random
import numpy as np
from src.individual import Individual
from src.utils import GenesType

default_max_integer_genes_type = 10
default_max_float_genes_type = 1

# Class Population
class Population:
    def __init__(self, population_size, mutation_rate, genes_length, max_generations, genes_type, genes_max_value = 1):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.max_generations = max_generations
        self.genes_length = genes_length
        self.genes_type = genes_type
        self.genes_max_value = genes_max_value
        
        self.optimal_generation = max_generations
        self.population = self.create_population()

    # Creates an initial random population
    def create_population(self):
        return [Individual(genes_type=self.genes_type, genes_max_value=self.genes_max_value, genes_length=self.genes_length) for _ in range(self.population_size)]

    # Selects two parents using a tournament selection
    def selection(self):
        # Roulette wheel selection based on fitness
        sum_fitness = sum(individual.fitness for individual in self.population)
        if sum_fitness == 0:
            return random.sample(self.population, 2)  # Fallback to random selection if no fitness
        selection_probs = [individual.fitness / sum_fitness for individual in self.population]
        parents = np.random.choice(self.population, size=2, p=selection_probs)
        return parents

    # Evolves the population over multiple generations
    def evolve(self):
        for generation in range(self.max_generations):
            print(f'Generation {generation}')

            # Sort the population by fitness
            self.population.sort(key=lambda x: x.fitness, reverse=True)
            print(f'Best fitness is {self.population[0].fitness} by {self.population[0].genes}')

            # If the optimal solution is found (e.g., max sum of genes)
            if self.population[0].fitness == self.genes_length:
                print(f'Optimal solution found at generation {generation}!')
                self.optimal_generation = generation
                break

            # Selection, crossover, and mutation to create the next generation
            new_population = []
            while len(new_population) < self.population_size:
                parent1, parent2 = self.selection()
                child1, child2 = parent1.crossover(parent2)
                child1.mutate(self.mutation_rate)
                child2.mutate(self.mutation_rate)
                new_population.append(child1)
                new_population.append(child2)

            # Replace the current population
            self.population = new_population[:self.population_size]

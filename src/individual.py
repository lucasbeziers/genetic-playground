from random import random, randint, uniform
from src.utils import GenesType, FitnessName
from src.fitness import Fitness

# Class Individual
class Individual:
    def __init__(self, genes_type:GenesType, fitness_name=FitnessName.SUM, genes_max_value=1, genes_length=10, genes=None):
        # If no genes provided, generate them
        if genes is None:
            if genes_type == GenesType.INTEGER:
                self.genes = [randint(0,genes_max_value) for _ in range(genes_length)]
            if genes_type == GenesType.FLOAT:
                self.genes = [uniform(0,genes_max_value) for _ in range(genes_length)] 
        else:
            self.genes = genes[::]
            genes_length = len(genes)
        self.fitness = Fitness(fitness_name=fitness_name, genes_length=genes_length, genes_max_value=genes_max_value)
        self.genes_length = genes_length
        self.genes_type = genes_type
        self.genes_max_value = genes_max_value
        self.calculate_fitness()

    # Fitness calculation (must be customized for the problem)
    def calculate_fitness(self):
        self.fitness_score = self.fitness.function(self.genes)

    def crossover(self, partner):
        # Single-point crossover
        crossover_point = randint(1, self.genes_length - 1)
        child1_genes = self.genes[:crossover_point] + partner.genes[crossover_point:]
        child2_genes = partner.genes[:crossover_point] + self.genes[crossover_point:]
        return Individual(genes_type=self.genes_type, genes=child1_genes, genes_max_value=self.genes_max_value), Individual(genes_type=self.genes_type, genes=child2_genes, genes_max_value=self.genes_max_value)
    
    def mutate(self, mutation_rate):
        # Mutate based on mutation rate
        for i in range(self.genes_length):
            if random() < mutation_rate:
                if self.genes_type == GenesType.INTEGER:
                    self.genes[i] = randint(0, self.genes_max_value)
                if self.genes_type == GenesType.FLOAT:
                    self.genes[i] = uniform(0, self.genes_max_value)
        self.calculate_fitness()
    
    # String representation for debugging
    def __repr__(self):
        return f'Individual(genes={self.genes}, fitness={self.fitness_score})'
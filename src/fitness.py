from enum import Enum
from src.utils import FitnessName

def even_function(genes):
    count = 0
    for gene in genes:
        if gene % 2 == 0:
            count += 1
    return count

class Fitness:
    def __init__(self,fitness_name,genes_length,genes_max_value):
        if fitness_name is FitnessName.SUM:
            self.name = fitness_name
            self.function = lambda genes : sum(genes)
            self.optimal_solution = genes_max_value*genes_length
        
        if fitness_name is FitnessName.EVEN:
            self.name = fitness_name
            self.function = lambda genes : even_function(genes)
            self.optimal_solution = genes_length
    
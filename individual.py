# Class Individual
class Individual:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = 0

    # Fitness calculation (must be customized for the problem)
    def calculate_fitness(self):
        # Example: maximize the sum of genes (this should be modified according to the problem)
        self.fitness = sum(self.genes)

    # String representation for debugging
    def __repr__(self):
        return f'Individual(genes={self.genes}, fitness={self.fitness})'
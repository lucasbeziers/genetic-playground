import numpy as np
import matplotlib.pyplot as plt

from population import Population

# Example usage
if __name__ == '__main__':
    # Parameters
    population_size = 10
    genome_size = 16
    # mutation_rate = 0.1
    max_generations = 1000
    tries_per_gen = 1
    step = 0.02
    
    mutation_rate_values = np.arange(0,1,step)
    mean_optimal_generation = np.zeros_like(mutation_rate_values)
    
    for i in range(len(mutation_rate_values)):
        mutation_rate = mutation_rate_values[i]
        optimal_generations = np.zeros(tries_per_gen)
        for t in range(tries_per_gen):
            # Initialize and run the genetic algorithm
            pop = Population(population_size, genome_size, mutation_rate, max_generations)
            pop.evolve()
            optimal_generations[t] = pop.optimal_generation
        mean_optimal_generation[i] = np.mean(optimal_generations)
    
plt.figure(0)
plt.plot(mutation_rate_values,mean_optimal_generation,'r.-')
plt.show()
            
        
        

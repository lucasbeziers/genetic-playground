from src.population import Population
from src.utils import GenesType, FitnessName
from src.individual import Individual

# Test initialization of the population class
def test_population_init():
    population_size = 10
    mutation_rate = 0.1
    genes_length = 5
    max_generations = 100
    genes_type = GenesType.INTEGER
    genes_max_value = 10

    population = Population(population_size=population_size,
                            mutation_rate=mutation_rate,
                            genes_length=genes_length,
                            max_generations=max_generations,
                            genes_type=genes_type,
                            genes_max_value=genes_max_value)
    
    # Ensure population is created with correct size
    assert len(population.population) == population_size
    # Ensure individuals are of correct type and attributes
    for individual in population.population:
        assert individual.genes_type == genes_type
        assert individual.genes_max_value == genes_max_value
        assert len(individual.genes) == genes_length


# Test selection method (ensure that it returns two individuals)
def test_selection():
    population_size = 10
    mutation_rate = 0.1
    genes_length = 5
    max_generations = 100
    genes_type = GenesType.INTEGER
    genes_max_value = 10

    population = Population(population_size=population_size,
                            mutation_rate=mutation_rate,
                            genes_length=genes_length,
                            max_generations=max_generations,
                            genes_type=genes_type,
                            genes_max_value=genes_max_value)
    
    # Set random fitness values for testing selection
    for i, individual in enumerate(population.population):
        individual.fitness_score = i + 1  # Fitness values from 1 to population_size
    
    # Ensure selection returns two individuals
    parent1, parent2 = population.selection()
    assert parent1 is not None
    assert parent2 is not None
    assert isinstance(parent1, Individual)
    assert isinstance(parent2, Individual)
    

# Test evolve method (check that it runs without errors and generations evolve)
def test_evolve():
    population_size = 10
    mutation_rate = 0.1
    genes_length = 5
    max_generations = 10
    genes_type = GenesType.INTEGER
    genes_max_value = 10
    fitness_name=FitnessName.EVEN

    population = Population(population_size=population_size,
                            mutation_rate=mutation_rate,
                            genes_length=genes_length,
                            max_generations=max_generations,
                            genes_type=genes_type,
                            genes_max_value=genes_max_value,
                            fitness_name=fitness_name)

    # Mock fitness values to force early convergence
    for individual in population.population:
        individual.fitness_score = genes_length - 1

    # Run evolution process
    population.evolve()

    # Check if population evolved and optimal generation is tracked correctly
    assert population.optimal_generation <= max_generations


# Test that crossover produces valid offspring
def test_crossover_in_population():
    population_size = 10
    mutation_rate = 0.1
    genes_length = 5
    max_generations = 10
    genes_type = GenesType.INTEGER
    genes_max_value = 10
    fitness_name=FitnessName.EVEN

    population = Population(population_size=population_size,
                            mutation_rate=mutation_rate,
                            genes_length=genes_length,
                            max_generations=max_generations,
                            genes_type=genes_type,
                            genes_max_value=genes_max_value,
                            fitness_name=fitness_name)
    
    # Test crossover of selected parents
    parent1, parent2 = population.selection()
    child1, child2 = parent1.crossover(parent2)

    # Ensure children are valid individuals
    assert isinstance(child1, Individual)
    assert isinstance(child2, Individual)
    # Ensure the children's genes match the length and max value constraints
    assert len(child1.genes) == genes_length
    assert len(child2.genes) == genes_length
    assert max(child1.genes) <= genes_max_value
    assert max(child2.genes) <= genes_max_value


# Test mutation in the population
def test_mutation_in_population():
    population_size = 10
    mutation_rate = 1  # High mutation rate for testing
    genes_length = 5
    max_generations = 10
    genes_type = GenesType.INTEGER
    genes_max_value = 10
    fitness_name=FitnessName.EVEN

    population = Population(population_size=population_size,
                            mutation_rate=mutation_rate,
                            genes_length=genes_length,
                            max_generations=max_generations,
                            genes_type=genes_type,
                            genes_max_value=genes_max_value,
                            fitness_name=fitness_name)
    
    # Test mutation of individuals in the population
    for individual in population.population:
        original_genes = individual.genes.copy()
        individual.mutate(mutation_rate)
        
        # Check that mutation occurred (genes should differ in most cases)
        assert original_genes != individual.genes
        # Ensure genes are still valid (within max value)
        assert max(individual.genes) <= genes_max_value
        assert len(individual.genes) == genes_length

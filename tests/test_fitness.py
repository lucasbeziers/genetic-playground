from src.utils import FitnessName
from src.fitness import Fitness

# Test initialization for SUM fitness function
def test_fitness_sum_initialization():
    genes_length = 5
    genes_max_value = 10
    fitness = Fitness(FitnessName.SUM, genes_length, genes_max_value)

    # Check that the correct function is assigned
    assert fitness.name == FitnessName.SUM
    assert callable(fitness.function)

    # Check that the optimal solution is correctly set
    expected_optimal = genes_max_value * genes_length
    assert fitness.optimal_solution == expected_optimal

# Test initialization for EVEN fitness function
def test_fitness_even_initialization():
    genes_length = 5
    genes_max_value = 10  # This value is irrelevant for the EVEN fitness

    fitness = Fitness(FitnessName.EVEN, genes_length, genes_max_value)

    # Check that the correct function is assigned
    assert fitness.name == FitnessName.EVEN
    assert callable(fitness.function)

    # Check that the optimal solution is correctly set (maximum number of even genes)
    assert fitness.optimal_solution == genes_length
    
# Test initialization for ALTERNATE fitness function
def test_fitness_alternate_initialization():
    genes_length = 5
    genes_max_value = 10

    fitness = Fitness(FitnessName.ALTERNATE, genes_length, genes_max_value)

    # Check that the correct function is assigned
    assert fitness.name == FitnessName.ALTERNATE
    assert callable(fitness.function)

    # Check that the optimal solution is correctly set (maximum number of even genes)
    assert fitness.optimal_solution == genes_max_value * ((genes_length // 2) + 1)

# Test SUM fitness function calculation
def test_fitness_sum_function():
    genes_length = 5
    genes_max_value = 10
    fitness = Fitness(FitnessName.SUM, genes_length, genes_max_value)

    genes = [1, 2, 3, 4, 5]
    expected_fitness = sum(genes)
    
    # Ensure the fitness function calculates correctly
    assert fitness.function(genes) == expected_fitness

# Test EVEN fitness function calculation
def test_fitness_even_function():
    genes_length = 5
    genes_max_value = 10  # This value is irrelevant for the EVEN fitness

    fitness = Fitness(FitnessName.EVEN, genes_length, genes_max_value)

    genes = [1, 2, 3, 4, 5]
    expected_fitness = 2  # 2 even numbers (2 and 4)

    # Ensure the fitness function calculates correctly
    assert fitness.function(genes) == expected_fitness

# Test ALTERNATE fitness function calculation
def test_fitness_alternate_function():
    genes_length = 5
    genes_max_value = 10

    fitness = Fitness(FitnessName.ALTERNATE, genes_length, genes_max_value)

    genes = [1, 2, 3, 4, 5]
    expected_fitness = 3 # (1 + 3 + 5) - (2 + 4)

    # Ensure the fitness function calculates correctly
    assert fitness.function(genes) == expected_fitness

# Test optimal solution calculation for SUM fitness
def test_fitness_sum_optimal_solution():
    genes_length = 5
    genes_max_value = 10
    fitness = Fitness(FitnessName.SUM, genes_length, genes_max_value)

    # Create a gene sequence that represents the optimal solution
    optimal_genes = [genes_max_value] * genes_length
    optimal_fitness = fitness.function(optimal_genes)

    # Ensure that the calculated fitness matches the optimal solution
    assert optimal_fitness == fitness.optimal_solution

# Test optimal solution calculation for EVEN fitness
def test_fitness_even_optimal_solution():
    genes_length = 5
    genes_max_value = 10  # This value is irrelevant for the EVEN fitness

    fitness = Fitness(FitnessName.EVEN, genes_length, genes_max_value)

    # Create a gene sequence that represents the optimal solution (all even numbers)
    optimal_genes = [2] * genes_length
    optimal_fitness = fitness.function(optimal_genes)

    # Ensure that the calculated fitness matches the optimal solution
    assert optimal_fitness == fitness.optimal_solution
    
# Test optimal solution calculation for ALTERNATE fitness
def test_fitness_alternate_optimal_solution():
    genes_length = 5
    genes_max_value = 10

    fitness = Fitness(FitnessName.ALTERNATE, genes_length, genes_max_value)

    # Create a gene sequence that represents the optimal solution
    # (alternating between the maximum and minimum values)
    optimal_genes = [genes_max_value, 0, genes_max_value, 0, genes_max_value]
    optimal_fitness = fitness.function(optimal_genes)

    # Ensure that the calculated fitness matches the optimal solution
    assert optimal_fitness == fitness.optimal_solution  

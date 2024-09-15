from src.utils import GenesType
from src.individual import Individual

# Can create individual
def test_init():
    indiv_int = Individual(genes_type=GenesType.INTEGER)
    indiv_float = Individual(genes_type=GenesType.FLOAT)
    assert (indiv_int is not None) and (indiv_float is not None)
    assert True

def test_attributes():
    indiv1 = Individual(genes_type=GenesType.INTEGER, genes_max_value=10, genes_length=5)
    assert max(indiv1.genes) <= indiv1.genes_max_value
    assert len(indiv1.genes) == indiv1.genes_length
    
    indiv2 = Individual(genes_type=GenesType.INTEGER,genes=[0,1,2,3], genes_max_value=3)
    assert indiv2.fitness is not None

def test_crossover():
    parent1 = Individual(genes_type=GenesType.INTEGER)
    parent2 = Individual(genes_type=GenesType.INTEGER)
    child1, child2 = parent1.crossover(parent2)
    child3, child4 = parent2.crossover(parent1)
    assert child1.genes_type == parent1.genes_type
    assert child1.genes_length == parent1.genes_length
    assert child1.genes_max_value == parent1.genes_max_value

def test_mutate():
    original_genes = [0 for _ in range(10)]
    indiv = Individual(genes_type=GenesType.INTEGER, genes=original_genes, genes_max_value=1)
    indiv.mutate(0)
    assert indiv.genes == original_genes
    indiv.mutate(1)
    assert indiv.genes != original_genes
    assert max(indiv.genes) <= 1
    assert indiv.genes_length == len(original_genes)
    assert indiv.genes_max_value == 1
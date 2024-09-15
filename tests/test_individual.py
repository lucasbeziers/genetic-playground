from src.utils import GenesType
from src.individual import Individual

# Can create individual
def test_init():
    indiv_int = Individual(genes_type=GenesType.INTEGER)
    indiv_float = Individual(genes_type=GenesType.FLOAT)
    assert (indiv_int is not None) and (indiv_float is not None)
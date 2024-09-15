from enum import Enum

# Possible genes
class GenesType(Enum):
    INTEGER = "integer"
    FLOAT = "float"

# Different fitness functions
def sum_genes(genes):
    return sum(genes)
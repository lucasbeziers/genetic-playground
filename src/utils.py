from enum import Enum

# Possible genes
class GenesType(Enum):
    INTEGER = "integer"
    FLOAT = "float"

# Possible fitness functions
class FitnessName(Enum):
    SUM = "sum"
    EVEN = "even"
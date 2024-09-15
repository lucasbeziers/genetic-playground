from enum import Enum

# Possible genes
class GenesType(Enum):
    INTEGER = "Integer"
    FLOAT = "Float"

# Possible fitness functions
class FitnessName(Enum):
    SUM = "Sum"
    EVEN = "Even"
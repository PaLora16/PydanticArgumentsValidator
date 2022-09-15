from src.classic_validation import validate as classic_validation
from src.pydantic_validation import validate as pydantic_validation

if __name__ == "__main__":
    # valid
    classic_validation(3.11, "USD", "EUR")
    # Raise TypeError amount must be float
    classic_validation("3", "USD", "EUR")

    # valid
    pydantic_validation(3.11, "GPB", "EUR")
    # valid due to pydantic implicit type converison
    pydantic_validation("3", "GPB", "EUR")


from typing import Annotated

from pydantic import Field, validate_arguments


class Currency(str):
    allowed_symbols = ("USD", "EUR", "JPY", "GPB", "CHF", "CAD", "AUD", "HKD")

    @classmethod
    def validate(cls, v):
        if not isinstance(v, str):
            raise TypeError("Pydantic check : string required")
        if v not in cls.allowed_symbols:
            raise ValueError(
                f"Pydantic check : {v} is not member of {cls.allowed_symbols}"
            )
        return v

    @classmethod
    def __get_validators__(cls):
        yield cls.validate


@validate_arguments
def pydantic_check(
    amount:  Annotated[float, Field(gt=0)], 
    from_currency: Currency,
    to_currency: Currency
) -> None:
    '''Validation is based on validate_argumets decorator, 
    which depends on typing.Annotated to verify float value 
    and on custom Currency type which contains __get_validators__ 
    called by decorator to verify constraints.'''
    print("Pydantic check OK")


def  validate(amount: float, from_currency: Currency, to_currency: Currency):
    try:
        pydantic_check(amount, from_currency, to_currency)
    except Exception as e:
        print(e)

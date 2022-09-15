def classic_check(amount, from_currency, to_currency, allowed_symbols) -> None:
    """Old fashioned type control"""
    if not isinstance(amount, float):
        raise TypeError("Classic check : amount must be float")
    
    if amount <= 0:
        raise ValueError("Classic check : Amount must be >=0")

    if type(allowed_symbols) != tuple:
        raise TypeError("Classic check : improper format of allowed_symbols")

    if from_currency not in allowed_symbols:
        raise ValueError(
            f"Classic check : {from_currency} is not member of {allowed_symbols}"
        )
    if to_currency not in allowed_symbols:
        raise ValueError(
            f"Classic check : {to_currency} is not member of {allowed_symbols}"
        )

    print("Classic check OK")




def validate(amount: float, from_currency: str, to_currency: str):
    try:
        classic_check(
            amount,
            from_currency,
            to_currency,
            ("USD", "EUR", "JPY", "GPB", "CHF", "CAD", "AUD", "HKD"),
        )
    except Exception as e:
        print(e)



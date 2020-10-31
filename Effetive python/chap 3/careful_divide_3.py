def careful_divide(a: float, b: float) -> float:
    try:
        return a / b

    except ZeroDivisionError as e:
        raise ValueError('Invalid Input')

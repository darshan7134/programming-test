def generate_odd_series(a: int) -> str:
    """
    Generate a series of odd numbers up to the given integer a.

    Args:
        a (int): The upper limit for the series.

    Returns:
        str: A comma-separated string of odd numbers.
    """
    if a < 1:
        return "Input must be a positive integer."

    odd_numbers = [str(2 * i + 1) for i in range(a)]
    return ', '.join(odd_numbers)


if __name__ == "__main__":
    a = int(input("Enter a positive integer: "))
    result = generate_odd_series(a)
    print(result)
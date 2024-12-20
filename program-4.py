def count_multiples(numbers):
    """
    Count the numbers in the input list that are multiples of each number from 1 to 9.

    Args:
        numbers (list): A list of integers.

    Returns:
        dict: A dictionary where the keys are the numbers from 1 to 9 and the values are the counts of multiples.
    """
    multiples_count = {i: 0 for i in range(1, 10)}

    for num in numbers:
        for i in range(1, 10):
            if num % i == 0:
                multiples_count[i] += 1

    return multiples_count


if __name__ == "__main__":
    numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
    result = count_multiples(numbers)
    print(result)

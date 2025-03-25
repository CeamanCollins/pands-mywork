import logging
# logging.basicConfig(level=logging.DEBUG)

def fibonacci(number):
    if number == 0:
        return []
    if number < 0:
        raise ValueError('number must be > 0')
    a = 0
    b = 1
    fibonacci_sequence = [0]
    for i in range(1, number):
        fibonacci_sequence.append(b)
        a, b = b, a + b
    logging.debug("%d: %s",number, fibonacci_sequence)
    try:
        return fibonacci_sequence
    except ValueError:
        pass
    else:
        assert False, 'Fibonacci missing value error'


if __name__ == "__main__":
    # test cases
    return11 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    assert fibonacci(7) == return11[:7]
    assert fibonacci(11) == return11
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    print("All good!")
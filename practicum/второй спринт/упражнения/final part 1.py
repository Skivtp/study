def fibonacci(n):
    # Допишите функцию.
    num_a, num_b = 0, 1

    for n in range(n):
        yield num_a
        num_a, num_b = num_b, num_a + num_b


sequence = fibonacci(130)
for number in sequence:
    print(number)
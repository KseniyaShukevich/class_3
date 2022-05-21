def pow_numbers(x, y):
    if x <= 0 or not isinstance(x, int):
        print('x должен быть целым положительным числом')

    if y >= 0 or not isinstance(y, int):
        print('y должен быть целым отрицательным числом')

    divider = x

    for i in range(1, abs(y)):
        divider *= x

    return 1 / divider


print(pow_numbers(5, -4))

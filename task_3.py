def sum_max_numbers(a, b, c):
    arr = [a, b, c]
    min_number = min(arr)
    arr.remove(min_number)

    return sum(arr)


print(sum_max_numbers(1, -5, 3))

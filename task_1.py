def divide(a, b):
    try:
        return int(a) / int(b)
    except (TypeError, ValueError) as error:
        print('Деление производится только с числами', error)
    except ZeroDivisionError as error:
        print('Нельзя делить на ноль', error)


dividend = input('Введите делимое: ')
divider = input('Введите делитель: ')

print(divide(dividend, divider))

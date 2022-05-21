sum_all_numbers = 0
isProcessing = True


def get_messages():
    print('Для завершения подсчета введите символ "x"')

    return input('Введите числа, разделенные пробелом: ')


def sum_numbers(string):
    global sum_all_numbers

    numbers = string.split()

    for item in numbers:
        if item == 'x':
            global isProcessing
            isProcessing = False
            break

        try:
            sum_all_numbers += float(item)
        except ValueError as error:
            print('Введены неверные данные: ', error)
            print('Сумма чисел: ', sum_all_numbers)
            sum_numbers(get_messages())

    return sum_all_numbers


while isProcessing:
    user_string = get_messages()
    print('Сумма чисел: ', sum_numbers(user_string))

def print_data(**kwargs):
    result = []

    for key, value in kwargs.items():
        result.append(f'{key}: {value}')

    print(', '.join(result))


print_data(first_name='Kate', last_name='Koval', birth=1997, city='Minsk', email='keta@test.com', telephon=2144323)

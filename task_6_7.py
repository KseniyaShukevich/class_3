def get_word_title(word):
    small_symbols = range(97, 122)
    step = 97 - 65

    for symbol in word:
        if ord(symbol) not in small_symbols:
            print('Допустимы только латинские буквы в нижнем регистре!')
            return

    new_word = chr(ord(word[0:1]) - step) + word[1:]

    return new_word


print('Все буквы должны быть латинскими в нижнем регистре!')
string = input('Введите строку из слов, разделенных пробелами: ').strip()
words = string.split()
result = []

for item in words:
    word_title = get_word_title(item)

    if not word_title:
        break

    result.append(word_title)

if len(result) == len(words):
    print(' '.join(result))

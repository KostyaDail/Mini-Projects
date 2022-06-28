"""
Аве, Цезарь
На вход программе подается условие: Шифрование или Дешифрование и строка текста на английском языке,
в которой нужно зашифровать (дешифровать) все слова. Каждое слово строки будет зашифровано (дешифровано)
с помощью шифра Цезаря (циклического сдвига на длину этого слова).
Строчные буквы при этом остаются строчными, а прописные – прописными.

Формат входных данных
Условие: Шифрование или Дешифрование
Строка текста на английском языке.

Формат выходных данных
Программа должна вывести зашифрованный (дешифрованный) текст в соответствии с условием задачи.

Примечание. Символы, не являющиеся английскими буквами, не изменяются.
"""


def main_menu():
    choose_encr_decr()


def encrypt(text: str):
    words = []

    for word in text.split():
        new_word = ''
        word_len = len([c for c in word if c.isupper() or c.islower()])

        for char in word:
            if char.isupper():
                new_word += chr((ord(char) + word_len - 65) % 26 + 65)
            elif char.islower():
                new_word += chr((ord(char) + word_len - 97) % 26 + 97)
            else:
                new_word += char
        words.append(new_word)

    print(' '.join(words))


def decrypt(text: str):  # Дешифровка текста
    words = []

    for word in text.split():
        new_word = ''
        word_len = len([c for c in word if c.isupper() or c.islower()])

        for char in word:
            if char.isupper():
                new_word += chr((ord(char) - word_len - 65) % 26 + 65)
            elif char.islower():
                new_word += chr((ord(char) - word_len - 97) % 26 + 97)
            else:
                new_word += char
        words.append(new_word)

    print(' '.join(words))


def choose_encr_decr():  # Выбор Шифрование или Дешифрование
    enc = input('Выберите действие: s=Шифрование/d=Дешифрование: ').lower()
    if enc == 's':
        encrypt(enter_text())
    elif enc == 'd':
        decrypt(enter_text())
    else:
        print('<---Вы не выбрали необходимое действие--->')
        choose_encr_decr()


def enter_text():  # Ввод текста
    text = input('Введите текст: ')
    while not text:
        print('<---Для шифрования (дешифрования) текста, нужен текст, а не пустота--->')
        text = input('Введите текст: ')
    return text



print('Шифратор/Дешифратор Цезаря приветствует тебя.')

main_menu()

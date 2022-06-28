# Самая часто повторяющаяся буква в слове

"""
На вход программе подается строка. Программа найдет самую часто повторяющуюся букву в этой строке, знаки препинания,
цифры и пробелы учитываться не будут, регистр не имеет значения. Если в тексте две и больше буквы с одинаковой частотой,
тогда результатом будет буква, которая идет первой в алфавите.
"""

import string

word = input("Введите слово: ")
while not word:
    word = input("Введите слово: ")

while not word.isalpha():
    print("Ваше слово содержит цифры или некорректные символы\n")
    word = input("Введите слово: ")

set_word = list(set(word.lower()))
arr = []
len_word = len(word)
for i in set_word:
    arr.append(word.lower().count(i))
arr_max = max(arr)

if arr_max == 1:
    print("Нет повторяющихся букв")
else:
    result = max(string.ascii_lowercase, key=lambda ch: word.lower().count(ch))
    print(f"Длина слова {len_word}")
    print(f"Самая часто повторяющаяся буква в слове '{word}': {result}, количество повторений: {arr_max}")

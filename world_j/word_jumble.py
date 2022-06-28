# Word Jumble
#
# Программа выбирает какое-либо слово и хаотически переставляет его буквы
# Задача игрока - восстановить исходное слово

import random

# Создадим последовательность слов, из которых программа будет выбирать
WORDS = ("питон", "автор", "невежа", "гербарий", "ответ", "мансарда", "ностальгия", "симбиоз", "прокрастинация")

# Создадим подсказки к словам
HINTS = ("змея",
         "творец чего-нибудь",
         "невоспитанный человек",
         "коллекция засушенных растений",
         "высказывание, сообщение, вызванное вопросом",
         "эксплуатируемое чердачное пространство",
         "радостные воспоминания о доме"
         "Совместное существование двух организмов разных видов",
         "Нездоровая склонность человека к постоянному откладыванию дел «на потом»")

# Создадим переменные для начисления очков и штрафов.
point = 0
BONUS = 100
FINE = 30

# случайным образом выберем из последовательности одно слово
word = random.choice(WORDS)

# создадим переменную, с которой будет затем сопоставлена версия игрока
correct = word

# создадим анаграмму выбранного слова, в котором буквы будут раставлены хаотично
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# начало игры
print(
    """
               Добро пожаловать в игру 'Анаграммы'!
    
       Надо переставить буквы так, чтобы получилось осмысленное слово. 
    (Для выхода нажмите Enter, не вводя своей версии.)
    """
)
print("Вот анаграмма:", jumble)
print("(Для подсказки введите - ?)")
guess = input("\nПопробуйте отгадать исходное слово: ")

while guess.lower() != correct and guess != "":
    if point <= -80:
        print("Вы проиграли!")
        exit()
    if guess == "?":
        point -= FINE
        print()
        print(f"Подсказка: {HINTS[WORDS.index(correct)]}")
        guess = input("Попробуйте отгадать исходное слово: ")
    else:
        point -= 5
        print("К сожалению, вы не правы.")
        guess = input("Попробуйте отгадать исходное слово: ")

if guess.lower() == correct:
    point += BONUS
    if point <= 30:
        print("\nНичоси, Вы угадали. Но...")
        print("Ваш интеллект упал на дно!")
    else:
        print("\nДа, именно так! Вы отгадали!")
        print(f"У Вас {point} очков.\n")

print("Спасибо за игру.")

input("\n\nНажмите Enter, чтобы выйти.")

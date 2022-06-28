# Игра угадай число от 1 до 100
from random import randint as r


# Генерируем случайное число от 1 до 100
def get_num():
    my_num = r(1, 100)
    return my_num


# Проверяем число на валидность
def is_valid(user_num):
    if user_num.isdigit():
        user_num = int(user_num)
        if 1 <= user_num <= 100:
            return True
        else:
            print("Ваше число не входит в диапазон от 1 до 100.")
            print("¯\_(ツ)_/¯\n")
            return False
    else:
        print("А может быть все-таки введем целое число от 1 до 100?")
        print("¯\_(ツ)_/¯\n")
        return False


# Игра=)
def play(number):
    cnt = 0
    while True:
        user_num = input("Я загадал число от 1 до 100 - угадай его: ")
        if not is_valid(user_num):
            continue
        cnt += 1
        user_num = int(user_num)
        if user_num == number:
            print(f"\nПравильно {user_num}. Ты угадал число! Количество попыток: {cnt}")
            print("\(＾◡＾)/\n")
            break

        elif user_num > number:
            print(f"\nМое число меньше {user_num}, попробуйте еще разок")
        else:
            print(f"\nМое число больше {user_num}, попробуйте еще разок")


# Рестарт игры
def restart():
    answer = input('Cыграем еще раз? "y|n": ').lower()
    while answer not in ("y", "n"):
        print("ШТА??? Некорректный ввод\n")
        answer = input('Хотите сыграть еще раз? "y|n": ').lower()
    return answer


# Старт игры
again = 'y'
print('Добро пожаловать в игру "Угадай число"')

while again == 'y':
    num = get_num()
    play(num)
    again = restart()

print("Спасибо за игру!")
input("\n\nНажмите Enter, чтобы выйти.")

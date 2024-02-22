import random

def guess_number_game():
    # Задаем диапазон угадывания
    min_number = 1
    max_number = 100
    # Генерируем случайное число в заданном диапазоне
    secret_number = random.randint(min_number, max_number)
    number_of_guesses = 0

    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"Я загадал число между {min_number} и {max_number}. Попробуйте угадать его с наименьшего количества попыток.")

    while True:
        # Пользователь вводит свою догадку
        guess = input("Введите ваше число: ")
        if not guess.isdigit():
            print("Пожалуйста, введите корректное числовое значение.")
            continue
        guess = int(guess)
        number_of_guesses += 1

        # Проверка догадки и выдача подсказок
        if guess < secret_number:
            print("Слишком мало, попробуйте еще раз.")
        elif guess > secret_number:
            print("Слишком много, попробуйте еще раз.")
        else:
            print(f"Поздравляем! Вы угадали число с {number_of_guesses} попытки.")
            break  # Выход из цикла, если число угадано

    # Предложение сыграть еще раз
    play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
    if play_again == "да":
        guess_number_game()
    else:
        print("Спасибо за игру!")

if __name__ == "__main__":
    guess_number_game()

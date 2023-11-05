import random
import time

your_first__cub_result = random.choice([1, 2, 3, 4, 5, 6])
your_second__cub_result = random.choice([1, 2, 3, 4, 5, 6])
computer_first__cub_result = random.choice([1, 2, 3, 4, 5, 6])
computer_second__cub_result = random.choice([1, 2, 3, 4, 5, 6])
end_game_answer = str("")
a = str("")
while end_game_answer == "" or end_game_answer == "1":
    a = int(input("Вибери час калатання кубиків від 1 до 5 "))
    i = 1
    while a < 1 or a > 5:
        if a < 1:
            print("Мусиш хоч трішки калатнути кубики")
            a = int(input("Вибери час калатання кубиків від 1 до 5 "))
        if a > 5:
            print("Довше ніж 5 секунд калатати не можна")
            a = int(input("Вибери час калатання кубиків від 1 до 5 "))
    while a > (i - 1):
        print(a)
        a = a - i
        time.sleep(0.7)
    print("Ваш результат: ")
    your_first__cub_result = random.choice([1, 2, 3, 4, 5, 6])
    your_second__cub_result = random.choice([1, 2, 3, 4, 5, 6])
    print(your_first__cub_result, your_second__cub_result)
    print("Результат комп'ютера: ")
    computer_first__cub_result = random.choice([1, 2, 3, 4, 5, 6])
    computer_second__cub_result = random.choice([1, 2, 3, 4, 5, 6])
    print(computer_first__cub_result, computer_second__cub_result)
    if (
        your_first__cub_result + your_second__cub_result
        > computer_first__cub_result + computer_second__cub_result
    ):
        print("Вітаю, ти переміг!!!")
    elif (
        your_first__cub_result + your_second__cub_result
        < computer_first__cub_result + computer_second__cub_result
    ):
        print("На жаль, ти програв :(")
    else:
        print("Нічия. Спробуй ще раз")
    end_game_answer = input(
        "Хочеш зіграти ще раз? Якщо так - натисни 1 або клавішу Enter, якщо ні - будь-яку іншу цифру або літеру "
    )
print("Ну ок, гарного дня :)")

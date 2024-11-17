# src/my_module.py

# Привітання
def greet(name):
    return f"Привіт, {name}!"

# Функція для перевірки парності числа
def is_even(number):
    return number % 2 == 0

# Основна частина програми
if __name__ == "__main__":
    name = input("Введіть ваше ім'я: ")
    print(greet(name))

    # Введення числа
    number = int(input("Введіть число: "))

    # Перевірка парності
    if is_even(number):
        print(f"{number} - парне число.")
    else:
        print(f"{number} - непарне число.")

    # Цикл для виведення чисел від 1 до 5
    print("Числа від 1 до 5:")
    for i in range(1, 6):
        print(i)

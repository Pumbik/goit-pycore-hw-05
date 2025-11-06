from typing import Callable

def generator_numbers(text: str):
    words = text.split()

    for word in words:
        try:
            # якщо слово приводиться до float --> число
            number = float(word)
            yield number
        except ValueError:
            continue


def sum_profit(text: str, func: Callable):
    #  викликаємо генератор
    num_gen = func(text)
    #  підсумовуємо всі числа з генератора
    total = sum(num_gen)
    return total


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
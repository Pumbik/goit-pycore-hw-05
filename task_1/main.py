def caching_fibonacci():
    cach = {}

    def fibonacci(n):
        if n <=0:
            return 0
        if n == 1:
            return 1
        # Перевіка --> чи є результат у кеші
        if n not in cach:
            # Рекурсивно викликаемо --> зберігаємо у кеш
            cach[n] = fibonacci(n-1) + fibonacci(n-2)
        
        return cach[n]

    return fibonacci


# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
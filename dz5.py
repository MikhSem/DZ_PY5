# Задача 26:

def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)

# запрос числа и степени у пользователя
a = int(input("Введите число A: "))
b = int(input("Введите степень B: "))

# вызов функции power() и вывод результата на экран
result = power(a, b)
print(f"{a} в степени {b} равно {result}")

# Задача 28: 

def recursive_sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return recursive_sum(a - 1, b + 1)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

result = recursive_sum(a, b)

print(f"Сумма чисел {a} и {b} равна {result}")

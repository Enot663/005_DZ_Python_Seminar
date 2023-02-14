# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.




# 1 Variant

# def sum(a, b):
#     if b > a:
#         a, b = b, a
#     if b == 0:
#         return a
#     return 1 + sum(a, b - 1)

# 2 Variant

def sum(a, b):
    if b == 0:
        return a
    else:
        if b > 0:
            return sum(a + 1, b - 1)
        else:
            return sum(a - 1, b + 1)
print(sum(int(input('Введите первое число a: ')), int(input('Введите второе число b: '))))
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.




# 1 Variant

# def summ(a, b):
#     if b > a:
#         a, b = b, a
#     if b == 0:
#         return a
#     return 1 + summ(a, b - 1)

# 2 Variant

def summ(a, b):
    if b == 0:
        return a        
    if b > 0:
        return summ(a + 1, b - 1)      
    return summ(a - 1, b + 1)
print(summ(int(input('Введите первое число a: ')), int(input('Введите второе число b: '))))
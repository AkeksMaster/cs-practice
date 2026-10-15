a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

print("Сумма:", a + b)
print("Разность:", a - b)
print("Произведение:", a * b)

if b != 0:
    print("Частное:", a / b)
else:
    print("Ошибка: деление на ноль")

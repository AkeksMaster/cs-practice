import numpy as np


# Задание 1

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print(hours)
print(hours.shape)
print(hours.ndim)
print(hours.size)
print(hours.dtype)


# Задание 2

print(hours[2])
print(hours[-1])
print(hours[2:6])
print(hours[::2])
print(hours[::-1])


# Задание 3

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print(temperatures.shape)
print(temperatures.ndim)
print(temperatures.size)

print(temperatures[1, 2])
print(temperatures[0])
print(temperatures[:, -1])
print(temperatures[:2, 1:])

central = temperatures[:2, 1:3]
print(central)
print(central.shape)

# Задание 4

matrix = np.arange(1, 26).reshape(5, 5)

part = matrix[:3, :]
print(part)
print(part.shape)

part = matrix[-2:, :]
print(part)
print(part.shape)

part = matrix[:, :2]
print(part)
print(part.shape)

part = matrix[1:4, 2:5]
print(part)
print(part.shape)

part = matrix[-2:, -2:]
print(part)
print(part.shape)


# Задание 5

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

# copy() создаёт независимую копию и сохраняет исходный массив.
changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print(changed_hours)
print(hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print(changed_matrix)
print(matrix)


# Задание 6

numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print(numbers.shape)
print(table.shape)
print(transposed.shape)

# reshape(3, 4) работает, потому что 3 * 4 = 12.
# reshape(5, 3) вызовет ошибку, потому что 5 * 3 = 15,
# а исходный массив содержит только 12 элементов.
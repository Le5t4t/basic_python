# Задание 1. Создание списков
cities = ["Москва", "Тверь", "Вологда"]
numbers = [1, 2, 3, 4, 5]
mixed = [10, "Python", True, 3.14]
print(cities, numbers, mixed, sep="\n")

# Задание 2. Доступ к элементам списка
print(cities[0], numbers[-1], mixed[1], sep="\n")

# Задание 3. Изменение элементов списка
numbers[1] = 10
mixed[-1] = "Stepik"
print( numbers, mixed, sep="\n")

# Задание 4. Функции для работы со спискам

print( len(numbers),min(numbers), max(numbers), sum(numbers), sorted(numbers), sep="\n")

#Задание 5. Срезы списков

letters = ["a", "b", "c", "d", "e"]
print(letters[1:4])
print(letters[:3])
print(letters[3:])
print(letters[::-1])

# Задание 6. Методы списков

marks = [3, 4, 5]
marks.append(5)
marks.insert(0, 2)
print(marks)
print(marks.count(5))
print(marks.index(4))
marks.reverse()
print(marks)
marks.sort()
print(marks)

# Задание 7. Вложенный список

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
print(matrix[1][1])
print(matrix[2][2])

# Задание 8. Повторение прошлых тем

course = "Python"
lesson = 5
print(f"{course} lesson {lesson}")

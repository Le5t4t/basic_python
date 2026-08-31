


#a = int(input())
#b = int(input())
#print(f"Сумма: {a + b} \n"
#       f"Произведение: {a * b}")

import tkinter as tk
from os.path import sep
from tkinter import ttk

from lesson_1.homework_1 import height

"""
n = int(input())
print(f"Четное: {n % 2 == 0}")
print(f"Делится на 3: {n % 3 == 0}")
print(f"От 10 до 99: {10 <= n <= 99}")


a = input()
print(a[0])
print(a[-1])
print(a[::-1])


text = input()
word = "Python"
result = word in text
print(len(text))
print(result)
"""
#Часть 1. print(), sep, end и f-строки
print("Привет, мир!")
print(f"5 10 15")
print(10 + 25)
print("1","2","3",sep = '&')
print("Python", end=" ")
print("лучший язык")
x = 3.14
y = -8
print(f"Координаты точки: x ={x}; y ={y}")
#Часть 2. input() и преобразование типов
name = input("Введите имя: ")
print(f"Привет, {name}!")
age = int(input("Возраст: "))
print(f"Имя: {name}, Возраст: {age} лет")

width = int(input("Введи первое число: "))
height = int(input("Введи второе число: "))
print(float((width + height) * 2))
#Часть 3. Булевые значения
print(
5 > 3,
10 < 2,
7 == 7,
6 != 8,
4 >= 4,
9 <= 3, sep='\n'
)
res = 8 > 12
print(type(res))
x = 15
print(x % 2 == 0,
x % 5 == 0,
x % 3 == 0 and x % 5 == 0)
y = 4.5
print( 1 <= y <= 10)
print(0 <= y <= 5 and 10 <= y <= 15)
print(not y < 5)
var = [0, -5 , 3.14, "", "Python", " "]
for v in var:
 print(f"{v!r} -> {bool(v)}")
 #Часть 4. Индексы и срезы строк
s = "Программирование"
print(s[0])
print(s[-1])
print(s[2])
print(s[-2])
print(s[0:6])
print(s[-5:])
print(s[2:8])
print(s[::2])
print(s[::-1])
print(s[1:-1])

#s[0] = "п"
s2 = "п" + s[1:]
print(s2)
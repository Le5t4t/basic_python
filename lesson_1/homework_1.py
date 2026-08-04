name = "Vlad"
age = 39
height = 1.75
print(f"Имя: {name}")
print(f"Возраст: {age}")
print(f"Рост: {height} ")

x = 10
print(type(x))
x = 25.5
print(type(x))
x_str = str(25.5)
print(x_str, type(x_str))

a = 7
b = a
print(a, b)
a = 10
print(b)
# значение переменной b не изменилось потому, что присвоение значения переменной b было до изменения зачения переменной а

x = y = z = 100
print(id(x),id(y),id(z))
x,y,z = 333,999,777
print(id(x),id(y),id(z))

a,b = 5,10
print(a,b)
a,b = b,a
print(a,b)

import keyword
print(keyword.kwlist)
# ЗАРЕЗЕРВИРОВАННЫЕ ИНТЕРПРИТАТОРОМ СЛОВА, МОЖНО ПЕРЕОПРЕДЕЛИТЬ НО НЕ СТОИТ , ТАК КАК ВЫЗЫВАЮТ ВСТРОИННЫЕ ФУНЦИИ. ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
# 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
var1 = 42.
var2 = 3.14
var3 = "Hello"
print(var1, type(var1))
print(var2, type(var2))
print(var3, type(var3))
var1_str = str(var1)
print(var1_str, type(var1_str))

user_name = "Vlad"
user_age = 39
user_height = 1.75
user_skill = "Python"
user_size = "Math"
переменная = "рас" # переменная работает выдает результат
print(user_name, type(user_name))
print(user_age, type(user_age))
print(user_height, type(user_height))
print(user_skill, type(user_skill))
print(user_size, type(user_size))
print(переменная, type(переменная))

s = "Python для автоматизации"
print(s.upper(),s.lower(),s, sep="\n")

msg = "абракадабра"
print(msg.count("а"),msg.count("ра"),msg.find("ка"),msg.rfind("а"), sep="\n")

text = "Я изучаю Java"
text = text.replace("Java", "Python")
print(text)

code = " lesson-4-python "
code = code.strip().replace("-", " ")
print(code)

tools = "Python, PyCharm, Git, GitHub"
tools = tools.split(", ")
tools = " | ".join(tools)
print(tools)

print("Урок 4 \nСтроки в Python")
path = "C:\new\test.txt"
print(path)
print(r"C:\new\test.txt")

name = "Даниил"
age = 35
course = "Python"
print(f"Меня зовут {name}, мне {age} лет. Я изучаю { course}.")

FOrM = "Курс {} подходит для старта в автоматизации.".format(course)
print(FOrM)

a = 10
b = 5
print(a + b , a - b, a * b, a / b, sep="\n")


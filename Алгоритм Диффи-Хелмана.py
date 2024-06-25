import random
a = int(input("Введите числовое сообщение:"))
b = int(random.randint(1, 100))
print("Коэфициент b:", b)
g = int(random.randint(1, 100))
print("Коэфициент g:",g)
p = int(random.randint(1, 100))
print("Коэфициент p:",p)
A = (g**a)%p
print("Коэфициент для общего ключа (А):",A)
B = (g**b)%p
print("Коэфициент для общего ключа (А):", B)
Ka = (B**a)%p
print("Ваш общий ключ:", Ka)
Kb = (A**b)%p
print("Общий ключ приятеля:",Kb)
print("Ka = Kb =",Kb)
def prime(h):
    if h <= 1:
        return False
    for i in range(2, int(h**0.5) + 1):
        if h%i == 0:
            return False
        return True


p = int(input("Введите p:"))
q = int(input("Введите q:"))
n = int(p*q)
print("Число n:", n)
f = int((q-1)*(p-1))
print("Число f:", f)
e = []
for prime_zn in range(1, f):
    if (prime(prime_zn) == True) and (f%prime_zn != 0):
        e.append(prime_zn)
print("Открытый ключ:","{", e[0], ";", n, "}")
d = []
for d_zn in range(1, 500):
    if (d_zn*e[0])%f == 1:
        d.append(d_zn)
print("Закрытый ключ:","{", d[0], ";", n, "}")
P0 = int(input("Введите сообщение (Число, взятое в роли сообщения должно быть не больше n):"))
crypt = (P0**e[0])%n
print("Закриптованное сообщение:", crypt)
question = str(input("Произвести обратную раскриптовку? (Да или нет):"))
if question == "Да" or "да":
    print("Раскриптованное сообщение:", (crypt**d[0])%n)
else:
    print("Хорошо. Работа окончена")

first = 1
second = 2
third = 3
if first == second and second == third:
    print(3)
elif first == second or second == third or first:
    print(2)
elif first != second and second != third and first != third:
    print(0)
else:
    print("ololo попячся")

first = input(int("Введите число №1: "))
second = input(int("Введите число №2: "))
third = input(int("Введите число №3: "))


if first == second and second == third:
    print(3)
elif first == second or second == third or first:
    print(2)
elif first != second and second != third and first != third:
    print(0)
else:
    print("ololo попячся")
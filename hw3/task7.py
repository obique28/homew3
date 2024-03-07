n = int(input("Введіть кількість рядів: "))

a= 0
for i in range(1, n + 1):
  a += i

print(f"В піраміді {n} рядів є {a} яблук.")

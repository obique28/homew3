a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

sum = 0
for i in range(a, b + 1):
  sum += i

print(f"Сума чисел від a до b: {sum}")

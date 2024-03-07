n = int(input("Введіть число n: "))

c = 0
for i in range(1, n + 1):
  if n % i == 0 and i == n // i:
    c += 1

print(f"Кількість рівних дільників числа {n}: {c}")

d= int(input("Введіть кількість днів: "))

c = 8
tc = 0

for i in range(1, d + 1):
  c += i
  tc += c

print(f"За {d} днів дівчинка купуватиме {c} цукерок.")
print(f"Всього за {d} днів вона купить {tc} цукерок.")

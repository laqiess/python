import math
a = 1

for i in range(2, 11):
    a *= math.sqrt(1 - 1 / (i * (i-1)))
print(f"в результате цикла получаем:",a)

from itertools import permutations
import time

# Перестановка - это упорядоченная выборка объектов.
# К примеру, 3124 является одной из возможных перестановок
# из цифр 1, 2, 3 и 4. Если все перестановки приведены в
# порядке возрастания или алфавитном порядке, то такой порядок
# будем называть словарным. Словарные перестановки из цифр 0, 1 и 2 представлены ниже:
# 012   021   102   120   201   210
# Какова миллионная словарная перестановка из цифр 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9?

st = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
start = time.time()
p = permutations(st)
ls_p = list(p)
# for i in range(1000001):
#     print(f'{i:>7d} -> {"".join(ls_p[i])}')
total = time.time() - start
print(f"Ответ: {''.join(ls_p[999999])}\nВыполнено за: {total} секунд")


# Ответ: 2783915460
# Выполнено за 0.8774611949920654 секунд

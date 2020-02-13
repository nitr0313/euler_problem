
# Перестановка - это упорядоченная выборка объектов.
# К примеру, 3124 является одной из возможных перестановок
# из цифр 1, 2, 3 и 4. Если все перестановки приведены в
# порядке возрастания или алфавитном порядке, то такой порядок
# будем называть словарным. Словарные перестановки из цифр 0, 1 и 2 представлены ниже:
# 012   021   102   120   201   210
# Какова миллионная словарная перестановка из цифр 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9?

st = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# ['0', '1', '2', '3', '4', '5', '6', '7', '9', '8'] 1
# ['0', '1', '2', '3', '4', '5', '6', '8', '7', '9'] 2
# ['0', '1', '2', '3', '4', '5', '6', '8', '9', '7'] 3
# ['0', '1', '2', '3', '4', '5', '6', '9', '7', '8'] 4
# ['0', '1', '2', '3', '4', '5', '6', '9', '8', '7'] 5
# ['0', '1', '2', '3', '4', '5', '7', '6', '8', '9'] 6
# ['0', '1', '2', '3', '4', '5', '7', '6', '9', '8'] 7
# ['0', '1', '2', '3', '4', '5', '7', '8', '6', '9'] 8
# ['0', '1', '2', '3', '4', '5', '7', '8', '9', '6'] 9
# ['0', '1', '2', '3', '4', '5', '7', '9', '6', '8'] 10
# ['0', '1', '2', '3', '4', '5', '7', '9', '8', '6'] 11
# ['0', '1', '2', '3', '4', '5', '8', '6', '7', '9'] 12
# ['0', '1', '2', '3', '4', '5', '8', '6', '9', '7'] 13
# ['0', '1', '2', '3', '4', '5', '8', '9', '6', '7'] 14
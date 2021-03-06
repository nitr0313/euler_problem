import time
from sympy import isprime
# Идеальным числом называется число, у которого сумма его делителей
# равна самому числу. Например, сумма делителей числа 28 равна
# 1 + 2 + 4 + 7 + 14 = 28, что означает, что число 28 является идеальным числом.

# Число n называется недостаточным, если сумма его делителей меньше n,
# и называется избыточным, если сумма его делителей больше n.

# Так как число 12 является наименьшим избыточным числом (1 + 2 + 3 + 4 + 6 = 16),
# наименьшее число, которое может быть записано как сумма двух избыточных чисел,
# равно 24. Используя математический анализ, можно показать, что все целые числа
# больше 28123 могут быть записаны как сумма двух избыточных чисел. Эта граница
# не может быть уменьшена дальнейшим анализом, даже несмотря на то, что наибольшее
# число, которое не может быть записано как сумма двух избыточных чисел, меньше этой границы.

# Найдите сумму всех положительных чисел, которые не могут быть записаны как сумма двух
# избыточных чисел.

N = 28123

def factors(num: int):
    """ Функция вычисляет делители числа и возвращает их списком
    input num int
    return set
    """
    res = {1}
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            res.add(i)
            # if i != num//i:
            res.add(num//i)
    return res


def sums_abudant(res=None):
    all_digs = { x for x in range(1, N+1) }  # Все числа
    abudant_digs = [x for x in range(12, N-11) if sum(factors(x)) > x]  # Все избыточные числа
    sums = { abudant_digs[x] + abudant_digs[y] for x in range(len(abudant_digs))
                for y in range(x, len(abudant_digs)) } # Все возможные суммы пар избыточных чисел
    result = sum(list(all_digs-sums)) # Остаются только те числа которые не могут быть получены суммой избыточных
    return result  # 4179871


if __name__ == "__main__":
    start = time.time()
    result = sums_abudant()
    mess = f'Решено верно! Ответ: {result}' if result == 4179871 else f'Решение не верно! Ответ: {result}, а должен быть 4179871'
    print(mess)
    elapsed = (time.time() - start)
    print(f'Затрачено времени: {elapsed}')


# Решено верно! Ответ: 4179871
# Затрачено времени: 4.74907660484314

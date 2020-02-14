from sympy import isprime
import time
import json

# n2+n+41
# Оказалось, что согласно данной формуле можно получить 40
# простых чисел, последовательно подставляя значения 0≤n≤39.
# Однако, при n = 40, 402+40+41 = 40(40+1)+41 делится на 41 без
# остатка, и, очевидно, при n = 41, 412+41+41 делится на 41 без остатка.

# При помощи компьютеров была найдена невероятная формула n2−79n+1601,
# согласно которой можно получить 80 простых чисел для последовательных
# значений n от 0 до 79. Произведение коэффициентов −79 и 1601 равно −126479.

# Рассмотрим квадратичную формулу вида:

# n2+an+b, где | a | <1000 и | b |≤1000

# где | n | является модулем(абсолютным значением) n.
# К примеру, | 11 |= 11 и |−4 |= 4
# Найдите произведение коэффициентов a и b квадратичного выражения, согласно
# которому можно получить максимальное количество простых чисел для последовательных
# значений n, начиная со значения n = 0.

res = {} # a*b:{'a':a,'b':b,'primes':{},'p_len':len(primes) }
base_file = 'p27_base.json'


def test_formula(a,b):
    global res
    ans = 1
    n = 0
    tmp_lst = set()
    while True:
        ans = n*n + a*n + b
        if isprime(ans):
            tmp_lst.add(ans)
            n+=1
            continue
        else:
            break
#    tmp_lst = list(tmp_lst)
#    res[a*b] = {'a': a, 'b': b, 'primes': tmp_lst, 'p_len': len(lst)}
    return len(tmp_lst)

def main():
    max_p = 0
    result = {0:0}
    for a in range(-999,1000):
        for b in range(1001,-1001,-2):
            if not isprime(b) or not isprime(1+a+b):
                continue  # Сильно ускоряет перебор :)
            tmp = test_formula(a,b)
            if tmp > max_p:
                max_p = tmp
                result[max_p] = a*b
    return result[max_p]

def save():
    global res
    with open(base_file, 'w') as fl:
        json.dump(res, fl)

if __name__ == "__main__":
    start = time.time()
    r = main()
    total = time.time() - start
    print(f'Ответ: {r}\nВыполнено за: {total} секунд') #-59231
#    save()

# Ответ: -59231
# Выполнено за: 6.761837005615234 секунд
# "-59231": {"a": -61, "b": 971,
    # "primes": [641, 131, 1033, 1163, 911, 1301,
        #  151, 281, 797, 547, 421, 1447, 41, 43, 173,
        #  47, 691, 53, 313, 61, 1601, 197, 71, 1097,
        #  971, 461, 1231, 593, 83, 853, 347, 1373, 223,
        #  97, 743, 113, 1523, 503, 251, 383],
    # "p_len": 40}

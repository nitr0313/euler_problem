

DEBAG = False


def factors(num):
    """ Функция вычисляет делители числа и возвращает их списком
    input num int
    return list
    """

    res = [1,]
    for i in range(2, int(num**0.5)+2):
        if num%i == 0:
            res.append(i)
            if i != num//i:
                res.append(num//i)

    return sorted(res)



def main(stop):
    res = {}
    for i in range(stop+1):
        tmp = factors(i)
        if len(tmp) == 1:
            continue
        res[i] = sum(tmp)
    counter = 0
    summ = 0

    for k,v in res.items():
        if v in res and res[v] == k and k != v:
            print(f"Дружественные числа {k} с суммой делителей {v} - которая является числом с суммой делитлей {k}")
            summ += k
            counter += 1

    print(counter)
    print(summ)



    pass

def test_factors():
    test = 1
    a = 8
    if factors(a) == [1,2,4]:
        print(f"Test{test} a={a} Ok!")
    else:
        print(f"Test{test} a={a} Fail! {factors(a)}")

    test = 2
    a = 16
    if factors(a) == [1,2,4,8]:
        print(f"Test{test} a={a} Ok!")
    else:
        print(f"Test{test} a={a} Fail! {factors(a)}")

    test = 3
    a = 7
    if factors(a) == [1]:
        print(f"Test{test} a={a} Ok!")
    else:
        print(f"Test{test} a={a} Fail! {factors(a)}")

    test = 4
    a = 220
    if factors(a) == [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]:
        print(f"Test{test} a={a} Ok!")
    else:
        print(f"Test{test} a={a} Fail! {factors(a)}")

    test = 5
    a = 284
    if factors(a) == [1, 2, 4, 71, 142]:
        print(f"Test{test} a={a} Ok!")
    else:
        print(f"Test{test} a={a} Fail! {factors(a)}")

if __name__ == "__main__":
    if DEBAG:
        test_factors()
    else:
        main(10000)



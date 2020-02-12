
import sys

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

    return res




def main():
    res = {x:x for x in range(1,28123)}
    abundant = []
    count = 1
    sums = []

    for i in range(12,28112):
        if i < sum(factors(i)):
            abundant.append(i)

    # print(abundant)
    # print(abundant[-1])

    for i in range(len(abundant)):
        for y in range(i, len(abundant)):
            s = abundant[i] + abundant[y]
            if s > 28123:
                continue
            sums.append(s)
            res.pop(s, 'None')
    sys.exit(1)
    return sum(list(res.keys())) #4178816







if __name__ == "__main__":
    print(main())

    # print(f"787 -> {sum(factors(787))}")

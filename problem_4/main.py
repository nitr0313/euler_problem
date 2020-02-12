


def is_palindrome(st):
    return st == st[::-1]


def main(dig):
    x = y = int('1'+'0'*(dig-1))
    stop = int('9'+'9'*(dig-1))
    tmp = 0
    results = 0
    gg = []
    for i in range(x,stop+1):
        for j in range(y,stop+1):
            tmp = i*j
            if is_palindrome(str(tmp)):
                gg.append((i,j,tmp))
                if results < tmp:
                    results = tmp


                #results.append(tmp)

        j = int('1'+'0'*(dig-1))
    return results,gg



def main2(dig):
    x = y = int('1'+'0'*(dig-1))
    stop = int('9'+'9'*(dig-1))
    tmp = 0
    results = 99999999

    for i in range(x,stop+1):
        for j in range(y,stop+1):
            if is_palindrome(str(i)) and is_palindrome(str(j)) and i == j:
                if is_palindrome(str(i*j)):
                    print("{} * {} = {}".format(i,j,i*j))

        j = int('1'+'0'*(dig-1))
    return results


if __name__ == '__main__':
    dig = 3
    res = main(dig)
    main2(res)

    print("максимальный палиндром!",res[0])
    print(res[1])


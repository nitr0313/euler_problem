
import sys

DEBAG = False

def len_seq(first_num):
    """
    Создает последовательность начмная с first_num(int) по двум правилам
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)
    и возвращает длинну этой последовательности и саму последовательность
    """
    sq = [first_num,]
    while first_num > 1:
        first_num = int(first_num/2) if first_num%2==0 else 3*first_num + 1
        # if first_num%2==0:
        #     first_num = int(first_num/2)
        # else:
        #     first_num = 3*first_num + 1
        sq.append(first_num)
    return len(sq), sq


def main():
    if DEBAG == True:
        test_len_seq()
        sys.exit("Включен режим дебага!")

    max_seq = 0
    for num in range(1000000,1,-1):
        tmp,seq = len_seq(num)
        if max_seq < tmp:
            max_seq = tmp
            f_num = num
    return f_num,max_seq


def test_len_seq():
    num1 = 13
    res = len_seq(13)
    if res[0] == 10:
        print(f"Test1 OK! {res[1]}")
    else:
        print(f"Test1 Fail! {res[1]}")

if __name__ == "__main__":
    print(f"Ответ {main()[0]}\nДлинна последовательности {main()[1]}")


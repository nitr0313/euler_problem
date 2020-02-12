

DEBAG = False

TBL = {
0:"",
1:"one",
2:"two",
3:"three",
4:"four",
5:"five",
6:"six",
7:"seven",
8:"eight",
9:"nine",
10:"ten",
11:"eleven",
12:"twelve",
13:"thirteen",
14:"fourteen",
15:"fifteen",
16:"sixteen",
17:"seventeen",
18:"eighteen",
19:"nineteen",
20:"twenty",
30:"thirty",
40:"forty",
50:"fifty",
60:"sixty",
70:"seventy",
80:"eighty",
90:"ninety",
100:"hundred",
1000:"thousand"
}



def count_letters(a):
    return len([ x for x in list(a) if x.isalpha()])


def int_to_words(x):
    res = ""
    if x == 1000:
        return "one " + TBL[x].strip()

    if x%100 == 0:
        hundred = int(str(x)[0])
        return f"{TBL[hundred]} hundred".strip()
    elif x >= 100:
        hundred = int(str(x)[0])
        res += f"{TBL[hundred]} hundred and "
        x = int(str(x)[1:])

    if x < 20 or x%10 == 0:
        return res + f"{TBL[x]}"
    # elif x %10 == 0:
    #     res += f"{TBL[x]}"
    else:
        tens = int(str(x)[0])
        units = int(str(x)[1])
        res += f"{TBL[tens*10]}-{TBL[units]}"

    return res.strip()


def main():
    res = 0
    for i in range(1,1001):
        words = int_to_words(i)
        count = count_letters(words)
        print(f"{i} \t-> {words} \t-> {count}")
        res += count

    return res

def test_count_letters():
    words = "three hundred and forty-two"
    if count_letters(words) == 23:
        print(f"Test1 \"{words}\" OK!")
    else:
        print(f"Test1 \"{words}\" Fail!")

    words = "one hundred and fifteen"
    if count_letters(words) == 20:
        print(f"Test2 \"{words}\" OK!")
    else:
        print(f"Test2 \"{words}\" Fail!")

def test_int_to_words():
    testNum = 1
    i = 5
    if int_to_words(5) == 'five':
        print(f"Test{testNum} \"{i}\" OK!")
    else:
        print(f"Test{testNum} \"{i}\" Fail! {int_to_words(i)}")

    testNum = 2
    i = 16
    if int_to_words(i) == 'sixteen':
        print(f"Test{testNum} \"{i}\" OK!")
    else:
        print(f"Test{testNum} \"{i}\" Fail! {int_to_words(i)}")

    testNum = 3
    i = 115
    if int_to_words(i) == "one hundred and fifteen":
        print(f"Test{testNum} \"{i}\" OK!")
    else:
        print(f"Test{testNum} \"{i}\" Fail!  {int_to_words(i)}")

    testNum = 4
    i = 342
    if int_to_words(i) == "three hundred and forty-two":
        print(f"Test{testNum} \"{i}\" OK!")
    else:
        print(f"Test{testNum} \"{i}\" Fail! {int_to_words(i)}")

    testNum = 5
    i = 200
    if int_to_words(i) == "two hundred":
        print(f"Test{testNum} \"{i}\" OK!")
    else:
        print(f"Test{testNum} \"{i}\" Fail! {int_to_words(i)}")




    pass

if __name__ == "__main__":
    if DEBAG:
        test_count_letters()
        test_int_to_words()
    else:
        print(main())




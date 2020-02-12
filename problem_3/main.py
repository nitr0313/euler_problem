import sympy

DEBAG = False

def func_delitel(delimoe, delitel):
    return True if (delimoe%delitel == 0) else False

def is_prime(num):
    if num%2 == 0:
        return False
    if num != 3 and num%3 == 0:
        return False
    if num !=5 and  num%5 == 0:
        return False

    for i in range(3,num**0.5,2):
        if num%i==0:
            return False
    return True

def is_prime2(num):
    return sympy.isprime(num)

def main(number):
    if DEBAG:
        import tests
        print(tests.test_func_delitel())
        print(tests.test_is_prime())



    for i in range(int(number**0.5),1,-1):
        if func_delitel(number,i ):
            if is_prime2(i):
                return i
            print(i,'not prime')



if __name__ == '__main__':
    number = 600851475143
    print(main(number))



# День недели по дате d + ((13*m - 1) / / 5 ) + y + (y / /4 + c / / 4 - 2*c + 777)


def week_day(d,m,y):
    """    Возвращает день недели по следующийм параметрам
        d - день
        m - месяц
        y - номер года в столетии
        Возвращает int - номер дня недели где 0- воскресенье и тд
    """
    m = m - 2 if m > 2 else m + 10

    c = y // 100
    y = y%100
    return (d + ((13*m - 1)//5 ) + y + (y//4 + c//4 - 2*c + 777))%7



def main():
    res = 0
    d = 1
    for y in range(1901,2001):
        for m in range(1,13):
            i = week_day(d,m,y)
            if i == 0:
                print(d,m,y,i)
                res += 1
    return res



if __name__ == "__main__":
    print(main())






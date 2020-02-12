

SUMM = 1000


def main(stp):
    res = 0
    for a in range(int(stp*0.5)):
        for b in range(a+1,int(stp*0.5)):
            c = stp - a - b
            if a**2 + b**2 == c**2:
                return a,b,c,a*b*c




if __name__ == "__main__":

    print(main(SUMM))
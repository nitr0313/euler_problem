


scores = {'Y': 25, 'W': 23, 'H': 8, 'T': 20, 'V': 22,
        'Z': 26, 'Q': 17, 'R': 18, 'B': 2, 'P': 16,
        'U': 21, 'E': 5, 'X': 24, 'D': 4, 'J': 10,
        'L': 12, 'A': 1, 'N': 14, 'F': 6, 'S': 19,
        'K': 11, 'G': 7, 'O': 15, 'I': 9, 'M': 13, 'C': 3}

def name_score(i,name):
    res = 0
    for n in name:
        res += scores[n]

    return res*(i+1)


def main():
    with open('p022_names.txt', 'r') as f:
        names = f.readline()

    names = names.strip('"').split('","')
    names.sort()

    res = {}

    for i in range(len(names)):
        res[names[i]] = name_score(i,names[i])

    # print(res['COLIN']) #49714
    return sum(res.values())




if __name__ == "__main__":
    print(main())
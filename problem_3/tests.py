import main
def test_func_delitel():
    print('test_func_delitel ')
    data = {
        (6,2):True,
        (10,5):True,
        (5,2):False,
        (0,5):True,
        (101,2):False
    }
    results = []
    for k,v in data.items():
        if main.func_delitel(k[0],k[1]) == v:
            results.append('Pass')
        else:
            results.append('FAIL')
    return results

def test_is_prime():
    print('test_is_prime ')
    data = {
        5:True,
        9:False,
        6:False,
        739:True,
        997:True,
    }
    results = []
    for k,v in data.items():
        if main.is_prime(k) == v:
            results.append('pass')
        else:
            results.append('fail')
    return results


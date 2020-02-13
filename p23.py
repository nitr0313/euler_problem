import os
import sys
import json
from sympy import isprime

DB = 'p23_base.json'
N = 100 #28123
res = {} # num:{'div':[,],'abundant':Bool, 'sq':Bool, 'prime':Bool}


def first_launch():
    global res
    sq = [ x*x for x in range(2, N**1/2) ]
    
    prime  = [ x for x in range(2, N) if x.isprime() ]
    for pr in prime:
        res[pr] = {'div':[], 'abudant':False,'prime':True,'sq':False}


def load_db():
    with open(DB, 'r') as fl:
        res = json.load(fl)
    return res

def save_db():
    global res
    with open(DB, 'w') as fl:
        json.dump(res, fl)
    return True






import random
from string import ascii_uppercase
from bottle import post, request
import re
import numpy as np
import Floid1
@post('/Floid', method='post')
def Start():
    n=int (request.forms.get('GetValue'))
    M = np.random.randint(0,2,(n,n))
    np.fill_diagonal(M, 0)
    C = np.tril(M) + np.tril(M,-1).T

    for i in range(len(C)):
        for j in range (len(C[i])):
            if (C[i][j] == 1):
                C[i][j] = np.random.randint(1,9)
    for i in range(len(C)):
        for j in range (len(C[i])):
            if (C[i][j] == 0 and i!=j):
                C[i][j] = 99
    T = np.tril(C) + np.tril(C,-1).T

    H=[[]]
    H=np.diag(np.arange(1,n+1))
    return Floid1.floyd(C,T,H,n)
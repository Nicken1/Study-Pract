from math import inf
from itertools import product
import math
def floyd(C,T,H,n):
    f="Прмежуточная матрица путей: "+"<br>"
    for i in range (n):
        for j in range (n):
            T[i][j] = C[i][j]
            if C[i][j] == 99:
                H[i][j]=0        
            elif C[i][j] != 99  and C[i][j] != 0: 
               H[i][j]=j
    for i in range (n):
        for j in range (n):
            f += str(H[i][j]) + " "
        f += "<br>"
    for i in range (n):
        for j in range (n):
            for k in range(n):
                if (i!=j and T[i][j]!=99 and i != k and T[i][k] != 99 and (T[j][k] == 99 or T[j][k] > T[j][i] + T[i][k])):
                    H[j][k] = H[j][i]
                    T[j][k] = T[j][i]+T[i][k]
    for i in range (n):
        if T[j][j] < 0:
            break
    f+="<br>"+"Матрица всех путей: "+"<br>"
    for i in range (n):
        for j in range (n):
            f += str(T[i][j]) + " "
        f += "<br>"
    return f

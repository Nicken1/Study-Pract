import random
from string import ascii_uppercase
from bottle import post, request
import re
import numpy as np
import DextraLogic

@post('/Dextra', method='post')
def Start():
    x=""
    n = int (request.forms.get('GetValue'))
    p = request.forms.get('Litr')
    M = np.random.randint(0,2,(n,n))
    np.fill_diagonal(M, 0)
    m = np.tril(M) + np.tril(M,-1).T
    for i in range(len(m)):
        for j in range (len(m[i])):
            if (m[i][j] == 1):
                m[i][j] = np.random.randint(1,9)
    W = np.tril(m) + np.tril(m,-1).T
    x="Матрица: "+"<br>"
    for i in range (n):
        for j in range (n):
            x += str(W[i][j]) + " "
        x += "<br>"
    j=0
    i=0
    c=[]
    z=""
    for v  in range(n*n):
        if (W[j][i] == 0 and i==n-1):
            c.append(j)
            if (j==n-1):
                print("вершина ",c)
                break
            else:
                i=0
                j=j+1
                continue
        elif(W[j][i] == 0 and i!=n-1):
            i=i+1
            continue
        elif(W[j][i] != 0 and j==n-1):
            if not c:
                print ('Нет пустых вершин')
                break
            else:
                print("вершина ",c)
                break
        elif(W[j][i] != 0 and j!=n-1):
            i=0
            j=j+1
            continue
    


    cities_count = len(W)
    for weights in W:
        assert len(weights) == cities_count
    city_labels = None
    if not city_labels:
        city_labels = [ascii_uppercase[x] for x in range(cities_count)]

    assert cities_count <= len(city_labels)
    print ('Список вершин: ',city_labels)
    for i in range(len(city_labels)):
        if (p==city_labels[i]):
            start_ver=i
            break
    i=0
    l=[]
    k=[]
    for f in range (n*n):
        if W[start_ver][i]==0 and i!=n-1:
           i=i+1
           continue
        elif W[start_ver][i]==0 and i==n-1:
             break
        elif W[start_ver][i]!=0:
             l.append(i)
             if i!=n-1:
                i=i+1
             elif i==n-1:
                  break
    if len(l)==1:
       i=0
       for f in range (n*n):
           if W[l[0]][i]==0 and i!=n-1:
              i=i+1
              continue
           elif W[l[0]][i]==0 and i==n-1:
                break
           elif W[l[0]][i]!=0 and i!=n-1:
                k.append(i)
                i=i+1
                continue
           elif W[l[0]][i]!=0 and i==n-1:
                k.append(i)
                break

    return (x+"<br>"+"Кратчайшие пути: "+"<br>"+DextraLogic.dijkstra(start_ver,c,l,k,city_labels,n,W))
    
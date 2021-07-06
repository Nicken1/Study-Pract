import unittest
from string import ascii_uppercase
import sys
import numpy as np
class Test_test_1(unittest.TestCase):
    def test_A(self):
        z=[0,9,2,0]
        n=4
        W = [[0, 0, 2, 0],
            [0, 0, 7, 0],
            [2, 7, 0, 1],
            [0, 0, 0, 0]]
        j=0
        i=0
        c=[]
        for v  in range(n*n):
            if (W[j][i] == 0 and i==n-1):
                c.append(j)
                if (j==n-1):
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
                    break
                else:
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
        start_ver=0
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

        graph=W
        V=n
        src=start_ver
        dist = [sys.maxsize] * V
        dist[src] = 0
        if len(c)>0:
            if c.count(src)>0:
                for f in range (V):
                    dist[f]=0
            else:
                for f in range (len(c)):
                    dist[c[f]]=0
        if len(k)==1 and k[0]==src:
          i=0
          for f in range (V):
              if i==l[0] or i==k[0]:
                 i=i+1
              elif i!=l[0] or i!=k[0]:
                   dist[i]=0
                   i=i+1

        sptSet = [False] * V

        for cout in range(V):
            min = sys.maxsize
            for v in range(V):
                if dist[v] < min and sptSet[v] == False: 
                    min = dist[v]
                    min_index = v
            u = min_index
            sptSet[u] = True
 
            for v in range(V):
               
                    if graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + graph[u][v]:
                        dist[v] = dist[u] + graph[u][v]
        i=0
        for node in range(V):
                if dist[i]==z[i]:
                    if i!=V:
                        i=i+1
                    elif i==V:
                        break
                elif dist[i]==z[i]:
                    break
        if i==V:
            a=True
        elif i!=V:
            a=False
        self.assertTrue(a)
if __name__ == '__main__':
    unittest.main()

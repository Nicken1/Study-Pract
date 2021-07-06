import unittest
import numpy as np
class Test_test_2(unittest.TestCase):
    def test_A(self):
       def test_A(self):
        n=4
        C= [[ 0, 99,  5, 99,],
            [99,  0,  3, 99,],
            [ 4,  1,  0,  7,],
            [99, 99,  2,  0]]
        T=[[ 0, 99,  4, 99,],
         [99,  0,  1, 99,],
         [ 4,  1,  0,  2,],
         [99, 99,  2,  0]]
        H=[[]]
        H=np.diag(np.arange(1,n+1))
        for i in range (n):
            for j in range (n):
                T[i][j] = C[i][j]
                if C[i][j] == 99:
                    H[i][j]=0        
                elif C[i][j] != 99  and C[i][j] != 0: 
                    H[i][j]=j
        N=[[1, 0, 2, 0,],
           [0, 2, 2, 0,],
           [0, 1, 3, 3,],
           [0, 0, 2, 4,]]
        for i in range (n):
            for j in range (n):
                for k in range(n):
                    if (i!=j and T[i][j]!=99 and i != k and T[i][k] != 99 and (T[j][k] == 99 or T[j][k] > T[j][i] + T[i][k])):
                       H[j][k] = H[j][i]
                       T[j][k] = T[j][i]+T[i][k]
        for i in range (n):
            if T[j][j] < 0:
              break
        A = [[0, 6, 5, 12], [7, 0, 3, 10], [4, 1, 0, 7], [6, 3, 2, 0]]
        if A==T and N==H:
            a=True
        else:
            a=False
        self.assertTrue(a)
if __name__ == '__main__':
    unittest.main()

import unittest
import numpy as np
class Test_test_2(unittest.TestCase):
    def test_A(self):
        n=8
        C= [[ 0, 99 ,99,  4,  6,  2, 99, 99,],
            [99,  0, 99, 99, 99,  3, 99, 99,],
            [99, 99,  0,  2,  6, 99, 99,  6,],
            [ 8, 99,  7,  0, 99,  5,  2, 99,],
            [ 4, 99,  1, 99,  0,  2, 99, 99,],
            [ 2,  3, 99,  7,  4,  0, 99,  4,],
            [99, 99, 99,  2, 99, 99,  0, 99,],
            [99, 99,  4, 99, 99,  6, 99,  0]]
        T =[[ 0, 99, 99,  8,  4,  2, 99, 99,],
            [99,  0, 99, 99, 99,  3, 99, 99,],
            [99, 99,  0,  7,  1, 99, 99,  4,],
            [ 8, 99,  7,  0, 99,  7,  2, 99,],
            [ 4, 99,  1, 99,  0,  4, 99, 99,],
            [ 2,  3, 99,  7,  4,  0, 99,  6,],
            [99, 99, 99,  2, 99, 99,  0, 99,],
            [99, 99,  4, 99, 99,  6, 99,  0]]
        H=[[]]
        H=np.diag(np.arange(1,n+1))
        for i in range (n):
            for j in range (n):
                T[i][j] = C[i][j]
                if C[i][j] == 99:
                    H[i][j]=0        
                elif C[i][j] != 99  and C[i][j] != 0: 
                    H[i][j]=j
        for i in range (n):
            for j in range (n):
                for k in range(n):
                    if (i!=j and T[i][j]!=99 and i != k and T[i][k] != 99 and (T[j][k] == 99 or T[j][k] > T[j][i] + T[i][k])):
                       H[j][k] = H[j][i]
                       T[j][k] = T[j][i]+T[i][k]
        for i in range (n):
            if T[j][j] < 0:
              break
        A = [[ 0,  5,  7,  4,  6,  2,  6,  6,],[ 5,  0,  8,  9,  7,  3, 11,  7,],
             [ 9, 10,  0,  2,  6,  7,  4,  6,],[ 7,  8,  7,  0,  9,  5,  2,  9,],
             [ 4,  5,  1,  3,  0,  2,  5,  6,],[ 2,  3,  5,  6,  4,  0,  8,  4,],
             [ 9, 10,  9,  2, 11,  7,  0, 11,],[ 8,  9,  4,  6, 10,  6,  8,  0,]]
        if A==T:
            a=True
        else:
            a=False
        self.assertTrue(a)

if __name__ == '__main__':
    unittest.main()

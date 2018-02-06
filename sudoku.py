from sets import Set

class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        n = 9
        q = [[] for _ in range(n)]
        w = [[] for _ in range(n)]
        r = [[] for _ in range(n)]
        for i, a in enumerate(A):
            for j, b in enumerate(a) :
                if b != '.':
                    q[i].append(b)
                    w[j].append(b)
                    o = (3*(i/3))+(j/3)
                    r[o].append(b)
        for i in range(n):
            l1 = Set(q[i])
            l2 = Set(w[i])
            l3 = Set(r[i])
            if len(l1) == len(q[i]) and len(l2) == len(w[i]) and len(l3) == len(r[i]):
                continue
            else :
                return 0
        return 1



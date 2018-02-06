class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        answer = 1
        pw = x
        if n == 0:
            if x == 0:
                return 0
            else:
                return 1%d
        if n == 1:
            return x%d
        while(n != 0):
            if(n%2):
                answer = answer*pw
            pw = (pw*pw)%d
            n = n/2
            if(answer > d):
                answer = answer % d
        return answer
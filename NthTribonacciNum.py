class Solution(object):
    #N th tribonacci num 
    #Program usage fixed memory(less than compared) and lesser time
    def tribonacci(self, n):
        T=[0,1,1]
        if n<3:
            return T[n]
        else:
            for i in range(3, n+1):
                T[0], T[1], T[2]=T[1], T[2], sum(T)   
            return T[2]
tribo=Solution()
n=int(input())
print(tribo.tribonacci(n))
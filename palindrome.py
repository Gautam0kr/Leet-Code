class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        l1=[]
        for i in x:
            l1.append(i)

        l2=l1.copy()
        l2.reverse()
        if l1==l2:
            return True
        else:
            return False

num=Solution()
n=int(input())
print(num.isPalindrome(n))

#same code can be written in very short and optimized way

# class Solution(object):
#     def isPalindrome(self, x):
#         return str(x) == str(x)[::-1]

# num = Solution()
# n = int(input("Enter a number: "))
# print(num.isPalindrome(n))

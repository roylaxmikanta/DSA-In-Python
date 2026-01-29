# class Solution:
#     def solve(self,index,total,brackets,result):
#         if(index>=len(brackets)):
#             if(total==0):
#                 result.append("".join(brackets))
#             return
#         if(total>len(brackets)//2):
#             return
#         if(total<0):
#             return
#         brackets[index]="("
#         sum=total+1
#         self.solve(index+1,sum,brackets,result)
#         brackets[index]=")"
#         sum=total-1
#         self.solve(index+1,sum,brackets,result)
#         return result
# s=Solution()
# numbers = [""] * (2*n)
# result = []
# print(s.solve(0, 0, numbers, result))
class Solution:
    def generateParenthesis(self, n: int):
        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        result = []
        backtrack()
        return result
s=Solution()
print(s.generateParenthesis(3))
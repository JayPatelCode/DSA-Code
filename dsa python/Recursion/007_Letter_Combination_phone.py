# class Solution:
#     def solve(self, index, subset, digits, char_map, result):
#         if index >=len(digits):
#             result.append("".join(subset))
#             return
#         for ch in char_map[digits[index]]:
#             subset.append(ch)
#             self.solve(index+1, subset, digits, char_map, result)
#             subset.pop()


#     def letterCombinations(self, digits: str) -> list[str]:
#         result=[]
#         char_map={
#             "2":"abc",
#             "3":"def",
#             "4":"ghi",
#             "5":"jkl",
#             "6":"mno",
#             "7":"pqrs",
#             "8":"tuv",
#             "9":"wxyz"
#         }
#         result=[]
#         self.solve(0,[],digits,char_map,result)
#         return result
    

# digits = "23"
# s1=Solution()
# print(s1.letterCombinations(digits))

st=""
print(len(st))
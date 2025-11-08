digits = [1,2,3]
def plusOne(self, digits: list[int]) -> list[int]:
        string=int("".join([str(i) for i in digits]))
        string+=1
        res=list(str(string))
        return [int(i) for i in res]
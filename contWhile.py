# # lis=[1,2,3]
# # i=0
# # while i<len(lis):
# #     print(lis[i])
# #     i+=1

# # for i in range(0,len(lis)):
# #     print(lis[i])

# # name = {
# #     "a":"jay"
# # }
# # print(name["a"])

# # x= int(input("Enter value of x"))
# # match x:
# #     case 0:
# #         print("Value is 0")
    
# #     case 1:
# #         print("value is 1")

# #     case _:
# #         print(x)    


# # name = 'jay'
# # for i in name:
# #     print(i)

# # colors = ["a","b","c"]
# # for c in colors:
# #     print(c)

# # a = int(input("Enter number to print its table"))
# # for i in range (1,12):
# #     if i>10:
# #         continue
# #     print(f"{a} * {i} = {a*i}")


# # lar=[1,33,56,7,2]

# # i=lar[0]
# # # j=lar[1]
# # for j in lar[1:]:
# #     if j>i:
# #         i=j
# # print(i)
    
# # lar=[1,33,56,7,2]

# # sum=[]

# movies = Movie.objects.all()
# serializer = MovieSerializer(movies,many=True)
# return Httpresponse(serializer.data)

# movie = Movie.objects.get(pk=pk)


# def get(self,request):
#     m = mov.objects.all()
#     ser=movser(m,many=True)
#     return response(ser.data)

# def post(self,request):
#     ser=movser(data=request.data)
#     if ser.is_valid():
#         ser.save()
#         return response(ser.data)
#     return res(ser.errors)    

# def get(self,request,pk):
#     mov = mov.objects.get(pk=pk)
#     ser=movser(m)
#     return response(ser.data)

# def put(self,request,pk):
#     mov = mov.objects.get(pk=pk)
#     ser=movser(mov,data=request.data)
#     if ser.is_valid():
#         ser.save()
#         return response(ser.data)
#     return res(ser.errors)    





###################### iterator and iterable #####################

# from typing import Iterable, Iterator
# fit: list[str] = ["ab","bc","cd"]
# ft: Iterator[str] = iter(fit)
# # print(next(ft))

# for i in range(2):
#     print(next(ft))





##################Generators######333333

# def generate():
#     i=1
#     while i<=200:
#         yield i
#         i+=1

# print(generate())
# x=generate()
# print(next(x))
# print(next(x))
# print(list(x))
        

# marks = [20,30,40,50]
# print(marks)
# print([mark + 3 for mark in marks])

# for mark in marks:
#     print(mark+3)



class Counter:
    def __init__(self):
        self.value=1

    def count_up(self):
        self.value += 1

    def count_down(self):
        self.value-=1

    def __str__(self):
        return f"count={self.value}"
    
    def __add__(self, other):
        return self.value+other.value

ct1=Counter()
ct2=Counter()
# print(ct1)
# print(ct2)
ct1.count_up()
ct2.count_up()
# print(ct1)
print(ct1 , ct2)
print(ct1 + ct2)

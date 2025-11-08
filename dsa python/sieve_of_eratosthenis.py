# num = int(input("Enter the number: "))


# def is_prime(num):
#     i=2
#     while i*i <=num:
#          if num%i==0:
#               return False
#          i+=1
#     return True

# print(is_prime(num))



num = int(input("Enter the number till you want to print series of prime number: "))

primelist=[True for i in range(num+1)]

i=2
while i*i<=num:
    if primelist[i]==True:
        for j in range(i*i,num+1,i):
            primelist[j]=False
    i=i+1

for i in range(2,num+1):
    if primelist[i]==True:
        print(i,end=" ")

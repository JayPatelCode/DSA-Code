# lst=[9,3,5,2]
# ind = 0
# def prallel(lst,ind):
#     if ind > len(lst)-1:
#         return 0
#     print(lst[ind])
#     ind += 1
#     prallel(lst,ind)

# prallel(lst,ind)


# lst=[9,3,5,2]
# ind = 0
# def prallel(lst,ind):
#     if ind > len(lst)-1:
#         return 0
    
#     prallel(lst,ind+1)
#     print(lst[ind])

# prallel(lst,ind)


# def num(n):
#     if n==0:
#         return
#     print("jay")
#     num(n-1)

# num(10)



# def num(i,n):
#     if i>n:
#         return
#     print("jay")
#     num(i+1,n)

# num(1,6)


##########print 1 to n


# def num(n):
#     if n==0:
#         return
#     num(n-1)
#     print(n)

# num(13)

###or

# def num(i,n):
#     if i>n:
#         return
#     print(i)
#     num(i+1,n)

# num(1,19)


##########print n to 1


# def num(n):
#     if n==0:
#         return
#     print(n)
#     num(n-1)

# num(13)


###or

# def num(i,n):
#     if i>n:
#         return
#     num(i+1,n)
#     print(i)

# num(1,19)




#### sum of first n numbers

# def son(num):
#     if num==0:
#         return 
#     for i in range(1,num+1):
#         sum=0
#         sum+=num
#         print(sum)
#         son(num-1)

# son(4)    


# sum of num using recursion

# def son(i,num,sum): 
#     if i>num:
#         return sum 
    
#     return son(i+1,num,sum+i)

# print(son(1,10,0))


############## or

# def son(i,num): 
#     if i>num:
#         return 0 
    
#     ans= son(i+1,num)+i
#     return ans

# print(son(1,10))




#############Factorial


# def fact(num): 
#     if num==0:
#         return 1

#     return num * fact(num-1) 
    

# print(fact(5))



#########revrse array


# lst=[1,5,7,12]

# for i in reversed(lst):
#     print(i)


######################OR

# lst=[1,5,7,12]

# def rev(s,e,lst):
#     if s>e:
#         return
#     lst[s],lst[e]=lst[e],lst[s]
#     return rev(s+1,e-1,lst)


# rev(0,len(lst)-1,lst)
# print(lst)

######palindrome

# n=input()
# def pal(s,e,str):
#     if s>e:
#         return True
#     if str[s]!=str[e]:
#         return False
#     return pal(s+1,e-1,str)


# ans=pal(0,len(n)-1,n)   
# print(ans)



#############fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

# def fib(n):

    
#     if n==0:
#         return 0
    
#     elif n==1:
#         return 1
    
#     else:
#         return fib(n-2) + fib(n-1)
    
# print(fib(8))


##########fibbonacci#
# def fibb(n):
#     if n==0 or n==1:
#         return n
#     return fibb(n-1)+fibb(n-2)

# print(fibb(6))


# for i in range(0,12):
#     print(fib(i))


###################hashing

# arr=[1,4,6,5,2,4,1,5,9,5]

# d={}
# for item in arr:
#     d[item]=d.get(item, 0)+1

# print(d)


# nums=[2,-1,1]

# closest=nums[0]

# for i in nums:
#     if abs(i)<abs(closest):
#         closest=i

# if closest<0 and abs(closest) in nums:
#     print(abs(closest))

# else:
#     print(closest)


# s="jVy"

# d={'j':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

# print(d[s[1]])









# def p_num(num,time):
#     if time==0:
#         return
#     print(num)
#     p_num(num,time-1)

# p_num(12,10)





# def p_num(num):
#     if num==0:
#         return
#     p_num(num-1)
#     print(num)

# p_num(8) 







#######palindrone#####
# s="ANBCDDCONA"

# l=len(s)
# left=0
# right=l-1
# while left<right:
#     if s[left]!=s[right]:
#         print(False)
#         break

#     left+=1
#     right-=1
# print(True)


# s="ANBCDDCBPA"

# n=len(s)
# l=0
# r=n-1
# def pal(s,l,r):
#     if l>=r:
#         return True
#     if s[l]!=s[r]:
#         return False
#     return pal(s,l+1,r-1)
# print(pal(s,l,r))






######reverse an array####
# nums=[1,3,5,6,7,8,5]
# i=0
# n=len(nums)
# j=n-1
    
# while i<j:
#     nums[i],nums[j]=nums[j],nums[i]
#     i+=1
#     j-=1
# print(nums)




def rev(nums,i,j):
    
    if i>j:
        return nums
    nums[i],nums[j]=nums[j],nums[i]
    return rev(nums,i+1,j-1)


nums=[1,3,5,6,7,8,5]  
n=len(nums)
print(rev(nums,0,n-1))
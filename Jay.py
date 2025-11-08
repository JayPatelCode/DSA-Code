print("Hello jay")
name="jaypatel is my name"
print(name[0::2])
print(name.endswith("el"))
print(name.title())
a="my name is \
jay patel"
print(a)

ages={
"jay":12,
"neel":23,
"prerak":23
}

# for age in ages.items():
#     print(age)

# for i,age in enumerate(ages.items()):
#         print(age)
#         if i == 0:
#                 break

# f=next(iter(ages.items()))
# print(f)
print(ages.update({"jay":"21"}))
print(ages)
print(ages["neel"])

a=(input("Enter the number between 10 and 15"))
if (a=="quit"):
        pass
else:
    if int(a)<10 or int(a)>15:
            raise ValueError("Your entered number is not between 10 and 15")

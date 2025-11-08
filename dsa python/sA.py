import os
def get_winner(ans):
    highest_bid=0
    winner=""
    for an in ans: #############jay
        price_of_bid=ans[an]#########100
        if price_of_bid>highest_bid:
            highest_bid=price_of_bid
            winner=f"Winner is {an} and with price {highest_bid} "
    print(winner)


ans={}

ans_no=False

while not ans_no:

    name=input("Enter your name: ")
    bid=int(input("Now enter bid amount: "))
    ans[name]=bid
    print(ans[name])
    print(ans)
    more_bid = input("Enter yes or no for continuing: ").lower()
    if more_bid == "no":
        ans_no=True
        get_winner(ans)
    elif more_bid == "yes":
        os.system('clear')

# print("Hello my name is jay")

# for i in range(20,0,-3):

#     print(i)


# list=[]
# for i in range (15):
#     if i%2==0:
#         list.append(i)
# print(list)        


# print([x for x in range(15) if x%2==0])





# ls = [1,2,3,4]
# print([x for x in ls if x%2==0])


# person = {
#     "jay":{
#         "age":21,
#         "bday":31
#     },
#     "neel":{
#         "age":22,
#     },
#     "kashish":{
#         "age":23,
#     }
# }
# print(person["jay"].values())




# print([x**2 for x in range(1,11) ])



# words = ["apple", "banana", "orange", "umbrella", "grape", "elephant"]
# print([x for x in words if x[0] not in 'aeiou'])

# keys = ["name", "age", "city"]
# values = ["Alice", 25, "New York"]
# print({key:value for key,value in zip(keys,values) })


# dict={}
# for i in range(15):
#     if i%2==0:
#         dict[i]=i*i
# print(dict)


# print({i:i*i for i in range(15) if i%2==0})



# def na(name: str) -> float:
#     return(f"My name is {name}")
    

# print(na("Jay"))


# print(na("Dhyey"))

# "jay@email.com"
# email=input("Enter email: ") 
# index=email.index("@")
# username=email[:index]
# domain=email[index+1:]
# print(f"Your username is {username} and your domain is {domain}")

# import random

# words = ("aardvark", "alligator", "alpaca", "ant", "anteater", "antelope", "ape", "armadillo", "baboon", "badger", "bat", "bear", "beaver", "bee", "bison", "boar", "buffalo", "butterfly", "camel", "capybara", "caribou", "cat", "caterpillar", "cattle", "chamois", "cheetah", "chicken", "chimpanzee", "chinchilla", "chough", "clam", "cobra", "cockroach", "cod", "coyote", "crab", "crane", "crocodile", "crow", "curlew", "deer", "dinosaur", "dog", "dogfish", "dolphin", "donkey", "dormouse", "dotterel", "dove", "dragonfly", "duck", "dugong", "dunlin", "eagle", "echidna", "eel", "eland", "elephant",  "elk", "emu", "falcon", "ferret", "finch", "fish", "flamingo", "fly", "fox", "frog", "gaur", "gazelle", "gerbil", "giraffe", "gnat", "gnu", "goat", "goldfinch", "goldfish", "goose", "gorilla", "goshawk", "grasshopper", "grouse", "guanaco", "gull", "hamster", "hare", "hawk", "hedgehog", "heron", "herring", "hippopotamus", "hornet", "horse", "human", "hummingbird", "hyena", "ibex", "ibis", "jackal", "jaguar", "jay", "jellyfish", "kangaroo", "kingfisher", "koala", "kookabura", "kouprey", "kudu", "lapwing", "lark", "lemur", "leopard", "lion", "llama", "lobster", "locust", "loris", "louse", "lyrebird", "magpie", "mallard", "manatee", "mandrill", "mantis", "marten", "meerkat", "mink", "mole", "mongoose", "monkey", "moose", "mosquito", "mouse", "mule", "narwhal", "newt", "nightingale", "octopus", "okapi", "opossum", "oryx", "ostrich", "otter", "owl", "ox", "oyster", "panda", "panther", "parrot", "partridge", "peafowl", "pelican", "penguin", "pheasant", "pig", "pigeon", "polar-bear", "pony", "porcupine", "porpoise", "quail", "quelea", "quetzal", "rabbit", "raccoon", "rail", "ram", "rat", "raven", "red-deer", "red-panda", "reindeer", "rhinoceros", "rook", "salamander", "salmon", "sand-dollar", "sandpiper", "sardine", "scorpion", "seahorse", "seal", "shark", "sheep", "shrew", "skunk", "snail", "snake", "sparrow", "spider", "spoonbill", "squid", "squirrel", "starling", "stingray", "stoat", "stork", "swallow", "swan", "tapir", "tarsier", "termite", "tiger", "toad", "trout", "turkey", "turtle", "viper", "vulture", "wallaby", "walrus", "wasp", "weasel", "whale", "wildcat", "wolf", "wolverine", "wombat", "woodcock", "woodpecker", "worm", "wren", "yak", "zebra")

# hangman_art = {0: ( "   ",
#                     "   ",
#                     "   "),
#                 1: (" o ",
#                     "   ",
#                     "   "),
#                 2: (" o ",
#                     " | ",
#                     "   "),
#                 3: (" o ",
#                     "/| ",
#                     "   "),
#                 4: (" o ",
#                     "/|\\",
#                     "   "),
#                 5: (" o ",
#                     "/|\\",
#                     "/  "),
#                 6: (" o ",
#                     "/|\\",
#                     "/ \\")}


# def display_man(wrong_guesses):
#     print("**********************")
#     for line in hangman_art[wrong_guesses]:
#         print(line)
#     print("**********************")
#     display_hint

# def display_hint(hint):
#     print(" ".join(hint))

# def display_answer(answer):
#     print(" ".join(answer))

# def main():
#     answer= random.choice(words)
#     hint = ["_"] * len(answer)
#     wrong_guesses=0
#     guessed_letters=set()
#     is_running=True

#     while is_running:
#         display_man(wrong_guesses)
#         display_hint(hint)
#         display_answer(answer)
#         guess= input("Enter a letter: ").lower()

#         if len(guess) != 1 or not guess.isalpha():
#             print("Invalid input")
#             continue
        
#         if guess in guessed_letters:
#             print(f"{guess} is already guessed")
#             continue

#         guessed_letters.add(guess)

#         if guess in answer:
#             for i in range (len(answer)):
#                 if answer[i] == guess:
#                     hint[i]=guess 
#         else:
#             wrong_guesses += 1
        
#         if "_" not in hint:
#             display_man(wrong_guesses)
#             display_answer(answer)
#             print("You Win")
#             is_running=False

#         elif wrong_guesses >= len(hangman_art) - 1:
#             display_man(wrong_guesses)
#             display_answer(answer)
#             print("You Lose")
#             is_running=False


# if __name__ == "__main__":
#     main()


# def add(*args):
#     print(sum(args))

# add(2,3,4,9)


# dct={"a":2,"b":3,"a":5}
# print(dct)





# n=3
# num=["0"]*n
# print(num)

s = "ABAB"
print(s[0])
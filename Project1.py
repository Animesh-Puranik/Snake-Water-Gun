# We all have played snake, water gun game in our childhood. If you haven’t, google the
# rules of this game and write a python program capable of playing this game with the user

computerChoice = -1
yourChoice = input("Enter your choice : ")
youDict = {
    "s":1, "w":-1, "g":0
}
reverseDict = {
    1:"Snake", -1:"Water", 0:"Gun"
}
younum = youDict[yourChoice]

if (computerChoice == younum):
    print("It is a draw")
else : 
    if(computerChoice == -1 and younum == 1):
        print("You Win!")
    elif(computerChoice == -1 and younum == 0):
        print("You Lose!")
    elif(computerChoice == 1 and younum == -1):
        print("You Lose!")
    elif(computerChoice == 1 and younum == 0):
        print("You Win!")
    elif(computerChoice == 0 and younum == -1):
        print("You Win!")
    elif(computerChoice == 0 and younum == 1):
        print("You Lose!")

    else: print("Something went wrong")
"""
WORKFLOW OF THE PROJECT
1. Input from the user(rock, paper, scissor)
2. Input from the computer(computer will choose randomly and not conditionally)
3.Result print

CASES:
A. Rock
   rock-rock = tie
   rock-paper= paper wins
   rock-scissor= scissor wins

B. Paper
   paper-paper= tie
   paper-rock = paper wins
   paper-scissor= scissor wins

C. Scissor
   scissor- scissor = tie
   scissor-paper = scissor wins
   scissor- rock = rock wins

"""
import random
item_list = [ "rock", "paper", "scissor"]

user_choice = input("enter your move- rock, paper, scissor =")
comp_choice = random.choice(item_list)

print(f"user choice = {user_choice}, computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("both chose same: match tie")

elif user_choice == "rock":
    if comp_choice == "paper":
        print("paper covers rock: computer wins")
    else:
        print("rock smashes scissor: you win") 

elif user_choice == "paper":
    if comp_choice == "scissor":
        print("scissor cuts paper: computer wins")
    else:
        print("paper covers rock: you win")
elif user_choice == "scissors":
    if comp_choice =="rock":
        print("rock smashes scissors: computer wins")
    else:
        print("scissor cuts paper: you win")
        






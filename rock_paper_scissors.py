import random

user_input = input("What is your choice? (rock, paper, scissors): ")

possible_input = ["rock", "paper", "scissors"]
computer_input = random.choice(possible_input)

print("\nYou chose: {} ".format(user_input))
print("Computer chose: {} ".format(computer_input))

# print(f"\nYou chose: {user_input}\nComputer chose: {computer_input}")

if user_input == computer_input:                                            #starting with a tie condition  first
    print("You both chose '{}', It's a tie!".format(user_input))            #to get rid of quite a few cases.     
elif user_input == "rock":
    if computer_input == "scissors":
        print("rock smashes scissors, You won!")
    else:
        print("paper covers rock, You lose!")
elif user_input == "paper":
    if computer_input == "rock":
        print("paper covers rock, You win!")
    else:
        print("scissors cut paper, You lose!")
elif user_input == "scissors":
    if computer_input == "paper":
        print("scissors cut paper, You win!")
    else:
        print("rock smashes scissors, You lose!")
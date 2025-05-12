import random 

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)

while player not in options:
    player = input("Enter a choice : ")

print(f"You: {player}")
print(f"computer: {computer}")

if player == computer:
    print("It's a draw!")
elif (player == "paper" and computer == "rock") or \
     (player == "rock" and computer == "scissors") or \
     (player == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("You lose!")

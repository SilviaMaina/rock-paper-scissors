import random
options = ['rock', 'paper', 'scissors']

user_pick = input("Choose btwn rock,paper,scissors: ")
computer_pick = random.choice(options)

print(f"You chose:{user_pick}")
print(f"Computer chose:{computer_pick}")

if user_pick == computer_pick:
    print("Its a tie")
elif user_pick == 'rock' and computer_pick =='scissors':
    print('You win')
elif user_pick == 'paper' and computer_pick =='rock':
    print('You win')
elif user_pick == 'scissors' and computer_pick =='paper':
    print('You win')
else:
    print('Computer wins')
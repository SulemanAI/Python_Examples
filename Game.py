import random
print("Welcome to the game of Rock, Paper, Scissor!")
options = ['Rock','Paper','Scissor']

user = input(f"Select any one: \n {options} \n").capitalize()
print(f"You choose: {user}")

computer_choice = random.choice(options)
print(f"Computer choose: {computer_choice}")

if user == computer_choice:
    print("Draw")
elif user == 'Rock' and computer_choice == 'Scissor':
    print("You Win!")
elif user == 'Rock' and computer_choice == 'Paper':
    print("You lose!")
elif user == 'Scissor' and computer_choice == 'Rock':
    print("You Win!")
elif user == 'scissor' and computer_choice == 'Paper':
    print("You Win!")
elif user == 'Paper' and computer_choice == 'Rock':
    print("You Win!")
elif user == 'Paper' and computer_choice == 'Scissor':
    print("You lose!")
else:
    print("Invalid choice")
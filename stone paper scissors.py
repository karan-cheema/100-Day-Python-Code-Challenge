import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

weapons = [rock, paper, scissors]
user_score = 0
computer_score = 0

print("Welcome to the game of stone, paper and scissors")
print("Let the game begin")
print("Rock = 1, Paper = 2, Scissors = 3")
choice = int(input("Choose your weapon: "))
user_choice = choice - 1
print(weapons[user_choice])
computer_weapon = random.randint(1,3)
computer_choice = computer_weapon - 1
print(weapons[computer_choice])
if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
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

#Write your code below this line 👇
answer = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
# cpu
random_number = random.randint(0, 2)
if random_number == 0:
  print("Computer choice: ", rock)
elif random_number == 1:
  print("Computer choice: ", paper)
elif random_number == 2:
  print("Computer choice: ", scissors)

# gamer
if answer == 0:
  print("Your choice: ", rock)
  if random_number == 1:
    print("CPU win!")
  elif random_number == 2:
    print("You win!")
elif answer == 1:
  print("Your choice: ", paper)
  if random_number == 0:
    print("You win!")
  elif random_number == 2:
    print("CPU win!")
elif answer == 2:
  print("Your choice: ", scissors)
  if random_number == 0:
    print("You win!")
  elif random_number == 1:
    print("CPU win!")
else:
  print("Choose another number!")

# logic
if random_number == answer:
  print("Remis, try again!")
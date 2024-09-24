import random as r

# RockPaperScissors Game

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
try:
    choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
    computer_choice = r.randint(0,2)

    if choice == computer_choice:
        
        if choice == 0:
            print(rock)
            print('Computer chose : \n')
            print(rock)
        
        elif choice == 1:
            print(paper)
            print('Computer chose : \n')
            print(paper)
        else:
            print(scissors)
            print('Computer chose : \n')
            print(scissors)
        print("It's Draw.")
        
    elif choice == 0:
        print(rock)
        print('Computer chose : \n')
        if computer_choice == 2:
            print(scissors)
            print('You won!')
        else:
            print(paper)
            print('You lose!')
            
    elif choice == 1:
        print(paper)
        print('Computer chose : \n')
        if computer_choice == 0:
            print(rock)
            print('You won!')
        else:
            print(scissors)
            print('You lose!')
            
    elif choice == 2:
        print(scissors)
        print('Computer chose : \n')
        if computer_choice == 1:
            print(paper)
            print('You won!')
        else:
            print(rock)
            print('You lose!')
    else:
        print("invalid choice!")
except Exception as e:
    print('Invalid input!')
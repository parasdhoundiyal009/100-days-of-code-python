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
scissor = scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#To prompt user to enter his choice and then check that with computers choice as to who won in the game stone paper and scissor.
try:
    my_input = int(input ("Choose from Rock(0), Paper(1), Scissor(2) & we will then see if you won against the computer or not. "))
    computers_choice = random.randint(0,2)

    if(my_input == computers_choice):
        print("Since both choose the same object, it's a tie and nobody won.")

    elif (my_input == 0):
        print (f"Your Choice is Rock\n{rock}")
        if(computers_choice == 1):
            print (f"Computer's Choice Paper\n{paper}")
            print ("You Loose. Rock looses against paper.")
        else:
            print (f"Computer's Choice Scissor\n{scissor}")
            print ("You Win. Rock wins against Scissor.")
    
    elif (my_input == 1):
        print (f"Your Choice is Paper\n{paper}")
        if(computers_choice == 0):
            print (f"Computer's Choice Rock\n{rock}")
            print ("You Win. Paper Wins against Rock.")
        else:
            print (f"Computer's Choice Scissor\n{scissor}")
            print ("You Loose. Paper looses against Scissor.")
    
    else:
        print (f"Your Choice is Scissor\n{scissor}")
        if(computers_choice == 0):
            print (f"Computer's Choice Rock\n{rock}")
            print ("You Loose. Scissor lost against Rock")
        else:
            print (f"Computer's Choice Paper\n{paper}")
            print ("You Win. Scissor Wins against paper.")

except ValueError:
    print("Wrong input. Please select number between 0, 1, 2.")

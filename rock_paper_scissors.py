import random


Rock='''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
Paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''

Scissors='''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

      '''
images=[Rock,Paper,Scissors]

user_choice=int(input("Enter your choice: Type 0 for Rock , 1 for paper , 2 for scissors "))


if(user_choice>2 or user_choice<0):
    print("Invalid choice")
else:
    print("user chose")
    print(images[user_choice])

    computer_choice=random.randint(0,2)

    print("computer chose:")
    print(images[computer_choice])

    if(user_choice==computer_choice):
        print("it's a draw")

    elif(user_choice==0 and computer_choice==2):
        print("you win")

    elif(user_choice==2 and computer_choice==0):
        print("you lose")

    elif(user_choice>computer_choice):
        print("you win")

    elif(user_choice<computer_choice):
        print("you lose")




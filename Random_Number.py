import random 
import math

print("                   NUMBER GUESSING GAME")
print("      -----------------Instructions----------------")
print("1.You will be given 5 chances to guess the correct number")
print("2.For correct guess you will earn 1 point and lose for wrong guess")
print("3.MAXIMUM SCORE:5 ")
print("4.MINIMUM SCORE:0")

print("**********************************************************************************************")
print("**********************************************************************************************")
print()
print("Input the Upper And Lower bound according to you.")
print()
low_bound = int(input("Enter the lower bound of the range : "))
print()
up_bound = int(input("Enter the upper bound of the range : "))
generated_number = random.randint(low_bound,up_bound)
score=5
i=1
while i<=5:
    print()
    guessed=int(input("Enter the number between "+ str(low_bound)+" and "+ str(up_bound)+": "))
    i=i+1
    if guessed==generated_number :
              print()
              print("*****************Congratulations,you have won!!!***************************")
              print("Your Guess is Correct and You have taken attempts for the right answer.")
              print()
              print("**************************YOUR FINAL SCORE:"+str(score)+"****")
              break
    elif(guessed>generated_number ):
              print()
              print("Guessed number is greater than generated number")
              score=score-1
              print("Wrong Guess,Try another chance!")

    elif(guessed<generated_number ):
              print()
              print("Guessed number is lesser than generated number")
              score=score-1
              print("Wrong Guess,Try another chance!")

    
if(score==0) :
    print()
    print("***************************Your chances hace been exhausted.********************************************")
    print("*******************************OOPS!!!YOU LOSE THE GAME*************************************************")
    score=score-1
    print()
  
    print("***YOUR FINAL SCORE:"+str(score)+"****")
    print()
    print("***************************************THANKYOU FOR PLAYING**********************************************")

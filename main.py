"""
------------------------------------------------------------------------------
Name: ics2o-cpt-2021
Purpose: This a quiz about the course content of ICS2O
 
Author: Lin.O
 
Created: 29/03/2021
------------------------------------------------------------------------------
"""
#import random is for randomizing numbers in a minigame
import random 

#Define the variables 
start_quiz = False 
continue_quiz = "yes"
stop = "no"
total = 0

#Initiate the quiz
while not start_quiz:
  
  print("Are you ready to do a review quiz about Computer Studies?")
  question = input("YOUR ANSWER: ").lower()
  if question == continue_quiz:
    print("\n*****Let's get started!*****\n")
    start_quiz = True
  elif question == stop:
    print("Maybe review the content then come back for another try!\n")
  else:
    print("Please answer yes or no.\n")

#Question starts here 
if question == continue_quiz:  
  print("1. What is a funtion that a CPU does? (ENTER a, b, c, or d)")
  print("a. A CPU is a chip that executes commands that make up a program.")
  print("b. A CPU supplies electricity to the entire computer.")
  print("c. A CPU is a storage that can hold large amounts of data.")
  print("d. A CPU is a computer case.\n")
  q1a = input("What is the answer? ")
  while not q1a == "a" and not q1a == "b" and not q1a == "c" and not q1a == "d":
    q1a = input("Please answer 'a, b, c, d'.\n").lower()
  if q1a == "a":
    print("CORRECT\n")
    total += 1
  else: 
    print("INCORRECT, the answer was a.\n")
    total += 0

  print("2. What is a value in Python?")
  print("a. A value is a string is programming language")
  print("b. A value is just a number")
  print("c. A value is nothing")
  print("d. A value is a basic piece of information a program works with, like a letter or a number\n")
  q2a = input("What is the answer? ")
  while not q2a == "a" and not q2a == "b" and not q2a == "c" and not q2a == "d":
    q2a = input("Please answer 'a, b, c, d'.\n").lower()
  if q2a == "d":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was d\n")
    total += 0

  (print("3. What is the order of the sequence of events in computer processing?"))
  print("a. Input, Output, Storage, Processing")
  print("b. Processing, Input, Storage, Output")
  print("c. Input, Processing, Output, Storage")
  print("d. Storage, Output, Input, Processing\n")
  q3a = input("What is the answer? ")
  while not q3a == "a" and not q3a == "b" and not q3a == "c" and not q3a == "d":
    q3a = input("Please answer 'a, b, c, d'.\n").lower()
  if q3a == "c":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was c\n")
    total += 0

  print("4. What is a variable?")
  print("a. just a letter")
  print("b. something that stores information in a program so it can be used later")
  print("d. just a symbol")
  print("c. none of the above\n")
  q4a = input("What is the answer? ")
  while not q4a == "a" and not q4a == "b" and not q4a == "c" and not q4a == "d":
    q4a = input("Please answer 'a, b, c, d'.\n").lower()
  if q4a == "b":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was b\n")
    total += 0

  print("5. What 3 things are in a variable?")
  print("a. name, type, value")
  print("b. value, storage, letters")
  print("c. data, name, letters")
  print("d. x, y, z\n")
  q5a = input("What is the answer? ")
  while not q5a == "a" and not q5a == "b" and not q5a == "c" and not q5a == "d":
    q5a = input("Please answer 'a, b, c, d'.\n").lower()
  if q5a == "a":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was a\n")
    total += 0

  print("6. How many bytes are in 1 Kilobyte?")
  print("a. 10 bytes")
  print("b. 100 bytes")
  print("c. 1000 bytes")
  print("d. 1 byte\n")
  q6a = input("What is the answer? ")
  while not q6a == "a" and not q6a == "b" and not q6a == "c" and not q6a == "d":
    q6a = input("Please answer 'a, b, c, d'.\n").lower()
  if q6a == "c" :
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was c\n")
    total += 0

  print("7. What does this '%' mean in Python? ")
  print("a. Division ")
  print("b. Multiplication")
  print("c. Modulus")
  print("d. Float Division\n")
  q7a = input("What is the answer? ")
  while not q7a == "a" and not q7a == "b" and not q7a == "c" and not q7a == "d":
    q7a = input("Please answer 'a, b, c, d'.\n").lower()
  if q7a == "c":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was c.\n")
    total += 0

  print("8. Adding two strings together is called: ")
  print("a. Concatenation")
  print("b. Addition")
  print("c. Double Strings")
  print("d. None of the above\n")
  q8a = input("What is the answer? ")
  while not q8a == "a" and not q8a == "b" and not q8a == "c" and not q8a == "d":
    q8a = input("Please answer 'a, b, c, d'.\n").lower()
  if q8a == "a":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was a.\n")
    total += 0

  print("9. How many megabytes in 1 gigabyte? ")
  print("a. 10,000 MB")
  print("b. 100 MB")
  print("c. 1000 MB")
  print("d. 800 MB\n")
  q9a = input("What is the answer? ")
  while not q9a == "a" and not q9a == "b" and not q9a == "c" and not q9a == "d":
    q9a = input("Please answer 'a, b, c, d'.\n").lower()
  if q9a == "c":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was c.\n")
    total += 0

  print("10. Which one of these hardware componenets stores short-term data in a computer?")
  print("a. CPU")
  print("b. Hard drive ")
  print("c. RAM")
  print("d. Power supply\n")
  q10a = input("What is the answer? ")
  while not q10a == "a" and not q10a == "b" and not q10a == "c" and not q10a == "d":
    q10a = input("Please answer 'a, b, c, d'.\n").lower()
  if q10a == "c":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was c.\n")
    total += 0

  print("11. Which one of these symbol is for commenting?")
  print("a. #")
  print("b. **")
  print("c. /comment")
  print("d. print(comment)\n")
  q11a = input("What is the answer? ")
  while not q11a == "a" and not q11a == "b" and not q11a == "c" and not q11a == "d":
    q11a = input("Please answer 'a, b, c, d'.\n").lower()
  if q11a == "a":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was a.")
    total += 0

  print("12. Which of these unit measures transfer speeds?")
  print("a. GBps")
  print("b. MBps")
  print("c. Mbps")
  print("d. All of the above\n")
  q12a = input("What is the answer? ")
  while not q12a == "a" and not q12a == "b" and not q12a == "c" and not q12a == "d":
    q12a = input("Please answer 'a, b, c, d'.\n").lower()
  if q12a == "d":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was d.\n")
    total += 0

  print("13. What is an algorithm in programming?")
  print("a. A process that the computer does by jumping around and performing tasks.")
  print("b. A language in programming.")
  print("c. A step-by-step set of instructions that describes a solution to a problem.")
  print("d. None of the above.\n")
  q13a = input("What is the answer? ")
  while not q13a == "a" and not q13a == "b" and not q13a == "c" and not q13a == "d":
    q13a = input("Please answer 'a, b, c, d'.\n").lower()
  if q13a == "c":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was c. \n")
    total += 0

  print("14. What is Moore's Law?")
  print("a. the number of transistors on a microchip quadruples about every four years")
  print("b. the number of transistors on a microchip doubles about every two years.")
  print("c. Benjamin Moore's paint is the best.")
  print("d. Everything is made up of matter.\n")
  q14a = input("What is the answer?")
  while not q14a == "a" and not q14a == "b" and not q14a == "c" and not q14a == "d":
    q14a = input("Please answer 'a, b, c, d'.\n").lower()
  if q14a == "b":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was b.\n")
    total += 0

  print("15. What is a peripheral component that displays an interface for the user to interact with?")
  print("a. Headphones")
  print("b. Keyboard and mouse")
  print("c. Monitor")
  print("d. External storage.")
  q15a = input("What is the answer? ")
  while not q15a == "a" and not q15a == "b" and not q15a == "c" and not q15a == "d":
    q15a = input("Please answer 'a, b, c, d'.\n").lower()
  if q15a:
    print("")

    total += 1
  else:
    print("")

    total += 0

#Number guessing minigame in the middle of the quiz 
correct_number = False
#Number guessing minigame in the middle of the quiz 
correct_number = False
print("*****Halftime break! You get 3 tries to guess the correct number for an extra point*****\n Rules:\n 1.The number range is 1-10\n 2.The number changes everytime you guess\n")

for i in range(2):
  while True:
    try:
      guess = int(input("What is your guess? "))
      break
    except ValueError:
        print("Please enter a number!")  
        continue
  if guess == random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    print("\nCONGRATS you get an extra point. The quiz will continue.")
    correct_number = True
    total += 1
    break
  else:
    print("Try again\n")

#Last attempt and different statements 
if correct_number != True:
  while True:
    try:
      guess = int(input("What is your guess? "))
      break
    except ValueError:
        print("Please enter a number!")  
        continue
  if guess  == random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    print("\nCONGRATS you get an extra point. The quiz will continue.\n")
    total += 1  
  else:
    print("Good try, the quiz will resume.\n")

  print("16. ")
  print("")
  print("")
  print("")
  print("")
  print(" ")
  q16a = input("What is the answer? ")
  if q16a:
    print("")

    total += 1
  else:
    print("")

    total += 0

  print("")
  print("")
  print("")
  print("")
  print("")
  print(" ")
  q17a = input("What is the answer? ")
  if q17a:
    print("")

    total += 1
  else:
    print("")

    total += 0

  print("")
  print("")
  print("")
  print("")
  print("")
  print(" ")
  q18a = input("What is the answer? ")
  if q18a :
    print("")

    total += 1
  else:
    print("")

    total += 0

  print("")
  print("")
  print("")
  print("")
  print("")
  print(" ")
  q19a = input("What is the answer? ")
  if q19a :
    print("")

    total += 1
  else:
    print("")

    total += 0

  print("")
  print("")
  print("")
  print("")
  print("")
  print(" ")
  q20a = input("What is the answer? ")
  if q20a :
    print("")

    total += 1
  else:
    print("")

    total += 0

  print("")
  print("")
  print("")
  print("")
  print("")
  print(" ")
  q21a = input("What is the answer? ")
  if q21a :
    print("")

    total += 1
  else:
    print("")

    total += 0

  print("")
  print("")
  print("")
  print("")
  print("")
  print(" ")
  q22a = input("What is the answer? ")
  if q22a :
    print("")

    total += 1
  else:
    print("")

    total += 0

  print("")
  print("")
  print("")
  print("")
  print("")
  print(" ")
  q23a = input("What is the answer? ")
  if q23a :
    print("")

    total += 1
  else:
    print("")

    total += 0

  print("")
  print("")
  print("")
  print("")
  print("")
  print(" ")
  q24a = input("What is the answer? ")
  if q24a :
    print("")

    total += 1
  else:
    print("")

    total += 0

  print("")
  print("")
  print("")
  print("")
  print("")
  print(" ")
  q25a = input("What is the answer? ")
  if q25a :
    print("")

    total += 1
  else:
    print("")

    total += 0

  print("")
  print("")
  print("")
  print("")
  print("")
  print(" ")
  q26a = input("What is the answer? ")
  if q26a :
    print("")

    total += 1
  else:
    print("")

    total += 0

  print("")
  print("")
  print("")
  print("")
  print("")
  print(" ")
  q27a = input("What is the answer? ")
  if q27a :
    print("")

    total += 1
  else:
    print("")

    total += 0

  print("")
  print("")
  print("")
  print("")
  print("")
  print(" ")
  q28a = input("What is the answer? ")
  if q28a :
    print("")

    total += 1
  else:
    print("")

    total += 0

  print("")
  print("")
  print("")
  print("")
  print("")
  print(" ")
  q29a = input("What is the answer? ")
  if q29a :
    print("")

    total += 1
  else:
    print("")

    total += 0

  print("")
  print("")
  print("")
  print("")
  print("")
  print(" ")
  q30a = input("What is the answer? ")
  if q30a == :
    print("")

    total += 1
  else:
    print("")

    total += 0

#End of the quiz and total score 
end = print("Your total score was", str(total), "/30")
print("Thank you for taking my quiz!")

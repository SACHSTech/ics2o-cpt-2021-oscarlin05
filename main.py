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

#Define the variables and booleans
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
  print("1. What is a function that a CPU does? (ENTER a, b, c, or d)")
  print("a. A CPU is a chip that executes commands that make up a program")
  print("b. A CPU supplies electricity to the entire computer")
  print("c. A CPU is a storage that can hold large amounts of data")
  print("d. A CPU is a computer case\n")
  q1a = input("What is the answer? ")
  while not q1a == "a" and not q1a == "b" and not q1a == "c" and not q1a == "d":
    q1a = input("Please answer 'a, b, c, d'.\n").lower()
  if q1a == "a":
    print("CORRECT\n")
    total += 1
  else: 
    print("INCORRECT, the answer was a.\n")
    total += 0

  print("2. What is the function of a power supply?")
  print("a. The power supply supplies electricity only to the CPU")
  print("b. The power supply supplies electricity only to the GPU")
  print("c. The power supply supplies electricity to your television")
  print("d. The power supply supplies electricity to computer hardware components \n")
  q2a = input("What is the answer? ")
  while not q2a == "a" and not q2a == "b" and not q2a == "c" and not q2a == "d":
    q2a = input("Please answer 'a, b, c, d'.\n").lower()
  if q2a == "d":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was d\n")
    total += 0

  print("3. What is the order of the sequence of events in computer processing?")
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

  print("4. What some input devices for a computer?")
  print("a. Mouse and speakers")
  print("b. Keyboard and mouse")
  print("d. Headphones")
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

  print("5. What is a spyware in a malware?")
  print("a. A spyware is a software that spies on you by tracking your online activities to send advertisements back to the system")
  print("b. A spyware is an application that stalks what you are doing")
  print("c. A spyware is a malware that records you from your computer camera")
  print("d. There is no such thing as a spyware\n")
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

  print("7. What are common malware strategies to get victims to download their files? ")
  print("a. Free money ads")
  print("b. A FBI notice that make the victim pay money")
  print("c. Sketchy website with unsafe download links")
  print("d. All of the above\n")
  q7a = input("What is the answer? ")
  while not q7a == "a" and not q7a == "b" and not q7a == "c" and not q7a == "d":
    q7a = input("Please answer 'a, b, c, d'.\n").lower()
  if q7a == "d":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was c.\n")
    total += 0

  print("8. What are some ways to avoid malware on your computer?")
  print("a. Click the ad immediately")
  print("b. Think twice before clicking")
  print("c. Install a trusted anti-virus software")
  print("d. Both b and c\n")
  q8a = input("What is the answer? ")
  while not q8a == "a" and not q8a == "b" and not q8a == "c" and not q8a == "d":
    q8a = input("Please answer 'a, b, c, d'.\n").lower()
  if q8a == "d":
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

  print("10. Which one of these hardware components stores short-term data in a computer?")
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

  print("11. What are some output devices from a computer?")
  print("a. Monitor and speakers")
  print("b. Mouse and keyboard")
  print("c. Monitor and mouse")
  print("d. None of the above \n")
  q11a = input("What is the answer? ")
  while not q11a == "a" and not q11a == "b" and not q11a == "c" and not q11a == "d":
    q11a = input("Please answer 'a, b, c, d'.\n").lower()
  if q11a == "a":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was a.\n")
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

  print("13. What does GHz (gigahertz) measure on a CPU?")
  print("a. How fast a CPU can refresh the frames for a monitor")
  print("b. How fast a CPU can process a mouse's sensitivity")
  print("c. How fast the processor can process data")
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
  print("b. the number of transistors on a microchip doubles about every two years")
  print("c. Benjamin Moore's paint is the best")
  print("d. Everything is made up of matter\n")
  q14a = input("What is the answer? ")
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
  print("d. External storage\n")
  q15a = input("What is the answer? ")
  while not q15a == "a" and not q15a == "b" and not q15a == "c" and not q15a == "d":
    q15a = input("Please answer 'a, b, c, d'.\n").lower()
  if q15a == "c":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was c.\n")
    total += 0

#Number guessing minigame in the middle of the quiz 
  correct_number = False
  print("*****Halftime break! You get 3 tries to guess the correct number for an extra point*****\n Rules:\n 1.The number range is 1-5\n 2.The number changes every time you guess\n")

  for i in range(2):
    while True:
      try:
        guess = int(input("What is your guess? "))
        break
      except ValueError:
          print("Please enter a number!")  
          continue
    if guess == random.choice([1, 2, 3, 4, 5]):
      print("\nCONGRATS you get an extra point. The quiz will continue.\n")
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
    if guess  == random.choice([1, 2, 3, 4, 5]):
      print("CONGRATS you get an extra point. The quiz will continue.\n")
      total += 1  
    else:
      print("Good try, the quiz will resume.\n")

  print("16. What is an operating system?")
  print("a. An operating system is the gears inside a computer spinning")
  print("b. An operating system is a hardware")
  print("c. An operating system is an unnecessary software on a computer that takes up space and makes your computer slower")
  print("d. An operating system provides a platform for all other software and hardware to operate on a computer\n")
  q16a = input("What is the answer? ")
  while not q16a == "a" and not q16a == "b" and not q16a == "c" and not q16a == "d":
    q16a = input("Please answer 'a, b, c, d'.\n").lower()
  if q16a == "d":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was d.\n")
    total += 0

  print("17. Whats is an ISP?")
  print("a. ISP stands for Internet Service Provider and is the company that gives you access to the internet and other web services")
  print("b. ISP stands for International Space Program and that teaches people about space")
  print("c. ISP is a program or a hardware in a computer that automatically allows them to access the internet")
  print("d. All of the above\n")
  q17a = input("What is the answer? ")
  while not q17a == "a" and not q17a == "b" and not q17a == "c" and not q17a == "d":
    q17a = input("Please answer 'a, b, c, d'.\n").lower()
  if q17a == "a":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was a\n")
    total += 0

  print("18. What is the internet?")
  print("a. The internet is a signal coming from a router")
  print("b. The internet is a software on a computer that boosts the performance of it")
  print("c. The internet is a software on a computer that gives access to modify hardware components")
  print("d. The internet is a system of computer networks connected to one another around the world\n")
  q18a = input("What is the answer? ")
  while not q18a == "a" and not q18a == "b" and not q18a == "c" and not q18a == "d":
    q18a = input("Please answer 'a, b, c, d'.\n").lower()
  if q18a == "d":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was d\n")
    total += 0

  print("19. What is a virus in a computer?")
  print("a. A virus is what makes a computer very sick")
  print("b. A virus is a contagious program or code that attaches itself to another part of software and then replicates when the program is started. ")
  print("c. A virus is a program that makes your computer explode")
  print("d. A virus is a program that gives a computer super processing speeds\n")
  q19a = input("What is the answer? ")
  while not q19a == "a" and not q19a == "b" and not q19a == "c" and not q19a == "d":
    q19a = input("Please answer 'a, b, c, d'.\n").lower()
  if q19a == "b":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was b\n")
    total += 0

  print("20. What is the function of a motherboard in a computer?")
  print("a. The motherboard cools down the hardware components of a computer")
  print("b. The motherboard is a software that only boosts the CPU performance")
  print("c. The motherboard serves as a single platform that connects all the components of the computer together")
  print("d. None of the above\n")
  q20a = input("What is the answer? ")
  while not q20a == "a" and not q20a == "b" and not q20a == "c" and not q20a == "d":
    q20a = input("Please answer 'a, b, c, d'.\n").lower()
  if q20a == "c":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT")
    total += 0

  print("21. What is the function of a graphics card in a computer?")
  print("a. A graphics card supplies electricity to the computer")
  print("b. A graphics card helps the computer cool down better with its fans")
  print("c. A graphics card stores long-term storage for the computer")
  print("d. A graphics card primary function is to render graphics\n")
  q21a = input("What is the answer? ")
  while not q21a == "a" and not q21a == "b" and not q21a == "c" and not q21a == "d":
    q21a = input("Please answer 'a, b, c, d'.\n").lower()
  if q21a == "d":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was d\n")
    total += 0

  print("22. How many bits are in a byte?")
  print("a. 1 bit")
  print("b. 8 bits")
  print("c. 1000 bits")
  print("d. 360 bits\n")
  q22a = input("What is the answer? ")
  while not q22a == "a" and not q22a == "b" and not q22a == "c" and not q22a == "d":
    q22a = input("Please answer 'a, b, c, d'.\n").lower()
  if q22a == "b":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was b\n")
    total += 0

  print("23. What is a ransomware in a malware?")
  print("a. A ransomware is a malware that gives your locations to people so that they can rob you")
  print("b. A malware that protects you from other viruses")
  print("c. A ransomware is a program that protects you from online scams")
  print("d. A virus that makes you think you must pay a ransom.\n")
  q23a = input("What is the answer? ")
  while not q23a == "a" and not q23a == "b" and not q23a == "c" and not q23a == "d":
    q23a = input("Please answer 'a, b, c, d'.\n").lower()
  if q23a == "d":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was d\n")
    total += 0

  print("24. Which answer below is a list of softwares?")
  print("a. Windows, Safari, Spotify")
  print("b. Monitor, Mouse, Keyboard")
  print("c. iPad, iPhone, Samsung Galaxy S21")
  print("d. CPU, GPU, Motherboard\n")
  q24a = input("What is the answer? ")
  while not q24a == "a" and not q24a == "b" and not q24a == "c" and not q24a == "d":
    q24a = input("Please answer 'a, b, c, d'.\n").lower()
  if q24a == "a":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was a\n")
    total += 0

  print("25. What is a keylogger in a malware?")
  print("a. Keyloggers is a type of monitoring software that captures every keystroke the user types")
  print("b. Keyloggers make your keyboard sticky and jammed")
  print("c. Keyloggers is a virus that automatically types random things on your computer")
  print("d. Keyloggers is a software that protects and hides your keystrokes from other people \n")
  q25a = input("What is the answer? ")
  while not q25a == "a" and not q25a == "b" and not q25a == "c" and not q25a == "d":
    q25a = input("Please answer 'a, b, c, d'.\n").lower()
  if q25a == "a":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was a\n")
    total += 0

  print("26. What is 'utility' in terms of a computer software?")
  print("a. Utility is a software that connects the mouse and keyboard to the computer")
  print("b. Utility is a software that fixes problems and maintains the performance of a computer")
  print("c. Utility is a hardware component boosts the performance of the entire computer")
  print("d. All of the above\n")
  q26a = input("What is the answer? ")
  while not q26a == "a" and not q26a == "b" and not q26a == "c" and not q26a == "d":
    q26a = input("Please answer 'a, b, c, d'.\n").lower()
  if q26a == "b":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was b.\n")
    total += 0

  print("27. What is a firewall?")
  print("a. A fire wall is a wall made up of fire")
  print("b. A fire wall is a wall that does not let anyone in or out")
  print("c. A firewall is a hardware device or software program that protects your network from malicious user, activities, and websites")
  print("d. All of the above\n")
  q27a = input("What is the answer? ")
  while not q27a == "a" and not q27a == "b" and not q27a == "c" and not q27a == "d":
    q27a = input("Please answer 'a, b, c, d'.\n").lower()
  if q27a == "c":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was c\n")
    total += 0

  print("28. What are some examples of Web Browsers?")
  print("a. Chrome, Safari, Firefox")
  print("b. iOS, Windows, Linux")
  print("c. iTunes, Spotify, Windows media player")
  print("d. Final Cut Pro, Logic Pro, Adobe Creative Cloud\n")
  q28a = input("What is the answer? ")
  while not q28a == "a" and not q28a == "b" and not q28a == "c" and not q28a == "d":
    q28a = input("Please answer 'a, b, c, d'.\n").lower()
  if q28a == "a":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was a.\n")
    total += 0

  print("29. The symbol for bits is B.")
  print("a. True")
  print("b. False\n")
  q29a = input("What is the answer? ").lower()
  while not q29a == "a" and not q29a == "b" and not q29a == "true" and not q29a == "false":
    q29a = input("Please answer 'a, b, true, false'.\n").lower()
  if q29a == "b":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was b.\n")
    total += 0

  print("30. What are some examples of operating systems?")
  print("a. RAM, CPU, GPU")
  print("b.Chrome, Safari, Edge")
  print("c. Apple, Samsung, LG")
  print("d. Linux, Mac OS, Unix\n")
  q30a = input("What is the answer? ")
  while not q30a == "a" and not q30a == "b" and not q30a == "c" and not q30a == "d":
    q30a = input("Please answer 'a, b, c, d'.\n").lower()
  if q30a == "d":
    print("CORRECT\n")
    total += 1
  else:
    print("INCORRECT, the answer was d\n")
    total += 0

#End of the quiz and total score 
end = print("*****Your total score was", str(total), "/30*****")
print("*****Thank you for taking my quiz!*****")
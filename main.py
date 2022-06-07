import random

cpuNumber = random.randint(0,10)
tries = 5
win = False
play = True

while play == True:
  while tries > 0:
    pickedNumber = input("pick a number between 0 and 10: ")
  
    if int(pickedNumber) == cpuNumber:
      win = True
      break
    elif int(pickedNumber) > 10 or int(pickedNumber) < 0:
      print("the number you typed was invalid!")
    else:
      tries -=1
      print(f"sorry thats the wrong number. You have {tries} tries left")
  
  
  if win == True:
    print(f"Congratulations the correct number was {cpuNumber} and it only took you {5-tries} tries!")
  else:
    print(f"Sorry the number was {cpuNumber}")

  again = input("play again? Y/N: ")
  if again == 'Y':
    win = False
    tries = 5
  else:
    print("goodbye!")
    play = False
  

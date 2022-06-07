import random

cpuNumber = random.randint(0,10)
tries = 5
win = False

print(cpuNumber)

while tries > 0:
  pickedNumber = input("pick a number between 0 and 10: ")

  if(int(pickedNumber) == cpuNumber):
    win = True
    break
  else:
    tries -=1
    print(f"sorry thats the wrong number. You have {tries} tries left")



if win == True:
  print(f"Congratulations the correct number was {cpuNumber} and it only took you {5 - tries}")
else:
  print(f"Sorry the number was {cpuNumber}")
  
#  End Results for Recipe Cost
#  By Eden Cave
#  17/11/2022
#  Version 2

#  sets up exit code
exit_code = False

#  asks for user input and prints error if input is invalid
while exit_code == False:
  try:
    total_cost = float(input("Please enter a total cost: "))
  except:
    print("Error: please enter a valid number")
    break
  #  exits loop if both inputs are recieved
  try:  
    serving_cost = float(input("Please enter a cost per serving: "))
    exit_code = True
  except:
    print("Error: please enter a valid number")
    break
#  displays user input
while exit_code == True:
  print(str("Total Cost:", total_cost))
  print(str("Cost Per Serving:", serving_cost))
  break
#  End Results for Recipe Cost (Iteration 2)
#  By Eden Cave
#  17/11/2022
#  Version 1

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
  print("Total Cost:\n", total_cost)
  print("---Cost Per Serving---/n", serving_cost)
  break
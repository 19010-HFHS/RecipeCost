#  Ingredients List for recipe cost (Iteration 2)
#  By Eden Cave
#  14/11/2022
#  Version 1

#  set up for ingredients list and exit code
exit_code = False
ingredient_named = []
amount_required = []
cost = []
amount_sold_as = []

#  asks for user input
while exit_code == False:
  #  asks for name of ingredient, stores answer and checks for exit code
  try:
    ingredient_name = input("Please enter an ingredient: ")
    #  exits program if exit code is detected
    if ingredient_name == "xxx":
      exit_code = True
      break
  #  checks that ingredient name isn't a number
  except:
    print("Error: please enter a valid string")
    break
  else:
    ingredient_named.append(ingredient_name)
  
  #  asks for amount needed, stores answer and checks for exit code
  try:
    amount_needed = int(input("Please enter the amount needed (in grams): "))
  #  checks that amount needed is a whole number
  except:
    print("Error: please enter a valid number")
    break
  #  prevents invalid inputs from being added to list
  else:
    amount_required.append(amount_needed)

  #  Asks for price, stores answer and checks for exit code
  try:
    price = float(input("please enter the price: $"))
  #  checks that the price is a float (decimal number)
  except:
    print("Error: please enter a valid number")
    break
  else:
    cost.append(price)

  # asks for amount sold, stores answer and checks for exit code
  try:
    amount_sold = int(input("please enter the amount sold (in grams): "))
  #  checks that the amount sold is a whole number
  except:
    print("Error: please enter a valid number")
    break
  else:
    amount_sold_as.append(amount_sold)

# ends program and prints results
if exit_code == True:
  print(ingredient_named)
  print(amount_required)
  print(cost)
  print(amount_sold_as)
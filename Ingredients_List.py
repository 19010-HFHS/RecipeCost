#  Ingredients List for recipe cost
#  By Eden Cave
#  13/11/2022
#  Version 6

#  set up for ingredients list and exit code
exit_code = False
ingredients = []

#  asks for user input
while exit_code == False:
  #  asks for name of ingredient, stores answer and checks for exit code
  ingredient_name = input("Please enter and ingredient: ")
  #  exits program if exit code is detected
  if ingredient_name == "xxx":
    exit_code = True
  #  checks that ingredient name isn't a number
  if type(ingredient_name) != str:
    print("Error: please enter a valid string")
    break
  else:
    ingredients.append(ingredient_name)
  
  #  asks for amount needed, stores answer and checks for exit code
  amount_needed = input("Please enter the amount needed (in grams): ")
  #  exits program if exit code is detected
  if amount_needed == "xxx":
    exit_code = True
  #  checks that amount needed is a whole number
  if type(amount_needed) != int:
    print("Error: please enter a valid number")
    break
  #  prevents invalid inputs from being added to list
  else:
    ingredients.append(amount_needed)

  #  Asks for price, stores answer and checks for exit code
  price = input("please enter the price: $")
  #  exits program if exit code is detected
  if price == "xxx":
    exit_code = True
  #  checks that the price is a float (decimal number)
  if type(price) != float:
    print("Error: please enter a valid number")
    break
  else:
    ingredients.append(price)

  # asks for amount sold, stores answer and checks for exit code
  amount_sold = input("please enter the amount sold (in grams): ")
  #  exits program if exit code is detected
  if amount_sold == "xxx":
    exit_code = True
  #  checks that the amount sold is a whole number
  if type(amount_sold) != int:
    print("Error: please enter a valid number")
    break
  else:
    ingredients.append(amount_sold)

# ends program and prints results
if exit_code == True:
  print(ingredients)
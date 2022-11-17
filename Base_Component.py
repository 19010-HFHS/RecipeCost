#  Base Component for Recipe Cost
#  By Eden Cave
#  11/11/2022
#  Version 3

#  defines tutorial function
def tutorial(question):
  
  #  defines instructions given
  instructions = "This program is called the Recipe Cost Calculator. It has been developed to help you manage your finances when cooking a recipe. To begin, you must enter the name of your recipe and the size of 1 serving, follwed by the ingredients you need, how much you need, and the prices and amounts they are sold for (enter xxx when you are done entering the required values). The RC Calculator will then calculate the total price of the recipe, along with the price per serving."

  yes_no = input(question)
  #  skips instructions if the user has used program before
  if yes_no.lower() == "yes" or yes_no.lower() == "y":
    #  asks for recipe name
    recipe = input("What is your recipe called? ")
    #  stores recipe name
    recipe_name.append(recipe)
    #  asks for serving size
    serving = input("what size are the servings you are making? ")
    #  stores srving size
    serving_size.append(float(serving))
  #  gives instructions if the user has not used program before
  elif yes_no.lower() == "no" or yes_no.lower() == "n":
    print(instructions)
    #  asks for recipe name
    recipe = input("\nWhat is your recipe called? ")
    #  stores recipe name
    recipe_name.append(recipe)
    #  asks for serving size
    serving = input("what size are the servings you are making? ")
    #  stores srving size
    serving_size.append(float(serving))
  
#  Main Routine

#  Stores values for later use
intro = ""
recipe_name = []
serving_size = []
exit_code = False
ingredient_costs = []

#  Main loop
while exit_code == False:
  #  asks if the user requires a tutorial
  intro = tutorial("Have you used this program before?: ")
  
  #  asks for name of ingredient, stores answer and checks for exit code
  try:
    ingredient_name = input("Please enter an ingredient: ")
  
  #  checks that ingredient name isn't a number
  except:
    print("Error: please enter a valid string")
    break
  
  #  asks for amount needed, stores answer and checks for exit code
  try:
    amount_required = int(input("Please enter the amount needed (in grams): "))
  #  checks that amount needed is a whole number
  except:
    print("Error: please enter a valid number")
    break

  #  Asks for price, stores answer and checks for exit code
  try:
    cost = float(input("please enter the price: $"))
  #  checks that the price is a float (decimal number)
  except:
    print("Error: please enter a valid number")
    break

  # asks for amount sold, stores answer and checks for exit code
  try:
    amount_sold_as = int(input("please enter the amount sold (in grams): "))
  #  checks that the amount sold is a whole number
  except:
    print("Error: please enter a valid number")
    break
  
  #  does the mathematical calculations
  base_price = (cost / amount_sold_as)
  result = (base_price * amount_required)
  ingredient_cost = "%.2f" % result
  print(ingredient_cost)
  ingredient_costs.append(ingredient_cost)

  #  asks if user whats to enter more variables or see results
  repeat = input("Would you like to continue?: ")  
  if repeat.lower() == "yes" or repeat.lower() == "y":
    continue
  if repeat.lower() == "no" or repeat.lower() == "n":
    exit_code = True

#  displays final results
while exit_code == True:
  total_cost = sum(ingredient_costs)
  print(total_cost)
  serving_cost = (total_cost / serving_size)
  print(serving_cost)
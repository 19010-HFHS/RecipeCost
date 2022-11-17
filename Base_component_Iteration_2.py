#  Base Component for Recipe Cost (Iteration 2)
#  By Eden Cave
#  11/11/2022
#  Version 1

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
  #  gives instructions if the user has not used program before
  elif yes_no.lower() == "no" or yes_no.lower() == "n":
    print(instructions)
    #  asks for recipe name
    recipe = input("\nWhat is your recipe called? ")
    #  stores recipe name
    recipe_name.append(recipe)

#  defines the boundary case question 
def bc_question(question):
  #  asks for feedback
  feedback = input(question)
  #  response if feedback is positive
  if feedback > 5:
    print("Wow! Thanks for the great feedback!")
  #  response if feedback is nuetral
  if feedback == 5:
    print("Thank you for your feedback!")
  #  response if feedback is negative
  if feedback < 5:
    ("Thank you for your feedback, I will work harder next time.")

#  Main Routine

#  Stores values for later use
intro = ""
recipe_name = []
exit_code = False
ingredient_costs = []

#  asks if the user requires a tutorial
intro = tutorial("Have you used this program before?: ")
#  asks for serving size
serving_size = float(input("what size are the servings you are making? "))

#  Main loop
while exit_code == False:
  
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
  ingredient_costs.append(float(ingredient_cost))

  #  asks if user whats to enter more variables or see results
  repeat = input("Would you like to continue?: ")  
  if repeat.lower() == "yes" or repeat.lower() == "y":
    continue
  if repeat.lower() == "no" or repeat.lower() == "n":
    exit_code = True

#  displays final results
while exit_code == True:
  total_cost = sum(ingredient_costs)
  print("\nTotal Cost:\n$" + str(total_cost))
  serving_cost = (total_cost / serving_size)
  print("\n---Cost Per Serving---\n$" + str(serving_cost))
  break

end_score = bc_question("On ascale of 1 to 10, how good was this program?: ")
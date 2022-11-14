#  Base Component for Recipe Cost
#  By Eden Cave
#  11/11/2022
#  version 2

#  defines tutorial function
def tutorial(question):
  
  #  defines instructions given
  instructions = "This program is called the Recipe Cost Calculator. It has been   developed to help you manage your finances when cooking a recipe. To begin, you must enter the name of your recipe and the size of 1 serving, follwed by the ingredients you need, how much you need, and the prices and amounts they are sold for (enter xxx when you are done entering the required values). The RC Calculator will then calculate the total price of the recipe, along with the price per serving."

    #  skips instructions if the user has used program before
  if yes_no.lower() == "yes" or yes_no.lower() == "y":
    #  asks for recipe name
    recipe = input("What is your recipe called? ")
    #  stores recipe name
    recipe_name.append(recipe)
    #  asks for serving size
    serving = input("what size are the servings you are making? ")
    #  stores srving size
    serving_size.append(int(serving))
  #  gives instructions if the user has not used program before
  elif yes_no.lower() == "no" or yes_no.lower() == "n":
    print(instructions)

#  Main Routine

#  Stores values for later use
recipe_name = []
serving_size = []
yes_no = ""
exit_code = False

#  Main loop
while exit_code == False and yes_no == "":
  #  asks if the user requires a tutorial
  yes_no = tutorial("Have you used this program before?: ")

#  Instructions for Recipe Cost (Iteration 2)
#  By Eden Cave
#  11/11/2022
#  Version 1

#  Stores values for later use
recipe_name = []
serving_size = []
#  defines instructions given
instructions = "This program is called the Recipe Cost Calculator. It has been developed to help you manage your finances when cooking a recipe. To begin, you must enter the name of your recipe and the size of 1 serving, follwed by the ingredients you need, how much you need, and the prices and amounts they are sold for. The RC Calculator will then calculate the total price of the recipe, along with the price per serving."
#  Asks the user if they have used the program before
tutorial = input("Have you used this program before? ")
#  skips instructions if the user has used program before
if tutorial.lower() == "yes" or tutorial.lower() == "y":
  recipe = input("What is your recipe called?")
  recipe_name.append(recipe)
  serving = input(int("what size are the servings you are making?"))
  serving_size.append(serving)
#  gives instructions if the user has not used program before
elif tutorial.lower() == "no" or tutorial.lower() == "n":
  print(instructions)
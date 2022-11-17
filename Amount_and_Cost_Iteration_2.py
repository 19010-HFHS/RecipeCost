#  Amount and Cost for Recipe Cost (Iteration 2)
#  By Eden Cave
#  16/11/2022
#  Version 2

#  stores values for later
serving_size = input("what size are the servings you are making?: ")
amount_required = ""
cost = ""
amount_sold_as = ""
exit_code = False
ingredient_costs = []


#  asks for user input
while exit_code != True:


  #  asks user for amount required
  try:
    amount_required = int(input("Please enter an amount required: "))
  except:
    print("please enter a whole number")
    break
    #  asks user for cost
  try:  
    cost = float(input("Please enter a cost: $"))
  except:
    print("please enter a valid decimal")
    break
    #  asks user for amount the ingredient is sold as
  try:    
    amount_sold_as = int(input("Please enter amount the ingredient is sold as: "))
  except:
    print("please enter a whole number")
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
  
while exit_code == True:
  total_cost = sum(ingredient_costs)
  print(total_cost)
  serving_cost = (total_cost / serving_size)
  print(serving_cost)
#  Amount and Cost for Recipe Cost (Iteration 2)
#  By Eden Cave
#  16/11/2022
#  Version 2

#  stores values for later
amount_required = ""
amount_sold_as = ""
exit_code = False
result = []

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
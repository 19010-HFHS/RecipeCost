#  Amount and Cost for Recipe Cost
#  By Eden Cave
#  15/11/2022
#  version 1

#  stores values for later
amount_required = ""
cost = ""
amount_sold_as = ""
exit_code = False

#  asks for user input
while exit_code != True:
  #  asks user for amount required
  amount_required = int(input("Please enter an amount required: "))
  #  asks user for cost
  cost = float(input("Please enter a cost: $"))
  #  asks user for amount the ingredient is sold as
  amount_sold_as = int(input("Please enter amount the ingredient is sold as: "))
  #  does the mathmatical calculations
  base_price = (amount_sold_as / cost)
  result = (base_price * amount_required)
  print("2d%" % result)
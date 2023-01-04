#How much the package weighs
weight = 8.4

#Ground shipping costs
#Output
print("Your ground shipping cost is ", end="")
#1.50 is price per pound if less than or equal to 2
if weight <= 2:
  print((weight * 1.50) + 20.00)
#3.00 is price per pound for packages btween 2-6 pounds
elif weight >= 2.01 and weight <= 6:
  print((weight * 3.00) + 20.00)
#4.00 is price per pound for packages between 6-10 pounds
elif weight >= 6.01 and weight <= 10:
  print((weight * 4.00) + 20.00)
#4.75 is price per pound on packages over 10 pounds
elif weight >= 10:
  print((weight * 4.75) + 20.00)

#Premium ground shipping is an additional 125 flat fee
premium_ground_cost = 125.00
#inform consumer of premium shipping
print("Premium shipping available for additional flat fee of ", end="")
print(premium_ground_cost)

#Drone Shipping
#How much the package weighs
weight = 1.5
#Output
print("Your ground shipping cost is ", end="")
#4.50 is price per pound if less than or equal to 2
if weight <= 2:
  print((weight * 4.50) + 0.00)
#3.00 is price per pound for packages btween 2-6 pounds
elif weight >= 2.01 and weight <= 6:
  print((weight * 9.00) + 0.00)
#4.00 is price per pound for packages between 6-10 pounds
elif weight >= 6.01 and weight <= 10:
  print((weight * 12.00) + 0.00)
#4.75 is price per pound on packages over 10 pounds
elif weight >= 10:
  print((weight * 14.25) + 0.00)


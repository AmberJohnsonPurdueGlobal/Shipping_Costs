#How much the package weighs
ground_weight = 10

#Ground shipping costs
#Output
print("Your ground shipping cost is ", end="")
#1.50 is price per pound if less than or equal to 2
if ground_weight <= 2:
  ground_cost = ((ground_weight * 1.50) + 20.00)
  print(ground_cost)
#3.00 is price per pound for packages btween 2-6 pounds
elif ground_weight >= 2.01 and ground_weight <= 6:
  ground_cost = ((ground_weight * 3.00) + 20.00)
  print(ground_cost)
#4.00 is price per pound for packages between 6-10 pounds
elif ground_weight >= 6.01 and ground_weight <= 10:
  ground_cost = ((ground_weight * 4.00) + 20.00)
  print(ground_cost)
#4.75 is price per pound on packages over 10 pounds
elif ground_weight >= 10:
  ground_cost = ((ground_weight * 4.75) + 20.00)
  print(ground_cost)

#Premium ground shipping is an additional 125 flat fee
premium_ground_cost = 125.00
#inform consumer of premium shipping
print("Premium shipping available for additional flat fee of ", end="")
print(premium_ground_cost)

#Drone Shipping
#How much the package weighs
drone_weight = 10
#Output
print("Your Drone shipping cost is ", end="")
#4.50 is price per pound if less than or equal to 2
if drone_weight <= 2:
  drone_cost = ((drone_weight * 4.50) + 0.00)
  print(drone_cost)
#3.00 is price per pound for packages btween 2-6 pounds
elif drone_weight >= 2.01 and drone_weight <= 6:
  drone_cost = ((drone_weight * 9.00) + 0.00)
  print(drone_cost)
#4.00 is price per pound for packages between 6-10 pounds
elif drone_weight >= 6.01 and drone_weight <= 10:
  drone_cost = ((drone_weight * 12.00) + 0.00)
  print(drone_cost)
#4.75 is price per pound on packages over 10 pounds
elif drone_weight >= 10:
  drone_cost((drone_weight * 14.25) + 0.00)
  print(drone_cost)
#Package Weight
#gound_weight = 4.8
#drone_weight = 4.8
#is drone weight is cheaper display the difference
if ground_cost >= drone_cost:
  print("Drone shipping is ", end="")
  print(ground_cost-drone_cost, end="")
  print(" cheaper than ground shipping")
#if ground weight is cheaper display the difference
elif drone_cost >= ground_cost:
  print("ground shipping is ", end="")
  print(drone_cost-ground_cost, end="")
  print(" cheaper than drone shipping") 


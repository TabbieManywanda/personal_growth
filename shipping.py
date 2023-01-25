#A programme to calculate total shipping charges
#for a package of particular weight.
#There are 3 packages:
#Ground shipping = A small flat charge + Weight based rate
#Premium ground shipping = Higher flat charge (no weight based rate)
#Drone shipping = Weight based rate(3X that of ground shipping) (no flat charge)


#flat shipping charges in dollars
flat_ground = 20.00
flat_premium = 125.00

#ask user to enter weight of package in lbs
weight = float(input("What is the weight of your package? "))

#raise TypeError if value entered by user is not int or float
if type(weight) != float: #and type(weight) != int:
  raise TypeError("Weight must be a number!")

#raise ValueError if number entered by user is a negative number
if weight < 0:
  raise ValueError("Weight cannot be a negative number!")

#normal ground shipping
if weight <= 2:
  cost = (1.50 * weight) + flat_ground
elif weight > 2 and weight <= 6:
  cost = (3.00 * weight) + flat_ground
elif weight > 6 and weight <= 10:
  cost = (4.00 * weight) + flat_ground
else:
  cost = (4.75 * weight) + flat_ground
print("Ground Shipping total: {}{}".format('$', round(cost, 2)))

#premium ground shipping
print("Premium Ground Shipping total: {}{}".format('$', flat_premium))

#drone shipping
if weight <= 2:
  cost = weight * 4.50
elif weight > 2 and weight <= 6:
  cost = weight * 9.00
elif weight > 6 and weight <= 10:
  cost = weight * 12.00
else:
  cost = weight * 14.25
print("Drone Shipping total: {}{}".format('$', round(cost, 2)))

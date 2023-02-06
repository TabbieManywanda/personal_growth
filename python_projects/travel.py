#welcome message
def trip_planner_welcome(name):
  '''welcomes users to the platform'''
  print("Welcome to tripplanner v1.0 {}".format(name))

#calculates a rounded time value based on a decimal
def estimated_time_rounded(estimated_time):
  '''should create a variable
  return rounded time'''
  rounded_time = round(estimated_time)
  return rounded_time

#generate messages
def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print("Your trip starts off in {}".format(origin))
  print("And you are traveling to {}".format(destination))
  print("You will be traveling by {}".format(mode_of_transport))
  print("It will take approximately {} hours".format(estimated_time))

#running the program
trip_planner_welcome("Tabitha Manywanda")
print()

estimate = estimated_time_rounded(2.78)

destination_setup("Rongai", "Madaraka", estimate)

import random

#taking name from user
name = input('Enter your name:')

#question to ask
question = input('What troubles your mind today?')

#magic 8 ball answer
answer = ""

#randomly generate values from 1 to 9
random_number = random.randint(1, 9)
#print(random_number)

#assigning magic ball phrases to values
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
else:
  answer = "Error"

#if no name entered
if len(name) == 0:
  print("Question: {}".format(question))
else:
  print("{} asks: {}".format(name, question))

#if no question entered
if len(question) == 0:
  raise Exception("A question must be asked!")
else:
  print("Magic 8-Ball's answer: {}".format(answer))

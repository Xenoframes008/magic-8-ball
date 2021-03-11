import random
random_number = random.randint(1,12)
#print(random_number)
name = "Rahul"
question = ""
answer = ""

if question == "":
 print("Please ask a question")
elif name == "":
 print("Question :" +question)
else:
 print(name + " asks : " + question)
 print("Magic 8-Ball's answer: "+ answer)
 
if random_number==1:
  print("Yes - Definitely.")
elif random_number ==2:
  print("It is decidedly so.")
elif random_number ==3:
  print("Without a doubt.")
elif random_number ==4:
  print("Reply hazy, Try again.")
elif random_number ==5:
  print("Ask again later")
elif random_number ==6:
  print("Better not tell you now")
elif random_number ==7:
  print("My sources say no.")
elif random_number ==8:
  print("Outlook not so good")
elif random_number ==9:
  print("Very doubtful")
elif random_number == 10:
  print("In your Dreams")
elif random_number == 11:
  print("Soon")
elif random_number == 12:
  print("today")
else:
  print("Error")



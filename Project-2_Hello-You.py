#Ask user for name.
print("Whats you name?")
name = input('-->')

#Ask user for age.
print("Whats you age?")
age = input('-->')

#Ask user for city.
print("What city are you from?")
city = input('-->')

#Ask user what they enjoy.
print("What do you enjoy the most?")
enjoy = input('-->')

#Create output text.
text = "Your name is {} and your age is {}. You live in {} city and you enjoy {} the most. Am I right?".format(name,age,city,enjoy)

#Print output to screen.
print(text)

#String sample

string = "Bath and body"

print (len(string))
print (string.upper())
print (string.lower())

number = 10

print ("This is a number "+str(number)+" in string.")
print ("I want to go to "+string.upper()+" right now.")

#This introduces input method

name = input("What is your name? ")
person = input("Who do you want to visit? ")
reason = input("What is your purpose for visiting? ")

print ("Good day %s, you want to visit %s with a purpose of %s."%(name, person, reason))

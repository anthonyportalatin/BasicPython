#This is an example of lists and dictionary

dogs = ['Casper', 'Pongo', 'Max', 'Molly', 'Meyli']
         
print(dogs[0:5])

dogs.append('Gilly')

print(dogs[0:6])

del dogs[2]

print(dogs[0:5])

phone = {'Ryan':1234, 'Sol':5678, 'Gil':9101, 'Tony':1213}

index = input("What number do you want? ")
print (phone[index])
    
index = input("Add a new contact, Name: ")
phone[index] = input("Number: ")
print("You added: " +index +" " +phone[index])


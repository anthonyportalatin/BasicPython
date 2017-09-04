#Dictionary Sample

age = {}

age['Anna'] = 20
age['Portia'] = 19
age['Ambrose'] = 65
age['Allain'] = 45

if ('Anna' in age):
    print("Anna is listed in the dictionary. She is\
\n" +str(age['Anna'])+" years old.")
else:
    print("Anna is not on the list")

print("This are all the people on the list and there age.")
print(age.keys())
print(age.values())

print(sorted(age.keys()))
print(sorted(age.values()))
print("The dictionary contains ",len(age)," entries.") 


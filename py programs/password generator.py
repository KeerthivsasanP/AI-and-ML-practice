import random

alphabets = 'abcdefghijklmnopqrstuvwxyz'
special_char =  '!@#$%^&*()_+,.'
lowercase = list(alphabets)
uppercase = list(alphabets.upper())
total_char = int(input("how many characters do you want to have ? "))
uppercount = int(input("How many uppercase ? "))
specialcount= int(input("How many special char ? "))
password = ""
lowercount = total_char-(uppercount+specialcount)

if uppercount+specialcount > total_char:
    print("Count exceeeded the total count")
else:
    for lower in range(lowercount):
        password += random.choice(lowercase)
    
    for upper in range(uppercount):
        password += random.choice(uppercase)
    
    for spec in range(specialcount):
        password += random.choice(special_char)
    
    password = list(password)
    random.shuffle(password)
    print(''.join(password))
    

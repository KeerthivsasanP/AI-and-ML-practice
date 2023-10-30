isContinue = True

auction={}
while isContinue:
    name = input("Enter your name \n")
    amount = int(input("What is your bid \n$"))
    auction[name]=amount
    choice = input("Do you want to continue(y/n)?")
    if choice != 'y':
        isContinue = False
        
    
greater = 0

for key in auction:
    if greater < auction[key]:
        person = key
        greater = auction[key]

print(f"{person} has quoted {greater} and wins")

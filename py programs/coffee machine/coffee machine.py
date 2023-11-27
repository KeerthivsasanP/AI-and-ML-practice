from coffeeMachinedb import data 

iwater = 100
imilk = 100
ipowder = 100
irupee = 0
ipaise = 0 

choice = input("What do you want to coffee or report?")

if choice == "report":
    print(f"Availability \nwater = {iwater}\npowder = {ipowder}\nmilk = {imilk}")
    irupee = irupee + (ipaise//100)
    irupee = "{:.2f}".format(irupee)
    ipaise %= 100
    ipaise = "{:.2f}".format(ipaise)
    print(f"Current amount \nRupees {irupee}\npaise = {ipaise}")

elif choice == "coffee":
    
        isContinue = True
        while isContinue:
            if (iwater > 0) and (imilk > 0) and (ipowder > 0):
                flavour = input("Enter the coffee type (cappachino/latte/iced)")
                if flavour not in data:
                    print("Flavour not found")
                    break
                input_rupee = int(input("Enter the rupee "))
                input_paise = int(input("Enter the paise "))
                input_rupee += (input_paise//100)
                input_paise %= 100
                
                if (iwater >= data[flavour]["water"]) and (ipowder >= data[flavour]["powder"]) and (imilk >= data[flavour]["milk"]) and (input_rupee >= data[flavour]["rupee"]) and (input_paise >= data[flavour]["paise"]):
                    iwater -= data[flavour]["water"]
                    ipowder -= data[flavour]["powder"]
                    imilk -= data[flavour]["milk"]
                    
                    bal_rupee = input_rupee - data[flavour]["rupee"]
                    bal_paise = input_paise - data[flavour]["paise"]

                    print(f"{input_rupee} {input_paise}")
                    print(f"bal rupees{bal_rupee}")
                    print(f"bal paise{bal_paise}")
                    irupee += data[flavour]["rupee"]
                    ipaise += data[flavour]["paise"]
                    print(f"Your {flavour} is ready")
                    
                    print(f"Your balance {bal_rupee} rupee and {bal_paise} paise")
                    print(f"Availability \nwater = {iwater}\npowder = {ipowder}\nmilk = {imilk}")

                    isContinue = input("Do you want to continue?(y/n)")
                    if isContinue != 'y':
                        isContinue = False
            else:
                Print("Out of stock")
print(f"Availability \nwater = {iwater}\npowder = {ipowder}\nmilk = {imilk}")
print(f"Amount {irupee} rupees and {ipaise} paise")

import os
import re
import time
import datetime

pastCustomers = []

date = datetime.date.today()

class Customer():

    def __init__(self, name, formula, cost, cut, color, date):
        self.name = name
        self.formula = formula
        self.cost = cost
        self.cut = cut
        self.color = color
        self.date = date

    def createCustomer(self):
        with open('Customer.txt', 'a') as file:
            file.write(self.name.title() + " paid " + str(self.cost) + " dollars  on " + str(date) + ", for: Formula: " + self.formula + " Cut: " + self.cut +"  Color: " + self.color + ",\n")
        with open('Clients', 'a') as file_object:
            file_object.write(self.name.title() + " paid " + str(self.cost) + " dollars  on " + str(date) + ", for: \nFormula: " + self.formula + " \nCut: " + self.cut +"  \nColor: " + self.color + ",\n")

#Creates Customer
def newCustomer():
    info = False
    userConfirm = False
    costError = True

    while info == False:
        print("*****************************************************************************************************************************************************************************************************************************************************")
        name = input("\nWhat is the client's name? (First and Last) \n")
        time.sleep(.3)
        formula = input("\nWhat formula was used? (if none: [N/A])\n")
        time.sleep(.3)
        cut = input("\nWhat kind of cut? (if none: [N/A]) \n")
        time.sleep(.3)
        color = input("\nWhat color did you use? (if none: [N/A])\n")
        time.sleep(.3)
        while costError == True:
            try:
                cost = int(input("\nHow much are you charging? \n" ))
                time.sleep(.3)
                costError = False
            except ValueError:
                print("No $, just numbers please")
                costError = True

        while userConfirm == False:
            userConfirm = False
            userChange = False

            print("\nClient " + name.title() + " is being charged $" + str(cost) + " for:\nFormula: " + formula + "\nCut: " + cut +"\nColor: " + color)
            time.sleep(1)
            confirm = input("\nPlease confirm this information: [Y/N]")

            while userChange == False:

                    if confirm.upper() == "Y":
                        client = Customer(name, formula, str(cost), cut, color, str(date))
                        pastCustomers.append(client)
                        client.createCustomer()
                        print("Thank You, your client has been saved!")
                        userChange = True
                        userConfirm = True
                        info = True

                    elif confirm.upper() == "N":
                        change = True
                        changeInfoError = True
                        while changeInfoError == True:
                            try:
                                changeInfo = int(input("What information would you like to change? \n\n[1] for name\n[2] for formula\n[3] for cut\n[4] for color\n[5] for cost\n\n"))
                                changeInfoError = False
                            except ValueError:
                                print("Error: invalid input")
                                changeInfoError = True


                        while change == True:

                            if str(changeInfo) == "1":
                                newName = input("\nWhat is the client's name?\n")
                                name = newName
                                changeAgain = input("Would you like to change anymore information? [Y/N]")
                                decision = False
                                while decision == False:
                                    if changeAgain.upper() == 'Y':
                                        change = True
                                        changeInfoError = True
                                        while changeInfoError == True:
                                            try:
                                                changeInfo = int(input(
                                                    "What information would you like to change? \n\n[1] for name\n[2] for formula\n[3] for cut\n[4] for color\n[5] for cost\n\n"))
                                                changeInfoError = False
                                            except ValueError:
                                                print("Error: invalid input")
                                                changeInfoError = True
                                        break
                                    elif changeAgain.upper() == 'N':
                                        change = False
                                        userChange = True
                                        break
                                    else:
                                        print("Error: Invalid input.\n\n")
                                        changeAgain = input("Would you like to change anymore information? [Y/N]")

                            elif str(changeInfo) == "2":
                                newFormula = input("\nWhat formula was used? (if none: [N/A])\n")
                                formula = newFormula
                                changeAgain = input("Would you like to change anymore information? [Y/N]")
                                decision = False
                                while decision == False:
                                    if changeAgain.upper() == 'Y':
                                        change = True
                                        changeInfoError = True
                                        while changeInfoError == True:
                                            try:
                                                changeInfo = int(input(
                                                    "What information would you like to change? \n\n[1] for name\n[2] for formula\n[3] for cut\n[4] for color\n[5] for cost\n\n"))
                                                changeInfoError = False
                                            except ValueError:
                                                print("Error: invalid input")
                                                changeInfoError = True
                                        break
                                    elif changeAgain.upper() == 'N':
                                        change = False
                                        userChange = True
                                        break
                                    else:
                                        print("Error: Invalid input.\n\n")
                                        changeAgain = input("Would you like to change anymore information? [Y/N]")

                            elif str(changeInfo) == "3":
                                newCut = input("\nWhat kind of cut? (if none: [N/A])\n")
                                cut = newCut
                                changeAgain = input("Would you like to change anymore information? [Y/N]")
                                decision = False
                                while decision == False:
                                    if changeAgain.upper() == 'Y':
                                        change = True
                                        changeInfoError = True
                                        while changeInfoError == True:
                                            try:
                                                changeInfo = int(input(
                                                    "What information would you like to change? \n\n[1] for name\n[2] for formula\n[3] for cut\n[4] for color\n[5] for cost\n\n"))
                                                changeInfoError = False
                                            except ValueError:
                                                print("Error: invalid input")
                                                changeInfoError = True
                                        break
                                    elif changeAgain.upper() == 'N':
                                        change = False
                                        userChange = True
                                        break
                                    else:
                                        print("Error: Invalid input.\n\n")
                                        changeAgain = input("Would you like to change anymore information? [Y/N]")

                            elif str(changeInfo) == "4":
                                newColor = input("\nWhat color did you use? (if none: [N/A])\n")
                                color = newColor
                                changeAgain = input("Would you like to change anymore information? [Y/N]")
                                decision = False
                                while decision == False:
                                    if changeAgain.upper() == 'Y':
                                        change = True
                                        changeInfoError = True
                                        while changeInfoError == True:
                                            try:
                                                changeInfo = int(input(
                                                    "What information would you like to change? \n\n[1] for name\n[2] for formula\n[3] for cut\n[4] for color\n[5] for cost\n\n"))
                                                changeInfoError = False
                                            except ValueError:
                                                print("Error: invalid input")
                                                changeInfoError = True
                                        break
                                    elif changeAgain.upper() == 'N':
                                        change = False
                                        userChange = True
                                        break
                                    else:
                                        print("Error: Invalid input.\n\n")
                                        changeAgain = input("Would you like to change anymore information? [Y/N]")

                            elif str(changeInfo) == "5":
                                costError = True
                                while costError == True:
                                    try:
                                        newCost = int(input("\nHow much are you charging? \n"))
                                        time.sleep(.3)
                                        costError = False
                                    except ValueError:
                                        print("No $, just numbers please")
                                        costError = True
                                cost = newCost
                                changeAgain = input("Would you like to change anymore information? [Y/N]")
                                decision = False
                                while decision == False:
                                    if changeAgain.upper() == 'Y':
                                        change = True
                                        changeInfoError = True
                                        while changeInfoError == True:
                                            try:
                                                changeInfo = int(input(
                                                    "What information would you like to change? \n\n[1] for name\n[2] for formula\n[3] for cut\n[4] for color\n[5] for cost\n\n"))
                                                changeInfoError = False
                                            except ValueError:
                                                print("Error: invalid input")
                                                changeInfoError = True
                                        break
                                    elif changeAgain.upper() == 'N':
                                        change = False
                                        userChange = True
                                        break
                                    else:
                                        print("Error: Invalid input.\n\n")
                                        changeAgain = input("Would you like to change anymore information? [Y/N]")

                            else:
                                print("ERROR: Invalid input.")
                                userChange = False


                    else:
                        print("ERROR: Invalid input.")
                        userConfirm = False
                        confirm = input("\nPlease confirm this information: [Y/N]")





#Reads all past users
with open("Customer.txt", 'r', encoding='utf-8') as file_object:
    document = file_object.readlines()
for client in document:
    match = re.match(r'(.*)paid (.*)dollars(.*)on(.*),(.*):(.*):(.*)Cut:(.*)Color:(.*),', client, re.I | re.M)
    if match:
        oldClient = Customer(match.group(1).strip(), match.group(7).strip(), match.group(2).strip(), match.group(8).strip(), match.group(9).strip(), match.group(4).strip())
        pastCustomers.append(oldClient)

def searchCustomer():
    searchDecision = False
    searchQue = input("Would you like to search by date or name? [D/N]")
    while searchDecision == False:

        if searchQue.title() == 'N':
            #Search by name
            search = input("What is the client's name? \n")
            x = 0
            for customer in pastCustomers:
                if search.title() == customer.name:
                    x = 1
                    print("\n\n" + customer.name.title() + " paid $" + str(customer.cost) + " on " + str(customer.date) + ", for:\nFormula: " + customer.formula + "\nCut: " + customer.cut +"\nColor: " + customer.color + "\n")
                    time.sleep(1)

            if x == 1:
                secDecision = False
                searchAgain = input("Would you like to search for another client? [Y/N]\n")
                while secDecision == False:
                    if searchAgain.title() == 'Y':
                        searchQue = input("Would you like to search by date or name? [D/N]\n")
                        searchDecision = False
                        secDecision = True
                    elif searchAgain.title() == 'N':
                        searchDecision = True
                        secDecision = True
                    else:
                        print("ERROR: Invalid input")
                        time.sleep(.5)
                        searchAgain = input("Would you like to search for another client? [Y/N]\n")
                        secDecision = False

            elif x == 0:
                print("Sorry, this client was not found.")
                time.sleep(1)
                secDecision = False
                searchAgain = input("Would you like to search for another client? [Y/N]\n")
                while secDecision == False:
                    if searchAgain.title() == 'Y':
                        searchQue = input("Would you like to search by date or name? [D/N]\n")
                        searchDecision = False
                        secDecision = True
                    elif searchAgain.title() == 'N':
                        searchDecision = True
                        secDecision = True
                    else:
                        print("ERROR: Invalid input")
                        time.sleep(.5)
                        searchAgain = input("Would you like to search for another client? [Y/N]\n")
                        secDecision = False

        elif searchQue.title() == 'D':
            #Search by date
            searchDate = input("What is the date you would like to search? [Year-month-day][Ex." + str(date) + "]")
            y = 0
            for customer in pastCustomers:
                if searchDate == customer.date:
                        y = 1
                        print("\n\n" + customer.name.title() + " paid $" + str(customer.cost) + " on " + str(customer.date) + ", for:\nFormula: " + customer.formula + "\nCut: " + customer.cut + "\nColor: " + customer.color + "\n")
                        time.sleep(1)

            if y == 1:
                secDecision = False
                searchAgain = input("Would you like to search for another client? [Y/N]\n")
                while secDecision == False:
                    if searchAgain.title() == 'Y':
                        searchQue = input("Would you like to search by date or name? [D/N]\n")
                        searchDecision = False
                        secDecision = True
                    elif searchAgain.title() == 'N':
                        searchDecision = True
                        secDecision = True
                    else:
                        print("ERROR: Invalid input")
                        time.sleep(.5)
                        searchAgain = input("Would you like to search for another client? [Y/N]\n")
                        secDecision = False

            elif y == 0:
                print("Sorry, this client was not found.")
                time.sleep(1)
                secDecision = False
                searchAgain = input("Would you like to search for another client? [Y/N]\n")
                while secDecision == False:
                    if searchAgain.title() == 'Y':
                        searchQue = input("Would you like to search by date or name? [D/N]\n")
                        searchDecision = False
                        secDecision = True
                    elif searchAgain.title() == 'N':
                        searchDecision = True
                        secDecision = True
                    else:
                        print("ERROR: Invalid input")
                        time.sleep(.5)
                        searchAgain = input("Would you like to search for another client? [Y/N]\n")
                        secDecision = False



        else:
            print("ERROR: Invalid input")
            time.sleep(.5)
            searchQue = input("Would you like to search by date or name? [D/N]\n")
            searchDecision = False


def start():
    flag = True
    goTo = input("[1] New Customer\n[2] Search Customer\n[E] To Exit\n\n")
    while flag == True:
        if goTo == '1':
            newCustomer()
            time.sleep(.5)
            print("************************************************************************")
            goTo = input("\n\n[1] New Customer\n[2] Search Customer\n[E] To Exit\n\n")
            flag = True

        elif goTo == '2':
            searchCustomer()
            time.sleep(.5)
            print("************************************************************************")
            goTo = input("\n\n[1] New Customer\n[2] Search Customer\n[E] To Exit\n\n")
            flag = True
        elif goTo.upper() == 'E':
            time.sleep(1)
            print("Goodbye!")
            time.sleep(1)
            flag = False
        else:
            print("ERROR: Invalid input")
            time.sleep(.5)
            print("************************************************************************")
            goTo = input("\n\n[1] New Customer\n[2] Search Customer\n[E] To Exit\n\n")
            flag = True



print("************************************************************************")
time.sleep(1)
print("\n\nWelcome\n\n")
time.sleep(1)
start()



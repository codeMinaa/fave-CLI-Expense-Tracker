expenses = []
while True:
    print("1.add an expense")
    print("2.view expenses")
    print("3.calculate expenses")
    print("4.quite")
    choice =input("enter an option:")
    if choice == "1":
        description = input("what did you spend:")
        amount = float(input("how much did you spend :"))
        expense = {
            "description" :description,
            "amount" : amount
        }    
        expenses.append(expense)   
    elif choice =="2":
            for expense in expenses:
                print(expense["description"],expense["amount"]) 
    if choice == "4":
        print("quite")
        break

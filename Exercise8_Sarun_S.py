userInput = input("Username : ")
pwdInput = input("Password : ")
if userInput == "admin" and pwdInput == "1234":
    print("Welcome to Drink-Shop")
    print("---------------------")
    print("------Drink List-----")
    print("1. Mojito    Price 110")
    print("2. Margarita Price 120")
    print("3. Mai Tai   Price 150")
    userSelect = int(input("Select Drink List : "))
    if userSelect == 1:
        number = int(input("จำนวนที่ต้องการ : "))
        print("Mojito ราคา110","X",number,"ราคา",number*110)
        print("Thank You")
    elif userSelect == 2:
        number = int(input("จำนวนที่ต้องการ : "))
        print("Margarita ราคา120","X",number,"ราคา",number*120)
        print("Thank You")
    elif userSelect == 3:
        number = int(input("จำนวนที่ต้องการ : "))
        print("Mai Tai ราคา150","X",number,"ราคา",number*150)
        print("Thank You")
else:
    print("Login Fail")


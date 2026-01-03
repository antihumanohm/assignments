def vatcalculate(totlePrice):
    result = totlePrice+(totlePrice*7/100)
    return result

price = int(input("Enter your price: "))
print(vatcalculate(price))
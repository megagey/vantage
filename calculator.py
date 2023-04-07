aluminiumPrice = 834
copperPrice = 208.4
fibrePrice = 834
glassPrice = 417
ironPrice = 1251
metalScrapPrice = 1251
plasticPrice = 1251
steelPrice = 1668
rubberPrice = 834

aluminiumStock = 5000
copperStock = 5000
fibreStock = 5000
glassStock = 5000
ironStock = 5000
metalScrapStock = 5000
plasticStock = 5000
steelStock = 5000
rubberStock = 5000

menuText = f""

def menu():
    print(20 * "-", "Vantage Tech and Hardware", 20 * "-")
    print("1 | Sell Item")
    print("2 | Check Stock")
    print("3 | Check Pricing")
    print("3 | Exit")
    return int(input("Please type 1, 2, 3 or 4"))

choice = 0
while True:
    choice = menu()
    if choice == 1:
        print("Sell Item")
    elif choice == 2:
        print("Check Stock")
    elif choice == 3:
        print("Check Pricing")
    elif choice == 4:
        print("Closing")
        break
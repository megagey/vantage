aluminiumBase = 834
copperBase = 208.4
fibreBase = 834
glassBase = 417
ironBase = 1251
metalScrapBase = 1251
plasticBase = 1251
steelBase = 1668
rubberBase = 834

aluminiumStock = 5000
copperStock = 5000
fibreStock = 5000
glassStock = 5000
ironStock = 5000
metalScrapStock = 5000
plasticStock = 5000
steelStock = 5000
rubberStock = 5000

def averageStock():
    return (aluminiumStock + copperStock + fibreStock + glassStock + ironStock + metalScrapStock + plasticStock + steelStock + rubberStock) / 9

def materialPrice(price, stock):
    difference = (averageStock / stock)
    return price * difference

items = {"Lock Pick": "metalScrap-42 plastic-52", "Advanced Lock Pick" : "metalScrap-42 plastic-52", 
"Electronic Kit" : "aluminium-34 metalScrap-87 plastic-55", "Steel Wire" : "steel-40", "Steel Hook" : "steel-100", 
"Rope" : "fibre-55", "Reinforced Rope" : "fibre-55 steel-1800", "Rope and Hook" : "fibre-55 steel-100",
 "Reinforced Rope and Hook" : "fibre-55 steel-1900", "MD5 Crack USB" : "aluminium-112 iron-23 metalScrap-195 plastic-164", 
 "Trojan USB" : "aluminium-146 iron-23 metalScrap-282 plastic-219", "Thermite" : "aluminium-260 glass-460 iron-260", 
 "Drill" : "iron-330 metalScrap-84 plastic-104 steel-350", 
 "Night Vision Goggles" : "aluminium-68 glass-365 metalScrap-174 plastic-110 steel-225 rubber-325", 
 "Light Armour" : "fibre-425 steel-550 rubber-435"}

def menu():
    print(20 * "-", "Vantage Tech and Hardware", 20 * "-")
    print("1 | Sell Item")
    print("2 | Check Stock")
    print("3 | Check Pricing")
    print("3 | Exit")
    return int(input("Please type 1, 2, 3, 4 or 5"))

def sell():
    print("1  | Lock Pick")
    print("2  | Advanced Lock Pick")
    print("3  | Tool Kit")
    print("4  | Electronic Kit")
    print("5  | Steel Wire")
    print("6  | Steel Hook")
    print("7  | Rope")
    print("8  | Reinforced Rope")
    print("9  | Rope and Hook")
    print("10 | Reinforced Rope and Hook")
    print("11 | MD5 Crack USB")
    print("12 | Trojan USB")
    print("13 | Repair Kit")
    print("14 | Pistol Ammo")
    print("15 | Iron Powder")
    print("16 | Aluminium Powder")
    print("17 | Thermite")
    print("18 | Drill")
    print("19 | Night Vision Goggles")
    print("20 | Light Armour")
    print("21 | Exit")
    return int(input("Please type 1, 2, 3, 4 or 5"))

choice = 0
while True:
    choice = menu()
    if choice == 1:
        select = sell()
        if select == 1:
            print("Lock Pick")
            materialPrice
        elif select == 2:
            print("Advanced Lock Pick")
        elif select == 3:
            print("Tool Kit")
        elif select == 4:
            print("Electronic Kit")
        elif select == 5:
            print("Steel Wire")
        elif select == 6:
            print("Steel Hook")
        elif select == 7:
            print("Rope")
        elif select == 8:
            print("Reinforced Rope")
        elif select == 9:
            print("Rope and Hook")
        elif select == 10:
            print("Reinforced Rope and Hook")
        elif select == 11:
            print("MD5 Crack USB")
        elif select == 12:
            print("Trojan USB")
        elif select == 13:
            print("Repair Kit")
        elif select == 14:
            print("Pistol Ammo")
        elif select == 15:
            print("Iron Powder")
        elif select == 16:
            print("Aluminium Powder")
        elif select == 17:
            print("Thermite")
        elif select == 18:
            print("Drill")
        elif select == 19:
            print("night Vision Goggles")
        elif select == 20:
            print("Light Armour")
        elif select == 21:
            print("Exit")
    elif choice == 2:
        print("Buy Van")
    elif choice == 3:
        print("Check Stock")
    elif choice == 4:
        print("Check Pricing")
    elif choice == 5:
        print("Closing")
        break
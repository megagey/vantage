from math import floor

prices = {"aluminiumBase" : 83.4, "copperBase" : 20.84, "fibreBase" : 83.4, "glassBase" : 41.7, "ironBase" : 125.1, 
"metalScrapBase" : 125.1, "plasticBase" : 125.1, "steelBase" : 166.8, "rubberBase" : 83.4}

stock = {"aluminiumStock" : 5000, "copperStock" : 5000, "fibreStock" : 5000, "glassStock" : 5000, "ironStock" : 5000, 
"metalScrapStock" : 5000, "plasticStock" : 5000, "steelStock" : 5000, "rubberStock" : 5000}

items = {"Lock Pick" : "metalScrap-42 plastic-52", "Advanced Lock Pick" : "metalScrap-42 plastic-52", 
"Electronic Kit" : "aluminium-34 metalScrap-87 plastic-55", "Steel Wire" : "steel-40", "Steel Hook" : "steel-100", 
"Rope" : "fibre-55", "Reinforced Rope" : "fibre-55 steel-1800", "Rope and Hook" : "fibre-55 steel-100", 
"Reinforced Rope and Hook" : "fibre-55 steel-1900", "MD5 Crack USB" : "aluminium-112 iron-23 metalScrap-195 plastic-164", 
"Trojan USB" : "aluminium-146 iron-23 metalScrap-282 plastic-219", "Iron Powder" : "glass-230 iron-260", 
"Aluminium Powder" : "aluminium-260 glass-230", "Thermite" : "aluminium-260 glass-460 iron-260", 
"Drill" : "iron-330 metalScrap-84 plastic-104 steel-350", 
"Night Vision Goggles" : "aluminium-68 glass-365 metalScrap-174 plastic-110 steel-225 rubber-325", 
"Light Armour" : "fibre-425 steel-550 rubber-435"}

toolKit = 1150
repairKit = 5500
ammo = 5000

def isFloat(string):
    if string.replace(".", "").isnumeric():
        return True
    else:
        return False

def averageStock():
    return (stock["aluminiumStock"] + stock["copperStock"] + stock["fibreStock"] + stock["glassStock"] + stock["ironStock"] 
    + stock["metalScrapStock"] + stock["plasticStock"]+ stock["steelStock"] + stock["rubberStock"]) / 9

def materialPrice(price, stock):
    average = averageStock()
    difference = (average / stock)
    return price * difference

def recipe(name):
    return items[name].split()

def sellItem(item):
    price = 0
    itemRecipe = recipe(item)
    for i in itemRecipe:
        materials = i.split("-")
        print(materials)
        for e in materials:
            if e.isdigit() == False:
                cost = materialPrice(prices[e + "Base"], stock[e + "Stock"])
            else:
                if int(e) > 100:
                    refined = floor(int(e)/100) 
                    price += cost * (int(e) + (10 * refined))
                else:
                    price += cost * int(e)
    return price

def menu():
    print("\n" + (20 * "-"), "Vantage Tech and Hardware", 20 * "-")
    print("1 | Sell Item")
    print("2 | Buy Van")
    print("3 | Check Stock")
    print("4 | Check Pricing")
    print("5 | Exit")
    return input("Please type a number\n")

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
    return input("Please type a number\n")

choice = ""
while True:
    choice = menu()
    if choice == "1":
        select = sell()
        if select == "1":
            print("The price for a Lock Pick is $" + str(sellItem("Lock Pick")))
        elif select == "2":
            print("The price for an Advanced Lock Pick is $" + str((sellItem("Advanced Lock Pick") + toolKit)))
        elif select == "3":
            print("The price for a Tool Kit is $" + str(toolKit + 100))
        elif select == "4":
            print("The price for an Electronic Kit is $" + str(sellItem("Electronic Kit")))
        elif select == "5":
            print("The price for a spool of Steel Wire is $" + str(sellItem("Steel Wire")))
        elif select == "6":
            print("The price for a Steel Hook is $" + str(sellItem("Steel Hook")))
        elif select == "7":
            print("The price for a Rope is $" + str(sellItem("Rope")))
        elif select == "8":
            print("The price for a Reinforced Rope is $" + str(sellItem("Reinforced Rope")))
        elif select == "9":
            print("The price for a Rope and Hook is $" + str(sellItem("Rope and Hook")))
        elif select == "10":
            print("The price for a Reinforced Rope and Hook is $" + str(sellItem("Reinforced Rope and Hook")))
        elif select == "11":
            print("The price for a MD5 Crack USB is $" + str(sellItem("MD5 Crack USB")))
        elif select == "12":
            print("The price for a Trojan USB is $" + str(sellItem("Trojan USB")))
        elif select == "13":
            print("The price for a Repair Kit is $" + str(repairKit + 100))
        elif select == "14":
            print("The price for a box of Pistol Ammo is $" + str(ammo + 100))
        elif select == "15":
            print("The price for a pile of Iron Powder is $" + str(sellItem("Iron Powder")))
        elif select == "16":
            print("The price for a pile of Aluminium Powder is $" + str(sellItem("Aluminium Powder")))
        elif select == "17":
            print("The price for a canister of Thermite is $" + str(sellItem("Thermite")))
        elif select == "18":
            print("The price for a Drill is $" + str((sellItem("Drill") + (toolKit * 2))))
        elif select == "19":
            print("The price for a pair of Night Vision Goggles is $" + str(sellItem("Night Vision Goggles")))
        elif select == "20":
            print("The price for a Light Armour is $" + str(sellItem("Light Armour")))
        elif select == "21":
            print("Exiting")
        else:
            print("Please type a valid number")
            print("Exiting")
    elif choice == "2":
        totalPrice = 0
        for x in prices:
            mat = x[0].lower() + x[1:-4]
            while True:
                amount = input("How much " + mat + "?")
                if isFloat(amount) == True:
                    amount = float(amount)
                    break
                else:
                    print("\nPlease enter valid number\n")
            totalPrice += (materialPrice(prices[x],  stock[mat + "Stock"]) * amount)
        print("\nThe total price for the van is $" + str(totalPrice))

    elif choice == "3":
        print("\n" + "\n".join("{}\t{}".format(k, v) for k, v in stock.items()))
    elif choice == "4":
        print("\n" + "\n".join("{}\t{}".format(k, v) for k, v in prices.items()))
    elif choice == "5":
        print("Closing")
        break
    else:
        print("Please type a valid number")
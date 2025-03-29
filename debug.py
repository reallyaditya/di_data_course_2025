store = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20",
    "Apple": "$4",
    "Honey": "$3",
    "Fan": "$14",
    "Bananas": "$4",
    "Pan": "$100",
    "Spoon": "$2",
    "Phone": "$999",
    "Speakers": "$300",
    "Laptop": "$5,000",
    "PC": "$1200",
}


items_purchase = {
    "Phone": "$999",
    "Speakers": "$300",
    "Laptop": "$5,000",
    "PC": "$1200",
}

wallet = "$1"

amount = int(wallet.replace("$", ""))
newlist = []

for eachitem in store.keys():
    if eachitem in items_purchase:
        if int(items_purchase[eachitem].replace("$", "").replace(",", "")) < amount:
            newlist.append(eachitem)

if newlist == []:
    print("Nothing")
else:
    print(sorted(newlist))

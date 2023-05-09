#!/usr/bin/python
import scrython
#import mariadb
import time
import sys

"""
try:
    conn = mariadb.connect(
        host="127.0.0.1",
        user="seer",
        password="blacklotus",
        database="mtg"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

qmtg = conn.cursor()

"""
query = input("Enter your card: ")
setname = str(input("Enter set abbreviation: "))

if setname == "":
    searchcard = scrython.cards.Named(fuzzy=query)
elif setname == "?":
    fullsetname = str(input("Enter the full set name : "))
    allsets = scrython.sets.Sets()
    setlist = allsets.data()
    for x in range(len(setlist)):
        if fullsetname == setlist[x]['name']:
            setname = setlist[x]['code'].upper()
    searchcard = scrython.cards.Named(fuzzy=query,set=setname)
else: searchcard = scrython.cards.Named(fuzzy=query,set=setname)

cardname = searchcard.name()
try: oracletext = searchcard.oracle_text()
except:
    loadjson = searchcard.card_faces()
    card0name = loadjson[0]['name']
    card1name = loadjson[1]['name']
    card0manacost = loadjson[0]['mana_cost']
    card1manacost = loadjson[1]['mana_cost']
    card0oracle = loadjson[0]['oracle_text']
    card1oracle = loadjson[1]['oracle_text']
    card0type = loadjson[0]['type_line']
    card1type = loadjson[1]['type_line']
    try: card1colorid = loadjson[1]['color_indicator']
    except: card1colorid = ""
setabbrv = searchcard.set_code().upper()
fullsetname = searchcard.set_name()
try: cardcolors = searchcard.colors()
except: cardcolors = loadjson[0]['colors']
colorid = searchcard.color_identity()
typeline = searchcard.type_line()
try: manacost = searchcard.mana_cost()
except:
    manacost = loadjson[0]['mana_cost']
allsets = scrython.cards.Search(q="++{}".format(cardname))

print("all printings for this card:")
for card in allsets.data():
    print(card['set'].upper(), ":", card['set_name'])

print(cardname)
if manacost == "":
    pass
else:
    print(manacost)
print(typeline)
if "Planeswalker" in typeline:
    print("Loyalty:",searchcard.loyalty())
else:
    pass
if setname == "":
    #print("no set code provided.")
    print("most recent printing:",setabbrv)
else:
    print(setabbrv,"-",fullsetname)
try: print(oracletext)
except:
    print(card0name)
    print(card0manacost)
    print(card0type)
    print(card0oracle)
    print(card1name)
    if not card1manacost:
        pass
    else:
        print(card1manacost)
    print(card1type)
    if not card1colorid:
        pass
    else:
        print(card1colorid)
    print(card1oracle)
try: searchcard.flavor_text()
except:
    print("there is no flavor text for this card.")
    flavortext = ""
else: flavortext = searchcard.flavor_text()
if setname == "" and flavortext != "":
    print("flavor text from:",setabbrv)
    print(flavortext)
elif flavortext == "" and setname != "" or setname == "":
    exit
else:
    print(flavortext)
if not cardcolors:
    print("colors: this card is colorless.")
else:
    print("colors:",cardcolors)
if not colorid:
    print("color identity: this card's color identity is colorless.")
else:
    print("color identity:",colorid)
if searchcard.reserved() == True:
    print("Reserved List?: You bet your ass!")
else:
    print("Reserved List?: this card is not on the reserved list.")

#conn.close()

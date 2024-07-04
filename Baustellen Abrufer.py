import requests
import json


def print_details(x):
    print("Art der Baumassnahme: " + x["art_der_baumassnahme"])
    print("Bereich: " + x["bereich"])
    print("Firma: " + x["firma"])
    print("Stadtbezirk: " + x["stadtbezirk"])
    print("Verkehrseinschraenkung: " + x["verkehrseinschraenkung"])
    print("Zeitraum: " + x["zeitraum"])
    print("Ostwert: " + x["ostwert"])
    print("Hochwert: " + x["hochwert"])


def print_all_baustellen():
    print("Aktuelle Baustellen Dortmunds")
    for i in range(0, len(res)):
        art = res[i]
        print(str(i + 1) + ". " + art["art_der_baumassnahme"])


response = requests.get("https://opendata.dortmund.de/OpenDataConverter/download/FB66/FB66-Baustellen%20aktuelle.json")
res = json.loads(response.text)
print_all_baustellen()
while True:
    user_input_menu = input("Welche Aktion wollen sie machen? \n "
                            "1.Eine Baustelle genauer betrachten \n "
                            "2.Eine Baustelle in ihrem Stadtbezirk finden \n")
    if user_input_menu == "1":
        user_input = input("Welche dieser Baustellen wollen sie genauer betrachten? ")
        if user_input.isdigit() and 0 < int(user_input) < len(res):
            user_baustelle = res[int(user_input) - 1]
            print("--------------------------------------------------------------------------")
            print_details(user_baustelle)
            print("--------------------------------------------------------------------------")
        else:
            print("--------------------------------------------------------------------------")
            print("Diese Baustellen Nummer ist nicht vorhanden!")
            print("--------------------------------------------------------------------------")
    if user_input_menu == "2":
        user_input_bezirk = input("In welchem Bezirk suchen Sie die Baustelle? (Leertaste mit - ersetzen) ")
        for i in range(0, len(res)):
            bezirk = res[i]
            bezirk = bezirk["stadtbezirk"]
            if bezirk == user_input_bezirk:
                bezirk = res[i]["art_der_baumassnahme"]
                print(bezirk)
        user_input_details = input(
            "Wollen sie einer dieser Baustellen im Detail ansehen? Wenn ja welche? Wenn nein q eingeben ")
        if user_input_details.lower() == "q":
            continue
        for i in range(0, len(res)):
            if str(res[i]["art_der_baumassnahme"]).lower() == user_input_details.lower():
                print_details(res[i])
                print("--------------------------------------------------------------------------")

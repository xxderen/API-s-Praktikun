import customtkinter as tk
import requests
import json
import math
from tkinter import messagebox
import webbrowser


class MyGui:

    def __init__(self):
        tk.set_appearance_mode("Dark")
        tk.set_default_color_theme("dark-blue")
        self.window = tk.CTk()
        self.window.geometry("300x200")
        self.window.title("Parkhaus Finder")
        self.window.attributes("-topmost", True)

        self.label1 = tk.CTkLabel(self.window, text="Parkhaus Finder Dortmund", font=("Arial", 16))
        self.label1.pack(padx=20, pady=20)

        self.adresse = tk.Variable()

        self.label2 = tk.CTkLabel(self.window, text="Adresse")
        self.label2.pack(padx=20)
        self.entry1 = tk.CTkEntry(self.window, textvariable=self.adresse)
        self.entry1.pack(padx=20)

        button = tk.CTkButton(self.window, text="Suchen", font=("Arial", 10), command=self.calculate_parkhaus)
        button.pack(pady=10)

        self.window.mainloop()

    def calculate_parkhaus(self):
        from geopy.geocoders import Nominatim
        loc = Nominatim(user_agent="GetLoc")
        getloc = loc.geocode(self.adresse.get())
        print(getloc.address)
        y_cord1 = getloc.latitude
        x_cord1 = getloc.longitude
        best_match = 0
        response = requests.get(
            "https://geoweb1.digistadtdo.de/doris_gdi/geoserver/parken/ogc/features/collections/pls/items?f"
            "=application%2Fgeo%2Bjson")
        res = json.loads(response.text)
        x_cord = float(res["features"][0]["geometry"]["coordinates"][0])
        y_cord = float(res["features"][0]["geometry"]["coordinates"][1])
        distance = math.sqrt((float(x_cord1) - x_cord) ** 2 + (float(y_cord1) - y_cord) ** 2)
        for i in range(1, len(res["features"])):
            if res["features"][i]["properties"]["stand"] != "Zur Zeit keine Verbindung zum Parkleitsystem":
                x_cord2 = float(res["features"][i]["geometry"]["coordinates"][0])
                y_cord2 = float(res["features"][i]["geometry"]["coordinates"][1])
                new_distance = math.sqrt((float(x_cord1) - x_cord2) ** 2 + (float(y_cord1) - y_cord2) ** 2)
                if new_distance < distance:
                    distance = new_distance
                    best_match = i
        print(res["features"][best_match]["properties"]["name"])
        if res["features"][best_match]["properties"]["offen"] == "geoeffnet":
            status = "Geöffnet"
        else:
            status = "Geschlossen"
        webbrowser.open("https://www.google.com/maps/dir/" + self.adresse.get() + "/" + str(
            res["features"][best_match]["geometry"]["coordinates"][1]) + "," + str(
            res["features"][best_match]["geometry"]["coordinates"][0]), new=0, autoraise=True)
        messagebox.showinfo(title="Result!",
                            message="Name des Parkhauses: " + res["features"][best_match]["properties"][
                                "name"] + "\n" + "Status: " + status + "\nFreie Plätze: " + str(
                                res["features"][best_match]["properties"]["frei"]))


MyGui()

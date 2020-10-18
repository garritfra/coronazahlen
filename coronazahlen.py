import requests
import json
from datetime import date
from openpyxl import Workbook

query = "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=1%3D1&outFields=GEN,BL,BEZ,cases7_per_100k&returnGeometry=false&outSR=4326&f=json&orderByFields=cases7_per_100k%20DESC"

data = requests.get(query).json()

today = date.today()

d1 = today.strftime("%Y-%m-%d")

filename = "coronazahlen_" + d1 + ".xlsx"

print("Writing to", filename)

wb = Workbook()
ws = wb.active

ws.append(["Bundesland", "Bezeichnung", "Landkreis", "7 Tage Inzidenz"])

for x in data["features"]:
    attributes = x["attributes"]
    print("writing", attributes)
    ws.append([
        attributes["BL"],
        attributes["BEZ"],
        attributes["GEN"],
        round(attributes["cases7_per_100k"], 1)
    ])

wb.save(filename)

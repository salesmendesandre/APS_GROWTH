import os
import urllib.request
import urllib.parse

names = {
    "andre_mendes": "André Mendes",
    "alvaro_lozano": "Álvaro Lozano",
    "diego_jimenez": "Diego Jiménez",
    "daniel_hernandez": "Daniel Hernández",
    "juan_navarro": "Juan Navarro",
    "sergio_garcia": "Sergio García",
    "sergio_perez": "Sergio Pérez",
    "hector_sanchez": "Héctor Sánchez",
    "yolanda_san_roman": "Yolanda San Román",
    "isaac_san_roman": "Isaac San Román"
}

os.makedirs("book/_static/team", exist_ok=True)

for key, name in names.items():
    formatted_name = urllib.parse.quote(name)
    url = f"https://ui-avatars.com/api/?name={formatted_name}&background=random&size=128"
    file_path = f"book/_static/team/{key}.png"
    print(f"Downloading {name} to {file_path}")
    urllib.request.urlretrieve(url, file_path)

print("Avatars downloaded.")

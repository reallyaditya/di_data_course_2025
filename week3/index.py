import json

with open("week3/file.json", "r") as file:
    family = json.load(file)

children = family["children"]
for child in children:
    child["favorite_color"] = "blue"

with open("week3/file.json", "w") as file:
    json.dump(family, file, indent=4, sort_keys=True)

import json

with open("file.json", 'r+') as file_obj:
    family = json.load(file_obj)
    children = family["children"]
    for child in children:
        print(f"Name: {child['firstName']}, Age: {child['age']}")
    for i in children:
        if i.get("firstName") == 'Alice':
            i["favorite_color"] = "red"
        if i.get("firstName") == 'Bob':
            i["favorite_color"] = "blue"

    file_obj.flush()
    file_obj.seek(0)
    json.dump(family, file_obj, indent=2, sort_keys=True)

# with open("file.json", 'w') as file_obj:
#     json.dump(family, file_obj, indent=2, sort_keys=True)

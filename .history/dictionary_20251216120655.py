people = {
    "Ram": 20,
    "Sita": 22,
    "Hari": 19,
    "Gita": 21,
    "Ram": 10,
    "Sita": 22,
    "Hari": 19,
    "Gita": 21
}

for name,age in people.items():
    if age>18:
        print(name,age)
contacts = {"Arek": 506234556,
            "Basia": 607456233,
            "Martyna": 778456332,
            "Maja": 589311911,
            "Paweł": 501223493,
            "Anastazja": 998312445
            }
def sort_by_key():
    sorted_by_key_contacts = sorted(contacts.items(), key = lambda t: t[0])
    for key in sorted_by_key_contacts:
        print(key)

print(sort_by_key())

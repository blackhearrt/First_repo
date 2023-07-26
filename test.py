def lookup_key(data, value):
    keys = []
    for k, v in data.items():
        if v == value:
            keys.append(k)
        else: 
            continue
    return keys
    
print(lookup_key({"Olena":2001, "Serhii":2001, "Andrii":1999, "Oleksandra":1986}, 2001))    
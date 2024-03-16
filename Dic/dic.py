#how to make a dictionary in a python 
haseeb = {
    "name" : "Haseeb",
    "fathers_name" : "Javed Raza",
    "mothers_name" : "Rehana kausar Raza"
}

print(haseeb["name"])
print(haseeb["fathers_name"])
print(haseeb["mothers_name"])


haseeb["name"] = "Hussy"
print(haseeb["name"])


for thing in haseeb:
    print(thing)
    print(haseeb[thing])
    
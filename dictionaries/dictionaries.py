phonebook = {}
phonebook["John"] = 111
phonebook["Jack"] = 222
phonebook["Jam"] = 333

#print(phonebook["John"])

phonelist = {"John" : 111, "Jack": 222, "Jill": 333}

for name, number in phonelist.items():
    print("Phone number of %s is %d" % (name, number))

# Tirando o John da listinha

del phonebook["John"]
print(phonebook)
# "Como se pode ver, ele não está mais lá" - alguem
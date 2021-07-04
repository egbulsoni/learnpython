#%s - String (or any object with a string representation, like numbers)
#%d - Integers
#%f - Floating point numbers
#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#%x/%X - Integers in hex representation (lowercase/uppercase)

print(f"%x/%X", 5/8)
#output abaixo (um pouco estranho, let's fix it)
#%x/%X 0.625
print(f"%x/%X" % (5,8))
#funcionou como eu esperava, retornando uma fração
#5/8
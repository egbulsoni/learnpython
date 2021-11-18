def foo(a, b, c, *args):
    return list(args)
    
def bar(a, b, c, magicnumber = 3):
    if (magicnumber == 7):
        return True
    
if foo(1,2,3,4) == 1:
    print("Good.")
if foo(1,2,3,4,5) == 2:
    print("Better.")
if bar(1,2,3,magicnumber = 6) == False:
    print("Great.")
if bar(1,2,3,magicnumber = 7) == True:
    print("Awesome")
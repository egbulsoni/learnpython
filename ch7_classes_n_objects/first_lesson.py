class MyClass:
    variable = "blah"
    
    def function(self):
        print("This is a message inside the class.")
        
myobjectx = MyClass()
print(myobjectx.variable)

myobjectx.variable = "yackity"
print(myobjectx.variable)

myobjectx = MyClass()

myobjectx.function()
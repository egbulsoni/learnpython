def my_function():
    print("Hello From My Function!")

my_function()
# primeira função
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s" % (username, greeting))
    
my_function_with_args("john", "hi there")
# just werks
# segunda função
def sum_two_numbers(a, b):
    return a + b

# chamada de função composta: o retorno é implícito
# ao menos na versão 3.9.5    
print(sum_two_numbers(10, 15))

# E começa a era das máquinas

class NodeTree:
    def __init__(self, key=None,left=None,right=None):
        self.key = key
        self.left = left
        self.right = right
    def __repr__(self):
        #this is just to present data, nothing special
        '%s <- %s -> %s' % (left, key, right)
    def fib():
        #this is the generator function
        # a generator function is a function that recurs many times
        # simply put, you can specify a range and it keeps generating as long as you need to         root = NodeTree(2,1,1)
        yield root.left
        yield root.right
        yield root.key
        for i iclass NodeTree:
    def __init__(self, key=None,left=None,right=None):
        self.key = key
        self.left = left
        self.right = right
    def __repr__(self):
        #this is just to present data, nothing special
        '%s <- %s -> %s' % (left, key, right)
    def fib():
        #this is the generator function
        # a generator function is a function that recurs many times
        # simply put, you can specify a range and it keeps generating as long as you need to         root = NodeTree(2,1,1)
        yield root.left
        yield root.right
        yield root.key
        for i in range(1,10):
            root = NodeTree(root.key + root.left, root.right)
            yield root.key

# and then we can use a function that does the rest...

def fib():
    #raiz = NodoArvore(0,1,1)
    raiz = NodoArvore(2,1,1)
    yield raiz.esquerda
    yield raiz.direita

yield raiz.chave
for i in range(1,10):

#sorry for that    raiz = NodoArvore(raiz.chave + raiz.esquerda, raiz.chave, raiz.direita)        
    yield raiz.chav

# so when you run "python3 gens.py" it should output
# 1,1,2,3,5,8,11
...
n range(1,10):
        root = NodeTree(root.key + root.left, root.right)
        yield root.key

# and then we can use a function that does the rest...

def fib():
    #raiz = NodoArvore(0,1,1)
    raiz = NodoArvore(2,1,1)
    yield raiz.esquerda

yield raiz.direita

yield raiz.chave
for i in range(1,10):

#sorry for that    raiz = NodoArvore(raiz.chave + raiz.esquerda, raiz.chave, raiz.direita)        
    yield raiz.chav

# so when you run "python3 gens.py" it should output
# 1,1,2,3,5,8,11
...
class NodeTree:
def __init__(self, key=None,left=None,right=None):
    self.key = key
        self.left = left
        self.right = right
    def __repr__(self):
        #this is just to present data, nothing special
        '%s <- %s -> %s' % (left, key, right)

#sorry for that

def fib():
    # this is the generator function
    # a generator function is a function that recurs many times
    # simply put, you can specify a range and it keeps generating as long as you need to
    root = NodeTree(2,1,1)
    yield root.left
    yield root.right
    yield root.key
    for i in range(1,10):
        root = NodeTree(root.key + root.left, root.right)
        yield root.key


# and then we can use a function that does the rest...

 
import types
if type(fib()) == types.GeneratorType:
    print("Good, the fib function is a generator.")
    
    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break

# so when you run "python3 gens.py" it should output
# 1,1,2,3,5,8,11...
class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita
        
    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda, self.direita, self.chave)

#raiz = NodoArvore(2,1,1)
#raiz.esquerda = NodoArvore(1)
#raiz.direita = NodoArvore(1)

#print("Árvore: ", raiz)

#import random

#def fib():
#    for i in range(6):
#        yield random.randint(1,40)
#    yield random.randint(1,15)
 
def fib():
    #raiz = NodoArvore(0,1,1)
    raiz = NodoArvore(2,1,1)
    yield raiz.esquerda
    yield raiz.direita
    yield raiz.chave
    for i in range(1,10):
        raiz = NodoArvore(raiz.chave + raiz.esquerda, raiz.chave, raiz.direita)        
        yield raiz.chave

 
import types
if type(fib()) == types.GeneratorType:
    print("Good, the fib function is a generator.")
    
    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
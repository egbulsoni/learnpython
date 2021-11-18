class Vetor:
    def __init__(self, nodo=None, prox=None):
        self.nodo = nodo
        self.prox = None
    def __inserir__(self, nodo=None, prox=None):
        self.nodo = nodo
        nodo.prox = None
    def __repr__(self):
        return 
    
a = Vetor(3,2)
print(a)
    
    
    

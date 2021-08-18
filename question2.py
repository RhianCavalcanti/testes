class Queue:
    def __init__(self):       
        self.items = []

    def isEmpty(self):        #retorna True or False se a lista estiver vazia
        return self.items == []

    def enqueue(self, item):      #Adiciona item no fim da fila.
        self.items.insert(0,item)

    def dequeue(self):            #Remove item no inicio da fila
        return self.items.pop()
    
    def queue(self):               #retornao que tem dentro da fila
        return self.items

    def size(self):
        return len(self.items)

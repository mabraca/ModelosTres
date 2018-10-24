'''
Created on Feb 8, 2017

@author: francisco
'''

class Cola:

    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        return self.items.pop(0)

    def tamano(self):
        return len(self.items)
    
    def primero(self):
        if not self.esta_vacia():
            return self.items[0]
        else:
            return None
        
    def __str__(self):
        return self.items
    
    def __unicode__(self):
        return self.items

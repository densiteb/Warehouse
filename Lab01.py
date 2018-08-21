from datetime import datetime as dt
from datetime import timedelta
import time as t


class Warehouse:
    
    def __init__(self):
        self.row =[]
        self.rows = 0

    def addRow(self,t = 1):
        for row in range(t):
            self.row.append([])
            self.rows += 1
    
    def addProduct(self, product = None, r = 0):
        self.row[r].append(product)
        
    def removeproduct(self, r):
        product = self.row[r].pop(0)
        return product
    
    def summary(self):
        length = 0
        r = 0
        while r != self.rows:
            length += len(self.row[r])
            r += 1
        return length,self.row

w = Warehouse()
w.addRow(3)
w.addProduct("Razer Keyboard",)
w.addProduct("Logitech Mouse",1)
w.addProduct("GTX 1080 Ti",2)
w.addProduct("GTX 1060",2)
w.addProduct("Crappy Graphic Card",2)
w.addProduct("Crappy, ancient keyboard",)
print(w.summary())
print(w.row)
print(w.removeproduct(0))


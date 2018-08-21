
from datetime import datetime as dt
from datetime import timedelta
import time as t


class Warehouse:
    
    def __init__(self):
        self.row =[]
        self.rows = 0

    def addRow(self,t = 0):
        for row in range(t):
            self.row.append([])
            self.rows += 1
    
    def addProduct(self, r = 0, product = None):
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


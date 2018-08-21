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


class Product:
    
    def __init__(self,name,crtdate = str(dt.now),expdate = str(dt.now() + timedelta(days=730))):
        self.name = name
        self.crtdate = crtdate
        self.expdate = expdate
        print(self.name)
        print(self.crtdate.strftime("%Y/%d/%m"))

    def isExpired(self):
        if dt.now == self.expdate:
            return True
        else:
            return False

    def iteminfo(self):
        return [self.name,str(self.crtdate.strftime("%Y/%d/%m")),str(self.expdate.strftime("%Y,%d,%m"))]

gh=Product("Milk")
print(str(gh.iteminfo))
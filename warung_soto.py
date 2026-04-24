class MieAyam:
    def __init__(self):
        self.orders = []
    
    def add(self, item):
        self.orders.append(item)
    
    def remove(self):
        if not self.is_empty():
            return self.orders.pop(0)
        return "mie habis"
    
    def peek(self):
        if not self.is_empty():
            return self.orders[0]
        
    def is_empty(self):
        return len(self.orders) == 0

    def size(self):
        return len(self.orders)
    
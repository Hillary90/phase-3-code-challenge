class Coffee:
    def __init__(self, name):
        self.name = name  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string.")
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters.")
        self._name = value
    def orders(self):
        from order import Order
        
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        from order import Order
    
        return list({order.customer for order in Order.all if order.coffee == self})

c1 = Coffee("capuchino")
print(c1.name)
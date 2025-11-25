class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []

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
    
    def num_orders(self):
        return len(self._orders)
    
    def add_order(self,orders):
        self._orders.append(orders)

    def num_orders(self):
        return len(self._order)

    def average_price(self):

        if not self._orders:
            return 0.0
        else:
            total = sum(order.price for order in self.orders)
            return total/ len(self.orders)


        

# c1 = Coffee("capuchino")
# print(c1.name)
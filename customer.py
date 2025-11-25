class Customer:
    
    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters.")
        self._name = value

    def orders(self):
        from order import Order
        return[order for order in Order.all if order.customer == self ]
    
    def coffees(self):
        from order import Order
        return list({order.coffee for order in Order.all if order.customer == self})
    
    def create_oder(self,coffee, price):
        from order import Order
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("Expected a Coffee instance")

        # to check if there is no otder
        if not coffee.orders():
            return None
        else:
            max_spend = 0
            for customer in cls.all_customer:
                spent = sum(order.price for order in customer.order if order.coffee == coffee)
                if spent > max_spend:
                    max_spend = max_spend
                    top_customer = customer
        return top_customer
        

# from customer import Customer
# from coffee import Coffee
class Order:
    all = []
    
    def __init__(self, customer, coffee, price):
        self.customer = customer 
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

        print(f"Order created: {self.customer.name} ordered {self.coffee.name} for Ksh{self.price}")

    def __str__(self):
        return f"Order({self.customer.name}, {self.coffee.name}, Ksh{self.price})"

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        from customer import Customer
        if not isinstance(value, Customer):
            raise TypeError("customer must be an instance of Customer.")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if not isinstance(value, Coffee):
            raise TypeError("coffee must be an instance of Coffee.")
        self._coffee = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("Price must be a int.")
        if not (1.0 <= value <= 10.0):
            raise ValueError("Price must be between 1.0 and 3000.0.")
        self._price = float(value)

# customer_1 = Customer("Jane")
# coffee_type = Coffee("Capuchino")
# order_1= Order(customer_1, coffee_type, 700)
# print(order_1)
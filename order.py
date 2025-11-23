from customer import Customer
from coffee import Coffee
class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer 
        self.coffee = coffee
        self.price = price
        print(f"Order created: {self.customer.name} ordered {self.coffee.name} for Ksh{self.price}")

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
        if not isinstance(value, int):
            raise TypeError("Price must be a int.")
        if not (1 <= value <= 3000):
            raise ValueError("Price must be between 1.0 and 3000.0.")
        self._price = value

customer_1 = Customer("Jane")
coffee_type = Coffee("Capuchino")
order_1= Order(customer_1, coffee_type, 700)
print(order_1)
from customer import Customer
from coffee import Coffee
from order import Order

# create customers
customer_1 = Customer("Hillary")
customer_2 = Customer("Jane")
customer_3 = Customer("Bruce")

# create coffee's
coffee_1 = Coffee("Cappuccino")
coffee_2 = Coffee("Americano")
coffee_3 = Coffee("Latte")

# creating orders between 1.0 to 10.0
order_1 = customer_1.create_order(coffee_1, 5.0)
order_2 = customer_1.create_order(coffee_2, 4.5)
order_3 = customer_2.create_order(coffee_1, 6.0)
order_4 = customer_3.create_order(coffee_1, 3.5)
order_5 = customer_2.create_order(coffee_3, 2.0)

# it will print order for the customer
print(f"\n{customer_1.name}'s orders: {[str(order) for order in customer_1.orders()]}")
print(f"{customer_2.name}'s orders: {[str(order) for order in customer_2.orders()]}")
print(f"{customer_3.name}'s orders: {[str(order) for order in customer_3.orders()]}")


# it's goint to  print Coffees each Customer has ordered
print(f"\n{customer_1.name}'s coffees: {[coffee.name for coffee in customer_1.coffees()]}")
print(f"{customer_2.name}'s coffees: {[coffee.name for coffee in customer_2.coffees()]}")


# printing Orders for each Coffee
print(f"\n{coffee_1.name} orders: {[str(order) for order in coffee_1.orders()]}")
print(f"{coffee_2.name} orders: {[str(order) for order in coffee_2.orders()]}")
print(f"{coffee_3.name} orders: {[str(order) for order in coffee_3.orders()]}")


# it's going to print the customer who ordered the coffee
print(f"\n{coffee_1.name} customers: {[customer.name for customer in coffee_1.customers()]}")
print(f"{coffee_2.name} customers: {[customer.name for customer in coffee_2.customers()]}")
print(f"{coffee_3.name} customers: {[customer.name for customer in coffee_3.customers()]}")

# it will print the average cost price of the coffee
print(f"\n{coffee_1.name} average price: {coffee_1.average_price():.2f}")
print(f"{coffee_2.name} average price: {coffee_2.average_price():.2f}")
print(f"{coffee_3.name} average price: {coffee_3.average_price():.2f}")

# print top Customer for a Coffee
top_customer = Customer.most_aficionado(coffee_1)
if top_customer:
    print(f"\nTop customer for {coffee_1.name}: {top_customer.name}")
else:
    print(f"\nNo orders for {coffee_1.name}")

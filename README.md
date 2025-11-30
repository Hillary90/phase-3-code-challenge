# Coffee Shop Code Challenge

A Python domain model representing a Coffee Shop with Customers, Coffees, and Orders.
This project demonstrates object-oriented programming, relationships, aggregation, and class methods in Python.

### Overview

This project models a simple Coffee Shop domain using Python classes:

Customer – represents a customer of the coffee shop.

Coffee – represents a type of coffee available.

Order – represents a single order made by a customer for a coffee.

It captures real-world relationships:

A Customer can place multiple Orders.

A Coffee can have multiple Orders.

An Order belongs to one Customer and one Coffee.

The Order class acts as the single source of truth for all relationships.

### Features

1. Fully validated Customer and Coffee names.

2. Price validation for Orders.

3. Many-to-many relationships implemented through Order.

4. Aggregate methods:

5. Customer: list of coffees ordered

6. Coffee: total orders, average price

7. Class method most_aficionado(coffee) to identify the customer who spent the most on a given coffee.

8. Encapsulation and defensive copying for safe object state management.

## Project Structure:

coffee_shop/
│
├── customer.py
├── coffee.py
├── order.py
├── README.md
├── LICENSE.md
└── tests/


## Installation

##### Clone the repository:
bash 
```
git clone https://github.com/Hillary90/phase-3-code-challenge.git

cd phase-3-code-challenge 
```

**Set up a virtual environment with pipenv:**

```
pipenv install
pipenv shell
```

**Install pytest for testing:**

```
pipenv install pytest
```

**Create objects:**

Hillary = Customer( "Hillary" ) 

latte = Coffee( "Latte" )

Cappuccino = Coffee( "Cappuccino" )

# Create orders
order1 = Hillary.create_order( latte, 5.0 )

order2 = Jane.create_order( espresso, 4.5 )

# Check customer's coffees
print( Jane.coffees() )

# Coffee aggregate info
print( Cappuccino.num_orders() )

print( Cappuccino.average_price() )


## Author

*Hillary Tanui*


# License

This project is licensed under the MIT License– see the [LICENSE](LICENSE.md) file.
 file for details.

Contributing

Contributions are welcome!

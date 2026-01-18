def add_order(order_id, orders=None):
    add_order.orders.append(order_id)
    print(add_order.orders)
    return add_order.orders

# Initialize storage once (outside function)
add_order.orders = []

# Sample calls
add_order(101)
add_order(102)
add_order(103)

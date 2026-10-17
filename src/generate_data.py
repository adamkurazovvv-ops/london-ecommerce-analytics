import pandas as pd
from faker import Faker
import random

fake = Faker()

london_areas = [
    ("E1", "Tower Hamlets"),
    ("E2", "Tower Hamlets"),
    ("E8", "Hackney"),
    ("N1", "Islington"),
    ("NW1", "Camden"),
    ("SE1", "Southwark"),
    ("SW1", "Westminster"),
    ("W1", "Westminster"),
    ("EC1", "Islington"),
    ("CR0", "Croydon")
]

customers = []

for i in range(1000):
    postcode_district, borough = fake.random_element(london_areas)

    customer = {
        "customer_id": i + 1,
        "name": fake.name(),
        "registration_date": fake.date(),
        "postcode_district": postcode_district,
        "borough": borough
    }

    customers.append(customer)

df = pd.DataFrame(customers)

print(df)

df.to_csv("data/customers.csv", index=False)


orders = []

for i in range(5000):
    order = {
        "order_id": i + 1,
        "customer_id": fake.random_int(min=1, max=1000),
        "order_date": fake.date_between(
            start_date="-2y",
            end_date="today"
        )
    }

    orders.append(order)

orders_df = pd.DataFrame(orders)

products=[
    {"product_id": 1, "product_name": "Wireless Headphones", "category": "Electronics", "price": 89.99},
    {"product_id": 2, "product_name": "Coffee Machine", "category": "Home", "price": 129.99},
    {"product_id": 3, "product_name": "Running Shoes", "category": "Sports", "price": 74.99},
    {"product_id": 4, "product_name": "Backpack", "category": "Fashion", "price": 49.99},
    {"product_id": 5, "product_name": "Smart Watch", "category": "Electronics", "price": 159.99},
    {"product_id": 6, "product_name": "Desk Lamp", "category": "Home", "price": 34.99},
    {"product_id": 7, "product_name": "Yoga Mat", "category": "Sports", "price": 29.99},
    {"product_id": 8, "product_name": "T-Shirt", "category": "Fashion", "price": 24.99},
    {"product_id": 9, "product_name": "Bluetooth Speaker", "category": "Electronics", "price": 59.99},
    {"product_id": 10, "product_name": "Water Bottle", "category": "Sports", "price": 19.99}
]

products_df=pd.DataFrame(products)

print(products_df)

products_df.to_csv("data/products.csv", index=False)


order_items = []
item_id = 1

# First, give every order at least one item
for order_id in range(1, 5001):
    product_id = fake.random_int(min=1, max=10)
    quantity = fake.random_int(min=1, max=3)

    order_items.append({
        "order_item_id": item_id,
        "order_id": order_id,
        "product_id": product_id,
        "quantity": quantity
    })
    item_id += 1

# Add 5,000 more items to reach exactly 10,000 rows
for _ in range(5000):
    order_id = fake.random_int(min=1, max=5000)
    product_id = fake.random_int(min=1, max=10)
    quantity = fake.random_int(min=1, max=3)

    order_items.append({
        "order_item_id": item_id,
        "order_id": order_id,
        "product_id": product_id,
        "quantity": quantity
    })
    item_id += 1

items_df = pd.DataFrame(order_items)

print(items_df.head())
print("Total order items:", len(items_df))
print("Unique orders with items:", items_df["order_id"].nunique())

items_df.to_csv("data/order_items.csv", index=False)


# Calculate order totals from product prices and quantities
items_with_prices = items_df.merge(
    products_df[["product_id", "price"]],
    on="product_id",
    how="left"
)

items_with_prices["item_total"] = (
    items_with_prices["price"] * items_with_prices["quantity"]
)

order_totals = (
    items_with_prices.groupby("order_id")["item_total"]
    .sum()
    .round(2)
    .reset_index()
)

orders_df = orders_df.merge(
    order_totals,
    on="order_id",
    how="left"
)

orders_df = orders_df.rename(columns={"item_total": "order_amount"})

orders_df.to_csv("data/orders.csv", index=False)

print("\nCalculated order amounts:")
print(orders_df.head())
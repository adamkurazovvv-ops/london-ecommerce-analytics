
import pandas as pd

customers = pd.read_csv("data/customers.csv")
orders = pd.read_csv("data/orders.csv")
products = pd.read_csv("data/products.csv")
order_items = pd.read_csv("data/order_items.csv")

# 1. Check row counts
print("Row counts:")
print("Customers:", len(customers))
print("Orders:", len(orders))
print("Products:", len(products))
print("Order items:", len(order_items))

# 2. Check missing values
print("\nMissing values:")
print("Customers:", customers.isnull().sum().sum())
print("Orders:", orders.isnull().sum().sum())
print("Products:", products.isnull().sum().sum())
print("Order items:", order_items.isnull().sum().sum())

# 3. Check duplicate IDs
print("\nDuplicate IDs:")
print("Customer IDs:", customers["customer_id"].duplicated().sum())
print("Order IDs:", orders["order_id"].duplicated().sum())
print("Product IDs:", products["product_id"].duplicated().sum())
print("Order item IDs:", order_items["order_item_id"].duplicated().sum())


print("\nForeign key checks:")

print(
    "Orders with unknown customers:",
    (~orders["customer_id"].isin(customers["customer_id"])).sum()
)

print(
    "Order items with unknown orders:",
    (~order_items["order_id"].isin(orders["order_id"])).sum()
)

print(
    "Order items with unknown products:",
    (~order_items["product_id"].isin(products["product_id"])).sum()
)


# Calculate order totals from products and quantities
items_with_prices = order_items.merge(
    products[["product_id", "price"]],
    on="product_id",
    how="left"
)

items_with_prices["item_total"] = (
    items_with_prices["price"] * items_with_prices["quantity"]
)

calculated_totals = (
    items_with_prices.groupby("order_id")["item_total"]
    .sum()
    .round(2)
)

orders_check = orders.set_index("order_id").copy()
orders_check["calculated_total"] = calculated_totals

orders_check["difference"] = (
    orders_check["order_amount"] - orders_check["calculated_total"]
).round(2)

print("\nOrder amount validation:")
print("Orders with different totals:", (orders_check["difference"].abs() > 0.01).sum())
print(orders_check[["order_amount", "calculated_total", "difference"]].head())

orders_without_items = (
    ~orders["order_id"].isin(order_items["order_id"])
).sum()

print("Orders without items:", orders_without_items
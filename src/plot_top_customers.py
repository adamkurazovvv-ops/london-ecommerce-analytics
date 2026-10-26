
import pandas as pd
import matplotlib.pyplot as plt

# Загружаем данные о 10 самых ценных клиентах
df = pd.read_csv("reports/top_customers.csv")

# Сортируем, чтобы самый ценный клиент был сверху
df = df.sort_values("total_spent", ascending=True)

# Строим горизонтальный график
plt.figure(figsize=(10, 6))
plt.barh(df["name"], df["total_spent"])

plt.title("Top 10 Customers by Spending (Synthetic Data)")
plt.xlabel("Total Spent (£)")
plt.ylabel("Customer")
plt.tight_layout()

# Сохраняем график
plt.savefig("reports/top_customers.png", dpi=150)

plt.show()
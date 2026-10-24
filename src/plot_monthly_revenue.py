import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("reports/monthly_revenue.csv")
df["month"] = pd.to_datetime(df["month"])

plt.figure(figsize=(12, 6))
plt.plot(df["month"], df["revenue"], marker="o")

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (£)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("reports/monthly_revenue.png", dpi=300)
plt.show()
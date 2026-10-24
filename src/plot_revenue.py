import pandas as pd
import matplotlib.pyplot as plt

# Read revenue data from CSV
df = pd.read_csv("reports/revenue_by_category.csv")

# Create a bar chart
plt.bar(df["category"], df["revenue"])
plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Revenue (£)")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart
plt.savefig("reports/revenue_by_category.png", dpi=300)
plt.show()
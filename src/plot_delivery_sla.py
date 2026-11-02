
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("reports/delivery_sla_by_borough.csv")
df = df.sort_values("late_percentage", ascending=True)

plt.figure(figsize=(10, 6))
plt.barh(df["borough"], df["late_percentage"])

plt.title("Delivery SLA: Late Deliveries by London Borough")
plt.xlabel("Late Deliveries (%)")
plt.ylabel("Borough")
plt.tight_layout()

plt.savefig("reports/delivery_sla_by_borough.png", dpi=300)
plt.show()
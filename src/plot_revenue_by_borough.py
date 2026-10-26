
import pandas as pd
import matplotlib.pyplot as plt

# Загружаем данные из CSV-файла
df = pd.read_csv("reports/revenue_by_borough.csv")

# Сортируем районы от самой высокой выручки к самой низкой
df = df.sort_values("revenue", ascending=True)

# Строим горизонтальный график
plt.figure(figsize=(10, 6))
plt.barh(df["borough"], df["revenue"])

plt.title("Revenue by London Borough (Synthetic Data)")
plt.xlabel("Revenue (£)")
plt.ylabel("Borough")
plt.tight_layout()

# Сохраняем график
plt.savefig("reports/revenue_by_borough.png", dpi=150)

plt.show()
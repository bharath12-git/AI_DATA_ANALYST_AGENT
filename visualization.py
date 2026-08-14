import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset

df = pd.read_csv("sample.csv")



# 1. Revenue by Product

revenue = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)


plt.figure(figsize=(10,5))

revenue.plot(
    kind="bar"
)

plt.title("Revenue by Product")

plt.xlabel("Product")

plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("revenue_product.png")

plt.show()



# 2. Profit by Product

profit = (
    df.groupby("Product")["Profit"]
    .sum()
    .sort_values(ascending=False)
)


plt.figure(figsize=(10,5))

profit.plot(
    kind="bar"
)

plt.title("Profit by Product")

plt.xlabel("Product")

plt.ylabel("Profit")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("profit_product.png")

plt.show()



# 3. Category Revenue

category = (
    df.groupby("Category")["Revenue"]
    .sum()
)


plt.figure(figsize=(7,5))

category.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Revenue Distribution by Category")

plt.ylabel("")

plt.tight_layout()

plt.savefig("category_revenue.png")

plt.show()



# 4. Correlation Heatmap

plt.figure(figsize=(8,6))

sns.heatmap(
    df.select_dtypes(
        include="number"
    ).corr(),
    annot=True
)


plt.title("Feature Correlation")

plt.tight_layout()

plt.savefig("correlation_heatmap.png")

plt.show()
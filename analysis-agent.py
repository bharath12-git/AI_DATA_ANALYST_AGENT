import pandas as pd


# Load dataset

file = "sample.csv"

df = pd.read_csv(file)



# 1. Dataset Overview

print("\n========== DATASET OVERVIEW ==========")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Names:")
print(list(df.columns))



# 2. Data Types

print("\n========== DATA TYPES ==========")

print(df.dtypes)



# 3. Missing Values

print("\n========== MISSING VALUES ==========")

missing = df.isnull().sum()

print(missing)



# 4. Duplicate Check

print("\n========== DUPLICATE ROWS ==========")

duplicates = df.duplicated().sum()

print("Duplicate rows:", duplicates)



# 5. Statistical Summary

print("\n========== STATISTICAL SUMMARY ==========")

print(df.describe())



# 6. Revenue Analysis

print("\n========== REVENUE ANALYSIS ==========")


highest_revenue = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)


print("Top Products by Revenue:")
print(highest_revenue)



# 7. Profit Analysis

print("\n========== PROFIT ANALYSIS ==========")


highest_profit = (
    df.groupby("Product")["Profit"]
    .sum()
    .sort_values(ascending=False)
)


print("Top Products by Profit:")
print(highest_profit)
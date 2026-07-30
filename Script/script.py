import pandas as pd

# Load dataset
df = pd.read_csv("SampleSuperstore.csv", encoding="latin1")

# Data Cleaning
df = df.drop_duplicates()
df = df.fillna(0)

# Save processed dataset
df.to_csv("Processed_SampleSuperstore.csv", index=False)

# Calculate KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
average_sales = df["Sales"].mean()

# Create KPI report
kpi = pd.DataFrame({
    "KPI": [
        "Total Sales",
        "Total Profit",
        "Total Orders",
        "Average Sales"
    ],
    "Value": [
        total_sales,
        total_profit,
        total_orders,
        average_sales
    ]
})
# Task 5 - Automation Script
# Sample Superstore Data Analysis

import pandas as pd


# Load Dataset
df = pd.read_csv("SampleSuperstore.csv", encoding="latin1")

print("Dataset Loaded Successfully")


# Data Cleaning
df = df.drop_duplicates()
df = df.fillna(0)

print("Data Cleaning Completed")


# Save Processed Data
df.to_csv("Processed_SampleSuperstore.csv", index=False)

print("Processed Data Saved")


# KPI Calculation

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
average_sales = df["Sales"].mean()


# Create KPI Report

kpi_report = pd.DataFrame({
    "KPI": [
        "Total Sales",
        "Total Profit",
        "Total Orders",
        "Average Sales"
    ],
    "Value": [
        total_sales,
        total_profit,
        total_orders,
        average_sales
    ]
})


kpi_report.to_excel("KPI_Report.xlsx", index=False)


print("\nKPI Report Created")


# Business Insights

print("\nTop Category by Sales:")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False).head(1))


print("\nTop Region by Profit:")
print(df.groupby("Region")["Profit"].sum().sort_values(ascending=False).head(1))


print("\nTop Segment by Sales:")
print(df.groupby("Segment")["Sales"].sum().sort_values(ascending=False).head(1))


print("\nTask 5 Automation Completed Successfully!")
# Export KPI report to Excel
kpi.to_excel("KPI_Report.xlsx", index=False)

print("Task 5 Automation Completed Successfully!")
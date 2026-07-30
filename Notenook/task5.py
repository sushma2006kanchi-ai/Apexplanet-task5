
import pandas as pd

df = pd.read_csv("SampleSuperstore.csv", encoding="latin1")

print("Dataset Loaded Successfully")

print("\nFirst 5 Rows:")

print(df.head())

print("\nDataset Information:")

df.info()

df = df.drop_duplicates()

print("\nDuplicates Removed")

print("\nMissing Values:")

print(df.isnull().sum())

df = df.fillna(0)

print("\nMissing Values Filled")

df.to_csv("Processed_SampleSuperstore.csv", index=False)

print("\nProcessed Dataset Saved")

total_sales = df["Sales"].sum()

total_profit = df["Profit"].sum()

total_orders = df["Order ID"].nunique()

average_sales = df["Sales"].mean()

print("\n------ KPI Report ------")

print("Total Sales :", total_sales)

print("Total Profit :", total_profit)

print("Total Orders :", total_orders)

print("Average Sales :", average_sales)

kpi = pd.DataFrame({

    "KPI Name": [
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


kpi.to_excel("KPI_Report.xlsx", index=False)

print("\nKPI Report Excel Created")


category_sales = df.groupby("Category")["Sales"].sum()

print("\nCategory Wise Sales:")

print(category_sales)


region_profit = df.groupby("Region")["Profit"].sum()

print("\nRegion Wise Profit:")

print(region_profit)

segment_sales = df.groupby("Segment")["Sales"].sum()

print("\nSegment Wise Sales:")

print(segment_sales)

print("\nTask 5 Automation Completed Successfully!")
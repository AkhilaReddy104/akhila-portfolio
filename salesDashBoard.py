import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel("salesData.xlsx")

# Show the first few rows
print("Preview of Sales Data:")
print(df.head())

# Total sales per product
product_sales = df.groupby("Product")["Total Sales"].sum().sort_values(ascending=False)
print("\nTotal Sales by Product:")
print(product_sales)

# Plot: Sales by Product
product_sales.plot(kind='bar', title="Total Sales by Product", color='skyblue')
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# Total sales per region
region_sales = df.groupby("Region")["Total Sales"].sum().sort_values(ascending=False)
print("\nTotal Sales by Region:")
print(region_sales)

# Plot: Sales by Region
region_sales.plot(kind='pie', title="Sales Distribution by Region", autopct='%1.1f%%')
plt.ylabel("")
plt.tight_layout()
plt.show()

# Monthly sales trend
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Total Sales"].sum()

# Plot: Monthly Sales
monthly_sales.plot(marker='o', title="Monthly Sales Trend", color='green')
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

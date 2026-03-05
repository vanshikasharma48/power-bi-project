import pandas as pd
import os

# Get script directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create file path
file_path = os.path.join(BASE_DIR, "Sample - Superstore.csv")

df = pd.read_csv(file_path, encoding_errors='ignore')
print(df.columns)
print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
df.duplicated().sum()
df = df.drop_duplicates()
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(" ", "_")
df.columns = df.columns.str.replace("-", "_")
df[df['Profit'] < 0].head()
df['Discount'].describe()
df['Profit_Margin'] = df['Profit'] / df['Sales']
df['Delivery_Days'] = (
    df['Ship_Date'] - df['Order_Date']
).dt.days
df['Year'] = df['Order_Date'].dt.year
df['Month'] = df['Order_Date'].dt.month
df['Month_Name'] = df['Order_Date'].dt.month_name()
df['Quarter'] = df['Order_Date'].dt.quarter
df['Sales'].describe()
monthly_sales = df.groupby(
    ['Year', 'Month_Name']
)['Sales'].sum().reset_index()

print(monthly_sales.head())
monthly_sales = df.groupby(
    ['Year', 'Month', 'Month_Name']
)['Sales'].sum().reset_index()

monthly_sales = monthly_sales.sort_values(
    ['Year', 'Month']
)
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))

plt.plot(
    monthly_sales['Month_Name'],
    monthly_sales['Sales']
)

plt.xticks(rotation=45)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
monthly_sales['Growth_Rate'] = (
    monthly_sales['Sales'].pct_change()
) * 100

monthly_sales.head()
seasonality = df.groupby(
    ['Month', 'Month_Name']
)['Sales'].mean().reset_index()

seasonality = seasonality.sort_values('Month')

print(seasonality)
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))

plt.bar(
    seasonality['Month_Name'],
    seasonality['Sales']
)

plt.xticks(rotation=45)
plt.title("Average Monthly Sales (Seasonality)")
plt.xlabel("Month")
plt.ylabel("Average Sales")

plt.show()
quarter_sales = df.groupby('Quarter')['Sales'].sum().reset_index()

plt.figure(figsize=(8,5))

plt.bar(
    quarter_sales['Quarter'],
    quarter_sales['Sales']
)

plt.title("Quarterly Sales Performance")
plt.xlabel("Quarter")
plt.ylabel("Sales")

plt.show()
segment_sales = df.groupby('Segment')['Sales'].sum().reset_index()

print(segment_sales)
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))

plt.bar(
    segment_sales['Segment'],
    segment_sales['Sales']
)

plt.title("Sales by Customer Segment")
plt.xlabel("Segment")
plt.ylabel("Total Sales")

plt.show()
segment_profit = df.groupby('Segment')['Profit'].sum().reset_index()

print(segment_profit)
plt.figure(figsize=(8,5))

plt.bar(
    segment_profit['Segment'],
    segment_profit['Profit']
)

plt.title("Profit by Customer Segment")
plt.xlabel("Segment")
plt.ylabel("Total Profit")

plt.show()
segment_analysis = df.groupby('Segment').agg({
    'Sales':'sum',
    'Profit':'sum'
}).reset_index()

segment_analysis['Profit_Margin'] = (
    segment_analysis['Profit'] /
    segment_analysis['Sales']
)

print(segment_analysis)
orders_segment = df.groupby('Segment')['Order_ID'].count().reset_index()

print(orders_segment)
category_sales = df.groupby('Category')['Sales'].sum().reset_index()

print(category_sales)
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))

plt.bar(
    category_sales['Category'],
    category_sales['Sales']
)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.show()
category_profit = df.groupby('Category')['Profit'].sum().reset_index()

print(category_profit)
plt.figure(figsize=(8,5))

plt.bar(
    category_profit['Category'],
    category_profit['Profit']
)

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")

plt.show()
subcat_profit = (
    df.groupby('Sub_Category')['Profit']
    .sum()
    .sort_values()
    .reset_index()
)

print(subcat_profit)
plt.figure(figsize=(10,6))

plt.barh(
    subcat_profit['Sub_Category'],
    subcat_profit['Profit']
)

plt.title("Profit by Sub Category")
plt.xlabel("Profit")

plt.show()
top_products = (
    df.groupby('Product_Name')['Profit']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)
loss_products = (
    df.groupby('Product_Name')['Profit']
    .sum()
    .sort_values()
    .head(10)
)

print(loss_products)
plt.figure(figsize=(8,5))

plt.scatter(
    df['Discount'],
    df['Profit']
)

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.show()
total_sales = df['Sales'].sum()
print("Total Sales:", total_sales)
total_profit = df['Profit'].sum()
print("Total Profit:", total_profit)
profit_margin = total_profit / total_sales

print("Profit Margin:", round(profit_margin*100,2), "%")
total_orders = df['Order_ID'].nunique()

print("Total Orders:", total_orders)
total_customers = df['Customer_ID'].nunique()

print("Total Customers:", total_customers)
aov = total_sales / total_orders

print("Average Order Value:", round(aov,2))
monthly_sales = (
    df.groupby(['Year','Month'])['Sales']
    .sum()
    .reset_index()
)

print(monthly_sales.head())
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))

plt.plot(
    monthly_sales['Month'],
    monthly_sales['Sales']
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
region_perf = (
    df.groupby('Region')[['Sales','Profit']]
    .sum()
    .reset_index()
)

print(region_perf)
category_perf = (
    df.groupby('Category')[['Sales','Profit']]
    .sum()
    .reset_index()
)

print(category_perf)
category_perf = (
    df.groupby('Category')[['Sales','Profit']]
    .sum()
    .reset_index()
)

print(category_perf)
top_customers = (
    df.groupby('Customer_Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_customers)
df['Sales'].mean()
df['Sales'].median()
df['Sales'].std()
df[['Sales','Profit','Discount','Quantity']].corr()
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(
    df[['Sales','Profit','Discount','Quantity']].corr(),
    annot=True
)

plt.show()
plt.hist(df['Sales'], bins=50)
plt.title("Sales Distribution")
plt.show()
high_discount = df[df['Discount'] > 0.2]['Profit']
low_discount = df[df['Discount'] <= 0.2]['Profit']
from scipy.stats import ttest_ind

t_stat, p_value = ttest_ind(
    high_discount,
    low_discount,
    equal_var=False
)

print(p_value)
df.to_csv("clean_superstore.csv", index=False)
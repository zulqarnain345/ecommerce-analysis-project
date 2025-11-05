import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("ecommerce_sales.csv")
print(df.head(10),"\n")

print(df.describe(),"\n")

# how many category are??
noOfCategoryies=df["Category"].nunique()
print(f"types of Categoryies = {noOfCategoryies} ")

# Product Types
typeofproduct=df["Product"].nunique()
print(f"The no of products = {typeofproduct}")

# total avenue are
total=df["Total_Sales"].sum()
print(f"Total avenue = {total}")

# profit on all products are 
profit=df["Profit"].sum()
print(f"Total profit = {profit}")

# how much money made
overallprofit=total-profit
print(f"Profit made = {overallprofit}")

# products you sell
quantity=df["Quantity"].sum()
print(f"Total Quantity of products we sell = {quantity}")

# order we dilvery
total_order=df["Order_ID"].count()
print(f"Total Order We Get = {total_order}\n")

# separating the category

for category, group in df.groupby("Category"):
    print(f"{category}: Total Sales = {group['Total_Sales'].sum()}")
print(" ") 

# category with the highest revenue 

category_revenue=df.groupby("Category")["Total_Sales"].sum()
highest_category=category_revenue.idxmax()
print(f"The top highest category is {highest_category} ")

# find the most products sell on category
for category,group in df.groupby("Category"):
    top_category=group.loc[group["Total_Sales"].idxmax()]
print(f"The top Category which genrate the most revenue are {top_category["Product"]} category of {top_category["Category"]}")        
    

# find the least category product sell
for category,group in df.groupby("Category"):
    least_category=group.loc[group["Total_Sales"].idxmin()]
print(f"The least Category which genrate the most revenue are {least_category["Product"]} with the price of {least_category["Category"]}")        


# product on which you give the highest discount

for product,group in df.groupby("Product"):
    top_discount=group.loc[group["Discount"].idxmax()]
print(f"The product {top_discount["Product"]} on which we give the highest discount is {top_discount["Discount"]*100:.0f}%")

# # product on which you give the least discount

for product,group in df.groupby("Product"):
    least_discount=group.loc[group["Discount"].idxmin()]
print(f"The product {least_discount["Product"]} on which we give the highest discount is {least_discount["Discount"]*100:.0f}% \n")

# in which region sells are higher 
region_sells=df.groupby("Region")["Total_Sales"].sum()
largenosell=region_sells.idxmax()
print(f"in this region sells are less {largenosell}")

# in which region sells are less
smallnoodsells=region_sells.idxmin()
print(f"in this region sells are less {smallnoodsells}")

# bar chart which represent the total sell in this region 
colors=["red","blue","black","gray","skyblue"]
plt.bar(region_sells.index,region_sells.values,color=colors)
plt.axhline(df["Total_Sales"].mean(),linestyle="--",color="black")
plt.grid(True,linestyle="--",alpha=0.5)
plt.title("REGION WISE SALES")
plt.xlabel("SALES")
plt.ylabel("REGION")
plt.show()

# pie chart
plt.pie(region_sells.values,labels=region_sells.index,autopct="%1.1f%%",startangle=90)
plt.axis("equal")
plt.tight_layout()
plt.show()

# bar chart product which show the price of the products
plt.bar(df["Product"],df["Price"],color="red")
plt.axhline(df["Price"].mean(),linestyle="--",linewidth=2,color="black")
plt.grid(True,linestyle="--",alpha=0.5)
plt.title("OVERALL PROJECT")
plt.xlabel("PRICE")
plt.ylabel("PRODUCT")
plt.show()

# bar chart represent the category wise 

unique_category=df["Category"].unique()

if len(unique_category)<=10:
    palette=sns.color_palette("tab10",len(unique_category))
elif(10 < len(unique_category)<20):
    palette=sns.color_palette("tab20",len(unique_category))
else:
    palette=sns.color_palette("husl",len(unique_category))

category_color_map={category: palette[i % len(palette)]for i,category in enumerate(unique_category)}
color=[category_color_map[category]for category in df["Category"]]

plt.figure(figsize=(12,8))
plt.bar(df["Product"],df["Price"],color=color)
plt.xlabel("Product")
plt.ylabel("Price")
plt.title("Category-wise Product Price Distribution")
plt.xticks(rotation=45)
plt.show()



# top 5 best sellings products

top_5=df.nlargest(5,"Total_Sales")[["Product","Category","Quantity"]]
top_5.index=range(1,len(top_5)+1)
print(top_5)

least_3=df.nsmallest(3,"Total_Sales")[["Product","Category","Quantity"]]
least_3.index=range(1,len(least_3)+1)
print(least_3)

plt.bar("Product","Quantity",data=least_3,color="green")
plt.title("least 3")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.xticks(rotation=45)
plt.grid(True,linestyle="--",alpha=0.5)
plt.legend()
plt.show()

plt.bar("Product","Quantity",data=top_5,color="red")
plt.title("TOP 5")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.xticks(rotation=45)
plt.grid(True,linestyle="--",alpha=0.5)
plt.legend()
plt.show()

#Sales Trend Over Time (Most Common Line Chart)

df["Date"]=pd.to_datetime(df["Date"])
sales_trend=df.groupby("Date")["Total_Sales"].sum()

plt.plot(sales_trend.index,sales_trend.values,marker="o",color="blue")
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()


# Profit Trend Over Time

profit_trend=df.groupby("Date")["Profit"].sum()
plt.plot(profit_trend.index,profit_trend.values,marker="o",color="blue")
plt.title("profit Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Profit")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

# Category-wise Average Sales

category_wise_trend=df.groupby("Category")["Total_Sales"].mean()

plt.plot(category_wise_trend.index,category_wise_trend.values,marker="o",color="blue")
plt.title("Category-wise Average Sales")
plt.xlabel("Category")
plt.ylabel("price")
plt.grid(True,alpha=0.5,linestyle="--")
plt.show()


# Region-wise Sales Comparison

date=pd.to_datetime(df["Date"])
region_wise_trend=df.groupby(["Date","Region"])["Total_Sales"].sum().reset_index()

for region in region_wise_trend["Region"].unique():
    date=region_wise_trend[region_wise_trend["Region"]==region]
    plt.plot(date["Date"], date["Total_Sales"], marker="o", label=region)

plt.title("Region-wise Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

#Correlation Heatmap

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Between Numerical Features")
plt.show()

# Average Profit by Category

category_profit = df.groupby("Category")["Profit"].mean().sort_values(ascending=False)
category_profit.plot(kind="bar", color="orange")
plt.title("Average Profit per Category")
plt.ylabel("Average Profit")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()


#Month-wise Sales Trend 

df["Month"] = df["Date"].dt.to_period("M")
month_sales = df.groupby("Month")["Total_Sales"].sum()
month_sales.plot(kind="line", marker="o", color="green")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

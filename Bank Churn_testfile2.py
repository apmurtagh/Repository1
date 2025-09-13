# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 14:42:42 2024

@author: Trente_NUC
"""

# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Sat Oct  5 11:06:04 2024)---
%reset
dir()

## ---(Sat Oct 12 08:47:22 2024)---
# Create an object x and assign a value 20
x=20
x
# Create an object y and assign a value 15
y=15
y
x+y
x*y
print ("Welcome to Ask Analytics")
print (55)
print(4*5*3)
print ("This is", "session no.", 3)
x=54
print("He is %d yr old" %x)
help(print)
quit
runfile('D:/Dbak/_DSI/EDA/2 Getting Started in Python/PyScri1.py', wdir='D:/Dbak/_DSI/EDA/2 Getting Started in Python')
quit
runfile('D:/Dbak/_DSI/EDA/2 Getting Started in Python/PyScri1.py', wdir='D:/Dbak/_DSI/EDA/2 Getting Started in Python')
x=10
x
type(x)
y=15*2
type y
type (y)
z=2.5
type(z)
v=-20.35
type(v)
x=int(-999.73)
x
type (c)
type (x)
y=float(25)
type y
type (y)
y
x='welcome to the Python world'
x
z='3948'
z
type(z)
x=x+", John"
x
quit
import pandas as pd
import numpy as np
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("Bank Churn.csv")
head (data)
data.info()
head.data()
data.head()
data.tail()
data.dim()
data_exited_1 = data[data['Exited'] == 1]
data_exited_0 = data[data['Exited'] == 0]
plt.figure(figsize=(8, 5))
plt.subplot(1, 2, 1)
sns.boxplot(x='Exited', y='CreditScore', data=data_exited_1)
plt.title('CreditScore Distribution for Exited=1')
plt.subplot(1, 2, 2)
sns.boxplot(x='Exited', y='CreditScore', data=data_exited_0)
plt.title('CreditScore Distribution for Exited=0')
plt.tight_layout()
# Show the plots
plt.show()
plt.tight_layout()
plt.show()
plt.figure(figsize=(8, 5))
# Box plot for Exited=1
plt.subplot(1, 2, 1)
sns.boxplot(x='Exited', y='CreditScore', data=data_exited_1)
plt.title('CreditScore Distribution for Exited=1')
# Box plot for Exited=0
plt.subplot(1, 2, 2)
sns.boxplot(x='Exited', y='CreditScore', data=data_exited_0)
plt.title('CreditScore Distribution for Exited=0')
# Adjust the layout
plt.tight_layout()
# Show the plots
plt.show()
# Calculate skewness for each group
skewness_exited_1 = stats.skew(data_exited_1['CreditScore'])
skewness_exited_0 = stats.skew(data_exited_0['CreditScore'])
print(f"Skewness for Exited=1: {skewness_exited_1:.2f}")
print(f"Skewness for Exited=0: {skewness_exited_0:.2f}")
summary_credit_score = data.groupby('Exited')['CreditScore'].agg(['count',
'mean'])
# Rename the columns for clarity
summary_credit_score = summary_credit_score.rename(columns={
'count': 'Count',
'mean': 'Mean'})
summary_credit_score.round(2)
# Create a cross table of 'Geography' vs. 'Exited' with counts
cross_table = pd.crosstab(data['Geography'], data['Exited'], margins=True,
margins_name='Total')
# Calculate proportions
cross_table_proportions = cross_table.div(cross_table['Total'], axis=0) *
100
# Rename the columns for clarity
cross_table = cross_table.rename(columns={0: 'Not Exited', 1: 'Exited'})
cross_table_proportions = cross_table_proportions.rename(columns={0: 'Not
Exited (%)', 1: 'Exited (%)'})
# Display the cross table and proportions
print("Cross Table (Counts):\n")
print(cross_table)
print("\nCross Table (Proportions):\n")
print(cross_table_proportions.round(2))
# Create a cross table of 'Geography' vs. 'Exited' with counts
cross_table = pd.crosstab(data['Geography'], data['Exited'], margins=True,
margins_name='Total')
# Calculate proportions
cross_table_proportions = cross_table.div(cross_table['Total'], axis=0) * 100
# Rename the columns for clarity
cross_table = cross_table.rename(columns={0: 'Not Exited', 1: 'Exited'})
cross_table_proportions = cross_table_proportions.rename(columns={0: 'Not
Exited (%)', 1: 'Exited (%)'})
# Display the cross table and proportions
print("Cross Table (Counts):\n")
print(cross_table)
print("\nCross Table (Proportions):\n")
print(cross_table_proportions.round(2))
# Create a cross table of 'Geography' vs. 'Exited' with counts
cross_table = pd.crosstab(data['Geography'], data['Exited'], margins=True, margins_name='Total')
# Calculate proportions
cross_table_proportions = cross_table.div(cross_table['Total'], axis=0) * 100
# Rename the columns for clarity
cross_table = cross_table.rename(columns={0: 'Not Exited', 1: 'Exited'})
cross_table_proportions = cross_table_proportions.rename(columns={0: 'Not Exited (%)', 1: 'Exited (%)'})
# Display the cross table and proportions
print("Cross Table (Counts):\n")
print(cross_table)
print("\nCross Table (Proportions):\n")
print(cross_table_proportions.round(2))
correlation_coefficient = data['CreditScore'].corr(data['EstimatedSalary']) correlation_coefficient.round(4)
correlation_coefficient = data['CreditScore'].corr(data['EstimatedSalary']
)
correlation_coefficient.round(4)
correlation_coefficient = data['CreditScore'].corr(data['EstimatedSalary'])
correlation_coefficient.round(4)
data['CreditScore_Cat'] = np.where(data['CreditScore']>=650,1,0)
data.head()
# Create a cross table of 'CreditScore_Cat' vs. 'Exited' with counts, excluding the "Total" row
cross_table = pd.crosstab(data['CreditScore_Cat'], data['Exited'], margins=False)
# Calculate proportions
cross_table_proportions = (cross_table.div(cross_table.sum(axis=1), axis=0) * 100).round(2)
# Rename the columns for clarity
cross_table.columns = ['Not Exited', 'Exited']
cross_table_proportions.columns = ['Not Exited (%)', 'Exited (%)']
# Concatenate the counts and proportions side by side
result_table = pd.concat([cross_table, cross_table_proportions], axis=1)
# Display the combined table
print(result_table)
# Sort the data by 'CreditScore' in descending order and select the top 300 rows
top_300_customers = data.sort_values(by='CreditScore', ascending=False).head(300)
# Create a cross table to check the distribution of these customers over 'Geography'
geo_distribution_top_300 = pd.crosstab(top_300_customers['Geography'], columns='Count')
# Display the cross table
print("Geography Distribution of Top 500 Customers:")
print(geo_distribution_top_300)
# Group the data by 'Geography' and 'Gender', and calculate count, mean, and median for 'CreditScore'
summary_credit_score = data.groupby(['Geography', 'Gender'])['CreditScore'].agg(['count', 'mean', 'median'])
# Reset the index to make the result more readable
summary_credit_score = summary_credit_score.reset_index()
# Rename the columns for clarity
summary_credit_score = summary_credit_score.rename(columns={'count': 'Count','mean': 'Mean','median': 'Median'})
# Display the summary
print(summary_credit_score)
# Count the number of products for each combination of Geography
product_count_by_geography = data.groupby('Geography')['NumOfProducts'].sum().reset_index()
print(product_count_by_geography)
# Create a bar plot to show the count of number of products by Geography
plt.figure(figsize=(6, 5))
sns.barplot(x='Geography', y='NumOfProducts', data=product_count_by_geography)
plt.title('Count of Number of Products by Geography')
plt.xlabel('Geography')
plt.ylabel('Count of Number of Products')
plt.show()
# Create a cross table of 'Geography' vs. 'Exited' with counts
cross_table = pd.crosstab(data['Geography'], data['Exited'], margins=True, margins_name='Total')
# Calculate proportions
cross_table_proportions = cross_table.div(cross_table['Total'], axis=0) * 100
# Rename the columns for clarity
cross_table = cross_table.rename(columns={0: 'Not Exited', 1: 'Exited'})
cross_table_proportions = cross_table_proportions.rename(columns={0: 'Not Exited (%)', 1: 'Exited (%)'})
# Display the cross table and proportions
print("Cross Table (Counts)")
print(cross_table)
print("\nCross Table (Proportions):\n")
print(cross_table_proportions.round(2))
# Create a cross table of 'Geography' vs. 'Exited' with counts
cross_table = pd.crosstab(data['Geography'], data['Exited'], margins=True, margins_name='Total')
# Calculate proportions
cross_table_proportions = cross_table.div(cross_table['Total'], axis=0) * 100
# Rename the columns for clarity
cross_table = cross_table.rename(columns={0: 'Not Exited', 1: 'Exited'})
cross_table_proportions = cross_table_proportions.rename(columns={0: 'Not Exited (%)', 1: 'Exited (%)'})
# Display the cross table and proportions
print("Cross Table (Counts):\n")
print(cross_table)
print("Cross Table (Proportions)")
print(cross_table_proportions.round(2))
data['CreditScore_Cat'] = np.where(data['CreditScore']>=650,1,0)
data.head()
## note the above content is shrunk (with "...." in centre) to allow for display - not an issue in Jupytertations
 data['CreditScore_Cat'] = np.where(data['CreditScore']>=650,1,0)
data.head()
# Sort the data by 'CreditScore' in descending order and select the top 500 rows
top_300_customers = data.sort_values(by='CreditScore', ascending=False).head(500)
# Create a cross table to check the distribution of these customers over 'Geography'
geo_distribution_top_300 = pd.crosstab(top_300_customers['Geography'], columns='Count')
# Display the cross table
print("Geography Distribution of Top 500 Customers:")
print(geo_distribution_top_300)
Geography Distribution of Top 500 Customers:
col_0      Count
Geography       
France       150
Germany       80
Spain         70
 # Sort the data by 'CreditScore' in descending order and select the top 500 rows
top_500_customers = data.sort_values(by='CreditScore', ascending=False).head(500)
# Create a cross table to check the distribution of these customers over 'Geography'
geo_distribution_top_300 = pd.crosstab(top_300_customers['Geography'], columns='Count')
# Display the cross table
print("Geography Distribution of Top 500 Customers:")
print(geo_distribution_top_300)
Geography Distribution of Top 500 Customers:
col_0      Count
Geography       
France       150
Germany       80
Spain         70
# Sort the data by 'CreditScore' in descending order and select the top 300 rows
top_400_customers = data.sort_values(by='CreditScore', ascending=False).head(300)
# Create a cross table to check the distribution of these customers over 'Geography'
geo_distribution_top_300 = pd.crosstab(top_300_customers['Geography'], columns='Count')
# Display the cross table
print("Geography Distribution of Top 500 Customers:")
print(geo_distribution_top_300)
# Sort the data by 'CreditScore' in descending order and select the top 500 rows
top_500_customers = data.sort_values(by='CreditScore', ascending=False).head(500)
# Create a cross table to check the distribution of these customers over 'Geography'
geo_distribution_top_500 = pd.crosstab(top_500_customers['Geography'], columns='Count')
# Display the cross table
print("Geography Distribution of Top 500 Customers:")
print(geo_distribution_top_500)
summary_credit_score = data.groupby(['Geography', 'Gender'])['CreditScore'].agg(['count', 'mean', 'median'])
summary_credit_score
summary_credit_score = summary_credit_score.reset_index()
summary_credit_score
summary_credit_score = summary_credit_score.rename(columns={ 'count': 'Count', 'mean': 'Mean', 'median': 'Median' })
print(summary_credit_score)
Count the number of products for each combination of Geography
product_count_by_geography = data.groupby('Geography')['NumOfProducts'].su
m().reset_index()
Count the number of products for each combination of Geography
product_count_by_geography = data.groupby('Geography')['NumOfProducts'].sum().reset_index()
##Count the number of products for each combination of Geography
product_count_by_geography = data.groupby('Geography')['NumOfProducts'].sum().reset_index()
print(product_count_by_geography)
# Create a bar plot to show the count of number of products by Geography
plt.figure(figsize=(6, 5))
sns.barplot(x='Geography', y='NumOfProducts', data=product_count_by_geogra
phy)
plt.title('Count of Number of Products by Geography')
plt.xlabel('Geography')
plt.ylabel('Count of Number of Products')
plt.show()
# Create a bar plot to show the count of number of products by Geography
plt.figure(figsize=(6, 5))
sns.barplot(x='Geography', y='NumOfProducts', data=product_count_by_geography)
plt.title('Count of Number of Products by Geography')
plt.xlabel('Geography')
plt.ylabel('Count of Number of Products')
plt.show()
import pandas as pd
import numpy as np


data_frm = pd.read_csv('/home/abdeljalil/Desktop/youcode/Brief_Nettoyage_des_Donn-es/data_set.csv', encoding='latin1')
# print(data_frm.head())
data_frm = pd.DataFrame(data_frm)
data_cpy = data_frm.copy()

# 1. Data Catalog Creation
data_catalog = pd.DataFrame({
    "Column Name": data_frm.columns,
    "Data Type": data_frm.dtypes,
    "Non-Null Count": data_frm.notnull().sum(),
    "Null Count": data_frm.isnull().sum(),
})

# Save the catalog as a CSV file
"""
data_catalog.to_csv('data_catalog.csv', index=False)
print("Data catalog created and saved as 'data_catalog.csv'.")
"""
# print (data_catalog)

# 2. Preliminary Data Analysis
# Calculate descriptive statistics
data_description = data_frm.describe()
# print("Data catalog created and saved as 'data_catalog.csv'.")
# print (data_description)


# Check for asymmetry by comparing mean and median for each numeric column
asymmetry_analysis = pd.DataFrame({
    "Mean": data_frm.mean(numeric_only=True),
    "Median": data_frm.median(numeric_only=True),
    "Std Dev": data_frm.std(numeric_only=True),
    "Difference (Mean - Median)": data_frm.mean(numeric_only=True) - data_frm.median(numeric_only=True)
})

# asymmetry_analysis.to_csv('asymmetry_analysis.csv', index=False)
# print (asymmetry_analysis)

# Save the descriptive statistics and asymmetry analysis as CSV files
data_description.to_csv('data_description.csv')
asymmetry_analysis.to_csv('asymmetry_analysis.csv')
print("Preliminary data analysis saved as 'data_description.csv' and 'asymmetry_analysis.csv'.")


# Clean the 'Price' column
# Step 1: Replace 'PRIX NON SPÉCIFIÉ' with NaN
# data_frm['Price'] = data_frm['Price'].replace('PRIX NON SPÉCIFIÉ', np.nan)


# Step 2: Remove 'DH' and '/Nuit' (and any other non-numeric text)
# We use regex to extract only the numeric part of each entry.
# data_frm['Price'] = data_frm['Price'].str.extract(r'(\d+)', expand=False)

# Step 2: Remove ' DH' from each entry
# data_frm['Price'] = data_frm['Price'].str.replace('DH', '')


# Step 3: Convert 'Price' column to numeric
# data_frm['Price'] = pd.to_numeric(data_frm['Price'], errors='coerce')


# Save the cleaned data to a new CSV file
data_frm.to_csv('cleaned_data.csv', index=False)
print("Price column cleaned and saved as 'cleaned_data.csv'.")


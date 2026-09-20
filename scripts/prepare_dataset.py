import os
import pandas as pd
import numpy as np

# Set random seed for consistent results
np.random.seed(42)

print("--- Step 1: Generating Raw Business Dataset ---")

# Sample data pools
categories = {
    'Technology': ['Phones', 'Laptops', 'Accessories', 'Copiers'],
    'Furniture': ['Chairs', 'Tables', 'Bookcases', 'Furnishings'],
    'Office Supplies': ['Storage', 'Paper', 'Binders', 'Art', 'Appliances']
}

products = {
    'Phones': ['iPhone 15 Pro', 'Samsung Galaxy S24', 'Google Pixel 8', 'Motorola Edge'],
    'Laptops': ['MacBook Air M3', 'Dell XPS 13', 'Lenovo ThinkPad', 'HP Spectre'],
    'Accessories': ['Wireless Mouse', 'Mechanical Keyboard', 'USB-C Hub', 'Monitor Arm'],
    'Copiers': ['Canon ImageCLASS', 'Brother Laser Printer', 'Epson EcoTank'],
    'Chairs': ['Ergonomic Mesh Chair', 'Executive Leather Chair', 'Drafting Stool'],
    'Tables': ['Standing Desk 60in', 'Conference Table', 'Executive Wooden Desk'],
    'Bookcases': ['Oak 4-Shelf Bookcase', 'Metal Storage Shelf', 'Walnut Bookshelf'],
    'Furnishings': ['Desk Lamp', 'Anti-Fatigue Mat', 'Monitor Stand'],
    'Storage': ['Filing Cabinet 3-Drawer', 'Plastic Storage Bin', 'Desktop Organizer'],
    'Paper': ['Multipurpose Printer Paper', 'Cardstock Paper', 'Sticky Notes Pack'],
    'Binders': ['Heavy-Duty 3-Ring Binder', 'Presentation Folder', 'Zipper Binder'],
    'Art': ['Marker Set 24-Pack', 'Cutting Mat', 'Drafting Pens'],
    'Appliances': ['Compact Refrigerator', 'Coffee Maker', 'Air Purifier']
}

segments = ['Consumer', 'Corporate', 'Home Office']
regions = ['North', 'South', 'East', 'West']

# Generate 500 synthetic realistic transactions
data = []
date_range = pd.date_range(start='2025-01-01', end='2025-12-31', freq='D')

for i in range(1, 501):
    order_id = f"ORD-{1000 + i}"
    order_date = np.random.choice(date_range)
    cust_id = f"CUST-{np.random.randint(100, 150)}"
    segment = np.random.choice(segments, p=[0.5, 0.3, 0.2])
    region = np.random.choice(regions)
    
    cat = np.random.choice(list(categories.keys()))
    sub_cat = np.random.choice(categories[cat])
    prod_name = np.random.choice(products[sub_cat])
    
    quantity = np.random.randint(1, 10)
    unit_price = np.random.uniform(15.0, 800.0)
    sales = round(quantity * unit_price, 2)
    
    discount = np.random.choice([0.00, 0.05, 0.10, 0.15, 0.20], p=[0.5, 0.2, 0.15, 0.10, 0.05])
    discounted_sales = sales * (1 - discount)
    
    # Profit calculation with realistic variability
    margin = np.random.uniform(0.10, 0.35)
    profit = round((discounted_sales * margin) - (sales * discount * 0.5), 2)
    shipping_cost = round(np.random.uniform(3.0, 35.0), 2)
    
    data.append([
        order_id, order_date, cust_id, segment, region, cat, sub_cat,
        prod_name, quantity, sales, discount, profit, shipping_cost
    ])

df = pd.DataFrame(data, columns=[
    'Order_ID', 'Order_Date', 'Customer_ID', 'Segment', 'Region', 
    'Category', 'Sub_Category', 'Product_Name', 'Quantity', 
    'Sales', 'Discount', 'Profit', 'Shipping_Cost'
])

# Intentionally introduce minor realistic noise (1 duplicate row & 2 missing values for cleaning demonstration)
df = pd.concat([df, df.iloc[[10]]], ignore_index=True)  # Duplicate row
df.loc[15, 'Segment'] = np.nan  # Missing segment
df.loc[25, 'Shipping_Cost'] = np.nan  # Missing shipping cost

print(f"Raw Data Created! Total Rows: {len(df)}")

print("\n--- Step 2: Cleaning Data ---")

# 1. Handle Duplicate Rows
initial_count = len(df)
df = df.drop_duplicates()
print(f"Removed {initial_count - len(df)} duplicate row(s).")

# 2. Handle Missing Values
df['Segment'] = df['Segment'].fillna('Consumer')  # Default missing segment to 'Consumer'
df['Shipping_Cost'] = df['Shipping_Cost'].fillna(df['Shipping_Cost'].median())  # Fill missing cost with median
print("Handled missing values successfully.")

# 3. Format Dates (YYYY-MM-DD)
df['Order_Date'] = pd.to_datetime(df['Order_Date']).dt.strftime('%Y-%m-%d')
print("Formatted Order_Date column to YYYY-MM-DD format.")

# 4. Check & Validate Numerical Columns
df['Quantity'] = df['Quantity'].astype(int)
df['Sales'] = df['Sales'].round(2)
df['Discount'] = df['Discount'].round(2)
df['Profit'] = df['Profit'].round(2)
df['Shipping_Cost'] = df['Shipping_Cost'].round(2)

# Ensure no negative sales or quantity
assert (df['Sales'] >= 0).all(), "Validation Error: Found negative sales!"
assert (df['Quantity'] > 0).all(), "Validation Error: Found non-positive quantity!"
print("Numerical validation passed successfully (all sales >= 0, quantity > 0).")

print("\n--- Step 3: Dataset Summary ---")
print(f"Total Clean Records: {len(df)}")
print(f"Total Revenue Generated: ${df['Sales'].sum():,.2f}")
print(f"Total Profit Generated: ${df['Profit'].sum():,.2f}")

# Save clean CSV to the data directory
output_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'sales_data.csv')

df.to_csv(output_path, index=False)
print(f"\nFinal dataset saved successfully to: {os.path.abspath(output_path)}")
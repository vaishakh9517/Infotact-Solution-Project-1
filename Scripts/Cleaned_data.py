import pandas as pd;

#Loaded the dataset
file_path = "data/raw/Aster Retail Holdings.csv"
df = pd.read_csv(file_path)

#Initial Check up
print("File Loaded Successfully")
print("Shape of the file = ", df.shape)
print("First 5 rows", )
print(df.head())

# Define correct mapping of products to categories
mapping = {
    "Clothing": ["Jacket", "T-shirt", "Shoes"],
    "Accessories": ["Sunglasses", "Watch", "Headphones"],
    "Electronics": ["Tablet", "Smartphone", "Camera", "Laptop"]
}

# Create a reverse mapping (product -> category)
reverse_mapping = {product: category for category, products in mapping.items() for product in products}

# Apply correct category
df["correct_category"] = df["product_name"].map(reverse_mapping)

# Replacing the old 'Category' column with the corrected values
df["category"] = df["correct_category"]

# Removing the extra column now
df = df.drop(columns=["correct_category"])

#Cleaning
print(df["order_date"].dtype)
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
print(df["order_date"].dtype)

print("Missing values per column :")
print(df.isnull().sum())

df['sales'] = df['quantity'] * df['unit_price']

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print(df.head())

duplicate_customer= df['customer_id'].duplicated().sum()
print("Total Duplicate Customer IDs : ", duplicate_customer)
duplicate_product= df['product_id'].duplicated().sum()
print("Total Duplicate Product IDs : ", duplicate_product)
duplicate_order= df['order_id'].duplicated().sum()
print("Total Duplicate Order IDs : ", duplicate_order)
#Not removing duplicates as customers and products could be repeated

#Checking the data type
print("Data types : ", df.dtypes)

#Saving the cleaned data
output_path = 'data/cleaned/Aster Retail Holdings Cleaned.csv'
df.to_csv(output_path, index= False)
print("\nData cleaned and saved successfully to:", output_path)

output_path = 'data/cleaned/Aster Retail Holdings (Excel).xlsx'
df.to_excel(output_path, index= False)
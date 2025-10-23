import pandas as pd;

#Loaded the dataset
file_path = "data/raw/Aster Retail Holdings.csv"
df = pd.read_csv(file_path)

#Initial Check up
print("File Loaded Successfully")
print("Shape of the file = ", df.shape)
print("First 5 rows", )
print(df.head())


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
#Not removing duplicates as customers and products could be repeated

#Checking the data type
print("Data types : ", df.dtypes)

#Saving the cleaned data
output_path = 'data/cleaned/Aster Retail Holdings Cleaned.csv'
df.to_csv(output_path, index= False)
print("\n✅ Data cleaned and saved successfully to:", output_path)

output_path = 'Pivot.xlsx'
df.to_excel(output_path, index= False)
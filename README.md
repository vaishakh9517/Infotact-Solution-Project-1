# Aster-Retail-Holdings-Sales-Data-Analytics

This repository presents an end-to-end retail sales data analytics project for Aster Retail Holdings (London), covering the complete workflow from raw data cleaning and transformation using Python to EDA in Excel and interactive dashboarding in Power BI.

The project simulates a real-world business analytics engagement, transforming unstructured sales data into actionable commercial insights for the year 2022 using industry-standard tools and best practices.

📁 Project Structure

/Aster-Retail-Holdings-Sales-Data-Analytics/
│
├── data/
│ ├── raw/
│ │ └── Aster Retail Holdings.csv
│ └── cleaned/
│ ├── Aster Retail Holdings Cleaned.csv
│ └── Aster Retail Holdings (Excel).xlsx
│
├── python/
│ └── data_cleaning_transformation.py
│
├── power_bi/
│ └── Aster_Retail_Sales_Dashboard.pbix
│
├── reports/
│ └── Aster_Retail_Holdings_Report_Vaishakh_K.pdf
│
└── README.md

📊 Project Overview
🔍 Objective

To perform a complete end-to-end sales data analysis by ensuring data accuracy, conducting exploratory analysis, defining KPIs, and delivering business-ready dashboards for decision-making.

🧮 Data Summary

Source: Retail sales CSV dataset (2022)

Key Fields:

order_date

customer_id

product_id

product_name

category

quantity

unit_price

sales (derived)

region / country

🛠️ Tools & Technologies

Python (pandas, openpyxl) – Data cleaning & transformation

Microsoft Excel – Exploratory Data Analysis (Pivot Tables)

Power BI – Interactive dashboards & DAX measures

Git & GitHub – Version control & documentation

🧹 Data Cleaning & Transformation (Python)
Methodology

Loaded and validated raw CSV data using pandas.

Standardized column naming conventions (lowercase, underscores).

Converted order_date to proper datetime format with error handling.

Checked for missing values and verified duplicates (customers, products, orders).

Corrected product-category mismatches using dictionary-based reverse mapping.

Created a derived sales column (quantity × unit_price) for revenue analysis.

Exported cleaned datasets to CSV and Excel formats for downstream analysis.

📈 Exploratory Data Analysis (Excel)
Key Analysis Performed

Sales by Category

Monthly Sales Trends

Sales by Country & Category

KPI identification using Pivot Tables and slicers

High-Level Insights

Electronics emerged as the top revenue-generating category (~40% of total sales).

August recorded the highest monthly sales, indicating seasonal demand.

Sales remained stable across Q2–Q3, supporting predictable revenue patterns.

📊 Power BI Dashboard & Insights
Dashboard Features

Category-wise sales distribution

Monthly sales trends

Regional sales performance (map visuals)

KPI cards: Total Sales, AOV, Quantity, Distinct Customers

Interactive slicers and drill-through filters

Business Insights

USA and Canada were the strongest markets, contributing over one-third of total revenue.

France underperformed, highlighting opportunities for targeted marketing.

Premium products (e.g., Watches, Jackets) showed high revenue with lower volumes, indicating strong margins.

Clear seasonal patterns observed, supporting inventory and demand planning.

✅ Skills Demonstrated

Data Cleaning & Data Quality Assurance

Python (pandas) for ETL

Excel Pivot Tables & EDA

Power BI Dashboarding & DAX

KPI Definition & Business Storytelling

GitHub Documentation & Version Control

📌 Conclusion

This project demonstrates the ability to translate raw retail data into business-ready insights using a structured analytics workflow:

Python ensured clean, reliable, analysis-ready data

Excel uncovered early trends and KPIs

Power BI enabled executive-level decision-making through visual storytelling

The analysis highlights revenue drivers, seasonal trends, regional dependencies, and product performance, offering actionable insights for sales optimization and strategic planning.

📎 License

This project is intended for educational and portfolio purposes only.

## 🙋‍♂️ About Me

**Vaishakh K**  
Data Analyst | Excel | MySQL | Python | Tableau | Power BI
[LinkedIn](https://www.linkedin.com/in/vaishakh-k-0b2bb8202/) • [Portfolio](https://github.com/vaishakh9517)


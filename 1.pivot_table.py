# Import the pandas library, which provides data structures and data analysis tools
import pandas as pd

# Read data from an Excel file named 'supermarket_sales.xlsx' into a DataFrame
df = pd.read_excel('supermarket_sales.xlsx')

# Select only the 'Gender', 'Product line', and 'Total' columns from the DataFrame
df = df[['Gender', 'Product line', 'Total']]

# Print the DataFrame to check the selected columns (currently commented out)
# print(df)

# Create a pivot table to summarize the total sales for each product line by gender
# - 'index' specifies 'Gender' as the row index of the pivot table
# - 'columns' specifies 'Product line' as the columns of the pivot table
# - 'values' specifies 'Total' as the data to aggregate
# - 'aggfunc' specifies the aggregation function, 'sum' in this case
# - 'round(0)' rounds the values in the pivot table to 0 decimal places
pivot_table = df.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum').round(0)

# Export the pivot table to a new Excel file named 'pivot_table.xlsx'
# - 'Report' specifies the sheet name where the data will be saved
# - 'startrow=4' places the pivot table starting from row 5 in the Excel sheet
pivot_table.to_excel('pivot_table.xlsx', sheet_name='Report', startrow=4)

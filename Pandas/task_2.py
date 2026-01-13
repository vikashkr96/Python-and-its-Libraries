import pandas as pd

# Sample dataset
data = {
    'Transaction_ID': [1, 2, 3],
    'Date': ['2023-08-01', '2023-08-02', '2023-08-03'],
    'Product': ['Product A', 'Product B', 'Product C'],
    'Quantity': [5, 10, 2],
    'Price_per_Unit': [100, 50, 200]
}

# Creating a pandas DataFrame
df = pd.DataFrame(data)

# Defining the function to calculate total revenue
def calculate_total_revenue(df):
    df['Total_Price'] = df['Quantity'] * df['Price_per_Unit']
    total_revenue = df['Total_Price'].sum()
    return total_revenue

# Calculating the total revenue
total_revenue = calculate_total_revenue(df)
print(f"The total revenue is: {total_revenue}")

### Output is 1400



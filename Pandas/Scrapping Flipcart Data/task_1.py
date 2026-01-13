# importing pandas lybrary as its alias pd...
import pandas as pd 

# The given dataset is :-

data = {
    'Transaction_ID': [1, 2, 3, 4, 5],
    'Product': ['A', 'B', 'A', 'C', 'B'],
    'Quantity': [10, 5, 2, 8, 7],
    'Price_per_Unit': [100, 200, 100, 300, 200]
}

# Creating dataframe of the dataset given ....

df = pd.DataFrame(data)

# now creating a function to calculate the average revenue per transaction...

def calculate_average_revenue(df):
    df['Revenue'] = df['Quantity'] * df['Price_per_Unit']
    average_revenue = df['Revenue'].mean()
    return average_revenue

# Finally  printing the average revenue per transaction
average_revenue = calculate_average_revenue(df)
print(average_revenue)



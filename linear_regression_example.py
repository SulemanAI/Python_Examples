import pandas as pd
# Load a dataset of house prices
data = {'Size':[1200,1500,1800,2000],
        'Bedrooms':[3,4,4,5],
        'Price':[300000,350000,400000,450000]}

df = pd.DataFrame(data)

# Displaying the dataset
print(df)

# Filter houses with more than 3 bedrooms
filtered_df = df[df['Bedrooms']>3]
print(f"\nHouses with more than 3 bedrooms.")
print(filtered_df)

# Calculate the average price of houses
average_price = df['Price'].mean()
print("\nAverage House Price:", average_price)

# Houses with more than 3 bedrooms.
#    Size  Bedrooms   Price
# 1  1500         4  350000
# 2  1800         4  400000
# 3  2000         5  450000
#
# Average House Price: 375000.0

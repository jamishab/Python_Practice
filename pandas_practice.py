import pandas as pd

coffee_data = {
    "Drink": ["Latte", "Cappuccino", "Espresso", "Americano", "Mocha"],
    "Price": [4.50, 4.25, 3.00, 3.50, 5.00],
    "Caffeine_mg": [150, 150, 63, 120, 175],
    "In_Stock": [True, True, True, False, True]
}

coffee_df = pd.DataFrame(coffee_data)

print(coffee_df)

print("\n", coffee_df.head(2))  # Display the first 2 rows of the DataFrame
print("\n", coffee_df.describe())  # Display summary statistics for numerical columns

# Specify row labels
coffee_df.index = ['a', 'b', 'c', 'd', 'e']
print("\n", coffee_df)
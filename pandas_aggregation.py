import pandas as pd
import numpy as np


orders = pd.read_csv('/Volumes/Bhumika/Work/Data Engineer/Python/orders.csv')
print(orders.head(10))

# Price of the Most expensive pair of shoes pucrchased
most_expensive = orders.price.max()
print("Most Expensive pair of shoes:",most_expensive)

# how many different colors of shoes we are selling
num_colors = orders.shoe_color.nunique()
print("number of different colors of shoes:",num_colors)

# most expensive shoe for each shoe_type
pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()
print(pricey_shoes)
print(type(pricey_shoes))

# calculate the 25th percentile for shoe price for each shoe_color
cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x, 25)).reset_index()
print(cheap_shoes)

# total number of shoes of each shoe_type/shoe_color combination purchased.
shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()
print(shoe_counts)

# Pivot View
shoe_counts_pivot = shoe_counts.pivot(columns='shoe_color', index='shoe_type', values='id').reset_index()
print(shoe_counts_pivot)
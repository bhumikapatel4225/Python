import pandas as pd

user_visits = pd.read_csv('/Volumes/Bhumika/Work/Data Engineer/Python/page_visits.csv')

# how many visits came from each of different sources
click_source = user_visits.groupby('utm_source').id.count().reset_index()
print(click_source)

# number of visits to site from each utm_source for each month
click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_index()
print(click_source_by_month)
# Pivot view
click_source_by_month_pivot = click_source_by_month.pivot(columns='month',
                                                          index='utm_source',
                                                          values='id').reset_index()
print(click_source_by_month_pivot)
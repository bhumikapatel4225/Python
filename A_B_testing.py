import pandas as pd

ad_clicks = pd.read_csv('/Volumes/Bhumika/Work/Data Engineer/Python/ad_clicks.csv')

# How many views (i.e., rows of the table) came from each utm_source
click_source = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(click_source)

# Add new column 'is_click'
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull() # ~ is NOT operator
# percent of people who clicked on ads from each utm_source
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
clicks_pivot = clicks_by_source.pivot(
    columns='is_click', 
    index='utm_source', 
    values='user_id'
    ).reset_index()
# Add new column in pivot view
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True]+clicks_pivot[False])
print(clicks_pivot)

experimental_users = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
experimental_users_pivot = experimental_users.pivot(
    columns='is_click', 
    index='experimental_group', 
    values='user_id'
    ).reset_index()
print(experimental_users_pivot)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
a_clicks_pivot = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(
    index='day', 
    columns='is_click', 
    values='user_id'
    ).reset_index()
a_clicks_pivot['percent_clicked'] = a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False])
print(a_clicks_pivot)

b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
b_clicks_pivot = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(
    index='day', 
    columns='is_click', 
    values='user_id'
    ).reset_index()
b_clicks_pivot['percent_clicked'] = b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False])
print(b_clicks_pivot)
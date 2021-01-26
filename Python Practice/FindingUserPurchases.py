# Practice problem from stratascratch.com
# Write a query that'll identify returning active users. 
# A returning active user is a user that has made a second purchase within 7 days of their first purchase.
## Output a list of user_ids of these returning active users.

## Data contains
# id (int64)
# user_id (int64)
# item (object)
# created_at (object)
# revenue (int64)


# Import your libraries
import pandas as pd
import numpy as np
from datetime import datetime


# Start writing code
amazon_transactions.head()

# convert the created_at column to datetime format
amazon_transactions["created_at"]= pd.to_datetime(amazon_transactions["created_at"]).dt.strftime('%m-%d-%Y')

# define the dataframe, sorting by user ID and creation date (ascending to do the subtraction)
df = amazon_transactions.sort_values(by = ['user_id', 'created_at'], ascending = [True,True])

# define prev_value column, lag for each user
df['prev_value'] = df.groupby('user_id')['created_at'].shift().fillna(0)

# define a second dataframe and get the 2nd purchase for each user
df1 = df.sort_values(by = ['user_id', 'created_at'], ascending = True).groupby('user_id').nth(1).reset_index() 

# calculating the difference between the dates for the second and first purchase
df1['created_at'] = pd.to_datetime(df1['created_at'], format='%m-%d-%Y')
df1['prev_value'] = pd.to_datetime(df1['prev_value'], format='%m-%d-%Y')
df1['days'] = (df1['created_at'] - df1['prev_value']).dt.days

# filter number of days for users' returns
df2 = df1[df1['days']<=7]

# output the resulting list of users
result = df2['user_id']

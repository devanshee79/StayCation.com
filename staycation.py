#!/usr/bin/env python
# coding: utf-8

# # Imporrting Files
# 

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


Listing = pd.read_csv(r'F:\Analyst projects\StayCationcom\listing.csv')
price = pd.read_csv(r'F:\Analyst projects\StayCationcom\price.csv')
reviews = pd.read_csv(r'F:\Analyst projects\StayCationcom\reviews.csv')
Listing.head()
price.head()
reviews.head()


# In[4]:


Listing.describe()
Listing = Listing.drop_duplicates()


# In[5]:


Listing.isnull().sum()


# In[6]:


Listing["HOST_NAME"] = Listing["HOST_NAME"].str.replace('[^a-zA-Z]','')
Listing["HOST_NAME"].head(10)


# In[15]:


Earning = {}

for List_id in Listing['LISTING_ID']:
    Earning[List_id] = 0

for ind,row in price.iterrows():
    if row['AVAILABLE']:
#         print(Earning[row['LISTING_ID']]+row['DAILY_PRICE'])
        Earning[row['LISTING_ID']] = Earning[row['LISTING_ID']]+row['DAILY_PRICE']
Earning


# In[19]:


Relation = {}
Earning_HostID = {}

# Creating a dictionary to relate LISTING_ID to HOST_ID
for index, row in Listing.iterrows():
    Relation[row['LISTING_ID']] = row['HOST_ID']

# Initializing Earning_HostID with 0 for each HOST_ID
for host_id in set(Relation.values()):
    Earning_HostID[host_id] = 0

# Calculating earnings for each host
for listing_id, earning in Earning.items():
    host_id = Relation.get(listing_id)
    Earning_HostID[host_id] += earning

Earning_HostID


# In[20]:


# Creating DataFrame from the dictionary
earning_df = pd.DataFrame({'HOST_ID': list(Earning_HostID.keys()), 'Earnings': list(Earning_HostID.values())})

# Displaying the DataFrame as a table
print(earning_df)


# In[22]:


csv_file_path = 'F:\Analyst projects\StayCationcom\earning_data.csv'

earning_df.to_csv(csv_file_path, index=False) 
print(f"CSV file '{csv_file_path}' has been created.")


# In[24]:


earning_df = pd.DataFrame(list(Earning.items()), columns=['LISTING_ID', 'Earning'])

merged_df = Listing.merge(earning_df, on='LISTING_ID', how='left')
merged_df['Earning'].fillna(0, inplace=True)

Listing = merged_df
print(Listing)


# In[26]:


csv_file_path = 'F:\Analyst projects\StayCationcom\Listing_updated.csv'

Listing.to_csv(csv_file_path, index=False)  
print(f"CSV file '{csv_file_path}' has been created.")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[2]:


# importing packages
import pandas as pd
import s3fs
from datetime import datetime
import tweepy


# In[6]:


# Extracting data from twitter api
#setting keys
access_key="RlpkZI3B0ClQH1nKBkAVyEsJw"
access_secret_key="QrkG3YXhWTWntXtlMJSXl0Xo90hqKHF6QCY7L4aq59V9Zqne6f"
consumer_key="1729812541402959873-ZYacgn4mNRfqO9KQIBrF5ccilBNSN7"
consumer_secret_key="1gGvJCclSaVoQ8loa8Cc8pWXgkcYWHDptxLjic11EEYS4"

#authication
auth=tweepy.OAuthHandler(access_key,access_secret_key)
auth.set_access_token(consumer_key,consumer_secret_key)

#creating API object
api=tweepy.API(auth)

#fetching tweets
tweets=api.user_timeline(screen_name='@elonmusk',
                         #maximum allowed count
                        count=20,
                         #including retweet
                        include_rts=False,
                         #get full text, by default limit is 140 charcaters.
                        tweet_mode='extended')

print(tweets)


# In[ ]:


# storing it in database or s3 bucket


# In[ ]:





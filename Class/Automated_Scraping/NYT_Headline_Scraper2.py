
# coding: utf-8

# In[35]:

import requests
from bs4 import BeautifulSoup


# In[36]:

#Grab the NYT homepage
response = requests.get("http://nytimes.com")


# In[37]:

#Feed it into BeautifulSoup
doc = BeautifulSoup(response.text, 'html.parser')


# In[38]:

#Get out the headlines
stories = doc.find_all('article', {'class': 'story'})
len(stories)


# In[39]:

for story in stories:
    headline = story.find('h2', {'class': 'story-heading'})
    if headline:
        headline_text = headline.text.strip()
        byline = story.find('p', {'class': 'byline'})
        if byline:
            byline_text = byline.text.strip()


# In[40]:

#Save the headlines and bylines to a timestamp CSV
#Turning it into Pandas, and making a list of dictionaries


# In[41]:

all_stories = []

for story in stories:
    headline = story.find('h2', {'class': 'story-heading'})
    if headline:
        headline_text = headline.text.strip()
        this_story = {'headline': headline_text}
        byline = story.find('p', {'class': 'byline'})
        if byline:
            byline_text = byline.text.strip()
            this_story['byline'] = byline_text
        all_stories.append(this_story)


# In[42]:

import pandas as pd


# In[43]:

stories_df = pd.DataFrame(all_stories)
stories_df.head(10)


# In[44]:

stories_df.to_csv("nyt-data.csv")


# In[45]:

#we want "nyt-data-2016-06-20.csv"
#we will use "nyt-data`date + "%Y-%m-%d`.csv", but this doesn't work

import time


# In[46]:

datestring = time.strftime('%Y-%m-%d-%I-%m-%p')
datestring


# In[47]:

filename = "nyt-data-" + datestring + ".csv"
stories_df.to_csv(filename)


# In[ ]:




# In[ ]:




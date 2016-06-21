
# coding: utf-8

# In[2]:

#get_ipython().system('pip install bs4')


# In[4]:

import requests
from bs4 import BeautifulSoup


# In[5]:

#Grab the NYT homepage
response = requests.get("http://nytimes.com")


# In[6]:

#Feed it into BeautifulSoup
doc = BeautifulSoup(response.text, 'html.parser')


# In[10]:

#Get out the headlines
stories = doc.find_all('article', {'class': 'story'})
len(stories)


# In[17]:

for story in stories:
    headline = story.find('h2', {'class': 'story-heading'})
    if headline:
        headline_text = headline.text.strip()
        byline = story.find('p', {'class': 'byline'})
        if byline:
            byline_text = byline.text.strip()


# In[ ]:

#Save the headlines and bylines to a timestamp CSV
#Turning it into Pandas, and making a list of dictionaries


# In[23]:

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


# In[24]:

import pandas as pd


# In[27]:

stories_df = pd.DataFrame(all_stories)
stories_df.head(10)


# In[28]:

stories_df.to_csv("nyt-data.csv")


# In[29]:

#we want "nyt-data-2016-06-20.csv"
#we will use "nyt-data`date + "%Y-%m-%d`.csv", but this doesn't work

import time


# In[33]:

datestring = time.strftime('%Y-%m-%d-%I-%m-%p')
datestring


# In[34]:

filename = "nyt-data-" + datestring + ".csv"
stories_df.to_csv(filename)


# In[ ]:


# coding: utf-8

# In[3]:

import requests
from bs4 import BeautifulSoup


# In[11]:

# Grab the NYT homepage
response = requests.get("http://www.nytimes.com")


# In[12]:

# Feed it into BeautifulSoup
doc = BeautifulSoup(response.text, 'html.parser')


# In[13]:

# Get out the stories
stories = doc.find_all("article", { 'class': 'story' })
len(stories)


# In[25]:

all_stories = []
# Grab their headlines and bylines
for story in stories:
    # Grab all of the h2's inside of the story
    headline = story.find('h2', {'class': 'story-heading'})
    # If a headline exists, then process the rest!
    if headline:
        # They're COVERED in whitespace
        headline_text = headline.text.strip()
        # Make a dictionary with the headline
        this_story = { 'headline': headline_text }
        byline = story.find('p', {'class': 'byline'})
        # Not all of them have a byline
        if byline:
            byline_text = byline.text.strip()
            this_story['byline'] = byline_text
        all_stories.append(this_story)


# In[32]:

all_stories


# In[33]:

len(all_stories)


# In[34]:

import pandas as pd


# In[36]:

# Convert the headlines and bylines into a pandas DataFrame
stories_df = pd.DataFrame(all_stories)
stories_df.head(2)


# In[38]:

stories_df.to_csv("nyt-data.csv")


# In[39]:

# We want "nyt-data-2016-06-20.csv"
# We will use "nyt-data`date +"%Y-%m-%d`.csv"
import time


# In[43]:

datestring = time.strftime("%Y-%m-%d-%H-%M")
datestring


# In[45]:

filename = "nyt-data-" + datestring + ".csv"
stories_df.to_csv(filename, index=False)


# In[ ]:




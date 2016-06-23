
# coding: utf-8

# In[1]:

import requests
from bs4 import BeautifulSoup


# In[2]:

# Grab the Reddit Homepage
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get("http://www.reddit.com", headers=headers)


# In[3]:

#Feed it into BeautifulSoup
reddit = BeautifulSoup(response.text, 'html.parser')


# In[4]:

#reddit


# In[5]:

one_sibling_up = reddit.find_all('div', {'class': 'clearleft'})


# In[6]:

#because only every other clearleft has a post in it:
posts = [tag.find_next_sibling('div') for tag in one_sibling_up if tag.find_next_sibling('div')]


# In[7]:

#Function to change the votes into int
def vote_count_int(x):
    if x == '•':
        return 0
    else:
        return int(x)


# In[8]:

all_stories = []
for article in posts:
    #subreddit
    if article.find("a", {'class': 'subreddit hover may-blank' }) is None:
        break
    else:
        article_subreddit = article.find("a", {'class': 'subreddit hover may-blank' })
    #title
    if article.find("a", {'class': 'title may-blank ' }) is None:
        break
    else:
        article_title = article.find("a", {'class': 'title may-blank ' }) 
    #time
    if article.find("time", {'class' : 'live-timestamp'}) is None:  
        break
    else:
        time = article.find("time", {'class' : 'live-timestamp'}).get('datetime')
    #URL
    if article.find("a", {'class': 'title may-blank ' }) is None:
        break
    else: 
        article_URL = article.find("a", {'class': 'title may-blank ' }).get('href')
    #Thumbnails
    #if article.find('img') is None:
    #    posts.remove(article)
    #else:
    #    image_url = article.find('img')
    #    if image_url:
    #        thumbnail = image_url.get('src')
    #votes
    if article.find("div", {'class': 'score unvoted' }) is None:
        break
    else:
        article_score = article.find("div", {'class': 'score unvoted' })
    #Dictionary
    article_subreddit_dict = {'subreddit': article_subreddit.string, 'title': article_title.string,                               'time': time, 'URL': article_URL,                               'votes': vote_count_int(article_score.string)} 
    #Dict List
    all_stories.append(article_subreddit_dict)


# In[9]:

all_stories


# In[10]:

import pandas as pd


# In[11]:

#convert to Pandas


# In[12]:

#date string import


# In[13]:

stories_df = pd.DataFrame(all_stories)
stories_df.head(2)


# In[14]:

import time


# In[15]:

datestring = time.strftime("%m-%h-%d")
datestring


# In[16]:

#creating .csv file


# In[17]:

filename = "reddit-frontpage-" + datestring + ".csv"
stories_df.to_csv(filename, index=False)


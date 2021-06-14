#!/usr/bin/env python
# coding: utf-8
# jupyter nbconvert --to script mission_to_mars.ipynb

# pip installa flask

# In[44]:


# Import dependencies
# pip install webdriver-manager
# pip install splinter

import pandas as pd
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
from selenium import webdriver

# driver = webdriver.Chrome(ChromeDriverManager().install())


# In[119]:


# Setup splinter

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[46]:


# Enter url to visit

url = 'https://redplanetscience.com/'
browser.visit(url)


# In[47]:


# Creating beautiful soup

html = browser.html
soup = bs(html,'html.parser')


# NASA Mars News

# In[48]:


# Scrapping news
news_title = soup.find('div',class_='content_title').text
news_p = soup.find('div', class_='article_teaser_body').text
print(f'Title: **{news_title}**')
print(f'Paragraph: {news_p}')


# JPL Mars Space Images - Featured Image

# In[49]:


# URL2 https://spaceimages-mars.com/

# Enter url to visit

url2 = 'https://spaceimages-mars.com/'
browser.visit(url2)


# In[56]:


# Creating beautiful soup

# Question: html always has to be called html?

html = browser.html
soup2 = bs(html, 'html.parser')


# In[57]:


# Scrap and print featured image

url3 = url2 + soup.find('img', class_='headerimage')['src']

print(url3)


# Mars Facts

# In[67]:


# Enter url to visit
# URL4: https://galaxyfacts-mars.com/

url4 = 'https://galaxyfacts-mars.com/'
browser.visit(url4)


# In[88]:


# Scrape the table containing facts about the planet including Diameter, Mass, etc.
# Use Pandas to convert the data to a HTML table string

facts = pd.read_html(url4)
mars_df = facts[0]
mars_df.columns = mars_df.iloc[0]
mars_df = mars_df.drop(0)
mars_df = mars_df.set_index(['Mars - Earth Comparison'])
mars_df


# Mars Hemispheres

# In[123]:


# Enter url to visit
# URL5: https://marshemispheres.com/

url5 = 'https://marshemispheres.com/'
browser.visit(url5)


# In[124]:


# Creating beautiful soup

html = browser.html
soup = bs(html, 'html.parser')


# In[125]:


# Set empty list
hemisphere_image_urls = []

# Variable with list of hemispheres
hemispheres = soup.find_all("div", class_="item")

# Loop

for hemisphere in hemispheres:
    
    # Create dictionary
    temp_dict = {}
    
    # Find and store titles
    title = hemisphere.find("h3").text
    
    hemispheres_img = hemisphere.find("a", class_="itemLink product-item")["href"]
    
    # Visit the link that contains the full image website 
    browser.visit(url5 + hemispheres_img)
    
    # HTML Object
    html = browser.html
    soup = bs(html, "html.parser")
    
    # Create full image url
    img_url = url5 + soup.find("img", class_="wide-image")["src"]
    
    # Create temporary dictionary and store temporary info
    temp_dict = {'title': title, 'img_url': img_url}
    
    # Append titles and images to a list
    hemisphere_image_urls.append(temp_dict)
    
hemisphere_image_urls


# In[ ]:





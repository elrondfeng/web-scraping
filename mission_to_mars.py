
# coding: utf-8

# In[52]:


from bs4 import BeautifulSoup
import requests
from splinter import Browser
import time
import pandas as pd


# In[53]:


executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[54]:


# NASA Mars News


# In[55]:


url = 'https://mars.nasa.gov/news/'


# In[56]:


browser.visit(url)


# In[60]:


html = browser.html


# In[61]:


soup = BeautifulSoup(html, 'html.parser')


# In[62]:


news_title = soup.find('div',class_="content_title").text
print(news_title)


# In[63]:


news_p = soup.find_all('div',class_="article_teaser_body")[0].text
print(news_p)


# In[64]:


# JPL Mars Space Images - Featured Image


# In[65]:


url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'


# In[66]:


browser.visit(url)


# In[67]:


html = browser.html


# In[68]:


soup = BeautifulSoup(html, 'html.parser')


# In[69]:


src = soup.find('div',class_="image_and_description_container").find('div',class_='img').find('img')['src']
print(src)


# In[70]:


featured_image_url = 'https://www.jpl.nasa.gov' + src
print(featured_image_url)


# In[71]:


# Mars Weather


# In[72]:


url = 'https://twitter.com/marswxreport?lang=en'


# In[73]:


browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[74]:


mars_weather = soup.find('div',class_="js-tweet-text-container").find('p').text
print(mars_weather)


# In[75]:


# mars facts 


# In[76]:



url = 'http://space-facts.com/mars/'
tables = pd.read_html(url)
print(tables)


# In[77]:


# Mars Hemisperes


# In[78]:


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


# In[79]:


browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
items = soup.find_all('div',class_='item')

hemisphere_image_urls = []

# wait for 10 seconds 
#time.sleep(10)

for item in items:
    linked_text = item.find('h3').text
    print(linked_text)
    dic = {}
    dic["title"] = linked_text
    browser.click_link_by_partial_text(linked_text)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    pic_url = soup.find('div',class_='downloads')
    href = pic_url.find('li').find('a').get('href')
    print(href)
    dic["img_url"] = href
    
    hemisphere_image_urls.append(dic)
    
    browser.visit(url)



# In[80]:


for item in hemisphere_image_urls:
    print(item['title'])
    print(item['img_url'])


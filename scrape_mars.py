from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd

executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


def scrape():

    print("#####  start to scrape ###### ")

    results = {}

    #
    url = 'https://mars.nasa.gov/news/'

    browser.visit(url)

    html = browser.html

    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find('div', class_="content_title").text
    print(news_title)

    results['news_title'] = news_title

    news_p = soup.find('div', class_="article_teaser_body").text
    print(news_p)

    results['news_p'] = news_p

    #
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    browser.visit(url)

    html = browser.html

    soup = BeautifulSoup(html, 'html.parser')

    src = soup.find('div', class_="image_and_description_container").find('div', class_='img').find('img')['src']
    print(src)

    featured_image_url = 'https://www.jpl.nasa.gov' + src
    print(featured_image_url)

    results['featured_image_url'] = featured_image_url

    #
    url = 'https://twitter.com/marswxreport?lang=en'

    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_weather = soup.find('div', class_="js-tweet-text-container").find('p').text
    print(mars_weather)
    results['mars_weather'] = mars_weather

    #
    url = 'http://space-facts.com/mars/'
    tables = pd.read_html(url,header=0, index_col=0)
    print(tables[0])

    results['tables'] = tables[0].to_json(orient="records", date_format="iso")

    #
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='item')

    hemisphere_image_urls = []

    for item in items:
        linked_text = item.find('h3').text
        print(linked_text)
        dic = {}
        dic["title"] = linked_text
        browser.click_link_by_partial_text(linked_text)

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        pic_url = soup.find('div', class_='downloads')
        href = pic_url.find('li').find('a').get('href')
        print(href)
        dic["img_url"] = href

        hemisphere_image_urls.append(dic)

        browser.visit(url)

    for item in hemisphere_image_urls:
        print(item['title'])
        print(item['img_url'])

    results['hemisphere_image_urls'] = hemisphere_image_urls
    return results

    
if __name__ == "__main__":
    scrape()
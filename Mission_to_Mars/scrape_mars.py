# Import dependency
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd

# Setup browser
def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    
    browser = init_browser()

# Scrapping urls and create an output dictionary

def scrap():
    
    # Make a dict to store all of the scraped data
    mars_data = {}
    
# Visit each website and get mars data
    
# NASA Mars News       
def mars_news():
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    soup = bs(browser.html, 'html.parser')
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text
    
    # mars_news = [news_title, news_p]
    # return mars_news

    # Add to dict
    mars_data['news_title'] = news_title
    mars_data['news_content'] = news_p

### JPL Mars Space Images - Featured Image
def mars_image():
    mars_img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    base_url = 'https://www.jpl.nasa.gov'
    browser.visit(mars_img_url)
    browser.click_link_by_partial_text('FULL IMAGE')
    browser.click_link_by_partial_text('more info')
    soup = bs(browser.html, 'html.parser')
    img_url = soup.find('figure', class_='lede').a['href']
    featured_image_url = base_url + img_url
    return featured_image_url

    # Add to dict
    mars_data['featured_image'] = featured_image_url
    
### Mars Weather
def mars_weather():
    mars_wx_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_wx_url)
    soup = bs(browser.html, 'html.parser')
    mars_weather = soup.find('p',class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text.strip()
    return mars_weather

    # Add to dict
    mars_data['mars_weather'] = mars_weather

### Mars Facts
def mars_facts():
    mars_facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(mars_facts_url)
    df = tables[0]
    mars_facts = df.to_html(index=False)
    return mars_facts

    # Add to dictt
    mars_data['html_table'] = mars_facts

### Mars Hemisphere
def mars_hemisphere():
    mars_hemi_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    base_url = 'https://www.jpl.nasa.gov'
    browser.visit(mars_hemi_url)
    soup = bs(browser.html, 'html.parser')
    thumb_imgs = soup.find_all('div', class_='item')
    mars_hemi_urls = []
    for i in thumb_imgs:
        browser = init_browser()
        base_url = 'https://astrogeology.usgs.gov'
        title = (i.find('h3').text ).replace(' Enhanced','')
        part_img_url = i.find('a', class_='itemLink product-item')['href']
        browser.visit(base_url + part_img_url)
        soup = bs(browser.html, 'html.parser')
        img_url = base_url + soup.find('img', class_='wide-image')['src']
        mars_hemi_urls.append({"title" : title, "img_url" : img_url})
    return mars_hemi_urls

    # Close the browser after scraping
    browser.quit()

    #add to dict
    mars_data['hemisphere_image'] = mars_hemi_urls

    # Return results
    return mars_data

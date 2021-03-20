# Import dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time 
import requests
import pandas as pd

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()

    # Assign URL and visit with browser
    url= "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    time.sleep(1)

    # Create an HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')
    # Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. Assign the text to variables.
    news_title = soup.find_all("div", class_="content_title")[1].text

    # Find and print first paragraph
    news_p = soup.find("div", class_="article_teaser_body").text
    time.sleep(1)

    # Load URL for image and visit using splinter 
    image_url= "https://www.jpl.nasa.gov/images?search=&category=Mars"
    browser.visit(image_url)
    
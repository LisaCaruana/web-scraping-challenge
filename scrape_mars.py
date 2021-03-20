# Import dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time 
import requests# Import dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time 
import requests
import pandas as pd

# Establish a path with Chrome Driver and create browser
executable_path={'executable_path': ChromeDriverManager().install()}
browser=Browser('chrome', **executable_path, headless=False)

# Assign URL and visit with browser
url= "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
browser.visit(url)

# Create an HTML object
html = browser.html

# Parse HTML with Beautiful Soup
soup = bs(html, 'html.parser')

#Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
news_title = soup.find_all("div", class_="content_title")[1].text

# Find and print first paragraph
news_p = soup.find("div", class_="article_teaser_body").text

# Load URL for image and visit using splinter 
image_url= "https://www.jpl.nasa.gov/images?search=&category=Mars"
browser.visit(image_url)
time.sleep(1)
browser.find_by_css('.mb-3').click()
html = browser.html
# Parse HTML with Beautiful Soup
soup = bs(html, 'html.parser')
In [132]:
# Locate image using splinter, assign to a variable, and save and print complete URL
featured_img= soup.find("img", class_="BaseImage")
featured_img_url= featured_img['data-src']
print(f"Featured_image_url: {featured_img_url}")
Featured_image_url: https://d2pn8kiwq2w21t.cloudfront.net/images/jpegPIA24505.2e16d0ba.fill-400x400-c50.jpg
In [133]:
### Mars Facts
In [134]:
#Visit the Mars Facts webpage [here](https://space-facts.com/mars/) 
#and use Pandas to scrape the table containing facts about the planet 
#including Diameter, Mass, etc.
facts_url= "https://space-facts.com/mars/"
browser.visit(facts_url)
In [135]:
# Read table on webpage using Pandas and assign to variable name
mars_facts=pd.read_html(facts_url)
#mars_facts
# mars_facts
# type(mars_facts)
In [136]:
# Create dataframe using scraped data
facts_df = mars_facts[0]
#facts_df.reset_index(name='Facts about Mars', drop=True)
# facts_df.rename(columns= {"0": "Facts","1": "On Mars"})
facts_df.columns= (['Category', 'Mars Facts'])
mars_facts_clean=facts_df.drop(0)
clean_df=mars_facts_clean.set_index('Category')

#facts_df.drop("index")
#facts_df.set_index=(['Category'])
clean_df.head(10)
Out[136]:
Mars Facts
Category	
Polar Diameter:	6,752 km
Mass:	6.39 × 10^23 kg (0.11 Earths)
Moons:	2 (Phobos & Deimos)
Orbit Distance:	227,943,824 km (1.38 AU)
Orbit Period:	687 days (1.9 years)
Surface Temperature:	-87 to -5 °C
First Record:	2nd millennium BC
Recorded By:	Egyptian astronomers
In [137]:
#Use Pandas to convert the data to a HTML table string.
In [138]:
html_table = facts_df.to_html('mars.html')
In [139]:
### Mars Hemispheres
In [140]:
# Visit the USGS Astrogeology site
astrogeo_url= "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(astrogeo_url)
In [141]:
html = browser.html
# Parse HTML with Beautiful Soup
soup = bs(html, 'html.parser')
#print(soup)
In [142]:
# Create an HTML object

#Scrape the USGS Astrogeology site and collect high resolution images for each of Mar's hemispheres. 
#Save both the image url string for the full resolution hemisphere image, 
#and the Hemisphere title containing the hemisphere name. 
# Use a Python dictionary to store the data using the keys `img_url` and `title`.
cerb_url=browser.links.find_by_partial_text('Cerberus')
cerb_url.click()
In [143]:
time.sleep(1)
html = browser.html
# Parse HTML with Beautiful Soup
soup_cerb = bs(html, 'html.parser')
cerb_photo = soup_cerb.find("a", text="Sample").get("href")
cerb_title = soup_cerb.find("h2", class_="title").text
#print(cerb_title)
browser.back()
#print(cerb_photo)
In [144]:
#want to grab text of URL and store into dictionary
#cerb_photo=cerb_url.find_by_partial_text('Sample').click()
#cerb_photo.click()
# Need to put code for all hemispheres into a loop; exercise stu_scrape_weather
# Put elements into a dictionary 
# Try craigslist exercises
In [145]:
html = browser.html
# Parse HTML with Beautiful Soup
soup = bs(html, 'html.parser')
In [146]:
schia_url=browser.links.find_by_partial_text('Schiaparelli')
schia_url.click()
In [147]:
time.sleep(1)
html = browser.html
# Parse HTML with Beautiful Soup
soup_schia = bs(html, 'html.parser')
schia_photo = soup_schia.find("a", text="Sample").get("href")
schia_title = soup_schia.find("h2", class_="title").text
#print(schia_photo)
browser.back()
In [148]:
html = browser.html
# Parse HTML with Beautiful Soup
soup = bs(html, 'html.parser')
In [149]:
syrtis_url=browser.links.find_by_partial_text('Syrtis')
syrtis_url.click()
In [150]:
time.sleep(1)
html = browser.html
# Parse HTML with Beautiful Soup
soup_syrtis = bs(html, 'html.parser')
syrtis_photo = soup_syrtis.find("a", text="Sample").get("href")
syrtis_title = soup_syrtis.find("h2", class_="title").text
#print(syrtis_photo)
browser.back()
In [151]:
html = browser.html
# Parse HTML with Beautiful Soup
soup = bs(html, 'html.parser')
In [152]:
valles_url=browser.links.find_by_partial_text('Valles')
valles_url.click()
In [153]:
time.sleep(1)
html = browser.html
# Parse HTML with Beautiful Soup
soup_valles = bs(html, 'html.parser')
valles_photo = soup_valles.find("a", text="Sample").get("href")
valles_title = soup_valles.find("h2", class_="title").text
#print(valles_photo)
browser.back()
In [172]:
#Store table and headlines in dictionary
mars_facts= {
    'Headline': news_title,
    'News': news_p,
    'Featured Image': featured_img_url,
    'Table': clean_df
    }
print(mars_facts)

## Need to add featured image?
{'Headline': 'Another First: Perseverance Captures the Sounds of Driving on Mars', 'News': 'NASA’s newest rover recorded audio of itself crunching over the surface of the Red Planet, adding a whole new dimension to Mars exploration.', 'Featured Image': 'https://d2pn8kiwq2w21t.cloudfront.net/images/jpegPIA24505.2e16d0ba.fill-400x400-c50.jpg', 'Table':                                          Mars Facts
Category                                           
Polar Diameter:                            6,752 km
Mass:                 6.39 × 10^23 kg (0.11 Earths)
Moons:                          2 (Phobos & Deimos)
Orbit Distance:            227,943,824 km (1.38 AU)
Orbit Period:                  687 days (1.9 years)
Surface Temperature:                   -87 to -5 °C
First Record:                     2nd millennium BC
Recorded By:                   Egyptian astronomers}
In [170]:
#Store hemisphere labels and images in a dictionary
hemisphere_image_urls=[
    {"Cerberus": cerb_title, "Cerberus_img": cerb_photo},
    {"Schiaparelli": schia_title, "Schiaparelli_img": schia_photo},
    {"Syrtis": syrtis_title, "Syrtis_img": syrtis_photo},
    {"Valles": valles_title, "Valles_img": valles_photo}
    
]
print(hemisphere_image_urls)
[{'Cerberus': 'Cerberus Hemisphere Enhanced', 'Cerberus_img': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'}, {'Schiaparelli': 'Schiaparelli Hemisphere Enhanced', 'Schiaparelli_img': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'}, {'Syrtis': 'Syrtis Major Hemisphere Enhanced', 'Syrtis_img': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'}, {'Valles': 'Valles Marineris Hemisphere Enhanced', 'Valles_img': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]
import pandas as pd
In [126]:
# Establish a path with Chrome Driver and create browser
executable_path={'executable_path': ChromeDriverManager().install()}
browser=Browser('chrome', **executable_path, headless=False)
[WDM] - ====== WebDriver manager ======
[WDM] - Current google-chrome version is 89.0.4389
[WDM] - Get LATEST driver version for 89.0.4389
[WDM] - Get LATEST driver version for 89.0.4389

[WDM] - Trying to download new driver from https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_win32.zip
[WDM] - Driver has been saved in cache [C:\Users\carua.DESKTOP-4FTJ629\.wdm\drivers\chromedriver\win32\89.0.4389.23]
In [127]:
# Assign URL and visit with browser
url= "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
browser.visit(url)
In [128]:
# Create an HTML object
html = browser.html
# Parse HTML with Beautiful Soup
soup = bs(html, 'html.parser')
#Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
news_title = soup.find_all("div", class_="content_title")[1].text
# Print headline
print(news_title)
Another First: Perseverance Captures the Sounds of Driving on Mars
In [129]:
# Find and print first paragraph
news_p = soup.find("div", class_="article_teaser_body").text
print(news_p)
NASA’s newest rover recorded audio of itself crunching over the surface of the Red Planet, adding a whole new dimension to Mars exploration.
In [130]:
# Load URL for image and visit using splinter 
image_url= "https://www.jpl.nasa.gov/images?search=&category=Mars"
browser.visit(image_url)
In [131]:
browser.find_by_css('.mb-3').click()
html = browser.html
# Parse HTML with Beautiful Soup
soup = bs(html, 'html.parser')
In [132]:
# Locate image using splinter, assign to a variable, and save and print complete URL
featured_img= soup.find("img", class_="BaseImage")
featured_img_url= featured_img['data-src']
print(f"Featured_image_url: {featured_img_url}")
Featured_image_url: https://d2pn8kiwq2w21t.cloudfront.net/images/jpegPIA24505.2e16d0ba.fill-400x400-c50.jpg
In [133]:
### Mars Facts
In [134]:
#Visit the Mars Facts webpage [here](https://space-facts.com/mars/) 
#and use Pandas to scrape the table containing facts about the planet 
#including Diameter, Mass, etc.
facts_url= "https://space-facts.com/mars/"
browser.visit(facts_url)
In [135]:
# Read table on webpage using Pandas and assign to variable name
mars_facts=pd.read_html(facts_url)
#mars_facts
# mars_facts
# type(mars_facts)
In [136]:
# Create dataframe using scraped data
facts_df = mars_facts[0]
#facts_df.reset_index(name='Facts about Mars', drop=True)
# facts_df.rename(columns= {"0": "Facts","1": "On Mars"})
facts_df.columns= (['Category', 'Mars Facts'])
mars_facts_clean=facts_df.drop(0)
clean_df=mars_facts_clean.set_index('Category')

#facts_df.drop("index")
#facts_df.set_index=(['Category'])
clean_df.head(10)
Out[136]:
Mars Facts
Category	
Polar Diameter:	6,752 km
Mass:	6.39 × 10^23 kg (0.11 Earths)
Moons:	2 (Phobos & Deimos)
Orbit Distance:	227,943,824 km (1.38 AU)
Orbit Period:	687 days (1.9 years)
Surface Temperature:	-87 to -5 °C
First Record:	2nd millennium BC
Recorded By:	Egyptian astronomers
In [137]:
#Use Pandas to convert the data to a HTML table string.
In [138]:
html_table = facts_df.to_html('mars.html')
In [139]:
### Mars Hemispheres
In [140]:
# Visit the USGS Astrogeology site
astrogeo_url= "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(astrogeo_url)
In [141]:
html = browser.html
# Parse HTML with Beautiful Soup
soup = bs(html, 'html.parser')
#print(soup)
In [142]:
# Create an HTML object

#Scrape the USGS Astrogeology site and collect high resolution images for each of Mar's hemispheres. 
#Save both the image url string for the full resolution hemisphere image, 
#and the Hemisphere title containing the hemisphere name. 
# Use a Python dictionary to store the data using the keys `img_url` and `title`.
cerb_url=browser.links.find_by_partial_text('Cerberus')
cerb_url.click()
In [143]:
time.sleep(1)
html = browser.html
# Parse HTML with Beautiful Soup
soup_cerb = bs(html, 'html.parser')
cerb_photo = soup_cerb.find("a", text="Sample").get("href")
cerb_title = soup_cerb.find("h2", class_="title").text
#print(cerb_title)
browser.back()
#print(cerb_photo)
In [144]:
#want to grab text of URL and store into dictionary
#cerb_photo=cerb_url.find_by_partial_text('Sample').click()
#cerb_photo.click()
# Need to put code for all hemispheres into a loop; exercise stu_scrape_weather
# Put elements into a dictionary 
# Try craigslist exercises
In [145]:
html = browser.html
# Parse HTML with Beautiful Soup
soup = bs(html, 'html.parser')
In [146]:
schia_url=browser.links.find_by_partial_text('Schiaparelli')
schia_url.click()
In [147]:
time.sleep(1)
html = browser.html
# Parse HTML with Beautiful Soup
soup_schia = bs(html, 'html.parser')
schia_photo = soup_schia.find("a", text="Sample").get("href")
schia_title = soup_schia.find("h2", class_="title").text
#print(schia_photo)
browser.back()
In [148]:
html = browser.html
# Parse HTML with Beautiful Soup
soup = bs(html, 'html.parser')
In [149]:
syrtis_url=browser.links.find_by_partial_text('Syrtis')
syrtis_url.click()
In [150]:
time.sleep(1)
html = browser.html
# Parse HTML with Beautiful Soup
soup_syrtis = bs(html, 'html.parser')
syrtis_photo = soup_syrtis.find("a", text="Sample").get("href")
syrtis_title = soup_syrtis.find("h2", class_="title").text
#print(syrtis_photo)
browser.back()
In [151]:
html = browser.html
# Parse HTML with Beautiful Soup
soup = bs(html, 'html.parser')
In [152]:
valles_url=browser.links.find_by_partial_text('Valles')
valles_url.click()
In [153]:
time.sleep(1)
html = browser.html
# Parse HTML with Beautiful Soup
soup_valles = bs(html, 'html.parser')
valles_photo = soup_valles.find("a", text="Sample").get("href")
valles_title = soup_valles.find("h2", class_="title").text
#print(valles_photo)
browser.back()
In [172]:
#Store table and headlines in dictionary
mars_facts= {
    'Headline': news_title,
    'News': news_p,
    'Featured Image': featured_img_url,
    'Table': clean_df
    }
print(mars_facts)

## Need to add featured image?
{'Headline': 'Another First: Perseverance Captures the Sounds of Driving on Mars', 'News': 'NASA’s newest rover recorded audio of itself crunching over the surface of the Red Planet, adding a whole new dimension to Mars exploration.', 'Featured Image': 'https://d2pn8kiwq2w21t.cloudfront.net/images/jpegPIA24505.2e16d0ba.fill-400x400-c50.jpg', 'Table':                                          Mars Facts
Category                                           
Polar Diameter:                            6,752 km
Mass:                 6.39 × 10^23 kg (0.11 Earths)
Moons:                          2 (Phobos & Deimos)
Orbit Distance:            227,943,824 km (1.38 AU)
Orbit Period:                  687 days (1.9 years)
Surface Temperature:                   -87 to -5 °C
First Record:                     2nd millennium BC
Recorded By:                   Egyptian astronomers}
In [170]:
#Store hemisphere labels and images in a dictionary
hemisphere_image_urls=[
    {"Cerberus": cerb_title, "Cerberus_img": cerb_photo},
    {"Schiaparelli": schia_title, "Schiaparelli_img": schia_photo},
    {"Syrtis": syrtis_title, "Syrtis_img": syrtis_photo},
    {"Valles": valles_title, "Valles_img": valles_photo}
    
]
print(hemisphere_image_urls)
[{'Cerberus': 'Cerberus Hemisphere Enhanced', 'Cerberus_img': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'}, {'Schiaparelli': 'Schiaparelli Hemisphere Enhanced', 'Schiaparelli_img': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'}, {'Syrtis': 'Syrtis Major Hemisphere Enhanced', 'Syrtis_img': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'}, {'Valles': 'Valles Marineris Hemisphere Enhanced', 'Valles_img': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]
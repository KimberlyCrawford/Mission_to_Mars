# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

### Visit the NASA Mars News Site

# Visit the Mars NASA news site to scrap the site.
Mars_news_url = 'https://redplanetscience.com/'
browser.visit(Mars_news_url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Use BeautifulSoup to parse the HTML.
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text') # Our parent element that holds all of the other elements within it.
slide_elem

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

### JPL Space Images Featured Image

# Visit URL
Mars_images_url = 'https://spaceimages-mars.com'
browser.visit(Mars_images_url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

### Mars Facts

# Scrape the entire table with Pandas' .read_html() function.
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()

# Define columns.
df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

# Convert our DataFrame back into HTML-ready code using the .to_html() function. 
df.to_html()

# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

### Hemispheres

### Steps 1-3

# 1. Use browser to visit the Mars Hemispheres website to view the hemisphere images. 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# 2. Create an empty list to hold the image URLs and titles.
hemispheres_info = []
    
# 3. Get a List of All the Hemispheres
links = browser.find_by_css("a.product-item h3")
for item in range(len(links)):
    hemisphere = {}
    
    # Find Element on Each Loop to Avoid a Stale Element Exception
    browser.find_by_css("a.product-item h3")[item].click()
    
    # Find Sample Image Anchor Tag & Extract <href>
    sample_element = browser.find_link_by_text("Sample").first
    hemisphere["img_url"] = sample_element["href"]
    
    # Get Hemisphere Title
    hemisphere["title"] = browser.find_by_css("h2.title").text
    
    # Append Hemisphere Object to List
    hemispheres_info.append(hemisphere)
    
    # Navigate Backwards
    browser.back()

# Quit the browser
browser.quit()

### Step 4: Print the list that holds the dictionary of each image url and title.

# Print the list that holds the dictionary of each image url and title.
hemispheres_info
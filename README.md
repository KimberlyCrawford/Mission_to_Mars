# Mission_to_Mars

# Overview
A project to extract the most recently published article's title and summary from Mars Websites.

## Purpose
Robin, who loves astronomy and wants to work for NASA one day, decided to use a specific method of gathering the latest data: web scraping. Using this technique, she had the ability to pull data from multiple websites, stored it in a database, then presented the collected data in a central location: a webpage.

## Resources

### Websites Scraped: 

- Mars NASA News Site https://redplanetscience.com
- Jet Propulsion Laboratory California Institute of Technology https://galaxyfacts-mars.com/

### Programming Software:

- BeautifulSoup and Splinter was used to automate a web browser and perform a web scrape.
- MongoDB was used to create a NoSQL database to store data from the web scrape.
- Flask was used to create a web application to display the data from the web scrape.
- Python libraries included: html5lib and lxml.
- A HTML/CSS portfolio was created to showcase projects. NOTE: HTML is a coding language used for creating webpages. It’s built using specific tags and arranging them in a nested order, a bit like building blocks. Most elements have opening and closing tags, which are identical except for the forward slash that begins the closing tag. The closing tags represent the end of that HTML element.
- Bootstrap components was used to polish and customize the portfolio.

# Challenge: 

#### Deliverable 1: 
Using BeautifulSoup and Splinter, Robin scraped full-resolution images of Mars’s hemispheres and the titles of those images. The deliverable included the following steps:

Step 1: Used browser to visit the Mars Hemispheres website to view the hemisphere images. Used the DevTools to inspect the page for the proper elements to scrape. Retrieved the full-resolution image for each of Mars's hemispheres.
Step 2: Created a list to hold the .jpg image URL string and title for each hemisphere image.
Step 3: Wrote code to retrieve the full-resolution image URL and title for each hemisphere image. The full-resolution image has the .jpg extension. Looped through the full-resolution image URL, clicked the link, found the Sample image anchor tag, and got the href. Saved the full-resolution image URL string as the value for the img_url key that will be stored in the dictionary that was created from the Hint.
Saved the hemisphere image title as the value for the title key that will be stored in the dictionary created from the Hint. Before getting the next image URL and title, added the dictionary with the image URL string and the hemisphere image title to the list created in Step 2.
Step 4: Printed the list of dictionary items. 
Setp 5: Confirmed that you have the image URLs and titles for all four hemisphere images and quit the browser.

#### Deliverable 2: 
Using her Python and HTML skills, Robin added the code created in Deliverable 1 to her scraping.py file, updated the Mongo database, and modified the index.html file so the webpage contains all the information you collected in this module as well as the full-resolution image and title for each hemisphere image.Update the Web App with Mars Hemisphere Images and Titles.

#### Deliverable 3: 
Using Bootstrap 3 components, Robin updated the web app to make it mobile-responsive and added two additional Bootstrap 3 components to make it stand out.
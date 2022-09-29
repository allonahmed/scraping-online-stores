import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

# ***NOTE*** this demo is intended for static websites only

#site url of demo site we want to scrape
SITE_URL = 'https://realpython.github.io/fake-jobs/'

def getSiteContent(url):
  try:
    response = requests.get(SITE_URL)
    # If the response was successful, no Exception will be raised
    response.raise_for_status()

  except HTTPError as http_err:
    return { 'http Error': f'HTTP error occurred: {http_err}' }

  except Exception as err:
    return { 'Exception message': f'Other error occurred: {err}' }

  else:
    return response.content

HTML_content = getSiteContent(SITE_URL)

# create beautiful soup object for parsing web content
soup = BeautifulSoup(HTML_content, 'html.parser') 

# example for extracting all images from page
def getImageSource():
  images = soup.find_all('img')
  results = []
  for index, image in enumerate(images, start = 1):
    print('image {}: {}'.format(index, image['src']))

# example function of parsing content and getting specific data from html
def getContentCardInformation():
  # we can navigate through the html content through the find and find_all method which 
  # creates new BeautifulSoup objects 
  results_container = soup.find(id = 'ResultsContainer')
  card_content = results_container.find_all('div', class_ = 'card-content')

  # further parsing of each 'card-content' element and accessing the text of the element
  # strip() is useful for removing whitespace that may be generated from the html to string conversion
  for card in card_content:
    title_element = card.find('h2', class_ = 'title')
    company_element = card.find('h3', class_ = 'company')
    location_element = card.find('p', class_ = 'location')
    print(f'title:    {title_element.text.strip()}')
    print(f'company:  {company_element.text.strip()}')
    print(f'location: {location_element.text.strip()}', end = '\n'*2)    

# example of passing a function to a BS method... using lambda
python_jobs = soup.find_all(
    "h2", string = lambda text: 'python' in text.lower()
)


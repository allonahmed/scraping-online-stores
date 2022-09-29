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

#create beautiful soup object for parsing web content
soup = BeautifulSoup(HTML_content, 'html.parser') 

# we can navigate through the html content through the find and find_all method which 
# creates new BeautifulSoup objects 
results_container = soup.find(id = 'ResultsContainer')
card_content = results_container.find_all('div', class_ = 'card-content')

#example for extracting all images from page
def getImageSource():
  images = soup.find_all('img')
  results = []
  for index, image in enumerate(images, start = 1):
    print('image {}: {}'.format(index, image['src']))

getImageSource()

# for card in card_content:
#   print(card.prettify(), end = '\n'*3)  

#
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

# ***NOTE*** this demo is intended for static websites only

#site url of demo site we want to scrape
SITE_URL = 'https://www.gymshark.com/collections/all-products/mens?collections=t-shirts-tops%2Cstringers%2Ctanks%2Choodies-jackets'

def Get_HTML_Content(url):
  try:
    response = requests.get(SITE_URL)
    # If the response was successful, no Exception will be raised
    response.raise_for_status()

  #returns err if api_url is invalid
  except HTTPError as http_err:
    return { 'http Error': f'HTTP error occurred: {http_err}' }

  except Exception as err:
    return { 'Exception message': f'Other error occurred: {err}' }

  else:
    return response.content

HTML_content = Get_HTML_Content(SITE_URL)

# create beautiful soup object for parsing web content
soup = BeautifulSoup(HTML_content, 'html.parser') 

print (soup)
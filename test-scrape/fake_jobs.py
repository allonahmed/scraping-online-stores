import requests
from requests.exceptions import HTTPError


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
    return response.text

print(getSiteContent(SITE_URL))
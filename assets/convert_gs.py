import json

# file for cleaning and converting json data scraped from gymshark

def convert_data(path):
  try:
    with open(path, "r") as file:
      data = json.loads(file.read())
      results = []
      for i in data:
        # converts each element into dict for parsing
        x = json.loads(i)
        # data we want to send to our db
        dict = {
          'organization': x.get('offers').get('seller').get('name'),
          'brand': x.get('brand').get('name'),
          'url': x.get('offers').get('url'),
          'img_url': x.get('image'),
          'price': x.get('offers').get('price'),
          'availability': x.get('offers').get('availability'),
          'sku': x.get('sku'),
          'description': x.get('description')
        }
        results.append(dict)
    return results
  except IOError:
    return 'cannot find file'

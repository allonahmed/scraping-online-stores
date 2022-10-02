import json


results = []
with open('test.json') as file:
  data = json.loads(file.read())

  for i in data:
    print(i, end='\n'*3)
    x = json.loads(i)

    print('image', x.get('image'))
    print('brand', x.get('brand'))
    print('offers', x.get('offers').get('url'))
    # prin'', t(x.get('description'))
    print('color', x.get('color'))
    print('name', x.get('name'))
    print('type', x.get('@type'))
    print('context', x.get('@context'))
    print('sku', x.get('sku'))
    results.append(x)

  # print(results)
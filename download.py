import requests
def download_image(url,filename,params=None):
  response = requests.get(url,params)
  with open(filename, 'wb') as file:
      file.write(response.content)
import requests
from download import download_image
def fetch_spacex_last_launch():
    response = requests.get("https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a")

    spacex_urls = response.json()["links"]["flickr"]["original"]
    for number, spacex_url in enumerate(spacex_urls):
        download_image(spacex_url,f"images/spacex{number}.jpg")
fetch_spacex_last_launch()
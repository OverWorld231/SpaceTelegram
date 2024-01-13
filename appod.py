import requests
import os
from download import download_image
from urllib.parse import urlparse, unquote


def extract_link(url):
    decoded_url = unquote(url)
    parsed_url = urlparse(decoded_url)
    path, full_name = os.path.split(parsed_url.path)
    file_extension = os.path.splitext(full_name)
    file_name, extansion = file_extension
    return extansion, file_name


def download_apod(api_key):
    apod_url = "https://api.nasa.gov/planetary/apod"
    count = 30
    params = {"api_key": api_key, "count": count}
    response = requests.get(apod_url, params=params)
    apod_images = response.json()
    for apod_image in apod_images:
        if apod_image.get("media_type") == "image":
            if apod_image.get("hdurl"):
                apod_link_image = apod_image["hdurl"]
            else:
                apod_link_image = apod_image["url"]
            extention, filename = extract_link(apod_link_image)
            path_image = os.path.join("images", f"{filename}{extention}")
            download_image(apod_link_image, path_image)


def main():
    api_key = os.environ['NASA_API_KEY']
    download_apod(api_key)


if __name__ == "__main__":
    main()

import requests
import datetime
import os
from download import download_image


def earth_images(api_key):
    epic_link = "https://api.nasa.gov/EPIC/api/natural"
    count = 5
    params = {"api_key": api_key, "count": count}
    response = requests.get(epic_link, params=params)
    response.raise_for_status()
    earth_url = response.json()
    for epic_url in earth_url:
        epic_date = epic_url["date"]
        epic_date = datetime.datetime.fromisoformat(epic_date).strftime(
            "%Y/%m/%d")
        epic_name = epic_url["image"]
        epic_link = f"https://api.nasa.gov/EPIC/archive/natural/{epic_date}/png/{epic_name}.png"
        path = os.path.join("images", f"{epic_name}.png")
        download_image(epic_link, path, params)


def main():
    api_key = os.environ['NASA_API_KEY']
    earth_images(api_key)


if __name__ == "__main__":
    main()

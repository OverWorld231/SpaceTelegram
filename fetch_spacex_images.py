import requests
from download import download_image


def fetch_spacex_last_launch(launch_id):
    response = requests.get(
        f"https://api.spacexdata.com/v5/launches/{launch_id}")
    response.raise_for_status()
    spacex_urls = response.json()["links"]["flickr"]["original"]
    for number, spacex_url in enumerate(spacex_urls):
        download_image(spacex_url, f"images/spacex{number}.jpg")


def main():
    parser = argparse.ArgumentParser(
        description='Эта программа позволит вам загрузить фотографии с запуска SpaceX.'
    )
    parser.add_argument(
        '--id',
        dest='launch_id',
        default="5eb87d47ffd86e000604b38a",
        help='Укажите ID запуска SpaceX, с которого можно загрузить фотографии.'
    )
    args = parser.parse_args()
    fetch_spacex_last_launch(args.launch_id)


if __name__ == "__main__":
    main()

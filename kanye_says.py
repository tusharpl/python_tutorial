# the app uses he api api.kanye.rest to show kanye west's quotes

import requests


def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()

    data = response.json()

    quote = data["quote"]
    print(f"Kanye says ... {quote}")


get_quote()

import sys
import requests

DEFAULT_SOURCE = "https://api.scryfall.com/cards/search?q=name%3A\"Atzocan\""
HEADERS = {"User-Agent": "json-parser/0.1", "Accept": "*/*"}
# DEFAULT_ARGS = {"c": "white", "set": "RIX"}


def main():
    r = requests.get(DEFAULT_SOURCE, headers=HEADERS)
    print(r.status_code)
    with open("test.txt", "w") as test:
        test.write(str(r.json()))


if __name__ == "__main__":
    main()

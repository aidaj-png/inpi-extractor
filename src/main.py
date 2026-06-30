from pprint import pprint

from config import SEARCH_TERM
from inpi_api import INPIApi


def main():
    print("=" * 60)
    print("INPI EXTRACTOR")
    print("=" * 60)

    api = INPIApi()

    api.print_request(SEARCH_TERM)

if __name__ == "__main__":
    main()

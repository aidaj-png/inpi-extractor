from pprint import pprint

from config import SEARCH_TERM
from inpi_api import INPIApi


def main():

    print("=" * 60)
    print("INPI EXTRACTOR")
    print("=" * 60)

    api = INPIApi()

    payload = api.build_query(
        word=SEARCH_TERM,
        position=0,
        size=100
    )

    print("\nPayload envoyé à l'API :\n")

    pprint(payload)

    print("\nEndpoint :")

    print(api.endpoint())


if __name__ == "__main__":
    main()

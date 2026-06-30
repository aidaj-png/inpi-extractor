from config import SEARCH_TERM
from inpi_api import INPIApi


def main():

    print("=" * 50)
    print("INPI EXTRACTOR")
    print("=" * 50)

    print(f"Recherche : {SEARCH_TERM}")

    api = INPIApi()

    api.test()

    print("\nProjet initialisé avec succès.")


if __name__ == "__main__":
    main()

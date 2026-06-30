from inpi_api import INPIApi


def main():

    print("=" * 60)
    print("INPI EXTRACTOR")
    print("=" * 60)

    username = input("Email INPI : ")
    password = input("Mot de passe : ")

    api = INPIApi()

    api.authenticate(username, password)


if __name__ == "__main__":
    main()

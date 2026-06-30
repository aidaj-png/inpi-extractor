import requests
from pprint import pprint


class INPIApi:

    BASE_URL = "https://api-gateway.inpi.fr/services/apidiffusion/api"

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({
            "Accept": "application/xml",
            "Content-Type": "application/json"
        })

        self.access_token = None
        self.refresh_token = None

    def build_query(
        self,
        word,
        position=0,
        size=100,
        collections=None
    ):

        if collections is None:
            collections = ["FR", "EU", "WO"]

        return {

            "collections": collections,

            "facetsList": [
                "APPLICANT",
                "CLASSIFICATION"
            ],

            "fields": [
                "ApplicationNumber",
                "Mark",
                "MarkCurrentStatusCode",
                "DEPOSANT",
                "ukey"
            ],

            "position": position,

            "query": f"[Mark={word}]",

            "size": size,

            "sortList": [
                "APPLICATION_DATE DESC",
                "MARK ASC"
            ],

            "withCTMRevendication": False,

            "withFacets": True
        }

    def endpoint(self):

        return f"{self.BASE_URL}/marques/search"

    def headers(self):

        return {
            "Accept": "application/xml",
            "Content-Type": "application/json"
        }

    def prepare_request(self, word, position=0, size=100):

        return {
            "url": self.endpoint(),
            "headers": self.headers(),
            "json": self.build_query(
                word=word,
                position=position,
                size=size
            )
        }

    def print_request(self, word):

        request = self.prepare_request(word)

        print("\nURL")
        print(request["url"])

        print("\nHEADERS")

        for key, value in request["headers"].items():
            print(f"{key}: {value}")

        print("\nJSON")

        pprint(request["json"])

    def authenticate(self, username, password):

        # Création de la session et récupération du cookie XSRF
        login_page = self.session.get("https://api-gateway.inpi.fr/login")

        print("GET /login :", login_page.status_code)

        xsrf = self.session.cookies.get("XSRF-TOKEN")

        if not xsrf:
            print("Erreur : cookie XSRF introuvable.")
            return None

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-XSRF-TOKEN": xsrf
        }

        payload = {
            "username": username,
            "password": password,
            "rememberMe": False
        }

        response = self.session.post(
            "https://api-gateway.inpi.fr/auth/login",
            json=payload,
            headers=headers
        )

        print("POST /auth/login :", response.status_code)
        print(response.text)

        if response.status_code == 200:

            tokens = response.json()

            self.access_token = tokens["access_token"]
            self.refresh_token = tokens["refresh_token"]

            self.session.headers.update({
                "Authorization": f"Bearer {self.access_token}"
            })

            print("Authentification réussie.")

        return response

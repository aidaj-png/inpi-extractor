import requests


class INPIApi:

    BASE_URL = "https://api-gateway.inpi.fr/services/apidiffusion/api"

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({
            "Accept": "application/xml",
            "Content-Type": "application/json"
        })

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

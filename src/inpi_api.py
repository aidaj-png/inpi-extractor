"""
Connexion à l'API INPI
Version 0.1
"""

import requests


class INPIApi:

    def __init__(self):
        self.base_url = "https://api-gateway.inpi.fr/services/apidiffusion/api"

    def test(self):
        print("Connexion à :", self.base_url)
        return True

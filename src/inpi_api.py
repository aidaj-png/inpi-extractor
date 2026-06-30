class INPIApi:

    def __init__(self):

        self.base_url = "https://api-gateway.inpi.fr/services/apidiffusion/api"

    def test(self):

        print("API INPI")

        print(self.base_url)

        return True

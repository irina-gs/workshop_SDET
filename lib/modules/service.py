import requests

from data.data import Config


class ServiceApi:
    def __init__(self, api_url=Config.BASE_API_URL):
        self.api_url = api_url

    def service_create_entity(self, data, endpoint=Config.ENDPOINT_CREATE):
        return requests.post(f"{self.api_url}{endpoint}", json=data)

    def service_delete_entity(self, entity_id, endpoint=Config.ENDPOINT_DELETE):
        return requests.delete(f"{self.api_url}{endpoint}{entity_id}")

    def service_get_entity(self, entity_id, endpoint=Config.ENDPOINT_GET):
        return requests.get(f"{self.api_url}{endpoint}{entity_id}")

    def service_get_all_entities(self, endpoint=Config.ENDPOINT_GET_ALL):
        return requests.get(f"{self.api_url}{endpoint}")

    def service_update_entity(self, entity_id, data, endpoint=Config.ENDPOINT_PATCH):
        return requests.patch(f"{self.api_url}{endpoint}{entity_id}", json=data)

import requests

from data.data import Config


class ServiceApi:
    endpoint_create_url = Config.BASE_API_URL + "/api/create"
    endpoint_delete_url = Config.BASE_API_URL + "/api/delete/"
    endpoint_get_url = Config.BASE_API_URL + "/api/get/"
    endpoint_get_all_url = Config.BASE_API_URL + "/api/getAll"
    endpoint_patch_url = Config.BASE_API_URL + "/api/patch/"

    def service_create_entity(self, **kwargs):
        return requests.post(url=self.endpoint_create_url, **kwargs)

    def service_delete_entity(self, entity_id, **kwargs):
        return requests.delete(url=f"{self.endpoint_delete_url}{entity_id}", **kwargs)

    def service_get_entity(self, entity_id, **kwargs):
        return requests.get(url=f"{self.endpoint_get_url}{entity_id}", **kwargs)

    def service_get_all_entities(self, **kwargs):
        return requests.get(url=self.endpoint_get_all_url, **kwargs)

    def service_update_entity(self, entity_id, **kwargs):
        return requests.patch(url=f"{self.endpoint_patch_url}{entity_id}", **kwargs)

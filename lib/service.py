from http import HTTPStatus

from data.models import EntityModel
from lib.modules.service import ServiceApi


def create_entity(entity: EntityModel):
    response = ServiceApi().service_create_entity(entity.model_dump())
    # import pdb; pdb.set_trace()
    assert response.status_code == HTTPStatus.OK
    return response.json()


def delete_entity(entity_id):
    response = ServiceApi().service_delete_entity(entity_id)
    assert response.status_code == HTTPStatus.NO_CONTENT


def get_entity(entity_id):
    response = ServiceApi().service_get_entity(entity_id)
    assert response.status_code == HTTPStatus.OK
    return response.json()


def get_all_entities():
    response = ServiceApi().service_get_all_entities()
    assert response.status_code == HTTPStatus.OK
    return response.json()


def update_entity(entity_id, entity: EntityModel):
    response = ServiceApi().service_update_entity(entity_id, entity.model_dump())
    assert response.status_code == HTTPStatus.NO_CONTENT


def should_be_deleted(entity_id):
    response = ServiceApi().service_get_entity(entity_id)
    return response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR

import allure
import pytest

from data.models import AllEntitiesModel, EntityModel
from lib.service import create_entity, delete_entity, get_all_entities, get_entity, should_be_deleted, update_entity


@allure.feature("Service")
@allure.story("API")
@allure.title("Создание сущности")
@allure.description(
    """
        Шаги:
            1. Создать сущность
            2. Проверить создание сущности
        
        Постусловие:  
            - Удалить тестовые данные
        
        Ожидаемый результат:  
            - Сущность создана
    """
)
def test_create_entity(entity):
    try:
        with allure.step("Создание сущности"):
            entity_id = create_entity(entity)

        with allure.step("Проверка создания сущности"):
            assert entity_id == EntityModel(**get_entity(entity_id)).id, "Сущность не была создана"

    except:
        with allure.step("Удаление тестовых данных"):
            delete_entity(entity_id)


@allure.feature("Service")
@allure.story("API")
@allure.title("Удаление сущности")
@allure.description(
    """
        Предусловие:
            - Создать тестовые данные

        Шаги:
        1. Удалить сущность
        2. Проверить удаление сущности

        Ожидаемый результат:
            - Сущность удалена
    """
)
@pytest.mark.parametrize("entity_id_for_testing", [False], indirect=True)
def test_delete_entity(entity_id_for_testing):
    with allure.step("Удаление сущности"):
        delete_entity(entity_id_for_testing)

    with allure.step("Проверка удаления сущности"):
        assert should_be_deleted(entity_id_for_testing), "Сущность не была удалена"


@allure.feature("Service")
@allure.story("API")
@allure.title("Получение сущности")
@allure.description(
    """
        Предусловие:
            - Создать тестовые данные

        Шаги:
            1. Получить сущность
            2. Проверить получение сущности

        Постусловие:
            - Удалить тестовые данные

        Ожидаемый результат:
            - Сущность получена
    """
)
def test_get_entity(entity_id_for_testing):
    with allure.step("Получение сущности"):
        entity = get_entity(entity_id_for_testing)

    with allure.step("Проверка получения сущности"):
        assert entity_id_for_testing == EntityModel(**entity).id, "Сущность не была получена"


@allure.feature("Service")
@allure.story("API")
@allure.title("Получение всех сущностей")
@allure.description(
    """
        Шаги:
            1. Получить всех сущностей
            2. Проверить получение сущностей

        Ожидаемый результат:
            - Получены все сущности
    """
)
def test_get_all_entities():
    with allure.step("Получение всех сущностей"):
        entities = get_all_entities()

    with allure.step("Проверка получения сущностей"):
        assert isinstance(AllEntitiesModel(**entities), AllEntitiesModel), "Сущности не были получены"


@allure.feature("Service")
@allure.story("API")
@allure.title("Обновление сущности")
@allure.description(
    """
        Предусловие:
            - Создать тестовые данные

        Шаги:
            1. Обновить сущность
            2. Проверить обновление сущности

        Постусловие:
            - Удалить тестовые данные

        Ожидаемый результат:
            - Сущность обновлена
    """
)
def test_update_entity(entity_id_for_testing, entity):
    with allure.step("Обновление сущности"):
        update_entity(entity_id_for_testing, entity)

    with allure.step("Проверка обновления сущности"):
        assert entity.title == EntityModel(**get_entity(entity_id_for_testing)).title, "Сущность не была обновлена"

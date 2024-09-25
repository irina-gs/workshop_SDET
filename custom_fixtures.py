import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data.models import AdditionModel, EntityModel
from lib.service import delete_entity, create_entity


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture
def last_name():
    faker = Faker()
    return faker.last_name()


@pytest.fixture
def entity():
    faker = Faker()
    entity = EntityModel(
        addition=AdditionModel(
            additional_info=faker.text(),
            additional_number=faker.random_int()
        ),
        important_numbers=[faker.random_int() for _ in range(faker.random_int(1, 10))],
        title=faker.text(),
        verified=faker.boolean()
    )
    return entity


@pytest.fixture
def entity_id_for_testing(entity, request):
    entity_id = create_entity(entity)
    yield entity_id

    should_delete = getattr(request, "param", True)
    if should_delete:
        delete_entity(entity_id)

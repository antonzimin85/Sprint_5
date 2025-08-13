import pytest
import random
from selenium import webdriver


@pytest.fixture(scope='function')
def webdriver_instance():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def new_user_credentials():
    new_user_email = f'test{random.randint(1, 10_000_000)}@test.com'
    new_user_password = f'test_password{random.randint(9999, 10_000_000)}'
    return new_user_email, new_user_password

@pytest.fixture(scope='function')
def existing_user_credentials():
    existing_user_email = 'testzimin777@test.net'
    existing_user_password = 'Halo1234'
    return existing_user_email, existing_user_password

@pytest.fixture(scope='function')
def product_with_attributes():
    product_name = 'Игрушка Капибара'
    product_description = 'Новая. С шарфиком. 35 см'
    product_price = 50
    return product_name, product_description, product_price
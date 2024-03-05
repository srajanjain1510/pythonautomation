"""
conftest.py is to define the fixtures
"""
import configparser

import pytest
import toml


@pytest.fixture(scope='session')
def get_url():
    config_parser = configparser.ConfigParser()
    config_parser.read('../config/api_config.ini')
    default_url_ = config_parser['DEFAULT']['url']
    return default_url_


@pytest.fixture()
def first_entry():
    return 'a'


@pytest.fixture()
def second_entry():
    return 2


@pytest.fixture()
def third_entry(first_entry, second_entry):
    return [first_entry, second_entry]


@pytest.fixture()
def fourth_entry():
    return 'a'


@pytest.fixture(scope='session')
def share_context():
    return []


@pytest.fixture()
def sixth_entry(fourth_entry, fifth_entry):
    return fifth_entry.append(fourth_entry)


# @pytest.fixture()
# def set_config():
#     config_parser = configparser.ConfigParser()
#     config_parser.read('../config/api_config.ini')
#     return config_parser

@pytest.hookimpl(optionalhook=True)
def pytest_add_option(parser):
    parser.addoption("--length", action="store", default="0", help="length of password")
    # parser.addoption("--no_of_alphanumeric", action="store", default="5", help="no of alphanumeric characters")


@pytest.fixture()
def generate_password_options(request):
    length = int(request.config.getoption("--length"))
    # alphanumberic_char_count = request.config.getoption("--no_of_alphanumeric")

    return length


@pytest.fixture(scope='session')
def get_config_toml():
    toml_file = open('../../config/config.toml', 'r')
    config = toml.load(toml_file)
    return config

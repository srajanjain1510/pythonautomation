"""This is a test module"""
import pytest
import requests

import apiautomation.requesttdd.core.library
from apiautomation.model.ResponseModel import ResponseModel
from apiautomation.model.payload_model import payload_model

# from pytest_mock import mocker

test_data = ['2', '4', '5']


@pytest.mark.regression
@pytest.mark.parametrize("page_num", test_data)
@pytest.mark.order(1)
def test_sample_get_api_0(get_url, page_num):
    """

    :param getUrl:
    :param page_num:
    """
    page_value = page_num
    response_get_api = requests.get(get_url, params={'page': page_value}, timeout=4)
    print(response_get_api.json())
    assert response_get_api.status_code == 200
    assert str(response_get_api.json()['page']) == page_value


@pytest.mark.regression
@pytest.mark.order(2)
def test_sample_get_api_1(get_url):
    """

    :param getUrl:
    """
    response_get_api = requests.get(get_url, timeout=3)
    print(response_get_api.json())
    assert response_get_api.status_code == 200


@pytest.mark.regression
@pytest.mark.order(after="test_sample_get_api_1")
def test_sample_get_api_2(get_url):
    """

    :param getUrl:
    """
    response_get_api = requests.get(get_url, timeout=5)
    print(response_get_api.json())
    assert response_get_api.status_code == 200


# def test_reqres_post_1(getUrl):
# fixture chaining
# def test_fixture_chaining(second_entry):
#     second_entry.append('b')
#     assert 'a' in second_entry
#

# fixture requesting more than one fixture

def test_calling_multiple_fixture(first_entry, second_entry, third_entry):
    """

    :param first_entry:
    :param second_entry:
    :param third_Entry:
    """
    third_entry.append({'a': 3})
    print(third_entry)


# #Fixture caching
#
# def test_caching_fixture(sixth_entry,fifth_entry,fourth_entry):
#     assert fifth_entry == [fourth_entry]

@pytest.mark.regression
def test_post_call_validation(get_url):
    """

    :param getUrl:
    """

    test_data_request_payload = payload_model("sj", "jain")
    requests_post = requests.post(get_url, test_data_request_payload.serialize(), timeout=5)
    print(requests_post.json())
    response_model = ResponseModel(requests_post.json())
    print(type(response_model))


def test_mock_pi_value(mocker):
    """

    :param mocker:
    """
    try:
        mocker.patch("apiautomation.requesttdd.core.Library.PI", 5.0)
        assert apiautomation.requesttdd.core.library.area_circle(5) == 125
    except Exception as exception:
        raise exception


def test_mock_joke_api_call_with_mock(mocker):
    mock_response = {
        "data": {"id": 7878, "name": "fuchsia rose", "year": 34444, "color": "#C74375", "pantone_value": "17-2031"},
        "support": {"url": "https://reqres.in/#support-heading",
                    "text": "To trtrtr keep ReqRes free, contributions towards server costs are appreciated!"}}

    mocker.patch(
        "apiautomation.requesttdd.core.library.get_jokes_yo_mamma_api").return_value.json.return_value = mock_response

    response = apiautomation.requesttdd.core.library.get_jokes_yo_mamma_api()

    assert response.json() == mock_response


def test_json_palceholder_api_get_call():
    response = requests.get('https://jsonplaceholder.typicode.com/users/1')

    print(ResponseModel(response.json()))


CONDITION = True


@pytest.mark.parametrize(

    ("n", "expected"),
    [
        (1, 2),
        (4, 5),
        pytest.param(-1, 0, marks=pytest.mark.skip(reason="negative numbers are not acceptable")),
        pytest.param('a', 'b', marks=pytest.mark.xfail(reason="non integers are not allowed")),
        pytest.param(0,-1,marks=pytest.mark.skipif(CONDITION == True, reason= "Condition is true"))
    ]
)
def test_increment(n, expected):
    assert n + 1 == expected

def test_password_gen(generate_password_options):
    length = generate_password_options
    print(length)
"""This is a test module"""
import pytest
import requests

from apiautomation.model.payload_model import payload_model


@pytest.mark.order(1)
def test_create_user(get_url, share_context):
    test_data_json = payload_model("Aknthony", "DuES")
    post_response = requests.post(get_url, test_data_json.serialize(),timeout=5)
    share_context.append(post_response.json()['id'])
    print(share_context[0])


@pytest.mark.order(after="test_create_user")
def test_get_created_user(get_url, share_context):
    api_url = get_url + '/{id}'
    final_url = api_url.format(id=share_context[0])
    response = requests.get(final_url,timeout=5)
    print(response.json())

# def test_check_user_in_list():
#
# def test_delete_user():
#
# def test_get_deleted_user():

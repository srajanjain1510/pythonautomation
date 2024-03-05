import logging
from dataclasses import asdict

import requests

from apiautomation.model.request_payload_create import RequestPayload


def test_dataclass_serialization(get_config_toml, caplog):
    base_url = get_config_toml['server']['url']
    caplog.set_level(logging.INFO)

    test_data_json = asdict(RequestPayload('SJ', 'AJ'))
    post_response = requests.post(base_url, test_data_json, timeout=5)
    print(post_response.json())

    assert post_response.status_code == 201
    logging.info('response successful')
    assert 'successful' in caplog.text
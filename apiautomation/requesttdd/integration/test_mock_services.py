import apiautomation


def test_mock_joke_api_call_with_mock(mocker):
    mock_response = {
        "data": {"id": 7878, "name": "fuchsia rose", "year": 34444, "color": "#C74375", "pantone_value": "17-2031"},
        "support": {"url": "https://reqres.in/#support-heading",
                    "text": "To trtrtr keep ReqRes free, contributions towards server costs are appreciated!"}}

    mocker.patch(
        "apiautomation.requesttdd.core.library.get_jokes_yo_mamma_api").return_value.json.return_value = mock_response

    response = apiautomation.requesttdd.core.library.get_jokes_yo_mamma_api()

    assert response.json() == mock_response

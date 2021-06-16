import requests

get_url = 'http://127.0.0.1:5000/pms/dm/application'


def test_get_api_status_code_equals_200():
    response = requests.get(get_url)
    assert response.status_code == 200


def test_get_api_status_code_not_equals_200():
    response = requests.get(get_url)
    assert response.status_code != 200


def test_get_api_check_content_type_equals_json():
    response = requests.get(get_url)
    assert response.headers["Content-Type"] == "application/json"


def test_get_request_response():
    actual_response = [
    {
        "cordinates": "1,2",
        "current_version": "2.0",
        "date_of_installation": "2021-05-30T00:00:00",
        "device_id": "De7sadjsf82",
        "id": 4,
        "mobile_model": "samsung guru",
        "mobile_number": "935763457345",
        "mobile_os": "935763457345",
        "mobile_technology": "Andriod",
        "probe_name": "AUH",
        "region": "Dubai",
        "remote_management": "Remote Access",
        "site_name": "xxx Pavalion",
        "timestamp": "2021-05-30T18:18:40.805190",
        "update": "update to 2.1"
    },
    {
        "cordinates": "1,2",
        "current_version": "2.0",
        "date_of_installation": "2021-05-30T00:00:00",
        "device_id": "De7sadjsf82",
        "id": 6,
        "mobile_model": "samsung guru",
        "mobile_number": "935763457345",
        "mobile_os": "935763457345",
        "mobile_technology": "Andriod",
        "probe_name": "AUH",
        "region": "Dubai",
        "remote_management": "Remote Access",
        "site_name": "xxx Pavalion",
        "timestamp": "2021-05-30T18:18:40.805190",
        "update": "update to 2.1"
    },
    {
        "cordinates": "1,2",
        "current_version": "2.0",
        "date_of_installation": "2021-05-30T00:00:00",
        "device_id": "De7sadjsf82",
        "id": 7,
        "mobile_model": "samsung guru",
        "mobile_number": "935763457345",
        "mobile_os": "935763457345",
        "mobile_technology": "Andriod",
        "probe_name": "AUH",
        "region": "Dubai",
        "remote_management": "Remote Access",
        "site_name": "xxx Pavalion",
        "timestamp": "2021-05-30T18:18:40.805190",
        "update": "update to 2.1"
    },
    {
        "cordinates": "1,2",
        "current_version": "2.0",
        "date_of_installation": "2021-05-30T00:00:00",
        "device_id": "De7sadjsf82",
        "id": 8,
        "mobile_model": "samsung guru",
        "mobile_number": "935763457345",
        "mobile_os": "935763457345",
        "mobile_technology": "Andriod",
        "probe_name": "AUH",
        "region": "Dubai",
        "remote_management": "Remote Access",
        "site_name": "xxx Pavalion",
        "timestamp": "2021-05-30T18:18:40.805190",
        "update": "update to 2.1"
    },
    {
        "cordinates": "1,2",
        "current_version": "2.0",
        "date_of_installation": "2021-05-30T00:00:00",
        "device_id": "De7sadjsf82",
        "id": 9,
        "mobile_model": "samsung guru",
        "mobile_number": "935763457345",
        "mobile_os": "935763457345",
        "mobile_technology": "Andriod",
        "probe_name": "AUH",
        "region": "Dubai",
        "remote_management": "Remote Access",
        "site_name": "xxx Pavalion",
        "timestamp": "2021-05-30T18:18:40.805190",
        "update": "update to 2.1"
    },
    {
        "cordinates": "1,2",
        "current_version": "2.0",
        "date_of_installation": "2021-05-30T00:00:00",
        "device_id": "De7sadjsf82",
        "id": 10,
        "mobile_model": "samsung guru",
        "mobile_number": "935763457345",
        "mobile_os": "935763457345",
        "mobile_technology": "Andriod",
        "probe_name": "AUH",
        "region": "Dubai",
        "remote_management": "Remote Access",
        "site_name": "xxx Pavalion",
        "timestamp": "2021-05-30T18:18:40.805190",
        "update": "update to 2.1"
    },
    {
        "cordinates": "3,5",
        "current_version": "2.0",
        "date_of_installation": "2021-05-31T00:00:00",
        "device_id": "De7sadjsf82",
        "id": 5,
        "mobile_model": "Iphone 12",
        "mobile_number": "935763457345",
        "mobile_os": "935763457345",
        "mobile_technology": "IOS",
        "probe_name": "AUH",
        "region": "Dubai",
        "remote_management": "Remote Access",
        "site_name": "yyy Pavalion",
        "timestamp": "2021-05-30T17:42:08.997179",
        "update": "update to 2.1"
    },
    {
        "cordinates": "1,2",
        "current_version": "2.0",
        "date_of_installation": "2021-05-30T00:00:00",
        "device_id": "De7sadjsf82",
        "id": 1,
        "mobile_model": "samsung guru",
        "mobile_number": "935763457345",
        "mobile_os": "935763457345",
        "mobile_technology": "Andriod",
        "probe_name": "AUH",
        "region": "Dubai",
        "remote_management": "Remote Access",
        "site_name": "xxx Pavalion",
        "timestamp": "2021-05-31T06:12:53.501883",
        "update": "update to 2.5"
    },
    {
        "cordinates": "1,2",
        "current_version": "2.0",
        "date_of_installation": "2021-05-30T00:00:00",
        "device_id": "De7sadjsf82",
        "id": 2,
        "mobile_model": "samsung guru",
        "mobile_number": "935763457345",
        "mobile_os": "935763457345",
        "mobile_technology": "Andriod",
        "probe_name": "AUH",
        "region": "Dubai",
        "remote_management": "Remote Access",
        "site_name": "YYY Pavalion",
        "timestamp": "2021-06-02T04:33:55.056807",
        "update": "update to 2.5"
    },
    {
        "cordinates": "1,4",
        "current_version": "2.0",
        "date_of_installation": "2021-05-30T18:18:40.789970",
        "device_id": "De7sadjsf82",
        "id": 3,
        "mobile_model": "IPHONE 12",
        "mobile_number": "935763457345",
        "mobile_os": "935763457345",
        "mobile_technology": "5G",
        "probe_name": "AUH",
        "region": "Dubai",
        "remote_management": "Remote Access",
        "site_name": "xxx Pavalion",
        "timestamp": "2021-06-02T04:41:27.928659",
        "update": "update to 2.2"
    }
]
    response = requests.get(get_url)
    assert response.json() == actual_response

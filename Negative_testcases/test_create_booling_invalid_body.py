import requests
BASE_URL = "https://restful-booker.herokuapp.com"
TIMEOUT = 30

def test_create_booking_with_invalid_body_returns_500():
    url = f"{BASE_URL}/booking"
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    invalid_payload = {"abc": "PQR"}  # deliberately wrong schema
    resp = requests.post(url, json=invalid_payload, headers=headers, timeout=TIMEOUT)
    assert resp.status_code == 500
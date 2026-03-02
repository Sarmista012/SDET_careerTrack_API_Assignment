import requests
BASE_URL = "https://restful-booker.herokuapp.com"
TIMEOUT = 30

def test_update_booking_with_invalid_token_returns_403():
    create_url = f"{BASE_URL}/booking"
    valid_payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 123,
        "depositpaid": True,
        "bookingdates": {"checkin": "2025-01-01", "checkout": "2025-01-05"},
        "additionalneeds": "Breakfast",
    }
    create_resp = requests.post(create_url, json=valid_payload, timeout=TIMEOUT)
    assert create_resp.status_code == 200
    booking_id = create_resp.json()["bookingid"]

    update_url = f"{BASE_URL}/booking/{booking_id}"
    invalid_token = "abcpqas12"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={invalid_token}",
    }
    update_payload = {"additionalneeds": "Dinner", "totalprice": 999}
    update_resp = requests.put(update_url, json=update_payload, headers=headers, timeout=TIMEOUT)
    assert update_resp.status_code == 403
    return update_resp

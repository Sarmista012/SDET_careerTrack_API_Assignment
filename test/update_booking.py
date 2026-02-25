import random
import string

def rand_alpha(n=10):
    return "".join(random.choice(string.ascii_letters) for _ in range(n))

def test_update_one_booking_additionalneeds_and_totalprice(created_bookings, booking_client, token):
    item = created_bookings[0]
    booking_id = item["id"]
    original = item["expected"]  # full booking payload used during create

    updated_payload = dict(original)  # shallow copy is fine here
    updated_payload["additionalneeds"] = rand_alpha(12)   # alphabetic string
    updated_payload["totalprice"] = random.randint(50, 5000)  # numeric

    put_resp, put_body = booking_client.update_booking(booking_id, updated_payload, token)
    assert put_resp.status_code == 200
    assert put_body["additionalneeds"] == updated_payload["additionalneeds"]
    assert int(put_body["totalprice"]) == int(updated_payload["totalprice"])


    get_resp, get_body = booking_client.get_booking(booking_id)
    assert get_resp.status_code == 200
    assert get_body["additionalneeds"] == updated_payload["additionalneeds"]
    assert int(get_body["totalprice"]) == int(updated_payload["totalprice"])

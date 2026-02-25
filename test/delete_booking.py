def test_delete_all_5_bookings(created_bookings, booking_client, token):
    for item in created_bookings:
        booking_id = item["id"]
        resp = booking_client.delete_booking(booking_id, token)
        print(f"DELETE /booking/{booking_id} -> {resp.status_code} | {resp.text!r}")
        assert resp.status_code in (201, 200)

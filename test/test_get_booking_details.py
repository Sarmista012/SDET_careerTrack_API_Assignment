def test_c_get_all_created_booking_details_and_validate(created_bookings, booking_client):
    for item in created_bookings:
        bookingid = item["id"]
        expected = item["expected"]

        resp, actual = booking_client.get_booking(bookingid)
        assert resp.status_code == 200
        assert "application/json" in resp.headers.get("Content-Type", "").lower()

        assert actual["firstname"] == expected["firstname"]
        assert actual["lastname"] == expected["lastname"]
        assert int(actual["totalprice"]) == int(expected["totalprice"])
        assert bool(actual["depositpaid"]) == bool(expected["depositpaid"])
        assert actual.get("additionalneeds") == expected.get("additionalneeds")

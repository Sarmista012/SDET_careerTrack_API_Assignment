from pathlib import Path
from src.api.booking_client import BookingClient
from src.utils.ini_config import IniConfig
from src.utils.excel_reader import read_booking_payloads_xlsx


def test_should_create_5_bookings_from_excel():
    project_root = Path(__file__).resolve().parents[1]
    cfg = IniConfig(str(project_root / "config" / "restful_booker.ini"))

    payloads = read_booking_payloads_xlsx(str(project_root / "data" / "bookings.xlsx"), sheet_name="Sheet1", limit=5)
    client = BookingClient(cfg)

    created_ids = []
    for p in payloads:
        body = {
            "firstname": p.firstname,
            "lastname": p.lastname,
            "totalprice": p.totalprice,
            "depositpaid": p.depositpaid,
            "bookingdates": {"checkin": p.checkin, "checkout": p.checkout},
            "additionalneeds": p.additionalneeds,
        }
        resp, bookingid = client.create_booking(body)
        assert resp.status_code == 200
        assert "application/json" in resp.headers.get("Content-Type", "").lower()
        assert bookingid is not None
        created_ids.append(bookingid)

    assert len(created_ids) == 5

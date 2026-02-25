
import pytest
from pathlib import Path

import requests

from src.api.booking_client import BookingClient
from src.utils.excel_reader import read_booking_payloads_xlsx
from src.utils.ini_config import IniConfig


@pytest.fixture(scope="session")
def project_root():
    return Path(__file__).resolve().parents[1]

@pytest.fixture(scope="session")
def cfg(project_root):
    return IniConfig(str(project_root / "config" / "restful_booker.ini"))

@pytest.fixture(scope="session")
def booking_client(cfg):
    return BookingClient(cfg)

@pytest.fixture(scope="session")
def created_bookings(project_root, booking_client):
    payloads = read_booking_payloads_xlsx(
        str(project_root / "data" / "bookings.xlsx"),
        sheet_name="Sheet1",
        limit=5
    )

    created = []
    for p in payloads:
        expected_body = {
            "firstname": p.firstname,
            "lastname": p.lastname,
            "totalprice": p.totalprice,
            "depositpaid": p.depositpaid,
            "bookingdates": {"checkin": p.checkin, "checkout": p.checkout},
            "additionalneeds": p.additionalneeds,
        }

        resp, bookingid = booking_client.create_booking(expected_body)
        assert resp.status_code == 200
        assert "application/json" in resp.headers.get("Content-Type", "").lower()
        assert bookingid is not None

        created.append({"id": int(bookingid), "expected": expected_body})

    assert len(created) == 5
    return created

@pytest.fixture(scope="session")
def token(cfg):
    scheme = cfg.get("api", "scheme")
    host = cfg.get("api", "host")
    base_url = f"{scheme}://{host}"


    resp = requests.post(
        base_url + "/auth",
        json={"username": "admin", "password": "password123"},
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        timeout=30,
    )
    assert resp.status_code == 200
    t = resp.json().get("token")
    assert t
    return t

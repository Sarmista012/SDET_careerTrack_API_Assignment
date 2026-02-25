import requests

class BookingClient:
    def __init__(self, cfg):
        self.cfg = cfg
        scheme = cfg.get("api", "scheme")
        host = cfg.get("api", "host")
        self.base_url = f"{scheme}://{host}"

    def create_booking(self, payload: dict):
        url = self.base_url + self.cfg.get("endpoints", "create_booking")
        headers = {
            "Content-Type": self.cfg.get("headers", "content_type"),
            "Accept": "application/json",
        }
        resp = requests.post(url, json=payload, headers=headers, timeout=30)
        bookingid = None
        try:
            bookingid = resp.json().get("bookingid")
        except Exception:
            pass
        return resp, bookingid

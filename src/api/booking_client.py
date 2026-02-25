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

    def get_booking(self, bookingid: int):
        url = self.base_url + f"/booking/{bookingid}"
        headers = {"Accept": "application/json"}
        resp = requests.get(url, headers=headers, timeout=30)
        data = resp.json() if "application/json" in resp.headers.get("Content-Type", "").lower() else None
        return resp, data

    def update_booking(self, bookingid: int, payload: dict, token: str):
        url = self.base_url + f"/booking/{bookingid}"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cookie": f"token={token}",
        }
        resp = requests.put(url, json=payload, headers=headers, timeout=30)
        return resp, resp.json()

    def delete_booking(self, bookingid: int, token: str):
        url = self.base_url + f"/booking/{bookingid}"
        headers = {
            "Content-Type": "application/json",
            "Cookie": f"token={token}",
        }
        return requests.delete(url, headers=headers, timeout=30)

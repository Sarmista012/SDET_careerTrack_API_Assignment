
import requests


class AuthClient:
    def __init__(self, cfg):
        self.cfg = cfg
        scheme = cfg.get("api", "scheme")
        host = cfg.get("api", "host")
        self.base_url = f"{scheme}://{host}"

    def create_token(self) -> tuple[requests.Response, str]:
        path = self.cfg.get("endpoints", "create_token")
        method = self.cfg.get("methods", "create_token").upper()

        username = self.cfg.get("auth", "username")
        password = self.cfg.get("auth", "password")

        token_key = self.cfg.get("response_keys", "create_token_token_key")  # "token"
        expected_ct = self.cfg.get("headers", "content_type")  # "application/json"

        url = f"{self.base_url}{path}"
        payload = {"username": username, "password": password}

        if method != "POST":
            raise ValueError(f"Unsupported method for create_token: {method}")

        resp = requests.post(url, json=payload, headers={"Content-Type": expected_ct}, timeout=30)

        token = resp.json().get(token_key) if resp.headers.get("Content-Type", "").lower().startswith("application/json") else None
        return resp, token

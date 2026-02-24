from src.api.auth_client import AuthClient
from src.utils.ini_config import IniConfig


def test_should_create_auth_token():
    cfg = IniConfig("config/restful_booker.ini")
    client = AuthClient(cfg)
    resp, token = client.create_token()
    print(resp,token)

    expected_status = int(cfg.get("expected_status", "create_token"))
    assert resp.status_code == expected_status
    assert "application/json" in resp.headers.get("Content-Type", "").lower()
    assert token is not None
    assert str(token).strip() != ""

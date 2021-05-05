import pytest
import app
from controllers import album, users

@pytest.fixture
def api(monkeypatch):
    config = {
        'MAIL_SERVER': 'smtp.mailtrap.io',
        'MAIL_PORT': 2525,
        'MAIL_USERNAME': '00015504bf6552',
        'MAIL_PASSWORD': '2730f909f1491b',
        'MAIL_USE_TLS': True,
        'MAIL_USE_SSL': False,
        'MAIL_DEFAULT_SENDER': '37a2ec0935-f570fb@inbox.mailtrap.io',
        'MAIL_SUPPRESS_SEND': True
    }
    flask_app = app.create_app(config)
    test_users = [
        {"id": 1, "email": "test@test.com"}
    ]
    test_albums = [
        {"id": 1, "name": "Guitar", "year-released": 2000}
    ]
    monkeypatch.setattr(users, "users", test_users)
    monkeypatch.setattr(album, "albums", test_albums)
    api = flask_app.test_client()
    return api
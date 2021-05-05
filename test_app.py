import json

def test_welcome(api):
    res = api.get('/')
    assert res.status == '200 OK'
    assert "Hello from Lenny!" in res.json["message"]

def test_all_albums(api):
    res = api.get('/albums')
    assert res.status == '200 OK'
    assert res.json[0] == {'id': 1, 'name': 'Guitar', 'year-released': 2000}

def test_post_albums(api):
    mock_data = json.dumps({'name': 'Piano', 'year-released': 2010})
    mock_headers = {'Content-Type': 'application/json'}
    res = api.post('/albums', data=mock_data, headers=mock_headers)
    assert res.status == '201 CREATED'
    assert res.json['id'] == 2

def test_users_handler(api):
    res = api.get('/users')
    assert res.status == '200 OK'
    assert res.json[0] == {"id": 1, "email": "test@test.com"}

def test_post_users(api):
    mock_data = json.dumps({'email': 'test@testing.com'})
    mock_headers = {'Content-Type': 'application/json'}
    res = api.post('/users', data=mock_data, headers=mock_headers)
    assert res.status == '201 CREATED'
    assert res.json['id'] == 2
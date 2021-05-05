users = [
    {"email": "bob@bobmail.com"}
]

def index(req):
    return users, 200

def create(req):
    new_user = req.get_json()
    new_user["id"] = len(users) + 1
    users.append(new_user)
    return new_user, 201

def all():
    return users
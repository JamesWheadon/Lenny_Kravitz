albums = [
    {'name': 'Let Love Rule', 'year-released': 1989, 'id': 1}, 
    {'name': 'Mama Said', 'year-released': 1991, 'id': 2}, 
    {'name': 'Are You Gonna Go My Way', 'year-released': 1993, 'id': 3}, 
    {'name': 'Circus', 'year-released': 1995, 'id': 4}, 
    {'name': '5', 'year-released': 1998, 'id': 5}, 
    {'name': 'Lenny', 'year-released': 2001, 'id': 6}, 
    {'name': 'Baptism', 'year-released': 2004, 'id': 7}, 
    {'name': 'It Is Time for a Love Revolution', 'year-released': 2008, 'id': 8}, 
    {'name': 'Black and White America', 'year-released': 2011, 'id': 9}, 
    {'name': 'Strut', 'year-released': 2014, 'id': 10}, 
    {'name': 'Raise Vibration', 'year-released': 2018, 'id': 11}
]

def index(req):
    return [a for a in albums], 200

def create(req):
    new_album = req.get_json()
    new_album["id"] = len(albums) + 1
    albums.append(new_album)
    return new_album, 201
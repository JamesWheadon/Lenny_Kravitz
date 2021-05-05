albums = [
    {'name': 'Let Love Rule', 'year-released': 1989, 'id': 1, "img": "https://upload.wikimedia.org/wikipedia/en/0/03/Lenny_Kravitz-Let_Love_Rule_%28album_cover%29.jpg"}, 
    {'name': 'Mama Said', 'year-released': 1991, 'id': 2, "img": "https://upload.wikimedia.org/wikipedia/en/8/88/Lenny_Kravitz-Mama_Said_%28album_cover%29.jpg"}, 
    {'name': 'Are You Gonna Go My Way', 'year-released': 1993, 'id': 3, "img": "https://upload.wikimedia.org/wikipedia/en/0/0f/Lenny_Kravitz-Are_You_Gonna_Go_My_Way.gif"}, 
    {'name': 'Circus', 'year-released': 1995, 'id': 4, "img": "https://upload.wikimedia.org/wikipedia/en/5/53/Lenny_Kravitz_Circus_album_cover.jpg"}, 
    {'name': '5', 'year-released': 1998, 'id': 5, "img": "https://upload.wikimedia.org/wikipedia/en/3/3b/LennyKravitz.jpg"}, 
    {'name': 'Lenny', 'year-released': 2001, 'id': 6, "img": "https://upload.wikimedia.org/wikipedia/en/1/1b/Lenny_Kravitz_Lenny.jpg"}, 
    {'name': 'Baptism', 'year-released': 2004, 'id': 7, "img": "https://upload.wikimedia.org/wikipedia/en/f/f0/Lenny_Kravitz_Baptism.jpg"}, 
    {'name': 'It Is Time for a Love Revolution', 'year-released': 2008, 'id': 8, "img": "https://upload.wikimedia.org/wikipedia/en/9/9d/It_Is_Time_For_A_Love_Revolution.jpg"}, 
    {'name': 'Black and White America', 'year-released': 2011, 'id': 9, "img": "https://upload.wikimedia.org/wikipedia/en/9/91/Black_and_White_America.jpg"}, 
    {'name': 'Strut', 'year-released': 2014, 'id': 10, "img": "https://upload.wikimedia.org/wikipedia/en/0/0a/Strut%2C_cover_by_Lenny_Kravitz.jpg"}, 
    {'name': 'Raise Vibration', 'year-released': 2018, 'id': 11, "img": "https://upload.wikimedia.org/wikipedia/en/9/93/Raise_Vibration_-_LK_album.jpg"}
]

def index(req):
    return [a for a in albums], 200

def create(req):
    new_album = req.get_json()
    new_album["id"] = len(albums) + 1
    albums.append(new_album)
    return new_album, 201
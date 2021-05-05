from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mail import Mail, Message
from controllers import album, users

def create_app(config=None):
    app = Flask(__name__)
    if config:
        app.config.update(config)
    else:
        app.config['MAIL_SERVER']='smtp.mailtrap.io'
        app.config['MAIL_PORT'] = 2525
        app.config['MAIL_USERNAME'] = '00015504bf6552'
        app.config['MAIL_PASSWORD'] = '2730f909f1491b'
        app.config['MAIL_USE_TLS'] = True
        app.config['MAIL_USE_SSL'] = False
        app.config['MAIL_DEFAULT_SENDER'] = '37a2ec0935-f570fb@inbox.mailtrap.io'
        app.config['MAIL_SUPPRESS_SEND'] = False
    mail = Mail(app)
    CORS(app)

    @app.route('/')
    def home():
        return jsonify({"message": "Hello from Lenny!"}), 200

    @app.route('/albums', methods=['GET', 'POST'])
    def albums_handler():
        fns = {
            'GET': album.index,
            'POST': album.create
        }
        resp, code = fns[request.method](request)
        if request.method == 'POST':
            with mail.connect() as conn:
                for user in users.all():
                    message = f"Hey there, come check out Lenny\'s new album, {resp['name']}!"
                    subject = 'New Release 🔥'
                    msg = Message(recipients=[user["email"]], 
                    body=message,
                    subject=subject)
                    with app.open_resource('twelve.jpg') as fp:
                        msg.attach('twelve.jpg', 'image/jpg', fp.read())
                    conn.send(msg)

        return jsonify(resp), code

    @app.route('/users', methods=['GET', 'POST'])
    def users_handler():
        fns = {
            'GET': users.index,
            'POST': users.create
        }
        resp, code = fns[request.method](request)
        if request.method == 'POST':
            msg = Message('Lenny Kravitz', recipients=[resp["email"]])
            msg.body = "Thank you for subscribing!"
            mail.send(msg)
        return jsonify(resp), code
    
    return app

if __name__ == '__main__':
    create_app()
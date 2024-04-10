from flask import Flask
from handlers.segmentation import segment
from handlers.gan import gan

app = Flask(__name__)
app.register_blueprint(segment, url_prefix='/segmentation')
app.register_blueprint(gan, url_prefix='/gan')


@app.get('/')
def check_health():
    return 'hello', 200


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5050
    )
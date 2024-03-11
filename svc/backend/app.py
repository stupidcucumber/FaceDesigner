from flask import Flask
from handlers.segmentation.api import segment

app = Flask(__name__)
app.register_blueprint(segment, url_prefix='/segmentation')


@app.get('/')
def check_health():
    return 'hello', 200


if __name__ == '__main__':
    app.run(
        host='localhost',
        port=5050
    )
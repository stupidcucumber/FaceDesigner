from flask import Flask
from .handlers.segmentation.api import segment

app = Flask(__name__)
app.register_blueprint(segment)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5050
    )
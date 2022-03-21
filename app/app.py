from flask import Flask

from app import routes


def create_app():
    app = Flask(__name__)
    app.add_url_rule('/',  methods=['GET'], view_func=routes.home)
    app.add_url_rule('/files', methods=['GET'], view_func=routes.list_files)
    app.add_url_rule('/calc', methods=['POST'], view_func=routes.calc)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')

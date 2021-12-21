from flask import Flask

from endpoints.ping import ping


def init_app() -> Flask:
    app = Flask(
        __name__,
        template_folder="public",
        static_folder="public",
        static_url_path="/",
    )
    app.register_blueprint(ping, url_prefix="/api/ping")
    return app


app = init_app()

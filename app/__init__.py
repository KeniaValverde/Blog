from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SENDGRID_KEY=os.environ.get('SENGRID_KEY')
    )

    from . import blog

    app.register_blueprint(blog.bp)
  # app.run(debug=True)

    return app
from flask import Blueprint, Flask
from .categories_route import bp_categories
from .tasks_route import bp_tasks

bp_api = Blueprint('api', __name__, url_prefix='/api')

def init_app(app: Flask):
    bp_api.register_blueprint(bp_tasks)
    bp_api.register_blueprint(bp_categories)

    app.register_blueprint(bp_api)

    
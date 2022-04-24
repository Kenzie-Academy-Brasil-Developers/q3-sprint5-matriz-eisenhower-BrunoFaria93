from flask import Blueprint
from app.controllers import tasks_controller

bp_tasks = Blueprint("tasks", __name__, url_prefix="/tasks")

bp_tasks.post('')(tasks_controller.create_task)

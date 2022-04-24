from http import HTTPStatus

from app.configs.database import db
from app.models.tasks import Tasks
from flask import jsonify, request
from psycopg2.errors import UniqueViolation, IntegrityError
from sqlalchemy.orm.session import Session


def create_task():
    try:
        data = request.get_json()

        data_keys = [key for key in data.keys()]

        wrong_key = []

        tasks_columns = [
                "name",
                "description",
                "duration",
                "importance",
                "urgency",
            ]

        for key in data_keys:
                if key not in tasks_columns:
                    wrong_key.append(key)
        
        if len(wrong_key) > 0:
                return {"Chaves válidas": tasks_columns,
                        "Chaves enviadas": wrong_key}, 422

        task = Tasks(**data)

        session: Session = db.session()

        session.add(task)
        session.commit()

        return jsonify(task), HTTPStatus.CREATED

    except IntegrityError as e:
        return {"missing keys": e.args}, HTTPStatus.UNPROCESSABLE_ENTITY

    except KeyError as e:
        return {"missing keys": e.args}, HTTPStatus.UNPROCESSABLE_ENTITY

    except UniqueViolation as e:
        return {"msg": "category already exists!"}, HTTPStatus.CONFLICT

# def update_category(category_id: int):

#     data = request.get_json()
    
#     session: Session = db.session

#     record = session.query(Tasks).get(category_id)

#     if not record:
#         return {"msg": "category not found!"}, HTTPStatus.NOT_FOUND

#     for key, value in data.items():
#         setattr(record, key, value)

#     session.commit()


#     return jsonify(record)

# def delete_category(category_id: int):
#     session: Session = db.session

#     record = session.query(Categories).get(category_id)

#     if not record:
#         return {"msg": "category not found!"}, HTTPStatus.NOT_FOUND

#     session.delete(record)
#     session.commit()

#     return "", HTTPStatus.NO_CONTENT
    # return jsonify(record), HTTPStatus.OK

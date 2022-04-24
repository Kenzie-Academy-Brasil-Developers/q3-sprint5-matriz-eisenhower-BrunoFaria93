from http import HTTPStatus
from flask import request, jsonify
from app.models.categories import Categories
from app.configs.database import db
from sqlalchemy.orm.session import Session

def create_category():
    try:
        data = request.get_json()

        data_keys = [key for key in data.keys()]

        wrong_key = []

        categories_columns = [
                "name",
                "description",
            ]

        for key in data_keys:
                if key not in categories_columns:
                    wrong_key.append(key)
        
        if len(wrong_key) > 0:
                return {"Chaves válidas": categories_columns,
                        "Chaves enviadas": wrong_key}, 422

        if len(data_keys) == 1:
            if type(data['name']) == str or type(data['description']) == str:

                    data['name'] = data['name'].title()

                    category = Categories(**data)

                    session: Session = db.session()

                    session.add(category)
                    session.commit()

                    return jsonify(category), HTTPStatus.CREATED

            else:
                return {"error": "Coloque strings em seus campos!"}, HTTPStatus.BAD_REQUEST

        if len(data_keys) == 2:
            if type(data['name']) == str and type(data['description']) == str:

                    data['name'] = data['name'].title()

                    category = Categories(**data)

                    session: Session = db.session()

                    session.add(category)
                    session.commit()

                    return jsonify(category), HTTPStatus.CREATED

            else:
                return {"error": "Coloque strings em seus campos!"}, HTTPStatus.BAD_REQUEST
    except:
        return {"msg": "category already exists!"}, HTTPStatus.CONFLICT

def update_category(category_id: int):

    data = request.get_json()
    
    session: Session = db.session

    record = session.query(Categories).get(category_id)

    if not record:
        return {"msg": "category not found!"}, HTTPStatus.NOT_FOUND

    for key, value in data.items():
        setattr(record, key, value)

    session.commit()


    return jsonify(record)

def delete_category(category_id: int):
    session: Session = db.session

    record = session.query(Categories).get(category_id)

    if not record:
        return {"msg": "category not found!"}, HTTPStatus.NOT_FOUND

    session.delete(record)
    session.commit()

    return "", HTTPStatus.NO_CONTENT
    # return jsonify(record), HTTPStatus.OK
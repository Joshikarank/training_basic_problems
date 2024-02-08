from core import app as flask, db
from flask import request, json


app = flask()

class Base(db.Model):
    abstract = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

class Question(Base):
    __tablename__ = 'question'
    question = db.Column(db.String, nullable=False)
    person = db.Column(db.String , nullable=False)

@app.route('/', methods=['POST', 'GET'])
def index():
    # print(dir(request))
    q = Question(**request.json)
    db.session.add(q)
    db.session.commit()
    return {'message': 'Successfully added'}, 201


@app.route('/<int:question_id>', methods=['DELETE'])
def remove_question(question_id):
    q = Question.query.get(question_id)
    if q:
        db.session.delete(q)
        db.session.commit()
        return {'message': 'Question deleted successfully'}, 200
    else:
        return {'message': 'Question not found'}, 404

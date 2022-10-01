from app.forms.baseForm import BaseValidation

# Forms.py defines how we validate `form` data usually, but we will validate json payloads as the frontend is decoupled.
# https://json-schema.org/understanding-json-schema/

'''
Model:
    name = db.Column(db.String(64), unique=True)
    title = db.Column(db.String(64))
    author = db.Column(db.String(64))
    description = db.Column(db.String(200))
    body = db.Column(db.Text())
    link = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime())
    tags = db.Column(db.String(200))
'''

class ArticlesValidation(BaseValidation):
    '''
    Validates a given json payload
    '''
    model = {
        "type": "object",
        "description": "Model to validate tasks route",
        "properties": {
            'name': {'type': 'string'},
            'title': {'type': 'string'},
            'author': {'type': 'string'},
            'description': {'type': 'string'},
            'body': {'type': 'string'},
            'link': {'type': 'string'},
            'timestamp': {
                'type': 'string',
                'format': 'date-time'
            }           
        }
    }

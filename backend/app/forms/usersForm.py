from app.forms.baseForm import BaseValidation

# Forms.py defines how we validate `form` data usually, but we will validate json payloads as the frontend is decoupled.
# https://json-schema.org/understanding-json-schema/

'''
Model:
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64))
    password = db.Column(db.String(128))
'''

class UsersValidation(BaseValidation):
    '''
    Validates a given json payload
    '''
    model = {
        "type": "object",
        "description": "Model to validate tasks route",
        "properties": {
            'username': {'type': 'string'},
            'email': {'type': 'string'},
            'password': {'type': 'string'},
        }
    }

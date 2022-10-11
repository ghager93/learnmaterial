import jsonschema

# Forms.py defines how we validate `form` data usually, but we will validate json payloads as the frontend is decoupled.
# https://json-schema.org/understanding-json-schema/

class CodeSnippetsValidation():
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
            },
            'language': {'type': 'string'},
            'tags': {'type': 'string'}           
        }
    }
    @classmethod
    def validate(self, jsonData):
        '''
        Input a jsonData payload, validates and returns 2 variables
        Boolean: Pass/Fail
        Message: String
        '''
        try:
            jsonschema.validate(instance=jsonData, schema=self.model)
        except jsonschema.exceptions.ValidationError as err:
            return False, err
        except Exception as e:
            return False, e
        return True, "Success"

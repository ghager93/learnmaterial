import jsonschema

# Forms.py defines how we validate `form` data usually, but we will validate json payloads as the frontend is decoupled.
# https://json-schema.org/understanding-json-schema/
'''
Model:
'''

class BaseValidation():
    '''
    Validates a given json payload
    '''
    model = {
        "type": "object",
        "description": "Model to validate tasks route",
        "properties": {}
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
import json
import base64

def authorize_token(token:str):
    print(token)
    decoded_token = base64.b64decode(token)
    return decoded_token

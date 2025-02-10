from auth.base64 import authorize_token

token="YWthbnNo"

decoded_token = authorize_token(token)

print(decoded_token)
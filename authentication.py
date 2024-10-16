from functools import wraps
from flask import abort, jsonify, make_response, request
from environment import supabase_secret
import jwt

# Validate token from supabase
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        auth_header = request.headers['Authorization']
        # ensure that the token is present
        if not auth_header or not 'Bearer' in auth_header:
            return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic-realm= "Login required!"'})
        try:
           # decode the token
            token = auth_header.split(' ')[1]
            data = jwt.decode(token, supabase_secret, algorithms=['HS256'], options={"verify_aud": False})
        except:
            return abort(jsonify({"message": "Invalid token!"}), 401)
        return f(*args, **kwargs)
    return decorator
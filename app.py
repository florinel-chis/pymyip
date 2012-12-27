import os

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    #s = request.headers.__repr__()
    s = 'Hello! Your IP is '
    
    if 'X-Forwarded-For' in request.headers:
        s += request.headers['X-Forwarded-For']
    else:
        s += request.remote_addr
        
    return s

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)

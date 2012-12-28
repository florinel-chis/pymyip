import os

from flask import Flask
from flask import request

from socket import inet_aton
from struct import unpack

app = Flask(__name__)

@app.route('/')
def hello():    
    #s = request.headers.__repr__()    
    s = 'Hello! Your IP is '
    #Heroku remote_addr is actually the load balancer in front of the web server so it won't contain the proper ip address
    #display instead X-Forwarded-For which contains the actual ip address
    if 'X-Forwarded-For' in request.headers:
        s += request.headers['X-Forwarded-For']
    else:
        s += request.remote_addr
        
    return s

@app.route('/ip2long/<ip>')
def ip2long(ip):
    
    ip_packed = inet_aton(ip)
    ip_address = unpack("!L", ip_packed)[0]
    return str(ip_address)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)

import os

from flask import Flask
from flask import request

from socket import inet_aton
from struct import unpack

app = Flask(__name__)

def get_ip_address():
    #s = request.headers.__repr__()    
    #Heroku remote_addr is actually the load balancer in front of the web server so it won't contain the proper ip address
    #display instead X-Forwarded-For which contains the actual ip address
    if 'X-Forwarded-For' in request.headers:
        ip_address = request.headers['X-Forwarded-For']
    else:
        ip_address = request.remote_addr
    return ip_address

@app.route('/')
def hello():    
    s = get_ip_address()    
    return s

@app.route('/ip2long')
def ip2long_default():
    ip = get_ip_address()
    return ip2long(ip)

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

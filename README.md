pymyip
======

Heroku What Is My Ip: simple app to display client ip address and useful ip conversion function (ip2long for now).

I use this application to play with Heroku, github and Flask.


Try it http://pymyip.herokuapp.com/

* `/` displays your ip address (X-Forwarded-For if present or remote_addr from request)
* `/ip2long`  displays your ip address converted to long
* `ip2long/<ip_address>` displays a custom ip address (passed as parameter) converted to long

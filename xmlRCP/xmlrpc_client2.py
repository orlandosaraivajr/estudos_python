from xmlrpc.client import ServerProxy
from xmlrpc.client import MultiCall
from xmlrpc.client import Error

ip = '127.0.0.1'
server_xmlrpc = "http://" + ip +":8000"
server = ServerProxy(server_xmlrpc)

try:
    print(server.currentTime.getCurrentTime())
except Error as v:
    print("ERROR", v)

multi = MultiCall(server)
multi.getData()
multi.pow(2, 9)
multi.add(1, 2)
try:
    for response in multi():
        print(response)
except Error as v:
    print("ERROR", v)

from xmlrpc.server import SimpleXMLRPCServer

def is_requisition(n):
    print("Request received with the following argument: " + str(n))
    return n % 2 == 0

server = SimpleXMLRPCServer(("localhost", 9000))
print("Listening on port 9000...")
server.register_function(is_requisition, "is_requisition")
server.serve_forever()
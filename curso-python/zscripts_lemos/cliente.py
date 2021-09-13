import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:9000/") as proxy:
    print("7 é par: %s" % str(proxy.is_requisition(7)))
    print("200 é par: %s" % str(proxy.is_requisition(200)))
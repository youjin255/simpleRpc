import rpclient

c = rpclient.RPCClient()
c.connect('127.0.0.1', 5000)
c.add(1, 2)
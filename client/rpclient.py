import tcpclient
import rpccstub


class RPCClient(tcpclient.Client, rpccstub.RPCStub):
    pass

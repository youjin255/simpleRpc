import tcpserver
import jsonrpc
import rpcstub


class RPCServer(tcpserver.Server, jsonrpc.JSONRPC, rpcstub.RPCStud):
    def __init__(self):
        super(RPCServer, self).__init__()

    def loop(self):
        self.bind_listen(5000)
        while True:
            self.accept_receive_close()

    def on_req(self, req):
        self.from_data(req)
        self.call_method()
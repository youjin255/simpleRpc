this is a simple rpc program

including two parts, rpcserver and rpcclient

this is five parts in server:
    tcpserver: procedure a tcp server
    jsonrpc: procedure the request data
    rpcstub: register functions that client can call

    rpcserver: use the three parts above to create a rpcserver
    servermain: run the rpcserver


this is four parts in client:
    tcpclient: procudure a tcp client
    rpccstub: divide function call into function name and args
    rpcclient:  bring tcpclient and rpccstub together

    clientmain: run the rpcclient


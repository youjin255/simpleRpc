import json


class RPCStub(object):
    def __getattr__(self, item):
        def func(*args, **kwargs):
            data = {'method_name': item, 'method_args': args, 'method_kwargs': kwargs}
            self.send(json.dumps(data).encode('utf-8'))

        setattr(self, item, func)
        return func
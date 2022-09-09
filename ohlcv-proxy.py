# coding=utf-8

from mprpc import RPCServer
import msgpackrpc
#class OhlcvProxyServer (RPCServer):
class OhlcvProxyServer (object):

    def __init__ (self):
        super().__init__()
        self.adaptors = {}

    def register_adaptor (self, adaptor):
        self.adaptors[adaptor.tickerid] = adaptor

    def ohlcv (self, tickerid, resolution, count):
        return self.adaptors[tickerid].ohlcv(resolution, count)
        
    def step_ohlcv (self, tickerid, resolution, next_clock):
        return self.adaptors[tickerid].step_ohlcv(resolution, next_clock)

if __name__ == '__main__':
    import os
    from gevent.server import StreamServer
    from pine.market.bitmex import BitMexOhlcAdaptor
    from pine.market.bitflyer import BitFlyerOhlcAdaptor
    from pine.market.base import PROXY_PORT

    server = OhlcvProxyServer()
    server.register_adaptor(BitMexOhlcAdaptor())
    server.register_adaptor(BitFlyerOhlcAdaptor())

    port = int(os.environ.get('PORT', PROXY_PORT))
    #server = StreamServer(('127.0.0.1', port), server)
    #server.serve_forever()
    server = msgpackrpc.Server(server, unpack_encoding='utf-8')
    server.listen(msgpackrpc.Address('0.0.0.0', port))
    server.start()

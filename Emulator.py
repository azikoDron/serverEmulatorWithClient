from lxml import etree
from spyne.protocol.soap import Soap11
from spyne import Application, ServiceBase, Unicode, rpc
from spyne.server.wsgi import WsgiApplication


class Soap(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def in_soap(ctx, words):
        print('Connection detected: ', ctx.in_document)
        some_method = str(words).capitalize()
        return some_method


app = Application([Soap], tns='words', in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())
application = WsgiApplication(app)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('localhost', 8010, application)
    server.serve_forever()

class QueryBus:

    def __init__(self):
        self.handlers = {}

    def register_handler(self, query_cls, handler):
        self.handlers[query_cls] = handler

    def handle(self, query):
        handler = self.handlers.get(type(query))
        if handler:
            handler.handle(query)
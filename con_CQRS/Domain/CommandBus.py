
class CommandBus:

    def __init__(self):
        self.handlers = {}

    def register_handler(self, command_cls, handler):
        self.handlers[command_cls] = handler

    def handle(self, command):
        handler = self.handlers.get(type(command))
        if handler:
            handler.handle(command)
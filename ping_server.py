from minindn.apps.application import Application

class PingServer(Application):
    prefix: str

    def __init__(self, node):
        Application.__init__(self, node)
        self.logFile = 'pingserver.log'
        self.prefix = f'/{node.name}'

    def start(self):
        Application.start(self, ['ndnpingserver', self.prefix], logfile=self.logFile)
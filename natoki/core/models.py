
class Client:
    def __init__(self):
        self.input = None
        self.output = None


class Enrollment(object):
    def __init__(self, client, role):
        self.client = client
        self.role = role


class Channel(object):
    def __init__(self):
        self.clients = []


class Interface(object):
    pass
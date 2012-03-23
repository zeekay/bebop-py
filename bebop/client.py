import json
import socket


class Client(object):
    '''
    Client object for communicating with Bebop's TCP interface.
    '''
    def __init__(self, host='127.0.0.1', port=9128):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.socket.settimeout(5)

    def send(self, data):
        self.socket.sendall(data)

    def recv(self):
        res = ''
        while True:
            data = self.socket.recv(1024)
            if '\r\n' in data:
                res += data
                break
            res += data
        res = json.loads(res)
        if res.get('result'):
            return res['result']

    def close(self):
        self.socket.close()


def eval(code):
    '''
    Sends code to Bebop, which will be run in browser.
    '''
    c = Client()
    c.send(json.dumps({'evt': 'eval', 'msg': code}))
    result = c.recv()
    c.close()
    return result


def complete(obj):
    '''
    Asks bebop to return a list of properties on a given object.
    '''
    c = Client()
    c.send(json.dumps({'evt': 'complete', 'msg': obj}))
    result = c.recv()
    c.close()
    return result

from thrift.Thrift import TApplicationException
from PlinePMD.Core import *
class Auth(object):

    def __init__(self, ip, op=None):
        self.ip = self.op = ip
        if op is not None:
            self.op = op
        self.seq = 0

    def sendLogin(self, loginRequest):
        self.op.writeMessageBegin('loginZ', 0x01, self.seq)
        args = loginArgs()
        args.loginRequest = loginRequest
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvLogin(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = loginResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(0x05, "Login failed")
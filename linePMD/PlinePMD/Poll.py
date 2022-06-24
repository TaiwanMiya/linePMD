from thrift.Thrift import TApplicationException
from PlinePMD.Core import *
class Poll(object):

    def __init__(self,ip,op=None) -> None:
        self.ip = self.op = ip
        if op is not None:
            self.op = op
        self.seq = 0

    def sendGetLastOpRevision(self):
        self.op.writeMessageBegin('getLastOpRevision', 0x01, self.seq)
        args = getLastOpRevisionArgs()
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvGetLastOpRevision(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = getLastOpRevisionResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(0x05, "GetLastOpRevision failed")

    def sendOperations(self, localRev, count):
        self.op.writeMessageBegin('fetchOperations', 0x01, self.seq)
        args = OperationsArgs()
        args.localRev = localRev
        args.count = count
        args.write(self.op)
        self.op.writeMessageEnd()
        self.op.trans.flush()

    def recvOperations(self):
        ip = self.ip
        (_, mtype, _) = ip.readMessageBegin()
        if mtype == 0x03:
            x = TApplicationException()
            x.read(ip)
            ip.readMessageEnd()
            raise x
        result = OperationsResult()
        result.read(ip)
        ip.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(0x05, "Operations failed")
from PlinePMD.Tools import ThreadingPMD,TthriftPMD
from PlinePMD.Poll import Poll
class Reply(object):

    def __init__(self,sender,count=1):
        self.sender = sender
        self.count = count
        self.sender.node.mid = self.sender.profile.mid
        self.sender.poll = Poll(TthriftPMD(site=self.sender.conf.Hosts+self.sender.conf.poll,headers=self.sender.header).TrequestsPMD)
        self.sender.poll.sendGetLastOpRevision()
        self.sender.revision = self.sender.poll.recvGetLastOpRevision()
        ThreadingPMD(self.sender.node.TaskResult).start()

    def Operation(self, revision, count=1):
        self.sender.poll.sendOperations(revision, count)
        return self.sender.poll.recvOperations()

    def SettingsRevision(self,revision):
        self.sender.revision = max(revision, self.sender.revision)

    @property
    def Trace(self):
        try:
            operations = self.Operation(self.sender.revision, count=self.count)
        except:return
        if operations is None:return []
        else:return operations
import traceback
from PlinePMD.Core import TalkException
from PlinePMD.Tools import LineRsaKeyPMD, ThreadingPMD,TthriftPMD,ProcessServerPMD
from PlinePMD.Auth import Auth,LoginJoined
from PlinePMD.Talk import Talk

class Login(object):

    def __init__(self):
        self.account = str()
        self.password = str()
        self.cert = str()
        self.hostA = None
        self.appType = None
        self.systemName = None
        self.keepLoggedIn = None
        self.conf = None
        self.header = dict()
        self.node = None

    @property
    def LineLoad(self):
        self.node.app = self.conf.appList
        self.talk = Talk(TthriftPMD(site=self.conf.Hosts+self.conf.api,headers=self.header).TrequestsPMD)
        self.talk.sendGetProfile()
        self.profile = self.talk.recvGetProfile()

    def mail(self):
        if not self.password:raise Exception('Please enter your account')
        if self.cert == str() or self.cert == None:
            CRT = ThreadingPMD(self.node.MailFirst,args=(self.account,))
            CRT.start()
        self.node.type = 0x1
        self.header = {
            'X-Line-Application':self.conf.appList
        }
        self.talk = Talk(TthriftPMD(site=self.conf.Hosts+self.conf.url,headers=self.header,OPEN=False).TrequestsPMD)
        self.talk.sendGetRSAKey(1)
        rsakey = self.talk.recvGetRSAKey()
        crypto = LineRsaKeyPMD(rsakey.sessionKey,rsakey.nvalue,rsakey.evalue,self.account,self.password).DealWith
        self.auth = Auth(TthriftPMD(site=self.conf.Hosts+self.conf.login,headers=self.header,OPEN=False).TrequestsPMD)
        log = LoginJoined()
        log.type = 0
        log.identityProvider = 0
        log.identifier = rsakey.keynm
        log.password = crypto
        log.keepLoggedIn = self.keepLoggedIn
        log.accessLocation = self.conf.accessLocation
        log.systemName = self.conf.systemName
        try:
            CRT.join()
            self.cert = CRT.getResult()
        except UnboundLocalError:...
        log.certificate = self.cert
        log.e2eeVersion = 0
        self.auth.sendLogin(log)
        res = self.auth.recvLogin()
        if res.authToken:
            yield f'Token -> \n{res.authToken}'
        if res.pinCode is not None and res.type == 3:
            yield f'PinCode -> \n{res.pinCode}'
            self.header = {
                'X-Line-Application':self.conf.appList,
                'X-Line-Access': res.verifier
            }
            processKey = ProcessServerPMD(self.conf.Hosts+self.conf.qr,self.header).GainSessionJson(headerJoined=True)
            self.auth = Auth(TthriftPMD(site=self.conf.Hosts+self.conf.login,headers=self.header,OPEN=False).TrequestsPMD)
            try:
                log = LoginJoined()
                log.type = 1
                log.identityProvider = 1
                log.accessLocation = self.conf.accessLocation
                log.systemName = self.conf.systemName
                log.keepLoggedIn = self.keepLoggedIn
                log.verifier = processKey['result']['verifier']
                log.e2eeVersion = 0
                self.auth.sendLogin(log)
                res = self.auth.recvLogin()
            except TalkException as error:
                raise TalkException(error)
            if res.certificate is not None:
                self.cert = res.certificate
                yield f'Cert -> \n{self.cert}'
                yield f'Token -> \n{res.authToken}'

        self.header = {
            'X-Line-Application': self.conf.appList,
            'X-Line-Access': res.authToken
        }
        self.authToken = res.authToken
        yield 'Mail Login...'
        self.node.acc = self.account
        self.node.pwd = self.password
        self.node.cert = self.cert
        self.node.token = self.authToken
        self.LineLoad

    def token(self):
        self.node.type = 0x2
        self.header = {
            'X-Line-Application': self.conf.appList,
            'X-Line-Access': self.account
        }
        yield 'Token Login...'
        self.authToken = self.account
        self.node.token = self.account
        self.LineLoad
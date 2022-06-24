from PlinePMD.Login import Login
from PlinePMD.Config import config
from PlinePMD.Tools import RegexPMD
from PlinePMD.Linq import Initial
from PlinePMD.SmsActivate import Activate

class linePMD(Login):

    def __init__(self,account=None,password=None,cert=None,host=None,appType=None,systemName=None,keepLoggedIn=True):
        self.account = account
        self.password = password
        self.cert=cert
        self.host=host
        self.appType=appType
        self.systemName=systemName
        self.keepLoggedIn = keepLoggedIn
        self.conf = config(Mhost=self.host,MappType=self.appType,SystemName=self.systemName)
        self.node = Initial()
        self.logintype : int = 0
        if RegexPMD(r'[^@]+@[^@]+\.[^@]+',account).regex != None:
            for msg in self.mail():
                print(msg)
            self.logintype = 1
        elif RegexPMD(r'[\d\w\/\+]{20}\.[\d\w\/\+]{22}\.[\d\w\/\+]{43}=$',account).regex != None:
            for msg in self.token():
                print(msg)
            self.logintype = 2
        else:
            raise ValueError('Invalid email and token, please re-enter ^^')

class smsPMD(Activate):
    
    def __init__(self,apikey=None):
        if not apikey:raise ValueError('Please enter your smsactivate apikey\nOfficial website -> https://api.sms-activate.org')
        Activate.__init__(self)
        self.apikey = apikey
from ClinePMD.cinclude.Initial import linePMD
from ClinePMD.cinclude.Tools import RegexPMD,ThreadingPMD,StringConversionPMD,Switch
from ClinePMD.cinclude.Replys import Reply
from ClinePMD.cinclude.Service import service,TalkException
from UI.MainProgram import Transfer
from UI.Integrate import *
import traceback
import os
import sys

class Cclasses(object):

    def __init__(self,MailORToken=None,PWD=None,Cert=None,count=None,servo=None) -> None:
        self.MailORToken = MailORToken
        self.PWD = PWD
        self.Cert = Cert
        self.bk = None
        self.backdoor = str()
        self.owner = list()
        self.admin = list()
        self.ERROR = ''
        self.count = count
        self.servo = servo

    def Initial(self) -> bool:
        try:
            self.main = linePMD(self.MailORToken,self.PWD,self.Cert)
            if self.main.logintype == 1:
                Transfer.UserUpdate(self.count,'token',self.main.authToken)
                Transfer.UserUpdate(self.count,'cert',self.main.cert)
                if self.servo:
                    Transfer.SetServoResult(code=0,result=['login','mail','success'])
                    Transfer.SetPidOnDos()
            elif self.main.logintype == 2:
                if self.servo:
                    Transfer.SetServoResult(code=0,result=['login','token','success'])
                    Transfer.SetPidOnDos()
        except TalkException as error:
            if error.code in [1,8]:
                Transfer.UserUpdate(self.count,'token','None')
                if self.servo:
                    Transfer.SetServoResult(code=1,result=str(error).splitlines())
                return print(error)
            elif error.code == 35:
                Transfer.UserUpdate(self.count,'token','None')
                Transfer.UserUpdate(self.count,'account','None')
                Transfer.UserUpdate(self.count,'password','None')
                Transfer.UserUpdate(self.count,'cert','None')
                if self.servo:
                    Transfer.SetServoResult(code=1,result=str(error).splitlines())
                return print(error)
            else:
                return print(error)
        self.svo = service(self.main)
        if self.backdoor in ['',None]:
            raise ValueError('You have not set the backdoor ><')
        try:
            self.svo.SendMessage(self.backdoor,f'Mymid >>>\n{self.main.profile.mid}\nMyName >>>\n{self.main.profile.displayName}\nAnd then login successfully ^^')
        except TalkException:
            ...
        self.repl = Reply(self.main,50)
        if self.servo:
            ThreadingPMD(UpdateFunction(self.svo).GetAllGroupsAndMembers()).start()
        self.LoopsPoll()

    def LoopsServo(self):
        DealData = [None] * 4
        while 1:
            try:
                for datatype,data in Transfer.GetServoArgs():
                    for case in Switch(datatype):
                        if case(1):
                            DealData[0] = data
                            break
                        if case(2):
                            DealData[1] = data
                            break
                        if case(3):
                            DealData[2] = int(data)
                            break
                        if case(4):
                            DealData[3] = data
                            break
                        if case(5):
                            self.owner.clear()
                            self.admin.clear()
                            self.backdoor = ''
                            break
                        if case(6):
                            self.admin.append(data)
                            break
                        if case(7):
                            self.owner.append(data)
                            break
                        if case(8):
                            self.backdoor = data
                            break
                        if case(None):
                            DealData = [None] * 4
                            break
                if DealData != [None] * 4:
                    new = DealWith(self.main,self.svo,self.owner,self.admin,self.backdoor)
                    new.args = DealData
                    new.servo = True
                    DealData = [None] * 4
                    new.DealWith()
            except:continue
            finally:DealData = [None] * 4

    def LoopsPoll(self):
        if self.servo:
            ThreadingPMD(self.LoopsServo).start()
        while 1:
            try:
                ts = self.repl.Trace
                if ts != None:
                    for params in ts:
                        try:
                            DealWith(self.main,self.svo,self.owner,self.admin,self.backdoor,params,servo=self.servo).DealWith()
                            self.repl.SettingsRevision(params.revision)
                        except ValueError:assert ValueError(),"Invaild Value ><"
                        except RuntimeError:assert RuntimeError(),"Invaild Runtime ><"
                        except Exception:
                            self.ERROR = traceback.format_exc() if traceback.format_exc() != self.ERROR else os._exit(0)
                            print(self.ERROR)
                        finally:...
            except Exception:assert Exception(),'Please turn it off asap ^^~'
            finally:continue

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, self.__class__) and self.__dict__ == __o.__dict__

    def __ne__(self, __o: object) -> bool:
        return not (self == __o)

class UpdateFunction(object):

    def __init__(self,svo:service) -> None:
        self.svo = svo

    def GetAllGroupsAndMembers(self):
        GroupInfo = self.svo.GetGroups(self.svo.GetGroupids())
        Index : list = []
        for group in GroupInfo:
            Index.append('this new groups')
            Index.extend([group.name,group.id])
            for i in group.members:
                Index.extend([i.displayName,i.mid])
        Transfer.SetServoResult(code=0,result=Index)

class DealWith(object):

    def __init__(self,main:linePMD,sv:service,owner,admin,backdoor,op=None,servo=False) -> None:
        self.main = main
        self.sv = sv
        self.owner = list(set(owner))
        self.admin = list(set(admin))
        self.backdoor = backdoor
        self.op = op
        self.args = None
        self.servo = servo

    def DealWith(self):
        if self.args:
            self.to = self.args[0]
            self.text : str = self.args[1]
            self.type : int = self.args[2]
            self.be = self.args[3]
            self.id = None
            self.reid = None
            self.data = None
            if '->' in self.text:
                orderly = self.text.split('->')
                for i in orderly:
                    self.text = i.strip()
                    self.MessageEventUI()
            else:
                return self.MessageEventUI()

        elif self.op.type in [25,26]:
            if self.op.message.text != None:
                self.text : str = self.op.message.text
                self.to = self.op.message.to
                self.id = self.op.message.id
                self.be = self.op.message._from
                self.reid = self.op.message.relatedMessageId
                self.data = self.op.message.contentMetadata
                self.type = self.op.message.contentType
                if self.type == 0:
                    if '->' in self.text:
                        orderly = self.text.split('->')
                        for i in orderly:
                            self.text = i.strip()
                            self.MessageEventUI()
                    else:
                        return self.MessageEventUI()
                elif self.type == 13:
                    return self.ContactEventUI()

        elif self.op.type in [13,124]:
            self.p1 = self.op.param1
            self.p2 = self.op.param2
            self.p3 = self.op.param3
            return self.InviteEventUI()

        else:return

    def AdmixDealWith(self,admix:Integrate,Method):
        if RegexPMD(r'^0([bdox])([\da-f]+)',Method).regex != None:
            func = RegexPMD(r'0([bdox])([\da-f]+)',Method).regexlist[0]
            if RegexPMD(admix.NewCode[func[0]][1],func[1]).regex == None:
                return self.sv(self.to,admix.Errors[0],self.id if self.id else None)
            Coding = StringConversionPMD(text=func[1],carry=admix.NewCode[func[0]][0])
            Coding.read
            admix.carry = Coding.byte
            return 0x1
        elif RegexPMD(r'^-\w+',Method).regex != None:
            admix.command = Method
            return 0x2

    def RegularExpressions(self,text,port=0):
        ADMIN = (
            r'^sp$',
            r'^sp[\s]?(-\w+|0([bdox])([\da-f]+))[\s]?[\d]*',
            r'^mid[\s]?(-?\w?|0([bdox])([\da-f]))[\s]?.*',
            r'^gid[\s]?(-?\w?|0([bdox])([\da-f]+))[\s]?.*',
            r'^send[\s]?(-\w+|0([bdox])([\da-f]+))[\s]?.*',
            r'^thread[\s]?(-\w+|0([bdox])([\da-f]+))[\s]?',
            r'^friend[\s]?(-\w+|0([bdox])([\da-f]+))[\s]?.*',
            r'^msg[\s]?(-\w+|0([bdox])([\da-f]+))[\s]?.*',
            r'^0([bdox])([01]+|[0-8]+|[\d]+|[\da-f]+)[\s]?-h',
            r'^url[\s]?(-\w+|0([bdox])([\da-f]+))[\s]?.*',
            r'^act[\s]?(-\w+|0([bdox])([\da-f]+))[\s]?.*'
        )
        OWNER = (
            r'^admin[\s]?(-\w|0([bdox])([\da-f]+))[\s]?.*',
            r'^cmd$',
            r'^out$',
            r'^out[\s]?@.+',
            r'^reb$',
            r'^reb[\s]?@.+',
            r'^signout$',
            r'^signout[\s]?@.+'
        )
        for case in Switch(port):
            if case(0):
                INDEX = ADMIN
                break
            if case(1):
                INDEX = OWNER
                break
        for re in range(len(INDEX)):
            if RegexPMD(INDEX[re],text).regex != None:
                return 0x01 << re

    def FindMembersId(self,text):
        mids = RegexPMD(r'u[\da-f]{32}',text).regexlist
        try:
            MENTION = eval(self.data['MENTION'])['MENTIONEES']
            [mids.append(i['M']) for i in MENTION]
        except:...
        if self.reid:
            message = self.sv.GetRecentMessages(self.to)
            for msg in message:
                if msg.id == self.reid:
                    mids.extend(RegexPMD(r'u[\da-f]{32}',msg.text).regexlist)
                    try:
                        MENTION = eval(msg.contentMetadata['MENTION'])['MENTIONEES']
                        mids.extend([i['M'] for i in MENTION])
                    except:...
        return mids

    def FindGroupsId(self,text):
        gids = RegexPMD(r'c[\da-f]{32}',text).regexlist
        if self.reid:
            message = self.sv.GetRecentMessages(self.to)
            for msg in message:
                if msg.id == self.reid:
                    gids.extend(RegexPMD(r'c[\da-f]{32}',msg.text).regexlist)
        return gids

    def FindGroupUrlId(self,text):
        urls = RegexPMD(r'[htp:|htps:]?/?/?line\.me/?R?/ti/g/([\w-]{10})',text).regexlist
        if self.reid:
            message = self.sv.GetRecentMessages(self.to)
            for msg in message:
                if msg.id == self.reid:
                    urls.extend(RegexPMD(r'[htp:|htps:]?/?/?line\.me/?R?/ti/g/(\w{10})',msg.text).regexlist)
        return urls

    def InviteEventUI(self):
        try:

            if self.p2 in (self.admin or self.owner):
                if self.main.profile.mid == self.p3:
                    self.sv.IntoGroup(self.p1)
                    p2id = self.sv.SendContact(self.p1,self.p2).id
                    self.sv.SendMessage(self.p1,'Joined the group successfully ^^\nNamed >>> %s\nGroupId >>> %s\nInviter mid >>> %s\nAnd inviter contact on top^' % (self.sv.GetGroup(self.p1).name,self.p1,self.p2),p2id)
                    if self.servo:
                        ThreadingPMD(UpdateFunction(self.sv).GetAllGroupsAndMembers()).start()
        
        except:
            error = traceback.format_exc()
            print(error)
            if self.servo:
                Transfer.SetServoResult(code=1,result=error.splitlines())
        finally:return

    def ContactEventUI(self):
        try:
            if self.be in (self.admin or self.owner):
                contact = self.data['mid']
                self.sv.SendMessage(self.to,str(self.sv.GetContact(contact)))
        except:
            error = traceback.format_exc()
            print(error)
            if self.servo:
                Transfer.SetServoResult(code=1,result=error.splitlines())
        finally:return

    def MessageEventUI(self,msg = lambda sv,to,message,id=None,data=None,type=0: sv.SendMessage(to,message,id,data,type)):
        try:

            if self.be in CMD:
                CMD.remove(self.be)
                try:return exec(self.text)
                except:
                    log = traceback.format_exc()
                    try:msg(self.sv,self.to,log,self.id if self.id else None)
                    except:print(log)

            text = self.text.casefold()
            admix = Integrate(self.sv,self.to,self.id if self.id else None,self.be,self.reid,self.data,self.type)
            if self.be in (self.admin or self.owner):

                mew : int = self.RegularExpressions(text)

                for case in Switch(mew):
                    if case(0x0001):
                        return Speed(admix).Command
                    
                    if case(0x0002):
                        Tuples = RegexPMD(r'sp[\s]?(-\w+|0[bdox][\da-f]+)[\s]?(\d*)',text).regexlist[0]
                        ADMIX = self.AdmixDealWith(admix,Tuples[0])
                        admix.args = 1 if Tuples[1] == str() else int(Tuples[1])
                        if ADMIX == 0x1:
                            return exec(Speed(admix).Carry)
                        elif ADMIX == 0x2:
                            return Speed(admix).Command

                    if case(0x0004):
                        Method = RegexPMD(r'mid[\s]?(-\w+|0[bdox][\da-f]+)',text).regexlist
                        admix.args = self.FindMembersId(text)
                        if Method != list():
                            ADMIX = self.AdmixDealWith(admix,Method[0])
                            if ADMIX == 0x1:
                                return exec(Contact(admix).Carry)
                            elif ADMIX == 0x2:
                                return Contact(admix).Command
                        else:
                            return Contact(admix).Command

                    if case(0x0008):
                        Method = RegexPMD(r'gid[\s]?(-\w+|0[bdox][\da-f]+)',text).regexlist
                        admix.args = self.FindGroupsId(text)
                        if Method != list():
                            ADMIX = self.AdmixDealWith(admix,Method[0])
                            if ADMIX == 0x1:
                                return exec(Group(admix).Carry)
                            elif ADMIX == 0x2:
                                return Group(admix).Command
                        else:
                            return Group(admix).Command

                    if case(0x0010):
                        Tuples = RegexPMD(r'send[\s]?(-\w+|0[bdox][\da-f]+)[\s]?(\d*)[\s]?(.*)',text).regexlist[0]
                        Method = Tuples[0]
                        admix.args = (int(Tuples[1]) if Tuples[1].isdecimal() else 1,Tuples[2] if Tuples[2] != str() else '^^')
                        ADMIX = self.AdmixDealWith(admix,Method)
                        if ADMIX == 0x1:
                            return exec(Send(admix).Carry)
                        elif ADMIX == 0x2:
                            return Send(admix).Command

                    if case(0x0020):
                        Tuples = RegexPMD(r'thread[\s]?(-\w+|0[bdox][\da-f]+)[\s]?(\d+)?',text).regexlist[0]
                        Method = Tuples[0]
                        admix.args = (0 if Tuples[1] == str() else int(Tuples[1]),linePMD,self.main.authToken,service)
                        ADMIX = self.AdmixDealWith(admix,Method)
                        if ADMIX == 0x1:
                            return exec(Thread(admix).Carry)
                        elif ADMIX == 0x2:
                            return Thread(admix).Command

                    if case(0x0040):
                        Method = RegexPMD(r'friend[\s]?(-\w+|0[bdox][\da-f]+)',text).regexlist[0]
                        admix.args = self.FindMembersId(text)
                        ADMIX = self.AdmixDealWith(admix,Method)
                        if ADMIX == 0x01:
                            return exec(Friend(admix).Carry)
                        elif ADMIX == 0x02:
                            return Friend(admix).Command

                    if case(0x0080):
                        Tuples = RegexPMD(r'msg[\s]?(-\w+|0[bdox][\da-f]+)[\s]?(\d+)?.*',text).regexlist[0]
                        admix.args = (self.main.profile.mid,Tuples[1],self.FindGroupsId(text))
                        ADMIX = self.AdmixDealWith(admix,Tuples[0])
                        if ADMIX == 0x01:
                            return exec(Message(admix).Carry)
                        elif ADMIX == 0x02:
                            return Message(admix).Command

                    if case(0x0100):
                        func = RegexPMD(r'^0([bdox])([\da-f]+)',text).regexlist[0]
                        if RegexPMD(admix.NewCode[func[0]][1],func[1]).regex == None:
                            return msg(self.to,'Invaild Carry ~',self.id if self.id else None)
                        Coding = StringConversionPMD(text=func[1],carry=admix.NewCode[func[0]][0])
                        Coding.read
                        Func = Coding.byte
                        return msg(self.sv,self.to,'Carry Helper\nIO >>> Binary:\n0b{:b}\nIO >>> Octal\n%#o\nIO >>> Decimal:\n%d\nIO >>> HexaDecimal:\n%#x'.format(Func) % (Func,Func,Func),self.id if self.id else None)

                    if case(0x0200):
                        Tuples = RegexPMD(r'url[\s]?(-\w+|0[bdox][\da-f]+)[\s]?.*',text).regexlist
                        admix.args = (self.FindGroupUrlId(self.text),self.FindGroupsId(text),Tuples[0])
                        ADMIX = self.AdmixDealWith(admix,Tuples[0])
                        if ADMIX == 0x01:
                            exec(GroupUrl(admix).Carry)
                        elif ADMIX == 0x02:
                            GroupUrl(admix).Command
                        if self.servo:
                            ThreadingPMD(UpdateFunction(self.sv).GetAllGroupsAndMembers()).start()

                    if case(0x0400):
                        Tuples = RegexPMD(r'act[\s]?(-\w+|0[bdox][\da-f]+)[\s]?.*',text).regexlist
                        admix.args = (self.FindMembersId(text),self.FindGroupsId(text),self.admin)
                        ADMIX = self.AdmixDealWith(admix,Tuples[0])
                        if ADMIX == 0x01:
                            exec(GroupAct(admix).Carry)
                        elif ADMIX == 0x02:
                            GroupAct(admix).Command
                        if self.servo:
                            ThreadingPMD(UpdateFunction(self.sv).GetAllGroupsAndMembers()).start()

                    if case(0x0800):
                        ...

            if self.be in self.owner:

                mew : int = self.RegularExpressions(text,1)

                for case in Switch(mew):
                    if case(0x0001):
                        Method = RegexPMD(r'admin[\s]?(-\w|0[bdox][\da-f]+)[\s]?.*',text).regexlist[0]
                        admix.args = (self.FindMembersId(text),self.admin)
                        ADMIX = self.AdmixDealWith(admix,Method)
                        if ADMIX == 0x1:
                            exec(Admin(admix).Carry)
                        elif ADMIX == 0x2:
                            Admin(admix).Command
                        if admix.result != None:
                            self.admin = admix.result
                            return Transfer.Reboot(self.admin,self.owner,self.backdoor)

                    if case(0x0002):
                        CMD.append(self.be)
                        return msg(self.sv,self.to,'I\'m get ready ~\nplease enter your code ^^\nPython >>>',self.id if self.id else None)

                    if case(0x0004):
                        try:
                            self.sv.LeaveGroup(self.to)
                            if self.servo:
                                ThreadingPMD(UpdateFunction(self.sv).GetAllGroupsAndMembers()).start()
                        except TalkException:
                            try:
                                self.sv.LeaveRoom(self.to)
                                if self.servo:
                                    ThreadingPMD(UpdateFunction(self.sv).GetAllGroupsAndMembers()).start()
                            except TalkException as error:
                                error.code = 0
                                error.reason = 'Failed to exit\n%s' % self.to
                                error.parameterMap = {}
                                raise TalkException(error)

                    if case(0x0008):
                        MENTION = eval(self.data['MENTION'])['MENTIONEES']
                        try:
                            return [self.sv.LeaveGroup(self.to) if i['M'] == self.main.profile.mid else ... for i in MENTION]
                        except TalkException:
                            return [self.sv.LeaveRoom(self.to) if i['M'] == self.main.profile.mid else ... for i in MENTION]

                    if case(0x0010):
                        msg(self.sv,self.to,f'Restart ><\n{Transfer.TimeNow()}')
                        Transfer.Reboot(self.admin,self.owner,self.to)
                        sys.stdout.flush()
                        os.execv(sys.executable, [sys.executable] + sys.argv)

                    if case(0x0020):
                        MENTION = eval(self.data['MENTION'])['MENTIONEES']
                        Transfer.Reboot(self.admin,self.owner,self.to)
                        sys.stdout.flush()
                        return [msg(self.sv,self.to,f'Restart ><\n{Transfer.TimeNow()}') & os.execv(sys.executable, [sys.executable] + sys.argv) if i['M'] == self.main.profile.mid else ... for i in MENTION]

                    if case(0x0040):
                        msg(self.sv,self.to,f'Signout ><\n{Transfer.TimeNow()}')
                        os._exit(0)

                    if case(0x0080):
                        MENTION = eval(self.data['MENTION'])['MENTIONEES']
                        return [msg(self.sv,self.to,f'Signout ><\n{Transfer.TimeNow()}') & os._exit(0) if i['M'] == self.main.profile.mid else ... for i in MENTION]

        except:
            error = traceback.format_exc()
            print(error)
            if self.servo:
                Transfer.SetServoResult(code=1,result=error.splitlines())
        finally:return
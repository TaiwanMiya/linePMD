from UI.MainProgram import Transfer
import time
import numpy as np
IsCobject = True
try:
    from ClinePMD.cinclude.Tools import ThreadingPMD,Switch
    from ClinePMD.cinclude.Core import TalkException
    from ClinePMD.cinclude.Service import service
    from ClinePMD.Complie.C_include.SpeedTest import Ttime
    from ClinePMD.Complie.C_include.C_accelerate import AccSingle,AccList
except ImportError:
    from PlinePMD.Tools import ThreadingPMD,Switch
    from PlinePMD.Core import TalkException
    from PlinePMD.Service import service
    IsCobject = False

TASK = list()
TASKS = list()
CMD = list()
np.set_printoptions(precision=17, threshold=17, edgeitems=17, linewidth=75, suppress=True, nanstr='nan', infstr='inf')

class Integrate(object):

    NewCode = {
        'b':[2,r'[01]+'],
        'o':[8,r'[0-8]+'],
        'd':[10,r'[\d]+'],
        'x':[16,r'[\da-f]+']
        }

    Errors = (
        'Invaild Carry ><',
        'Failed to load the C environment ><\nTherefore, it is not possible to use the C language to measure the speed ~'
    )

    def __init__(self,sv:service,to,ID,be,reid,data,type,command:str='',carry=None,*args) -> None:
        self.sv = sv
        self.to = to
        self.id = ID
        self.be = be
        self.reid = reid
        self.data = data
        self.type = type
        self.command = command
        self.carry = carry
        self.args = args
        self.result = None

class HelpConfig(object):

    def __init__(self,where:str) -> None:
        self.type = where
        self.tuples = (
            'speed',
            'send',
            'thread',
            'contact',
            'admin',
            'group',
            'friend',
            'message',
            'groupurl',
            'groupact'
        )

    @property
    def Inspection(self):
        case = self.type.casefold()
        select = self.tuples.index(case)
        for case in Switch(select):
            if case(0):
                return self.Speed
            if case(1):
                return self.Send
            if case(2):
                return self.Thread
            if case(3):
                return self.Contact
            if case(4):
                return self.Admin
            if case(5):
                return self.Group
            if case(6):
                return self.Friend
            if case(7):
                return self.Message
            if case(8):
                return self.GroupUrl
            if case(9):
                return self.GroupAct

    @property
    def Speed(self):
        foo = 'sp'
        instruction = [
            "%s -p",
            "%s %#x",
            "%s -pm",
            "%s %#x",
            "%s -ps decimal",
            "%s %#x decimal",
            "%s -pt decimal",
            "%s %#x decimal",
            "%s -c",
            "%s %#x",
            "%s -cm",
            "%s %#x",
            "%s -cs decimal",
            "%s %#x decimal",
            "%s -ct decimal",
            "%s %#x decimal"
        ]
        menu = [
            ">>>Py profile",
            ">>>Py message",
            ">>>Py messages",
            ">>>Py threads",
            ">>>C profile",
            ">>>C message",
            ">>>C messages",
            ">>>C threads"
        ]
        for i in range(len(instruction)):
            instruction[i] = instruction[i] % (foo,0x01 << i//0x02) if i % 0x02 != 0 else instruction[i] % foo
        for i in range(0x02,len(instruction) + len(menu),0x03):
            instruction.insert(i,menu[i // 0x03] + '\x0a')
        return '<SPEED>'+''.join(i for i in ['\x0a'] * 2)+'\n'.join([i for i in instruction]) + '\n' + Transfer.TimeNow()

    @property
    def Send(self):
        foo = 'send'
        instruction = [
            "%s -f decimal string",
            "%s %#x decimal string",
            "%s -t decimal string",
            "%s %#x decimal string"
        ]
        menu = [
            ">>>Message range",
            ">>>Thread range"
        ]
        for i in range(len(instruction)):
            instruction[i] = instruction[i] % (foo,0x01 << i//0x02) if i % 0x02 != 0 else instruction[i] % foo
        for i in range(0x02,len(instruction) + len(menu),0x03):
            instruction.insert(i,menu[i // 0x03] + '\x0a')
        return '<SEND>'+''.join(i for i in ['\x0a'] * 2)+'\n'.join([i for i in instruction]) + '\n' + Transfer.TimeNow()

    @property
    def Thread(self):
        foo = 'thread'
        instruction = [
            "%s -a decimal",
            "%s %#x decimal",
            "%s -l",
            "%s %#x"
        ]
        menu = [
            ">>>Thread append",
            ">>>Inquire thread"
        ]
        for i in range(len(instruction)):
            instruction[i] = instruction[i] % (foo,0x01 << i//0x02) if i % 0x02 != 0 else instruction[i] % foo
        for i in range(0x02,len(instruction) + len(menu),0x03):
            instruction.insert(i,menu[i // 0x03] + '\x0a')
        return '<THREAD>'+''.join(i for i in ['\x0a'] * 2)+'\n'.join([i for i in instruction]) + '\n' + Transfer.TimeNow()

    @property
    def Contact(self):
        foo = 'mid'
        display = '(tag or mid or re)'
        skip = [6,7]
        instruction = [
            "%s %s",
            "%s %#x %s",
            "%s -c %s",
            "%s %#x %s",
            "%s -p %s",
            "%s %#x %s",
            "%s -m",
            "%s %#x"
        ]
        menu = [
            ">>>Send mid list",
            ">>>Send contact",
            ">>>Send profile",
            ">>>Mymid"
        ]
        for i in range(len(instruction)):
            if i == skip[0]:instruction[skip[0]] = instruction[skip[0]] % foo
            elif i == skip[1]:instruction[skip[1]] = instruction[skip[1]] % (foo,0x01 << i//0x02)
            else:instruction[i] = instruction[i] % (foo,0x01 << i//0x02,display) if i % 0x02 != 0 else instruction[i] % (foo,display)
        for i in range(0x02,len(instruction) + len(menu),0x03):
            instruction.insert(i,menu[i // 0x03] + '\x0a')
        return '<CONTACT>'+''.join(i for i in ['\x0a'] * 2)+'\n'.join([i for i in instruction]) + '\n' + Transfer.TimeNow()

    @property
    def Admin(self):
        foo = 'admin'
        display = '(tag or mid)'
        instruction = [
            "%s -a {}".format(display),
            "%s %#x {}".format(display),
            "%s -d {}".format(display),
            "%s %#x {}".format(display),
            "%s -l",
            "%s %#x"
        ]
        menu = [
            ">>>Add administrator",
            ">>>Del administrator",
            ">>>View administrator"
        ]
        for i in range(len(instruction)):
            instruction[i] = instruction[i] % (foo,0x01 << i//0x02) if i % 0x02 != 0 else instruction[i] % foo
        for i in range(0x02,len(instruction) + len(menu),0x03):
            instruction.insert(i,menu[i // 0x03] + '\x0a')
        return '<CONTACT>'+''.join(i for i in ['\x0a'] * 2)+'\n'.join([i for i in instruction]) + '\n' + Transfer.TimeNow()

    @property
    def Group(self):
        foo = 'gid'
        instruction = [
            "%s",
            "%s %#x",
            "%s -l",
            "%s %#x",
            "%s -i (gids or re)",
            "%s %#x (gids or re)"
        ]
        menu = [
            ">>>Get current chat ID",
            ">>>View all your own groups",
            ">>>View specified group"
        ]
        for i in range(len(instruction)):
            instruction[i] = instruction[i] % (foo,0x01 << i//0x02) if i % 0x02 != 0 else instruction[i] % foo
        for i in range(0x02,len(instruction) + len(menu),0x03):
            instruction.insert(i,menu[i // 0x03] + '\x0a')
        return '<GROUP>'+''.join(i for i in ['\x0a'] * 2)+'\n'.join([i for i in instruction]) + '\n' + Transfer.TimeNow()

    @property
    def Friend(self):
        foo = 'friend'
        display = '(tag or mid or re)'
        instruction = [
            "%s -a {}".format(display),
            "%s %#x {}".format(display),
            "%s -l",
            "%s %#x"
        ]
        menu = [
            ">>>Add friends",
            ">>>View your friends"
        ]
        for i in range(len(instruction)):
            instruction[i] = instruction[i] % (foo,0x01 << i//0x02) if i % 0x02 != 0 else instruction[i] % foo
        for i in range(0x02,len(instruction) + len(menu),0x03):
            instruction.insert(i,menu[i // 0x03] + '\x0a')
        return '<FRIEND>'+''.join(i for i in ['\x0a'] * 2)+'\n'.join([i for i in instruction]) + '\n' + Transfer.TimeNow()

    @property
    def Message(self):
        foo = 'msg'
        instruction = [
            "%s -u (decimal)",
            "%s %#x (decimal)"
        ]
        menu = [
            ">>>Retract message"
        ]
        for i in range(len(instruction)):
            instruction[i] = instruction[i] % (foo,0x01 << i//0x02) if i % 0x02 != 0 else instruction[i] % foo
        for i in range(0x02,len(instruction) + len(menu),0x03):
            instruction.insert(i,menu[i // 0x03] + '\x0a')
        return '<MESSAGE>'+''.join(i for i in ['\x0a'] * 2)+'\n'.join([i for i in instruction]) + '\n' + Transfer.TimeNow()

    @property
    def GroupUrl(self):
        foo = 'url'
        group_url = '(group url)'
        all_can = '(group url or gid or None)'
        instruction = [
            "%s -f {}".format(group_url),
            "%s %#x {}".format(group_url),
            "%s -j {}".format(group_url),
            "%s %#x {}".format(group_url),
            "%s -on {}".format(all_can),
            "%s %#x {}".format(all_can),
            "%s -off {}".format(all_can),
            "%s %#x {}".format(all_can)
        ]
        menu = [
            ">>>Find Group by url",
            ">>>Joined Group by url",
            ">>>Group url on",
            ">>>Group url off"
        ]
        for i in range(len(instruction)):
            instruction[i] = instruction[i] % (foo,0x01 << i//0x02) if i % 0x02 != 0 else instruction[i] % foo
        for i in range(0x02,len(instruction) + len(menu),0x03):
            instruction.insert(i,menu[i // 0x03] + '\x0a')
        return '<GROUP URL>'+''.join(i for i in ['\x0a'] * 2)+'\n'.join([i for i in instruction]) + '\n' + Transfer.TimeNow()

    @property
    def GroupAct(self):
        foo = 'act'
        all_can = '(mid and gid or None)'
        instruction = [
            "%s -k {}".format(all_can),
            "%s %#x {}".format(all_can),
            "%s -i {}".format(all_can),
            "%s %#x {}".format(all_can),
            "%s -c {}".format(all_can),
            "%s %#x {}".format(all_can)
            ]
        menu = [
            ">>>Kicked to group",
            ">>>Invite to group",
            ">>>Cancel to Invitation"
        ]
        for i in range(len(instruction)):
            instruction[i] = instruction[i] % (foo,0x01 << i//0x02) if i % 0x02 != 0 else instruction[i] % foo
        for i in range(0x02,len(instruction) + len(menu),0x03):
            instruction.insert(i,menu[i // 0x03] + '\x0a')
        return '<GROUP ACT>'+''.join(i for i in ['\x0a'] * 2)+'\n'.join([i for i in instruction]) + '\n' + Transfer.TimeNow()

class Speed(object):

    def __init__(self,Index:Integrate) -> None:
        self.index = Index

    @property
    def Command(self):

        if self.index.command in [str(),'-p']:return self.Speed_0x1
        elif self.index.command == '-pm':return self.Speed_0x2
        elif self.index.command == '-ps':return self.Speed_0x4
        elif self.index.command == '-pt':return self.Speed_0x8
        elif self.index.command == '-c':return self.Speed_0x10
        elif self.index.command == '-cm':return self.Speed_0x20
        elif self.index.command == '-cs':return self.Speed_0x40
        elif self.index.command == '-ct':return self.Speed_0x80
        elif self.index.command == '-h':return self.index.sv.SendMessage(self.index.to,HelpConfig('speed').Inspection,self.index.id)

    @property
    def Carry(self):
        locate : list = []
        for i in range(8):
            k = self.index.carry & 0x01 << i
            if k > 0x0:
                locate.append('ThreadingPMD(Speed(admix).Speed_%#x).start()' % k)
        return '\n'.join([i for i in locate])

    @property
    def Speed_0x1(self):
        start = time.perf_counter()
        self.index.sv.GetProfile()
        end = time.perf_counter() - start
        return self.index.sv.SendMessage(self.index.to,f'Python Speed...\n{end}')

    @property
    def Speed_0x2(self):
        start = time.perf_counter()
        self.index.sv.SendMessage(self.index.to,'Python object testing ^^')
        end = time.perf_counter() - start
        return self.index.sv.SendMessage(self.index.to,f'Python message speed >>>\n{end}')

    @property
    def Speed_0x4(self):
        start = time.perf_counter()
        [self.index.sv.SendMessage(self.index.to,f'Python message speed >>>\n{i+1}') for i in range(self.index.args)]
        end = time.perf_counter() - start
        return self.index.sv.SendMessage(self.index.to,f'Python message range >>>\n{self.index.args}\nSpeed >>>\n{end}',self.index.id)

    @property
    def Speed_0x8(self):
        start = time.perf_counter()
        for i in range(len(TASKS)):
            ThreadingPMD(TASKS[i].SendMessage,args=(self.index.to,f'Python thread message speed >>>\n{i+1}')).start() if i < self.index.args else ...
        end = time.perf_counter() - start
        return self.index.sv.SendMessage(self.index.to,f'Python thread message range >>>\n{self.index.args}\nSpeed >>>\n{end}',self.index.id)

    @property
    def Speed_0x10(self):
        if IsCobject:
            csp = str(np.array([Ttime(self.index.sv.GetProfile())])).strip('[]')
            return self.index.sv.SendMessage(self.index.to,f'C Speed...\n{csp}')
        else:return self.index.sv.SendMessage(self.index.to,self.index.Errors[1])
    
    @property
    def Speed_0x20(self):
        if IsCobject:
            csp = str(np.array([Ttime(self.index.sv.SendMessage(self.index.to,'Test c object message~',self.index.id))])).strip('[]')
            return self.index.sv.SendMessage(self.index.to,f'C message speed >>>\n{csp}')
        else:
            return self.index.sv.SendMessage(self.index.to,self.index.Errors[1])

    @property
    def Speed_0x40(self):
        if IsCobject:
            def NewSpeed(count):
                [AccSingle(self.index.sv.SendMessage(self.index.to,f'C message speed >>>\n{i+1}')) for i in range(count)]
            csp = str(np.array([Ttime(NewSpeed(self.index.args))])).strip('[]')
            return self.index.sv.SendMessage(self.index.to,f'C message range >>>\n{self.index.args}\nSpeed >>>\n{csp}',self.index.id)
        else:
            return self.index.sv.SendMessage(self.index.to,self.index.Errors[1])

    @property
    def Speed_0x80(self):
        if IsCobject:
            def NewSpeed():
                for i in range(len(TASKS)):
                    AccSingle(ThreadingPMD(TASKS[i].SendMessage,args=(self.index.to,f'C thread message speed >>>\n{i+1}')).start() if i < self.index.args else ...)
            csp = str(np.array([Ttime(NewSpeed())])).strip('[]')
            return self.index.sv.SendMessage(self.index.to,f'C thread message range >>>\n{self.index.args}\nSpeed >>>\n{csp}',self.index.id)
        else:
            return self.index.sv.SendMessage(self.index.to,self.index.Errors[1])

class Send(object):

    def __init__(self,Index:Integrate) -> Integrate:
        self.index = Index

    @property
    def Command(self):
        if self.index.command == '-f':return self.Send_0x1
        elif self.index.command == '-t':return self.Send_0x2
        elif self.index.command == '-h':return self.index.sv.SendMessage(self.index.to,HelpConfig('send').Inspection,self.index.id)

    @property
    def Carry(self):
        locate : list = []
        for i in range(2):
            k = self.index.carry & 0x01 << i
            if k > 0x0:
                locate.append('ThreadingPMD(Send(admix).Send_%#x).start()' % k)
        return '\n'.join([i for i in locate])

    @property
    def Send_0x1(self):
        return [self.index.sv.SendMessage(self.index.to,self.index.args[1]) for _ in range(self.index.args[0])]

    @property
    def Send_0x2(self):
        Count = self.index.args[0]
        for i in range(len(TASKS)):
            ThreadingPMD(TASKS[i].SendMessage,args=(self.index.to,self.index.args[1])).start() if Count > 0x00 else ...
            Count -= 1

class Thread(object):

    def __init__(self,Index:Integrate) -> Integrate:
        self.index = Index

    @property
    def Command(self):
        if self.index.command == '-a':return self.Thread_0x1
        elif self.index.command == '-l':return self.Thread_0x2
        elif self.index.command == '-h':return self.index.sv.SendMessage(self.index.to,HelpConfig('thread').Inspection,self.index.id)

    @property
    def Carry(self):
        locate : list = []
        for i in range(2):
            k = self.index.carry & 0x01 << i
            if k > 0x0:
                locate.append('ThreadingPMD(Thread(admix).Thread_%#x).start()' % k)
        return '\n'.join([i for i in locate])

    @property
    def Thread_0x1(self):
        def ThreadAppend():
            TASK.append(self.index.args[1](self.index.args[2]))
        def ThreadLoad(obj):
            TASKS.append(self.index.args[3](obj))

        External = [ThreadingPMD(ThreadAppend) for _ in range(int(self.index.args[0]))]
        start = time.perf_counter()
        [i.start() for i in External]
        end = time.perf_counter() - start
        self.index.sv.SendMessage(self.index.to,f'Finished adding external thread ^^\nTotal >>> {self.index.args[0]}\nexecution time >>>\n{end}')
        [i.join() for i in External]
        Struct = [ThreadingPMD(ThreadLoad,args=(i,)) for i in TASK]
        start = time.perf_counter()
        [i.start() for i in Struct]
        end = time.perf_counter() - start
        self.index.sv.SendMessage(self.index.to,f'Join the structure is complete ^^\nTotal >>> {self.index.args[0]}\nexecution time >>>\n{end}')
        [i.join() for i in Struct]
        TASK.clear()

    @property
    def Thread_0x2(self):
        return self.index.sv.SendMessage(self.index.to,f'{Transfer.TimeNow()}\nTHREADING >>>\n{len(TASKS)}')

class Contact(object):

    def __init__(self,Index:Integrate) -> Integrate:
        self.index = Index

    @property
    def Command(self):
        if self.index.command == str():return self.Contact_0x1
        elif self.index.command == '-c':return self.Contact_0x2
        elif self.index.command == '-p':return self.Contact_0x4
        elif self.index.command == '-m':return self.Contact_0x8
        elif self.index.command == '-h':return self.index.sv.SendMessage(self.index.to,HelpConfig('contact').Inspection,self.index.id)

    @property
    def Carry(self):
        locate : list = []
        for i in range(4):
            k = self.index.carry & 0x01 << i
            if k > 0x0:
                locate.append('ThreadingPMD(Contact(admix).Contact_%#x).start()' % k)
        return '\n'.join([i for i in locate])

    @property
    def Contact_0x1(self):
        Msg : list = []
        if self.index.args != list():
            for i in range(len(self.index.args)):
                Msg.append(f'<{i+1}>{self.index.args[i]}')
            return self.index.sv.SendMessage(self.index.to,'\n'.join([i for i in Msg]),self.index.id)

    @property
    def Contact_0x2(self):
        if len(TASKS) >= len(self.index.args):
            for i in range(len(self.index.args)):
                TASKS[i].SendContact(self.index.to,self.index.args[i])
        else:
            return [self.index.sv.SendContact(self.index.to,i) for i in self.index.args]

    @property
    def Contact_0x4(self):
        contacts = self.index.sv.GetContacts(self.index.args)
        for i in contacts:
            self.index.sv.SendMessage(self.index.to,str(i))

    @property
    def Contact_0x8(self):
        return self.index.sv.SendMessage(self.index.to,self.index.be,self.index.id)

class Admin(object):

    def __init__(self,Index:Integrate) -> Integrate:
        self.index = Index

    @property
    def Command(self):
        if self.index.command == '-a':return self.Admin_0x1
        elif self.index.command == '-d':return self.Admin_0x2
        elif self.index.command == '-l':return self.Admin_0x4
        elif self.index.command == '-h':return self.index.sv.SendMessage(self.index.to,HelpConfig('admin').Inspection,self.index.id)

    @property
    def Carry(self):
        locate : list = []
        for i in range(3):
            k = self.index.carry & 0x01 << i
            if k > 0x0:
                locate.append('ThreadingPMD(Admin(admix).Admin_%#x).start()' % k)
        return '\n'.join([i for i in locate])

    @property
    def Admin_0x1(self):
        result : list = ['<<Admin add>>']
        contacts = self.index.sv.GetContacts(self.index.args[0])
        for i in range(len(contacts)):
            if contacts[i].mid not in self.index.args[1]:
                self.index.args[1].append(contacts[i].mid)
                result.append(f'[Success]\n{i+1} >>> {contacts[i].displayName}\n>>>{contacts[i].mid}')
            else:
                result.append(f'[Failed]\n{i+1} >>> {contacts[i].displayName}\n>>>{contacts[i].mid}')
        result.append(f'Total >>> {len(contacts)}')
        self.index.result = self.index.args[1]
        return self.index.sv.SendMessage(self.index.to,'\n'.join([i for i in result]),self.index.id)

    @property
    def Admin_0x2(self):
        result :list = ['<<Admin del>>']
        contacts = self.index.sv.GetContacts(self.index.args[0])
        for i in range(len(contacts)):
            if contacts[i].mid in self.index.args[1]:
                self.index.args[1].remove(contacts[i].mid)
                result.append(f'[Success]\n{i+1} >>> {contacts[i].displayName}\n>>>{contacts[i].mid}')
            else:
                result.append(f'[Failed]\n{i+1} >>> {contacts[i].displayName}\n>>>{contacts[i].mid}')
        result.append(f'Total >>> {len(contacts)}')
        self.index.result = self.index.args[1]
        return self.index.sv.SendMessage(self.index.to,'\n'.join([i for i in result]),self.index.id)

    @property
    def Admin_0x4(self):
        result : list = ['<<Admin array>>']
        contacts = self.index.sv.GetContacts(self.index.args[1])
        for i in range(len(contacts)):
            result.append(f'{i+1} >>> {contacts[i].displayName}\n>>>{contacts[i].mid}')
        result.append(f'Total >>> {len(contacts)}')
        return self.index.sv.SendMessage(self.index.to,'\n'.join([i for i in result]),self.index.id)

class Group(object):

    def __init__(self,Index:Integrate) -> Integrate:
        self.index = Index

    @property
    def Command(self):
        if self.index.command == str():return self.Group_0x1
        elif self.index.command == '-l':return self.Group_0x2
        elif self.index.command == '-i':return self.Group_0x4
        elif self.index.command == '-h':return self.index.sv.SendMessage(self.index.to,HelpConfig('group').Inspection,self.index.id)

    @property
    def Carry(self):
        locate : list = []
        for i in range(3):
            k = self.index.carry & 0x01 << i
            if k > 0x0:
                locate.append('ThreadingPMD(Group(admix).Group_%#x).start()' % k)
        return '\n'.join([i for i in locate])

    @property
    def Group_0x1(self):
        return self.index.sv.SendMessage(self.index.to,self.index.to,self.index.id)

    @property
    def Group_0x2(self):
        gids = self.index.sv.GetGroupids()
        groups = self.index.sv.GetGroups(gids)
        result = ['<<Get Groups Joined>>']
        for i in range(len(groups)):
            UrlSwit = 'OFF' if groups[i].preventedJoinByTicket else 'ON'
            created_t = Transfer.TimeNow(groups[i].createdTime // 1000)
            result.append('<%d>%s\n%s\nUrlSwit > %s\n%s' % (i+1,groups[i].name,groups[i].id,UrlSwit,created_t))
        result.append('Total >>> %d' % len(groups))
        self.index.sv.SendMessage(self.index.to,'\n'.join([i for i in result]),self.index.id)

    @property
    def Group_0x4(self):
        groups = self.index.sv.GetGroups(self.index.args)
        result = ['<<Get Groups>>']
        for i in range(len(groups)):
            UrlSwit = 'OFF' if groups[i].preventedJoinByTicket else 'ON'
            created_t = Transfer.TimeNow(groups[i].createdTime // 1000)
            result.append('<%d>%s\n%s\nUrlSwit > %s\n%s' % (i+1,groups[i].name,groups[i].id,UrlSwit,created_t))
        result.append('Total >>> %d' % len(groups))
        self.index.sv.SendMessage(self.index.to,'\n'.join([i for i in result]),self.index.id)

class Friend(object):

    def __init__(self,Index:Integrate) -> Integrate:
        self.index = Index

    @property
    def Command(self):
        if self.index.command == '-a':return self.Friend_0x1
        elif self.index.command == '-l':return self.Friend_0x2
        elif self.index.command == '-h':return self.index.sv.SendMessage(self.index.to,HelpConfig('friend').Inspection,self.index.id)

    @property
    def Carry(self):
        locate : list = []
        for i in range(2):
            k = self.index.carry & 0x01 << i
            if k > 0x0:
                locate.append('ThreadingPMD(Friend(admix).Friend_%#x).start()' % k)
        return '\n'.join([i for i in locate])

    @property
    def Friend_0x1(self):
        contacts = self.index.sv.GetContacts(self.index.args)
        Msg = ['<<Add Friend>>']
        for i in range(len(contacts)):
            try:
                self.index.sv.AddFriend(contacts[i].mid)
                Msg.append('[Success]\n<%d>%s\n%s' % (i+1, contacts[i].displayName, contacts[i].mid))
            except TalkException as error:
                Msg.append('[Failed]\n%s\n<%d>%s\n%s' % (error.reason, i+1, contacts[i].displayName, contacts[i].mid))
        return self.index.sv.SendMessage(self.index.to,'\n'.join([i for i in Msg]),self.index.id)

    @property
    def Friend_0x2(self):
        contacts = self.index.sv.GetAllFriends()
        contacts = self.index.sv.GetContacts(contacts)
        Msg = ['<<Friend Array>>']
        for i in range(len(contacts)):
            Msg.append('<%d>%s\n%s' % (i+1, contacts[i].displayName, contacts[i].mid))
        Msg.append(f'Total >>> {len(contacts)}')
        return self.index.sv.SendMessage(self.index.to,'\n'.join([i for i in Msg]),self.index.id)

class Message(object):

    def __init__(self,Index:Integrate) -> Integrate:
        self.index = Index

    @property
    def Command(self):
        if self.index.command == '-u':return self.Message_0x1
        elif self.index.command == '-h':return self.index.sv.SendMessage(self.index.to,HelpConfig('message').Inspection,self.index.id)

    @property
    def Carry(self):
        locate : list = []
        for i in range(1):
            k = self.index.carry & 0x01 << i
            if k > 0x0:
                locate.append('ThreadingPMD(Message(admix).Message_%#x).start()' % k)
        return '\n'.join([i for i in locate])

    @property
    def Message_0x1(self):
        if self.index.args[2] == list():
            self.index.args[2].append(self.index.to)
        for group in self.index.args[2]:
            counter = int()
            retract : list = []
            if self.index.args[1] == str():counter = 1
            elif int(self.index.args[1]) == 0:counter = 1000
            else:counter = int(self.index.args[1])
            try:
                for msg in self.index.sv.GetRecentMessages(group):
                    if msg._from == self.index.args[0]:
                        if len(retract) < counter:
                            retract.append(msg.id)
                if len(TASKS) >= counter:
                    pool = [ThreadingPMD(TASKS[i].RetractMessage,args=(retract[i],)) for i in range(len(retract))]
                    [i.start() for i in pool]
                else:
                    [self.index.sv.RetractMessage(retract[i]) for i in range(len(retract))]
            except TalkException:...

    @property
    def Message_0x2(self):...

    @property
    def Message_0x4(self):...

class GroupUrl(object):

    def __init__(self,Index:Integrate) -> Integrate:
        self.index = Index

    @property
    def Command(self):
        if self.index.command == '-f':return self.GroupUrl_0x1
        elif self.index.command == '-j':return self.GroupUrl_0x2
        elif self.index.command == '-on':return self.GroupUrl_0x4
        elif self.index.command == '-off':return self.GroupUrl_0x8
        elif self.index.command == '-h':return self.index.sv.SendMessage(self.index.to,HelpConfig('groupurl').Inspection,self.index.id)

    @property
    def Carry(self):
        locate : list = []
        for i in range(4):
            k = self.index.carry & 0x01 << i
            if k > 0x0:
                locate.append('ThreadingPMD(GroupUrl(admix).GroupUrl_%#x).start()' % k)
        return '\n'.join([i for i in locate])

    @property
    def GroupUrl_0x1(self):
        groups : list = []
        Msg : list = ['<<Group List>>']
        for url in self.index.args[0]:
            try:
                groups.append(self.index.sv.FindGroupByUrl(url))
            except TalkException as error:
                if error.code == 5:
                    Msg.append('[Error Url]\n%s' % url)
        for i in range(len(groups)):
            created_t = Transfer.TimeNow(groups[i].createdTime // 1000)
            Msg.append('<%d>%s\n%s\n%s' % (i+1, groups[i].name, groups[i].id, created_t))
        return self.index.sv.SendMessage(self.index.to,'\n'.join([i for i in Msg]),self.index.id)

    @property
    def GroupUrl_0x2(self):
        groups : list = []
        Msg : list = ['<<Group Joined Success>>']
        for url in self.index.args[0]:
            try:
                group = self.index.sv.FindGroupByUrl(url)
                if group.preventedJoinByTicket == False:
                    self.index.sv.UrlIntoGroup(group.id,url)
                    groups.append(group)
            except TalkException:...
        for i in range(len(groups)):
            Msg.append('<%d>%s\n%s' % (i+1, groups[i].name, groups[i].id))
        try:
            return self.index.sv.SendMessage(self.index.to,'\n'.join([i for i in Msg]),self.index.id)
        except TalkException:...

    @property
    def GroupUrl_0x4(self):
        groups : list = []
        if (self.index.args[0],self.index.args[1]) != ([],[]):
            mygroups = self.index.sv.GetGroupids()
            groups.extend(self.index.sv.GetGroups(self.index.args[1]))
            for url in self.index.args[0]:
                groups.append(self.index.sv.FindGroupByUrl(url))
            for cheak in groups:
                if cheak.id not in mygroups:
                    groups.remove(cheak)
        else:
            groups.append(self.index.sv.GetGroup(self.index.to))
        Msg : list = ['<<Group URL ON>>']
        for i in range(len(groups)):
            groups[i].preventedJoinByTicket = False
            self.index.sv.UpdateGroup(groups[i])
            newurl = self.index.sv.UpdateGroupUrl(groups[i].id)
            Msg.append('<%d>%s\n%s\nurl >>>\n%s' % (i+1, groups[i].name, groups[i].id, 'https://line.me/R/ti/g/'+newurl))
        return self.index.sv.SendMessage(self.index.to,'\n'.join([i for i in Msg]),self.index.id)

    @property
    def GroupUrl_0x8(self):
        groups : list = []
        if (self.index.args[0],self.index.args[1]) != ([],[]):
            mygroups = self.index.sv.GetGroupids()
            groups.extend(self.index.sv.GetGroups(self.index.args[1]))
            for url in self.index.args[0]:
                groups.append(self.index.sv.FindGroupByUrl(url))
            for cheak in groups:
                if cheak.id not in mygroups:
                    groups.remove(cheak)
        else:
            groups.append(self.index.sv.GetGroup(self.index.to))
        Msg : list = ['<<Group URL OFF>>']
        for i in range(len(groups)):
            groups[i].preventedJoinByTicket = True
            self.index.sv.UpdateGroup(groups[i])
            Msg.append('<%d>%s\n%s' % (i+1, groups[i].name, groups[i].id))
        return self.index.sv.SendMessage(self.index.to,'\n'.join([i for i in Msg]),self.index.id)

class GroupAct(object):

    def __init__(self,Index:Integrate) -> Integrate:
        self.index = Index

    @property
    def Command(self):
        if self.index.command == '-k':return self.GroupAct_0x1
        elif self.index.command == '-i':return self.GroupAct_0x2
        elif self.index.command == '-c':return self.GroupAct_0x4
        elif self.index.command == '-h':return self.index.sv.SendMessage(self.index.to,HelpConfig('groupact').Inspection,self.index.id)

    @property
    def Carry(self):
        locate : list = []
        for i in range(3):
            k = self.index.carry & 0x01 << i
            if k > 0x0:
                locate.append('ThreadingPMD(GroupAct(admix).GroupAct_%#x).start()' % k)
        return '\n'.join([i for i in locate])

    @property
    def GroupAct_0x1(self):
        groups : list = []
        if len(self.index.args[0]) < 1:return
        array = list(set(self.index.args[0]))
        if self.index.args[1] == []:
            groups.append(self.index.to)
        else:
            groups.extend(self.index.args[1])
        [array.remove(i) if i in array else ... for i in self.index.args[2]]
        pool : list = []
        counter = 0
        if len(TASKS) >= len(groups) * len(array):
            for gid in range(len(groups)):
                for i in range(len(array)):
                    pool.append(ThreadingPMD(TASKS[counter].Kickout,args=(groups[gid],[array[i]])))
                    counter += 1
            [i.start() for i in pool]
        else:
            [self.index.sv.Kickout(gid,[i]) for i in array for gid in groups]

    @property
    def GroupAct_0x2(self):
        groups : list = []
        Msg : list = ['<<Invitation>>']
        if self.index.args[1] == []:
            groups.append(self.index.to)
        else:
            groups.extend(self.index.args[1])
        contacts = self.index.sv.GetContacts(self.index.args[0])
        myfriends = self.index.sv.GetAllFriends()
        for i in range(len(contacts)):
            if contacts[i].mid not in myfriends:
                try:
                    self.index.sv.AddFriend(contacts[i].mid)
                    Msg.append('[Success]\n<%d>%s\n%s' % (i+1, contacts[i].displayName, contacts[i].mid))
                except TalkException as e:
                    Msg.append('[Failed]\n<%d>\n%s\n%s' % (i+1, e.reason, contacts[i].mid))
                    del contacts[i]
                    del self.index.args[0][i]
            else:
                Msg.append('[Success]\n<%d>%s\n%s' % (i+1, contacts[i].displayName, contacts[i].mid))
        [self.index.sv.Invitation(gid,self.index.args[0]) for gid in groups]
        return self.index.sv.SendMessage(self.index.to,'\n'.join([i for i in Msg]),self.index.id)

    @property
    def GroupAct_0x4(self):
        groups : list = []
        if len(self.index.args[0]) < 1:return
        array = list(set(self.index.args[0]))
        if self.index.args[1] == []:
            groups.append(self.index.to)
        else:
            groups.extend(self.index.args[1])
        [array.remove(i) if i in array else ... for i in self.index.args[2]]
        pool : list = []
        counter = 0
        if len(TASKS) >= len(groups) * len(array):
            for gid in range(len(groups)):
                for i in range(len(array)):
                    pool.append(ThreadingPMD(TASKS[counter].CancelInvitation,args=(groups[gid],[array[i]])))
                    counter += 1
            [i.start() for i in pool]
            [i.join() for i in pool]
            [print(i.getResult()) for i in pool]
        else:
            [self.index.sv.CancelInvitation(gid,[array[i]]) for i in range(len(array)) for gid in groups]

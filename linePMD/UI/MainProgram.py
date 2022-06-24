import os
from PlinePMD.Tools import WhichSystem
import time
import configparser

class Handle:

    def __init__(self,mail:str='',PWD:str='',token:str='',Cert:str='',count:int=...,servo=False) -> None:
        self.MailORToken = token if token not in ['',None] else mail
        self.PWD = PWD
        self.Cert = Cert
        self.servo = servo
        self.count = count
        (self.admin,self.owner,self.backdoor) = ([], [], '')
        for datatype,data in Transfer.Permission():
            if datatype == 1:self.admin.append(data)
            elif datatype == 2:self.owner.append(data)
            elif datatype == 3:self.backdoor = data

    def Which(self):
        newsys = WhichSystem.Dealwith()
        if newsys in ['Windows','Java']:
            from UI.Py_language import Pyclasses
            new = Pyclasses(self.MailORToken,self.PWD,self.Cert,self.count,self.servo)
        elif newsys == 'Linux':
            from UI.C_language import Cclasses
            new = Cclasses(self.MailORToken,self.PWD,self.Cert,self.count,self.servo)
        else:raise SystemError('Unknown system %s' %newsys)
        new.owner = self.owner
        new.admin = self.admin
        new.backdoor = self.backdoor
        new.Initial()

class Transfer:

    def TimeNow(method=None):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(method))

    def Permission():
        try:
            with open('Txt/Permission.txt','r',encoding='UTF8') as reader:
                new = reader.readlines()
                for data in new:
                    if data.strip().casefold() == 'admin':
                        datatype = 1
                    elif data.strip().casefold() == 'owner':
                        datatype = 2
                    elif data.strip().casefold() == 'backdoor':
                        datatype = 3
                    else:
                        if data.strip() != '':
                            yield datatype,data.strip()
        except FileNotFoundError:
            raise FileNotFoundError('Don\'t mess with my file ><')
        finally:
            reader.close()

    def Reboot(admin:list,owner:list,backdoor:str):
        [admin.remove(i) if i.casefold() == 'admin' else ... for i in admin]
        [owner.remove(i) if i.casefold() == 'owner' else ... for i in owner]
        try:
            with open('Txt/Permission.txt','w') as writer:
                data = []
                if isinstance(admin,list):
                    admin.insert(0,'admin')
                    data.extend([i+'\n' for i in admin])
                if isinstance(owner,list):
                    owner.insert(0,'owner')
                    data.extend([i+'\n' for i in owner])
                if isinstance(backdoor,str):
                    data.extend(['backdoor\n',backdoor+'\n'])
                writer.writelines(data)
                writer.close()
        except FileNotFoundError:
            raise FileNotFoundError('Don\'t mess with my file ><')

    def UserCheak():
        try:
            config = configparser.ConfigParser()
            config.read('Txt/MyUsers.ini')
            count = 0
            for i in config.sections():
                yield (
                    count,
                    config[i]['mid'] if config[i]['mid'] != 'None' else None,
                    config[i]['account'] if config[i]['account'] != 'None' else None,
                    config[i]['password'] if config[i]['password'] != 'None' else None,
                    config[i]['token'] if config[i]['token'] != 'None' else None,
                    config[i]['cert'] if config[i]['cert'] != 'None' else None
                )
                count += 1
        except FileNotFoundError:
            raise FileNotFoundError('Don\'t mess with my file ><')

    def UserUpdate(specify,keys,newobj):
        try:
            config = configparser.ConfigParser()
            filepath = 'Txt/MyUsers.ini'
            config.read(filepath)
            for index in config.sections():
                if specify != None and specify == int(index):
                    for key,value in config.items(index):
                        if key == keys:
                            config.set(index,key,newobj)
                            with open(filepath,'w') as writer:
                                config.write(writer)
                                writer.close()
                elif specify == None:
                    for key,value in config.items(index):
                        if key == keys:
                            config.set(index,key,newobj)
                            with open(filepath,'w') as writer:
                                config.write(writer)
                                writer.close()
        except FileNotFoundError:
            raise FileNotFoundError('Don\'t mess with my file ><')

    def GetServoArgs():
        try:
            with open('Txt/ServoArgs.txt','r',encoding='UTF8') as reader:
                new = reader.readlines()
                for data in new:
                    if data.strip().casefold() == 'to':
                        datatype = 1
                    elif data.strip().casefold() == 'text':
                        datatype = 2
                    elif data.strip().casefold() == 'type':
                        datatype = 3
                    elif data.strip().casefold() == 'from':
                        datatype = 4
                    elif data.strip().casefold() == 'permission':
                        yield 5,None
                    elif data.strip().casefold() == 'admin':
                        datatype = 6
                    elif data.strip().casefold() == 'owner':
                        datatype = 7
                    elif data.strip().casefold() == 'backdoor':
                        datatype = 8
                    else:
                        if data.strip() != '' and data != None:
                            yield datatype,data.strip()
                reader.close()
            os.remove('Txt/ServoArgs.txt')
        except FileNotFoundError:yield None,None

    def SetServoResult(code:int,result:...=...) -> str:
        try:
            with open('Txt/ServoResult.txt','w',encoding='UTF8') as writer:
                data = []
                if isinstance(code,int):
                    data.insert(0,'code')
                    data.append('%x' % code)
                if isinstance(result,list):
                    data.append('result')
                    data.extend([i for i in result])
                if isinstance(result,str):
                    data.append('result')
                    data.append(result)
                writer.writelines([i+'\n' for i in data])
                writer.close()
        except FileNotFoundError:
            raise FileNotFoundError('Don\'t mess with my file ><')

    def SetPidOnDos():
        try:
            with open('Txt/ServoPid.txt','w',encoding='UTF8') as writer:
                writer.write(str(os.getpid()))
                writer.close()
        except FileNotFoundError:...
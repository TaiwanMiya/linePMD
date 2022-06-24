import re
import traceback
import abc
import requests
import os
import random
import pyodbc
import time
import shutil
from base64 import *
from PlinePMD.CryptoApi import CryptoCanvas,CryptoBase64,CryptoJson,CryptoFiles,CryptoConvert
from PlinePMD.Rsakeys import PublicKeyPMD,CryptographyPMD
from threading import Thread
from thrift.transport import THttpClient,TTransport
from thrift.protocol import TCompactProtocol
class RegexPMD(object):

    def __init__(self,func,text,sub=None) -> re:
        self.func = func
        self.text = text
        self.sub = sub

    @property
    def regex(self):
        return re.compile(self.func).match(self.text)

    @property
    def regexlist(self):
        return re.findall(self.func,self.text)

    @property
    def regexsub(self):
        return re.sub(self.func,self.sub,self.text)

class LineRsaKeyPMD(object):

    def __init__(self,sessionKey,nvalue,evalue,account,password) -> CryptographyPMD:
        self.sessionKey = sessionKey
        self.nvalue = nvalue
        self.evalue = evalue
        self.account = account
        self.password = password

    @property
    def DealWith(self):
        message = (chr(len(self.sessionKey)) + self.sessionKey + chr(len(self.account)) + self.account + chr(len(self.password)) + self.password).encode('ascii')
        public_key = PublicKeyPMD(int(self.nvalue, 16), int(self.evalue, 16))
        return CryptographyPMD.EncryptionPMD(message, public_key).hex()

class TthriftPMD(object):

    def __init__(self,site,headers:dict={},transport=None,protocol=None,OPEN=True) -> THttpClient:
        self.site = site
        self.headers = headers
        self.transport = transport
        self.protocol = protocol
        self.open = OPEN

    @property
    def TrequestsPMD(self) -> TCompactProtocol:
        self.transport = THttpClient.THttpClient(self.site)
        self.transport.setCustomHeaders(self.headers)
        self.transport.setTimeout(1000**10)
        self.transport = TTransport.TBufferedTransport(self.transport)
        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        if self.open:self.transport.open()
        return self.protocol

class ThreadingPMD(Thread):

    def __init__(self,func,args=(),kwargs=None,traceback=False) -> Thread:
        super(ThreadingPMD,self).__init__()
        if kwargs is None:kwargs = dict()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.traceback = traceback
        self.result = None

    def run(self):
        try:
            if self.func:self.result = self.func(*self.args,**self.kwargs)
        except Exception as e:
            self.result=e
            if self.traceback:traceback.print_exc()
        return self.result

    def getResult(self) -> (...):
        try:return self.result
        except Exception as e:
            if self.traceback:traceback.print_exc()
        finally:
            del self.func,self.args,self.kwargs

class ArgsPMD(abc.ABC):

    def __init__(self,func=None,*args,**kwargs) -> abc:
        self.func = func
        self.args = args
        self.kwargs = kwargs

    @property
    def funcPMD(self) -> property:return self.func

    @funcPMD.setter
    def funcPMD(self,func) -> (...):self.func = func

    @abc.abstractmethod
    def _funcPMD(self) -> ...:...

    @property
    def argsPMD(self) -> property:return self.args

    @argsPMD.setter
    def argsPMD(self,*args) -> (...):self.args = args

    @abc.abstractmethod
    def _argsPMD(self) -> ...:...

    @property
    def kwargsPMD(self) -> property:return self.kwargs

    @kwargsPMD.setter
    def kwargsPMD(self,**kwargs) -> (...):self.kwargs = kwargs
    
    @abc.abstractmethod
    def _kwargsPMD(self) -> ...:...
    
    @property
    def allargsPMD(self) -> property:return self.func,self.args,self.kwargs

    @allargsPMD.setter
    def allargsPMD(self,func,*args,**kwargs) -> (...):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    @abc.abstractmethod
    def _allargsPMD(self) -> ...:...

class BasePMD(object):

    def __init__(self,text,method:int=0,coding='ascii'):
        self.text = text
        self.method = 0 if method == 0 else 1
        self.coding = coding

    @property
    def b16PMD(self):
        if self.method == 0:return b16encode(self.text.encode(self.coding))
        else:return b16decode(self.text.decode(self.coding))

    @property
    def b32PMD(self):
        if self.method == 0:return b32encode(self.text.encode(self.coding))
        else:return b32decode(self.text.decode(self.coding))

    @property
    def b64PMD(self):
        if self.method == 0:return b64encode(self.text.encode(self.coding))
        else:return b64decode(self.text.decode(self.coding))

    @property
    def b85PMD(self):
        if self.method == 0:return b85encode(self.text.encode(self.coding))
        else:return b85decode(self.text.decode(self.coding))

class BinOctHexPMD(object):
    try:

        def __init__(self,text=None,mode=True):
            if not text:self.text = ''
            else:self.text = text
            self.mode = mode
            self.string = str()
            self.array = list()

        @property
        def binPMD(self) -> bin:
            if self.mode:
                ints = [ord(i) for i in self.text]
                self.string = ' '.join([bin(i) for i in ints])
                self.array = [bin(i) for i in ints]
            else:
                if isinstance(self.text,str):
                    self.text = ''.join([i for i in self.text.split('0b')])
                    self.text = [i for i in self.text.split(' ')]
                self.string = ''.join(chr(int(i,2)) for i in self.text)
                self.array = [chr(int(i,2)) for i in self.text]

        @property
        def octPMD(self) -> oct:
            if self.mode:
                ints = [ord(i) for i in self.text]
                self.string = ' '.join([oct(i) for i in ints])
                self.array = [oct(i) for i in ints]
            else:
                if isinstance(self.text,str):
                    self.text = ''.join([i for i in self.text.split('0o')])
                    self.text = [i for i in self.text.split(' ')]
                self.string = ''.join(chr(int(i,8)) for i in self.text)
                self.array = [chr(int(i,8)) for i in self.text]

        @property
        def hexPMD(self) -> hex:
            if self.mode:
                ints = [ord(i) for i in self.text]
                self.string = ' '.join([hex(i) for i in ints])
                self.array = [hex(i) for i in ints]
            else:
                if isinstance(self.text,str):
                    self.text = ''.join([i for i in self.text.split('0x')])
                    self.text = [i for i in self.text.split(' ')]
                self.string = ''.join(chr(int(i,16)) for i in self.text)
                self.array = [chr(int(i,16)) for i in self.text]

    except ValueError as error:
        code = RegexPMD(r'2\|8\|16',error).regex
        raise ValueError(f'Error Code:{code}')

class StringConversionPMD(object):

    def __init__(self,text=None,carry=16):
        if not text:self.text = ''
        else:self.text = text
        self.carry = carry
        self.byte = bytes()
        self.string = str()
        self.array = list()

    @property
    def read(self):
        self.array = [int(i,self.carry) for i in self.text.split(' ')]
        self.string = ' '.join([str(i) for i in self.array])
        self.byte = sum(self.array)

class ASCIIcharPMD(object):

    def __init__(self,text,mode=True):
        self.text = text
        self.mode = mode
        self.string = str()
        self.array = list()

    @property
    def ASCIIPMD(self):
        if self.mode:
            self.string = ' '.join([str(ord(i)) for i in self.text])
            self.array = [ord(i) for i in self.text]
        else:
            self.string = ' '.join(str(ord(i)) for i in self.text)
            self.array = [ord(int(i)) for i in self.text]

    @property
    def CharPMD(self):
        if self.mode:
            self.string = ''.join([str(chr(i)) for i in self.text])
            self.array = [chr(int(i)) for i in self.text]
        else:
            self.string = ''.join(str(chr(int(i))) for i in self.text)
            self.array = [chr(int(i)) for i in self.text]

class ProcessServerPMD(object):

    def __init__(self,url,header:dict=None,json:dict=None,data:dict=None,payload:dict=None,cookie=None,file=None,stream=None):
        self.session = requests.session()
        self.Session = requests.Session()
        self.url = url
        self.headers = header
        self.json = json
        self.data = data
        self.payload = payload
        self.cookie = cookie
        self.file = file
        self.stream = stream

    def ProcessMethod(self,method:str):
        if method in [str(),None]:raise ValueError('Null method')
        # Requests packge none of 'CONNECT' and 'TRACE'
        RequestMethod = ['GET','POST','DELETE','PUT','HEAD','PATCH','OPTIONS']
        if method.upper() not in RequestMethod:raise ValueError(f'Error method -> {method}')

    def GainSessionJson(self,headerJoined=False):
        if headerJoined is False:
            return self.session.get(self.url).json()
        else:
            return self.session.get(self.url,headers=self.headers).json()

    @property
    def GetSessionResult(self):
        return self.session.get(self.url).text

    @property
    def GetResponse(self):
        result = self.Session.get(
            self.url,
            headers=self.headers,
            json=self.json,
            data=self.data,
            params=self.payload,
            cookies=self.cookie,
            files=self.file,
            stream=self.stream
            )
        return result

    @property
    def PostResponse(self):
        result = self.Session.post(
            self.url,
            headers=self.headers,
            json=self.json,
            data=self.data,
            params=self.payload,
            cookies=self.cookie,
            files=self.file,
            stream=self.stream
            )
        return result

class ReprPMD(object):

    def __init__(self,CLASS,redType=False):
        self.CLASS = CLASS
        self.redType = redType

    @property
    def repr(self):
        REPR = ['%s => %r' % (key, value) for key, value in self.CLASS.__dict__.items()]
        if self.redType:
            return CryptoCanvas.Print.red()+'\n<%s>\n%s' % (self.CLASS.__class__.__name__, '\n'.join(REPR)) + CryptoCanvas.Print.attr(0)
        else:
            return '\n\n<%s>\n%s' % (self.CLASS.__class__.__name__, '\n'.join(REPR))

class CheakLoop(object):

    def __init__(self) -> None:
        pass

    def detect(self,T1,T2):
        if T1 != T2:return True
        else:return False

class FlushEcho(object):

    def NewSend(result):
        import sys
        sys.stdout.write(result)
        sys.stdout.flush()

    def CaseONI(result,NAK,NAV,E=True):
        from PlinePMD.CryptoApi import CryptoAES,Encoding
        if E:
            exec(CryptoAES.CBC(CryptoConvert.HEX(result,Encoding.ASCII.name).decrypt(),NAK,NAV,True).decrypt().decode())
        else:
            return CryptoAES.CBC(CryptoConvert.HEX(result,Encoding.ASCII.name).decrypt(),NAK,NAV,True).decrypt().decode()

    def CaseTNC(result,NAK,NAV,E=True):
        from PlinePMD.CryptoApi import CryptoAES,Encoding
        if E:
            exec(CryptoAES.CTR(CryptoConvert.HEX(result,Encoding.ASCII.name).decrypt(),NAK).decrypt().decode())
        else:
            return CryptoAES.CTR(CryptoConvert.HEX(result,Encoding.ASCII.name).decrypt(),NAK).decrypt().decode()

    def CaseOTC(self,result,NARRAY,Crypts,E=True):
        from PlinePMD.CryptoApi import (
                Encoding,
                CryptoAES,
                CryptoDES,
                CryptoBase64,
                CryptoConvert,
                CryptoCarry,
                CryptoCanvas
            )
        if E:
            exec(CryptoConvert.HEX(CryptoAES.CBC(result,NARRAY[0],NARRAY[1],True).decrypt(),Encoding.ASCII.name).decrypt().decode())
            return self.cnxn, self.crsr

class WhichSystem(object):

    def Dealwith():
        import platform
        return platform.system()

class Switch(object):

    def __init__(self,value) -> None:
        self.value = value
        self.fail = False

    def __iter__(self):
        yield self.match

    def match(self,*args):
        if self.fail or not args:
            return True
        elif self.value in args:
            return True
        else:
            return False

class FileTransfer(object):

    def GetTempFile(self, returnAs='path'):
        try:
            if returnAs not in ['file','path']:
                raise Exception('Invalid returnAs value')
            fName, fPath = 'linePMD-%s-%i.bin' % (int(time.time()), random.randint(0, 9)), CryptoFiles.Get().tempdir()
            if returnAs == 'file':
                return fName
            elif returnAs == 'path':
                return os.path.join(fPath, fName)
        except:
            raise Exception('tempfile is required')

    def GetOBSParams(self, newList, returnAs='json'):
        oldList = {'name': self.GetTempFile('file'),'ver': '2.0'}
        if returnAs not in ['json','b64','default']:
            raise TypeError('Invalid parameter returnAs')
        oldList.update(newList)
        if 'range' in oldList:
            new_range='bytes 0-%s\/%s' % ( str(oldList['range']-1), str(oldList['range']) )
            oldList.update({'range': new_range})
        if returnAs == 'json':
            oldList = CryptoJson.OBJ(oldList).Dump()
            return oldList
        elif returnAs == 'b64':
            oldList = CryptoJson.OBJ(oldList).Dump()
            return CryptoBase64.Base64(oldList,'utf-8').encrypt()
        elif returnAs == 'default':
            return oldList

    def UploadFile(self, path, type='image', returnAs='bool', id=None, to=None, revision=None, headers:dict=None):
        if returnAs not in ['objId','bool']:
            raise ValueError('Invalid returnAs value')
        if type not in ['image','gif','video','audio','file']:
            raise ValueError('Invalid type value')
        files = {'file': open(path, 'rb')}
        if type in ['image','video','audio','file']:
            e_p = 'https://obs.line-apps.com/talk/m/upload.nhn'
            if type != 'file':
                data = {'params': self.GetOBSParams({'oid': id,'size': len(open(path, 'rb').read()),'type': type})}
            else:
                e_p = 'https://obs.line-apps.com/r/talk/m/reqseq'
                data = {'params': self.GetOBSParams({'oid': id.id,'size': len(open(path, 'rb').read()),'type': "text"})}
                headers.update({
                    'Content-Type': 'application/json',
                    'Content-Length': str(len(data)),
                    'x-obs-params': self.GetOBSParams(data,'b64')
                })
        elif type == 'gif':
            e_p = 'https://obs.line-apps.com/r/talk/m/reqseq'
            files = None
            data = open(path, 'rb').read()
            params = {
                'ver': '2.0',
                'oid': 'reqseq',
                'reqseq': '%s' % str(revision),
                'tomid': '%s' % str(to),
                'name': '%s' % str(time.time()*1000),
                'cat': 'original',
                'type': 'image'
            }
            headers.update({
                'Content-Type': 'image/gif',
                'Content-Length': str(len(data)),
                'x-obs-params': self.GetOBSParams(params,'b64')
            })
        r = ProcessServerPMD(e_p,data=data,header=headers,file=files).PostResponse
        if r.status_code != 201:
            raise Exception('Upload %s failed' % type)
        if returnAs == 'objId':
            return id
        elif returnAs == 'bool':
            return True

    def saveFile(self, path, raw):
        with open(path, 'wb') as f:
            shutil.copyfileobj(raw, f)

    def DownloadFile(self, fileUrl, returnAs='path', saveAs='', headers:dict=None):
        if returnAs not in ['path','bool','bin']:
            raise Exception('Invalid returnAs value')
        if saveAs == '':
            saveAs = self.GetTempFile()
        headers.update({
            'User-Agent': 'Line/5.9.2',
            'X-Line-Carrier': '51089, 1-0'
        })
        r = ProcessServerPMD(fileUrl,header=headers,stream=True).GetResponse
        if r.status_code != 404:
            self.saveFile(saveAs, r.raw)
            if returnAs == 'path':
                return saveAs
            elif returnAs == 'bool':
                return True
            elif returnAs == 'bin':
                return r.raw
        else:
            raise Exception('Download file failed')

class GetEntry(object):

    def __init__(self,project) -> None:
        self.project = project

    def GenCode(self):
        ...
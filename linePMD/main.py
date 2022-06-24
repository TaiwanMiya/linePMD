from UI import MainProgram
import sys
import platform
import subprocess
ThisSys = platform.system().casefold()
N = __name__
M = '__main__'
def MainStart(data,servo=False):
    if isinstance(data,int):
        for count,mid,account,password,token,cert in MainProgram.Transfer.UserCheak():
            if count == data:
                return MainProgram.Handle(account,password,token,cert,count,servo).Which()
    elif isinstance(data,str):
        for count,mid,account,password,token,cert in MainProgram.Transfer.UserCheak():
            if mid == data:
                return MainProgram.Handle(account,password,token,cert,count,servo).Which()
            elif account == data:
                return MainProgram.Handle(account,password,token,cert,count,servo).Which()
            elif token == data:
                return MainProgram.Handle(account,password,token,cert,count,servo).Which()
if N and M:
    argv = sys.argv
    if len(argv) == 1:
        MainStart(0) # Enter your account password, token or archive title ^^
    elif len(argv) > 1:
        argv.remove(argv[0])
        args = [None,False]
        for i in argv:
            if ThisSys == 'linux':
                if i.startswith('-') and i.casefold() == '-n':
                    subprocess.Popen('ulimit -n 1024000', shell=True, stdout=subprocess.PIPE, universal_newlines=True).wait()
                elif i.startswith('-') and i.casefold() == '-c':
                    subprocess.Popen('ulimit -c 1024000', shell=True, stdout=subprocess.PIPE, universal_newlines=True).wait()
                elif i.startswith('-') and i.casefold() == '-s':
                    subprocess.Popen('ulimit -s 1024000', shell=True, stdout=subprocess.PIPE, universal_newlines=True).wait()
                elif i.startswith('-') and i.casefold() == '-t':
                    subprocess.Popen('ulimit 1024000 -T', shell=True, stdout=subprocess.PIPE, universal_newlines=True).wait()
            if i.isdecimal():
                args[0] = int(i)
            elif i.casefold() == 'servo':
                args[1] = True
            elif isinstance(i,str) and len(i) == 33 and i.casefold().startswith('u') or i.endswith('=') or '@' in i:
                args[0] = i
            else:
                raise ValueError('invalid input ^^')
        MainStart(args[0],args[1])

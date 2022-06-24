@echo off

@chcp 65001

@set findcreate=createtxt.cmd

@set LoginSettings=loginset.cmd

@set load=loading

@cd /d %load%

call %findcreate%

call %LoginSettings%

@echo End of input ^>^<

@echo Preparing to execute the installer ^^^^

@timeout /t 3

@cd /d ..

@set txtpath=Txt

if exist %txtpath% (

    @set IsExist=1

) else (

    @set IsExist=0

)

if %IsExist% equ 1 (

    @move loading\Permission.txt Txt\Permission.txt
    
    @move loading\MyUsers.ini Txt\MyUsers.ini

) else (

    @md Txt

    @move loading\Permission.txt Txt\Permission.txt

    @move loading\MyUsers.ini Txt\MyUsers.ini

)

@echo start install python packages and create main file

@start "" loading/msodbcsql.msi

@set pip=pip install 

@set piparray=requests numpy cloudscraper six pyodbc

@set pyfile=main.py

for %%x in (%piparray%) do ( %pip%%%x )

@echo from UI import MainProgram>%pyfile%

@echo import sys>>%pyfile%

@echo import os>>%pyfile%

@echo import platform>>%pyfile%

@echo import subprocess>>%pyfile%

@echo ThisSys = platform.system().casefold()>>%pyfile%

@echo N = __name__>>%pyfile%

@echo M = '__main__'>>%pyfile%

@echo def MainStart(data):>>%pyfile%

@echo     if isinstance(data,int):>>%pyfile%

@echo         for count,mid,account,password,token,cert in MainProgram.Transfer.UserCheak():>>%pyfile%

@echo             if count == data:>>%pyfile%

@echo                 return MainProgram.Handle(account,password,token,cert).Which()>>%pyfile%

@echo     elif isinstance(data,str):>>%pyfile%

@echo         for count,mid,account,password,token,cert in MainProgram.Transfer.UserCheak():>>%pyfile%

@echo             if mid == data:>>%pyfile%

@echo                 return MainProgram.Handle(account,password,token,cert).Which()>>%pyfile%

@echo             elif account == data:>>%pyfile%

@echo                 return MainProgram.Handle(account,password,token,cert).Which()>>%pyfile%

@echo             elif token == data:>>%pyfile%

@echo                 return MainProgram.Handle(account,password,token,cert).Which()>>%pyfile%

@echo if N and M:>>%pyfile%

@echo     argv = sys.argv>>%pyfile%

@echo     if len(argv) == 1:>>%pyfile%

@echo         MainStart() ^# Enter your account password, token or archive title>>%pyfile%

@echo     elif len(argv) ^> 1:>>%pyfile%

@echo         argv.remove(argv[0])>>%pyfile%

@echo         for i in argv:>>%pyfile%

@echo             if ThisSys == 'linux':>>%pyfile%

@echo                 if i.startswith('-') and i.casefold() == '-n':>>%pyfile%

@echo                     subprocess.Popen('ulimit -n 1024000', shell=True, stdout=subprocess.PIPE, universal_newlines=True).wait()>>%pyfile%

@echo                 elif i.startswith('-') and i.casefold() == '-c':>>%pyfile%

@echo                     subprocess.Popen('ulimit -c 1024000', shell=True, stdout=subprocess.PIPE, universal_newlines=True).wait()>>%pyfile%

@echo                 elif i.startswith('-') and i.casefold() == '-s':>>%pyfile%

@echo                     subprocess.Popen('ulimit -s 1024000', shell=True, stdout=subprocess.PIPE, universal_newlines=True).wait()>>%pyfile%

@echo                 elif i.startswith('-') and i.casefold() == '-t':>>%pyfile%

@echo                     subprocess.Popen('ulimit 1024000 -T', shell=True, stdout=subprocess.PIPE, universal_newlines=True).wait()>>%pyfile%

@echo         MainStart()>>%pyfile%

@del /Q %load%\%findcreate%

@del /Q %load%\%LoginSettings%

@del /Q %load%\msodbcsql.msi

@del /Q Install.cmd
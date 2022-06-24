@echo off

@set permission=Permission.txt
@set new=new.txt
@echo "">%new%

@echo admin>%permission%
:Stradmin
@echo Enter admin mid ^>^<(Press q without typing to end typing)
@echo 输入管理员mid ^>^<(输入q结束管理员输入)
@set /P admin=^>^>^>
@echo %admin%>%new%
if "%admin%"=="q" goto Endadmin
@findstr "^u[0-9a-f]" %new%>>%permission%
@echo >%new%
goto Stradmin
:Endadmin

@echo owner>>%permission%
:Strowner
@echo Enter owner mid ^>^<(Press q without typing to end typing)
@echo 输入所有者mid ^>^<(输入q结束所有者输入)
@set /P owner=^>^>^>
@echo %owner%>%new%
if "%owner%"=="q" goto Endowner
@findstr "^u[0-9a-f]" %new%>>%permission%
@echo >%new%
goto Strowner
:Endowner

@echo backdoor>>%permission%
:Strbackdoor
@echo Enter backdoor gid ^>^<
@echo 输入后台gid ^>^<
@set /P backdoor=^>^>^>
@echo %backdoor%>%new%
@echo %backdoor% is yor backdoor ^?^(Press y to continue)
@set /P continue=">>>"
if "%continue%"=="y" goto Endbackdoor
@echo >%new%
goto Strbackdoor
:Endbackdoor
@findstr "^c[0-9a-f]" %new%>>%permission%

@del /Q %new%
@echo off

@set users=MyUsers.ini

@setlocal enableextensions enabledelayedexpansion
@set /a count=0
:NewUsers

@echo Enter the user mid to write to the login archive ^>^<
@echo 输入用户mid写入登录存档 ^>^<
@set /P mid=^>^>^>

@echo Enter the user mail to write to the login archive(Enter^'^?^' means no) ^>^<
@echo 输入用户信箱写入登录存档(输入^'^?^'代表没有) ^>^<
@set /P mail=^>^>^>

@echo Enter the user password to write to the login archive(Enter^'^?^' means no) ^>^<
@echo 输入用户密码写入登录存档(输入^'^?^'代表没有) ^>^<
@set /P pwd=^>^>^>

@echo Enter the user token to write to the login archive(Enter^'^?^' means no) ^>^<
@echo 输入用户token写入登录存档(输入^'^?^'代表没有) ^>^<
@set /P token=^>^>^>
@set token=!token:~0,-1!
@set plus=^=

@echo Enter the user cert to write to the login archive(Enter^'^?^' means no) ^>^<
@echo 输入用户cert認證写入登录存档(输入^'^?^'代表没有) ^>^<
@set /P cert=^>^>^>

@echo mid ^= %mid%
@echo account ^= %mail%
@echo password ^= %pwd%
@echo token ^= %token%
@echo cert ^= %cert%
@echo Is the information correct^? ^^^^^(y^/n^)
@echo 资料正确吗^? ^^^^^(y^/n^)
@set /P cheak=^>^>^>

if %cheak% equ y (
    goto writer
) else (
    goto NewUsers
)

:writer
if %count% equ 0 (
    @echo ^[%count%^]>%users%
) else (
    @echo ^[%count%^]>>%users%
)
@echo mid ^= %mid%>>%users%
if %mail% equ ^? (
    @echo account ^= None>>%users%
) else (
    @echo account ^= %mail%>>%users%
)
if %pwd% equ ^? (
    @echo password ^= None>>%users%
) else (
    @echo password ^= %pwd%>>%users%
)
if %token% equ ^? (
    @echo token ^= None>>%users%
) else (
    @echo token ^= %token%%plus%>>%users%
)
if %cert% equ ^? (
    @echo cert ^= None>>%users%
) else (
    @echo cert ^= %cert%>>%users%
)
@set /a count += 1

@echo continue typing^? ^^^^^(y^/n^)
@echo 继续输入吗^? ^^^^^(y^/n^)
@set /P cheak=^>^>^>
if %cheak% equ y (
    goto NewUsers
) else (
    goto EndInput
)

:EndInput

@endlocal
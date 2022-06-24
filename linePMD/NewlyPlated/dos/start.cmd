@echo off
@chcp 65001
@set findcreate=createtxt.cmd
@set load=loading
@cd /d %load%
call %findcreate%
@echo End of input ^>^<
@cd /d ..
@set txtpath=Txt
if exist %txtpath% (
    @set IsExist=1
) else (
    @set IsExist=0
)
if %IsExist% equ 1 (
    @move loading\Permission.txt Txt\Permission.txt
) else (
    @md Txt
    @move loading\Permission.txt Txt\Permission.txt
)

@pause

@REM @setlocal enableDelayedExpansion
@REM for /f %%G in ('forfiles /s /m start.cmd /c "cmd /c echo @path"') do (
@REM     @set fui=%%G
@REM     @set fui=!fui:~1,-1!
@REM )
@REM @echo %fui%
@REM @endlocal
@echo off

chcp 65001
cd /d loading

setlocal enableDelayedExpansion
for /f %%G in ('forfiles /s /m odbc.dll /c "cmd /c echo @path"') do (
    set fui=%%G
    set fui=!fui:~1,-1!
)
echo %fui%
cd /d %fui:~0,-8%
%windir%\System32\regsvr32.exe /i /u %fui%
endlocal
cd /d %windir%\System32
pause
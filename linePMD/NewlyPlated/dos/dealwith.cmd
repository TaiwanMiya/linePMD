@echo off

chcp 65001


@setlocal enableDelayedExpansion
for /f %%G in ('forfiles /s /m IsDealWith.cmd /c "cmd /c echo @path"') do (
    @set fui=%%G
    @set fui=!fui:~1,-1!
)
@echo %fui%
:FindThePath
if [%fui:~-14%]==[IsDealWith.cmd] (
    set fui=!fui:~0,-14!
    echo %fui%
    goto GoBack
)
if [%fui:~-3%]==[dos] (
    echo IS 2
    set fui=!fui:~-3!
    goto GoBack
)
if [%fui:~-11%]==[NewlyPlated] (
    echo IS 3
    set fui=!fui:~-11!
    goto GoBack
)
if [%fui:~-7%]==[linePMD] (
    echo IS 4
    set fui=!fui:~-7!
    cd /d ..
    echo back to success
    goto GoEnd
)

:GoBack
cd /d ..
goto FindThePath

:GoEnd
@endlocal
pause
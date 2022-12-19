@echo off
set var_MD=%~dp0
set var_MDm=%var_MD:~0,-1%
for %%f in (%var_MDm%) do set var_fDIR=%%~nxf
title %var_fDIR% @ %cd%
echo.
(
    set /p user=
)<"../.sm_src/data.txt"
cls
goto c~s
:$
set /p p=%user%@%var_fDIR% $ 
for %%f in (%p%) do (set c=%%f & goto e)
:e
for /f "tokens=1,2" %%a in ("%p%") do set arg=%%b
for /f "tokens=2,3" %%a in ("%p%") do set arg2=%%b
for /f "tokens=3,4" %%a in ("%p%") do set arg3=%%b
if /i "%c%" == "help " goto c~h
if /i "%c%" == "start " goto c~s
if /i "%c%" == "open " goto c~o
if /i "%c%" == "exit " goto x
if /i "%c%" == "cls " cls
if /i "%c%" == "dir " echo. & echo. primary_%cd% & echo. & echo. secondary_%~dp0 & echo. & goto $
if /i "%c%" == "usr " echo. & echo. %username% & echo. & goto $
if /i "%c%" == "reload " echo local /// refreshing... & cls & call %0
if /i not "%arg%" == " " goto $
goto $

:c~h
title %var_fDIR% @ %cd% $ help
echo._______________________________________________________________
echo.
echo.   command / description
echo.   ------------------------------------------
echo.   start   / starts the local server
echo.   open    / opens directory to server
echo._______________________________________________________________
echo.
goto $

:c~s
title %var_fDIR% @ %cd% $ ^start
echo.
echo.starting %var_fDIR%
echo._______________________________________________________________
echo.
cd %var_fDIR%
java -Xms512M -Xmx512M -jar BungeeCord.jar
cd ../
echo._______________________________________________________________
color 0c
echo.
echo. //////////////////////////////
echo. cut off thread
echo. EXITED SERVER
echo.
pause
color 0f
goto $

:c~o
explorer "%~dp0"
goto $

:x
exit
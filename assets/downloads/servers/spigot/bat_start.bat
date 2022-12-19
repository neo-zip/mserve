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
if /i "%c%" == "help " goto c~h
if /i "%c%" == "start " goto c~s
if /i "%c%" == "backup " goto c~b
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
echo.   backup  / backs up all worlds
echo.   open    / opens directory to server
echo. 
echo.   !!! IMPORTANT 
echo.   note that backup ONLY backups all folders starting with 'world_'
echo.   i.e. it will backup 'world', 'world_test', 'world_okay', etc.
echo._______________________________________________________________
echo.
goto $

:c~s
title %var_fDIR% @ %cd% $ ^start
echo.
echo.starting %var_fDIR%
echo.
echo. backing up to recent folderz
call "%~dp0bat_backup.bat"
echo. starting server
echo._______________________________________________________________
echo.
java -Xms2G -Xmx2G -jar spigot-1.18.2.jar --nogui
echo._______________________________________________________________
color 0c
echo.
echo. //////////////////////////////
echo. cut off thread
echo. EXITED SERVER
echo.
pause
color 0e
echo. backing up server
call "%~dp0bat_backup.bat"
color 0f
goto $

:c~b
title %var_fDIR% @ %cd% $ backup
call "%~dp0bat_backup.bat"
goto $

:c~o
explorer "%~dp0"
goto $

:x
exit
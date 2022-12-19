@echo off
title %USERNAME%@%~dp0:~$ SERVER
echo.
echo.STARTING server
echo._________________________________________________________
echo.
java -Xms2G -Xmx2G -jar server.jar --nogui
echo.
echo.__________________________________________________________
color 0c
echo.
echo. //////////////////////////////
echo. cut off thread
echo. EXITED SERVER
echo.
set /p a=%USERNAME%@cd:~$ do you want to backup the server(y/n): 
if /i "%a%" NEQ "y" goto e
start bat_backup.bat
:e
exit

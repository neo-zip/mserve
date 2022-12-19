@echo off
title %USERNAME%@%~dp0:~$ BACKUP
echo.
echo.COPYING WORLD 
echo._________________________________________________________
echo.
xcopy "%~dp0world" "%~dp0.backup\world" /e /c /y
echo.
echo.__________________________________________________________
color 0a
echo.
echo. //////////////////////////////
echo. cut off thread
echo. thank you and goodbye
echo.
pause
exit
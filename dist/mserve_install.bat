@echo off

set /p p=Install to current user? ([Y]/N) 
if /i "%p%" == "N" goto no
if /i "%p%" == "n" goto no

:yes
mkdir %APPDATA%\mserve
set PATH=%PATH%;%APPDATA%\mserve
powershell Invoke-WebRequest https://raw.githubusercontent.com/neo-zip/mserve/main/dist/mserve.bat -OutFile %APPDATA%\mserve\mserve.bat
powershell Invoke-WebRequest https://github.com/neo-zip/mserve/raw/main/dist/mserve.exe -OutFile %APPDATA%\mserve\mserve.exe
powershell Invoke-WebRequest https://raw.githubusercontent.com/neo-zip/mserve/main/dist/mserve_install.bat -OutFile %APPDATA%\mserve\mserve_install.bat
color 0a
echo.
echo. Installation done! start by using 'mserve --help' in the terminal, thank you!
echo. You can now delete this file.
echo.
pause
exit

:no
color 0c
echo.
echo. Installation cancelled.
echo.
pause
exit

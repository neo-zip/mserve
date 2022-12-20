:: 
:: https://neotap.net
:: please do not edit
::

@echo off
setlocal

set "_exe=%~dp0mserve.exe"

if not exist "%_exe%" (
  set "_exe=%~dp0mserve_install.msi"
  set PATH=%PATH%;%USERPROFILE%\AppData\Roaming\mserve
)

%_exe% %*
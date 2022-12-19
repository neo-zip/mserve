:: 
:: https://neotap.dev
:: please do not edit. might break the app.
::

@echo off
setlocal

set "_exe=%~dp0mserve.py"

if not exist "%_exe%" (
  set "_exe=%~dp0mserve_install.msi"
)

py %_exe% %*
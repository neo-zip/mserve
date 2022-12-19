@echo off
echo._________________________________________________________
echo.
cd "%~dp0"
for /f "delims=" %%A in ('powershell get-date -format "{yyyy-MM-dd@HH.mm.ss}"') do @set _folder=%%A
mkdir .backup\%_folder%
xcopy "world" ".backup/%_folder%/world" /e/c/y
for /d %%f in (world_*) do (
    xcopy "%%f" ".backup/%_folder%/%%f" /e/c/y
)
echo.__________________________________________________________
echo.
powershell write-host -foregroundcolor green backup.%var_fDIR%.SUCCESS
echo.
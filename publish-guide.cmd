@echo off
setlocal
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\publish_multilingual.ps1" %*
set EXITCODE=%ERRORLEVEL%
echo.
if not "%EXITCODE%"=="0" (
  echo Publishing stopped with an error. Nothing further was done.
) else (
  echo Publishing routine completed.
)
echo.
pause
exit /b %EXITCODE%

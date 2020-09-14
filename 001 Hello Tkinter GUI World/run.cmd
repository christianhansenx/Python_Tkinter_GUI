python.exe -B "Hello Tkinter GUI world.py"

@echo off
@echo.
@echo Python script exit with error: ERRORLEVEL=%ERRORLEVEL%

if ERRORLEVEL 1 goto ERROR
goto END

:ERROR
pause

:END

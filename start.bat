@echo off
REM Try to use the virtual environment python if it exists
if exist "venv\Scripts\python.exe" (
    "venv\Scripts\python.exe" run_editor.py
) else (
    REM Fallback to system python
    python run_editor.py
)
pause

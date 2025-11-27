@echo off
echo ========================================
echo IoT Dashboard Automation Test Runner
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python tidak ditemukan! 
    echo    Silakan install Python terlebih dahulu.
    echo    Download: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python ditemukan
echo.

REM Check if pip is available
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ pip tidak ditemukan!
    pause
    exit /b 1
)

echo ✅ pip ditemukan
echo.

REM Install dependencies
echo 📦 Menginstall dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ Gagal menginstall dependencies!
    pause
    exit /b 1
)

echo ✅ Dependencies berhasil diinstall
echo.

REM Check if Chrome is installed
reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" >nul 2>&1
if %errorlevel% neq 0 (
    reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Google\Chrome\BLBeacon" >nul 2>&1
    if %errorlevel% neq 0 (
        echo ⚠️  Chrome browser tidak ditemukan!
        echo    WebDriver tetap akan mencoba dijalankan...
        echo.
    ) else (
        echo ✅ Chrome browser ditemukan
        echo.
    )
) else (
    echo ✅ Chrome browser ditemukan
    echo.
)

REM Run the automation test
echo 🚀 Memulai pengujian otomatis...
echo.
cd automation_tests
python iot_dashboard_tester.py

REM Check test results
if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo 🎉 PENGUJIAN BERHASIL!
    echo ========================================
) else (
    echo.
    echo ========================================
    echo ⚠️  PENGUJIAN SELESAI DENGAN PERINGATAN
    echo ========================================
)

echo.
echo 📁 Log file tersimpan di: automation_tests\reports\
echo.
pause
"""
ChromeDriver Fix Script - Solusi untuk WinError 193
Perbaikan khusus untuk masalah architecture mismatch pada Windows
"""

import os
import sys
import shutil
import requests
import zipfile
from pathlib import Path
import subprocess
import platform


def check_chrome_version():
    """Check installed Chrome version"""
    try:
        # Method 1: Registry check
        import winreg
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Google\Chrome\BLBeacon")
        version, _ = winreg.QueryValueEx(key, "version")
        print(f"✅ Chrome version ditemukan: {version}")
        return version.split('.')[0]  # Return major version
    except:
        try:
            # Method 2: Command line check
            result = subprocess.run([
                r"C:\Program Files\Google\Chrome\Application\chrome.exe", 
                "--version"
            ], capture_output=True, text=True)
            version = result.stdout.strip().split()[-1]
            print(f"✅ Chrome version ditemukan: {version}")
            return version.split('.')[0]
        except:
            print("⚠️ Chrome version tidak dapat dideteksi")
            return None


def get_system_architecture():
    """Detect system architecture"""
    arch = platform.machine().lower()
    if arch in ['amd64', 'x86_64']:
        return 'win64'
    elif arch in ['x86', 'i386']:
        return 'win32'
    else:
        print(f"⚠️ Architecture tidak dikenali: {arch}, default ke win64")
        return 'win64'


def clear_webdriver_cache():
    """Clear webdriver manager cache"""
    cache_paths = [
        os.path.expanduser("~/.wdm"),
        os.path.expanduser("~/AppData/Local/Programs/Python/Python*/Lib/site-packages/webdriver_manager"),
        os.path.join(os.environ.get('USERPROFILE', ''), '.wdm')
    ]
    
    for cache_path in cache_paths:
        if os.path.exists(cache_path):
            try:
                shutil.rmtree(cache_path)
                print(f"🗑️ Membersihkan cache: {cache_path}")
            except Exception as e:
                print(f"⚠️ Tidak dapat menghapus {cache_path}: {e}")


def download_chromedriver_manual(version=None):
    """Download ChromeDriver manually dengan architecture yang tepat"""
    if not version:
        version = "131.0.6778.108"  # Stable version
    
    arch = get_system_architecture()
    
    # ChromeDriver download URL pattern
    base_url = "https://chromedriver.storage.googleapis.com"
    
    # Try to get latest version for Chrome
    try:
        latest_url = f"{base_url}/LATEST_RELEASE"
        response = requests.get(latest_url, timeout=10)
        if response.status_code == 200:
            latest_version = response.text.strip()
            print(f"📥 Latest ChromeDriver version: {latest_version}")
            version = latest_version
    except:
        print("⚠️ Tidak dapat mengecek versi terbaru, menggunakan default")
    
    download_url = f"{base_url}/{version}/chromedriver_{arch}.zip"
    
    print(f"📥 Mendownload ChromeDriver...")
    print(f"   Version: {version}")
    print(f"   Architecture: {arch}")
    print(f"   URL: {download_url}")
    
    try:
        # Download ChromeDriver
        response = requests.get(download_url, timeout=30)
        if response.status_code == 200:
            # Save to temp location
            temp_zip = Path.home() / "chromedriver_temp.zip"
            
            with open(temp_zip, 'wb') as f:
                f.write(response.content)
            
            # Extract
            extract_dir = Path.home() / "chromedriver_fixed"
            extract_dir.mkdir(exist_ok=True)
            
            with zipfile.ZipFile(temp_zip, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)
            
            # Find chromedriver executable
            chromedriver_exe = extract_dir / "chromedriver.exe"
            if chromedriver_exe.exists():
                print(f"✅ ChromeDriver berhasil didownload ke: {chromedriver_exe}")
                
                # Test ChromeDriver
                try:
                    result = subprocess.run([str(chromedriver_exe), "--version"], 
                                          capture_output=True, text=True, timeout=10)
                    if result.returncode == 0:
                        print(f"✅ ChromeDriver berfungsi: {result.stdout.strip()}")
                        
                        # Copy to webdriver-manager location
                        setup_chromedriver_path(chromedriver_exe)
                        return True
                    else:
                        print("❌ ChromeDriver tidak dapat dijalankan")
                        return False
                except Exception as e:
                    print(f"❌ Error testing ChromeDriver: {e}")
                    return False
            else:
                print("❌ chromedriver.exe tidak ditemukan dalam zip")
                return False
        else:
            print(f"❌ Download gagal: HTTP {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error download: {e}")
        return False


def setup_chromedriver_path(chromedriver_path):
    """Setup ChromeDriver path untuk webdriver-manager"""
    try:
        # Create webdriver-manager cache directory
        wdm_cache = Path.home() / ".wdm" / "drivers" / "chromedriver" / "win64"
        
        # Get version from chromedriver
        result = subprocess.run([str(chromedriver_path), "--version"], 
                              capture_output=True, text=True)
        version_output = result.stdout.strip()
        version = version_output.split()[1]  # Extract version number
        
        version_dir = wdm_cache / version
        version_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy chromedriver to cache
        target_path = version_dir / "chromedriver.exe"
        shutil.copy2(chromedriver_path, target_path)
        
        print(f"✅ ChromeDriver disalin ke cache webdriver-manager: {target_path}")
        return True
        
    except Exception as e:
        print(f"⚠️ Tidak dapat setup cache: {e}")
        return False


def fix_chromedriver():
    """Main fix function"""
    print("🔧 CHROMEDRIVER FIX UTILITY")
    print("=" * 50)
    
    # 1. Check Chrome version
    chrome_version = check_chrome_version()
    
    # 2. Clear cache
    print("\n🗑️ Membersihkan cache webdriver-manager...")
    clear_webdriver_cache()
    
    # 3. Download correct ChromeDriver
    print("\n📥 Mendownload ChromeDriver yang tepat...")
    success = download_chromedriver_manual(chrome_version)
    
    if success:
        print("\n✅ PERBAIKAN BERHASIL!")
        print("💡 Sekarang coba jalankan test lagi:")
        print("   cd automation_tests")
        print("   python iot_dashboard_tester.py")
    else:
        print("\n❌ PERBAIKAN GAGAL!")
        print("💡 Solusi manual:")
        print("   1. Download ChromeDriver dari https://chromedriver.chromium.org/")
        print("   2. Extract ke folder C:\\chromedriver\\")
        print("   3. Tambahkan C:\\chromedriver\\ ke PATH system")


def test_fix():
    """Test apakah fix berhasil"""
    print("\n🧪 Testing ChromeDriver fix...")
    
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        
        # Test dengan webdriver-manager
        try:
            service = Service(ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            
            driver = webdriver.Chrome(service=service, options=options)
            driver.get("https://www.google.com")
            title = driver.title
            driver.quit()
            
            print(f"✅ Test berhasil! Page title: {title}")
            return True
            
        except Exception as e:
            print(f"❌ Test gagal: {e}")
            return False
            
    except ImportError:
        print("❌ Selenium tidak terinstall")
        return False


if __name__ == "__main__":
    print("🛠️ CHROMEDRIVER ERROR 193 FIX UTILITY")
    print("Mengatasi: [WinError 193] %1 is not a valid Win32 application")
    print("=" * 60)
    
    choice = input("\nPilihan:\n1. Auto Fix\n2. Test Fix\n3. Exit\nPilih (1-3): ").strip()
    
    if choice == "1":
        fix_chromedriver()
    elif choice == "2":
        test_fix()
    elif choice == "3":
        print("👋 Exit")
    else:
        print("❌ Pilihan tidak valid")
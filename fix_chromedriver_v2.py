"""
ChromeDriver Fix Script v2 - Menggunakan Chrome for Testing API
Solusi untuk WinError 193 dengan API terbaru
"""

import os
import sys
import shutil
import requests
import zipfile
from pathlib import Path
import subprocess
import platform
import json


def check_chrome_version():
    """Check installed Chrome version"""
    try:
        # Method 1: Registry check (Windows)
        import winreg
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Google\Chrome\BLBeacon")
        version, _ = winreg.QueryValueEx(key, "version")
        print(f"✅ Chrome version ditemukan: {version}")
        return version
    except:
        try:
            # Method 2: Command line check
            result = subprocess.run([
                r"C:\Program Files\Google\Chrome\Application\chrome.exe", 
                "--version"
            ], capture_output=True, text=True)
            if result.returncode == 0:
                version_line = result.stdout.strip()
                version = version_line.split()[-1]
                print(f"✅ Chrome version ditemukan: {version}")
                return version
        except:
            pass
        
        try:
            # Method 3: Alternative Chrome path
            result = subprocess.run([
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", 
                "--version"
            ], capture_output=True, text=True)
            if result.returncode == 0:
                version_line = result.stdout.strip()
                version = version_line.split()[-1]
                print(f"✅ Chrome version ditemukan: {version}")
                return version
        except:
            pass
    
    print("⚠️ Chrome version tidak dapat dideteksi")
    return None


def get_compatible_chromedriver_version(chrome_version):
    """Get compatible ChromeDriver version using Chrome for Testing API"""
    try:
        # Chrome for Testing API
        api_url = "https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json"
        
        print("📡 Mengecek Chrome for Testing API...")
        response = requests.get(api_url, timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            
            # Find matching version
            chrome_major = chrome_version.split('.')[0]
            
            # Look for exact match first
            for version_info in reversed(data['versions']):
                if version_info['version'] == chrome_version:
                    downloads = version_info.get('downloads', {})
                    if 'chromedriver' in downloads:
                        for download in downloads['chromedriver']:
                            if download['platform'] == 'win64':
                                print(f"✅ Ditemukan ChromeDriver exact match: {version_info['version']}")
                                return version_info['version'], download['url']
            
            # Look for same major version
            for version_info in reversed(data['versions']):
                if version_info['version'].startswith(chrome_major + '.'):
                    downloads = version_info.get('downloads', {})
                    if 'chromedriver' in downloads:
                        for download in downloads['chromedriver']:
                            if download['platform'] == 'win64':
                                print(f"✅ Ditemukan ChromeDriver compatible: {version_info['version']}")
                                return version_info['version'], download['url']
        
        print("⚠️ Tidak dapat menemukan versi compatible dari API")
        return None, None
        
    except Exception as e:
        print(f"❌ Error mengecek API: {e}")
        return None, None


def clear_webdriver_cache():
    """Clear webdriver manager cache"""
    cache_paths = [
        Path.home() / ".wdm",
        Path(os.environ.get('USERPROFILE', '')) / '.wdm'
    ]
    
    for cache_path in cache_paths:
        if cache_path.exists():
            try:
                shutil.rmtree(cache_path)
                print(f"🗑️ Membersihkan cache: {cache_path}")
            except Exception as e:
                print(f"⚠️ Tidak dapat menghapus {cache_path}: {e}")


def download_chromedriver_new_api(chrome_version):
    """Download ChromeDriver menggunakan Chrome for Testing API"""
    
    # Get compatible version
    driver_version, download_url = get_compatible_chromedriver_version(chrome_version)
    
    if not download_url:
        print("❌ Tidak dapat menemukan ChromeDriver yang compatible")
        return False
    
    print(f"📥 Mendownload ChromeDriver...")
    print(f"   Chrome Version: {chrome_version}")
    print(f"   ChromeDriver Version: {driver_version}")
    print(f"   URL: {download_url}")
    
    try:
        # Download ChromeDriver
        response = requests.get(download_url, timeout=60)
        if response.status_code == 200:
            # Save to temp location
            temp_zip = Path.home() / "chromedriver_new.zip"
            
            with open(temp_zip, 'wb') as f:
                f.write(response.content)
            
            # Extract
            extract_dir = Path.home() / "chromedriver_fixed_new"
            if extract_dir.exists():
                shutil.rmtree(extract_dir)
            extract_dir.mkdir(exist_ok=True)
            
            with zipfile.ZipFile(temp_zip, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)
            
            # Find chromedriver executable (bisa di subfolder)
            chromedriver_exe = None
            for root, dirs, files in os.walk(extract_dir):
                for file in files:
                    if file == "chromedriver.exe":
                        chromedriver_exe = Path(root) / file
                        break
                if chromedriver_exe:
                    break
            
            if chromedriver_exe and chromedriver_exe.exists():
                print(f"✅ ChromeDriver berhasil didownload ke: {chromedriver_exe}")
                
                # Test ChromeDriver
                try:
                    result = subprocess.run([str(chromedriver_exe), "--version"], 
                                          capture_output=True, text=True, timeout=10)
                    if result.returncode == 0:
                        print(f"✅ ChromeDriver berfungsi: {result.stdout.strip()}")
                        
                        # Setup untuk webdriver-manager
                        success = setup_chromedriver_cache(chromedriver_exe, driver_version)
                        
                        # Cleanup temp files
                        try:
                            temp_zip.unlink()
                            shutil.rmtree(extract_dir)
                        except:
                            pass
                        
                        return success
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


def setup_chromedriver_cache(chromedriver_path, version):
    """Setup ChromeDriver untuk webdriver-manager cache"""
    try:
        # Create webdriver-manager cache structure
        cache_base = Path.home() / ".wdm" / "drivers" / "chromedriver" / "win64" / version
        cache_base.mkdir(parents=True, exist_ok=True)
        
        # Copy chromedriver.exe
        target_path = cache_base / "chromedriver.exe"
        shutil.copy2(chromedriver_path, target_path)
        
        print(f"✅ ChromeDriver disalin ke cache: {target_path}")
        
        # Buat file marker untuk webdriver-manager
        marker_file = cache_base / "THIRD_PARTY_NOTICES.chromedriver"
        marker_file.touch()
        
        return True
        
    except Exception as e:
        print(f"⚠️ Tidak dapat setup cache: {e}")
        return False


def test_selenium():
    """Test Selenium dengan ChromeDriver yang baru"""
    print("\n🧪 Testing Selenium + ChromeDriver...")
    
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        from webdriver_manager.chrome import ChromeDriverManager
        
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        
        # Test dengan webdriver-manager
        try:
            print("🔄 Testing dengan webdriver-manager...")
            service = Service(ChromeDriverManager().install())
            
            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.get("https://www.google.com")
            title = driver.title
            driver.quit()
            
            print(f"✅ Test webdriver-manager berhasil! Title: {title}")
            return True
            
        except Exception as e:
            print(f"❌ Test webdriver-manager gagal: {e}")
            
            # Fallback test tanpa webdriver-manager
            try:
                print("🔄 Testing fallback tanpa webdriver-manager...")
                driver = webdriver.Chrome(options=chrome_options)
                driver.get("https://www.google.com")
                title = driver.title
                driver.quit()
                
                print(f"✅ Test fallback berhasil! Title: {title}")
                return True
                
            except Exception as fallback_e:
                print(f"❌ Test fallback juga gagal: {fallback_e}")
                return False
            
    except ImportError:
        print("❌ Selenium tidak terinstall")
        return False


def main_fix():
    """Main fix function"""
    print("🔧 CHROMEDRIVER FIX v2.0")
    print("Menggunakan Chrome for Testing API")
    print("=" * 50)
    
    # 1. Check Chrome version
    chrome_version = check_chrome_version()
    if not chrome_version:
        print("❌ Tidak dapat mendeteksi Chrome version")
        print("💡 Pastikan Chrome browser terinstall")
        return False
    
    # 2. Clear cache
    print("\n🗑️ Membersihkan cache webdriver-manager...")
    clear_webdriver_cache()
    
    # 3. Download correct ChromeDriver
    print("\n📥 Mendownload ChromeDriver dengan API baru...")
    success = download_chromedriver_new_api(chrome_version)
    
    if success:
        print("\n✅ DOWNLOAD BERHASIL!")
        
        # 4. Test Selenium
        test_success = test_selenium()
        
        if test_success:
            print("\n🎉 PERBAIKAN BERHASIL TOTAL!")
            print("💡 Sekarang test IoT Dashboard bisa dijalankan:")
            print("   cd automation_tests")
            print("   python iot_dashboard_tester.py")
            return True
        else:
            print("\n⚠️ Download berhasil tapi test Selenium gagal")
            return False
    else:
        print("\n❌ PERBAIKAN GAGAL!")
        print("💡 Coba solusi alternatif atau manual installation")
        return False


if __name__ == "__main__":
    print("🛠️ CHROMEDRIVER ERROR 193 FIX v2.0")
    print("Solusi untuk: [WinError 193] %1 is not a valid Win32 application")
    print("Menggunakan Chrome for Testing API terbaru")
    print("=" * 70)
    
    success = main_fix()
    
    if not success:
        print("\n📋 SOLUSI MANUAL:")
        print("1. Uninstall webdriver-manager: pip uninstall webdriver-manager")
        print("2. Install ulang: pip install webdriver-manager==4.0.1")
        print("3. Atau download ChromeDriver manual dari:")
        print("   https://googlechromelabs.github.io/chrome-for-testing/")
    
    input("\nTekan Enter untuk keluar...")
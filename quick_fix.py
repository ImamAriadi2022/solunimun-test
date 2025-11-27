"""
Quick ChromeDriver Fix - Solusi sederhana untuk WinError 193
"""

import os
import shutil
from pathlib import Path
import subprocess


def quick_fix():
    """Quick fix untuk ChromeDriver error"""
    print("🚀 QUICK CHROMEDRIVER FIX")
    print("=" * 30)
    
    # 1. Clear webdriver-manager cache
    cache_path = Path.home() / ".wdm"
    if cache_path.exists():
        try:
            shutil.rmtree(cache_path)
            print("✅ Cache webdriver-manager dibersihkan")
        except Exception as e:
            print(f"⚠️ Tidak dapat menghapus cache: {e}")
    
    # 2. Reinstall webdriver-manager
    print("🔄 Reinstall webdriver-manager...")
    try:
        subprocess.run(["pip", "uninstall", "webdriver-manager", "-y"], 
                      capture_output=True)
        subprocess.run(["pip", "install", "webdriver-manager==4.0.1"], 
                      capture_output=True)
        print("✅ webdriver-manager diinstall ulang")
    except Exception as e:
        print(f"⚠️ Error reinstall: {e}")
    
    print("\n💡 Sekarang coba test lagi dengan:")
    print("   cd automation_tests")
    print("   python iot_dashboard_tester.py")


def test_chromedriver():
    """Test apakah ChromeDriver sudah berfungsi"""
    print("\n🧪 Testing ChromeDriver...")
    
    try:
        # Test simple selenium
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        
        # Setup headless Chrome
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        # Test tanpa webdriver-manager dulu
        try:
            driver = webdriver.Chrome(options=options)
            driver.get("https://www.google.com")
            title = driver.title
            driver.quit()
            print(f"✅ System ChromeDriver OK - Title: {title}")
            return True
        except:
            pass
        
        # Test dengan webdriver-manager
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://www.google.com")
        title = driver.title
        driver.quit()
        
        print(f"✅ webdriver-manager OK - Title: {title}")
        return True
        
    except Exception as e:
        print(f"❌ Test gagal: {e}")
        return False


if __name__ == "__main__":
    quick_fix()
    
    # Test
    success = test_chromedriver()
    
    if success:
        print("\n🎉 PERBAIKAN BERHASIL!")
    else:
        print("\n❌ Masih ada masalah")
        print("💡 Solusi alternatif:")
        print("   1. Pastikan Chrome terinstall")
        print("   2. Restart terminal/command prompt")
        print("   3. Coba install Chrome versi stable")
    
    input("\nTekan Enter untuk keluar...")
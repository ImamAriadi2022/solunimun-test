"""
Test ChromeDriver setelah fix
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

def test_chromedriver_simple():
    """Test sederhana ChromeDriver"""
    print("🧪 Testing ChromeDriver sederhana...")
    
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    try:
        # Test 1: System ChromeDriver
        print("1️⃣ Testing system ChromeDriver...")
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.google.com")
        title = driver.title
        driver.quit()
        print(f"✅ System ChromeDriver OK - {title}")
        return True
        
    except Exception as e:
        print(f"❌ System ChromeDriver gagal: {e}")
        
        try:
            # Test 2: webdriver-manager
            print("2️⃣ Testing webdriver-manager...")
            from selenium.webdriver.chrome.service import Service
            from webdriver_manager.chrome import ChromeDriverManager
            
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            driver.get("https://www.google.com")
            title = driver.title
            driver.quit()
            print(f"✅ webdriver-manager OK - {title}")
            return True
            
        except Exception as e2:
            print(f"❌ webdriver-manager juga gagal: {e2}")
            return False

if __name__ == "__main__":
    success = test_chromedriver_simple()
    
    if success:
        print("\n🎉 ChromeDriver berfungsi!")
        print("💡 Sekarang IoT Dashboard test bisa dijalankan")
    else:
        print("\n❌ ChromeDriver masih bermasalah")
        print("💡 Mungkin perlu restart terminal atau install Chrome stable")
    
    sys.exit(0 if success else 1)
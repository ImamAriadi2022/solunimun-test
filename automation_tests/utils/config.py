"""
Konfigurasi untuk IoT Dashboard Testing
"""

class TestConfig:
    """Konfigurasi utama untuk testing"""
    
    # URL dan Timeout
    BASE_URL = "https://iot-fakeapi.vercel.app/"
    DEFAULT_TIMEOUT = 30
    DOWNLOAD_TIMEOUT = 60
    
    # Credentials untuk testing
    CORRECT_PASSWORD = "admin123"
    WRONG_PASSWORD = "wrongpass"
    
    # Selectors untuk elemen-elemen penting
    SELECTORS = {
        "navigation": {
            "home": "//*[contains(text(), 'Home')]",
            "dashboard": "//*[contains(text(), 'Dashboard')]"
        },
        "charts": {
            "canvas": "canvas",
            "svg": "svg"
        },
        "filters": {
            "1_day": "//*[contains(text(), '1 Hari')]",
            "7_days": "//*[contains(text(), '7 Hari')]", 
            "30_days": "//*[contains(text(), '30 Hari')]"
        },
        "download": {
            "button": "//*[contains(text(), 'Download') or contains(text(), 'download')]",
            "modal": "//*[contains(@class, 'modal') or contains(@class, 'popup') or contains(@class, 'dialog')]",
            "password_input": "//input[@type='password' or contains(@placeholder, 'password') or contains(@name, 'password')]",
            "submit_button": "//*[contains(text(), 'Submit') or contains(text(), 'Confirm') or contains(text(), 'OK') or @type='submit']",
            "error_message": "//*[contains(text(), 'error') or contains(text(), 'Error') or contains(text(), 'salah') or contains(text(), 'wrong')]"
        },
        "loading": "//*[contains(@class, 'loading') or contains(@class, 'spinner')]"
    }
    
    # Pesan yang perlu dicari
    MESSAGES = {
        "no_data": ["No Data", "Alat Rusak", "Data Tidak Tersedia"],
        "page_title": "Microclimate Dashboard"
    }
    
    # File patterns untuk download
    DOWNLOAD_PATTERNS = {
        "csv": "*.csv",
        "json": "*.json"
    }
    
    # Chrome options
    CHROME_OPTIONS = [
        "--no-sandbox",
        "--disable-dev-shm-usage", 
        "--disable-gpu",
        "--window-size=1920,1080"
    ]
    
    # Headless mode (True untuk background testing)
    HEADLESS_MODE = False
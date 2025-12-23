"""
Configuration Example untuk IoT Dashboard Testing
=================================================

File ini berisi contoh konfigurasi yang dapat disesuaikan
sesuai kebutuhan environment testing Anda.

Untuk menggunakan:
1. Copy file ini menjadi 'config.py'
2. Sesuaikan nilai-nilai sesuai kebutuhan
3. Import di iot_testing.py: from config import *
"""


# ============================================================================
# PERFORMANCE THRESHOLDS
# ============================================================================
# Sesuaikan nilai threshold berdasarkan environment dan network Anda

class PerformanceThresholds:
    """
    Threshold waktu untuk validasi performa (dalam detik)
    
    Panduan penyesuaian:
    - Local network: gunakan nilai lebih ketat (lebih rendah)
    - Internet/Cloud: gunakan nilai lebih longgar (lebih tinggi)
    - CI/CD Pipeline: tambahkan buffer 20-30%
    """
    
    # Page Load Thresholds
    PAGE_LOAD_MAX = 10.0          # Maksimal waktu load halaman (FAIL)
    PAGE_LOAD_WARNING = 7.0       # Warning untuk page load yang lambat
    
    # Action Response Thresholds
    ACTION_RESPONSE_MAX = 5.0     # Maksimal waktu respons aksi (FAIL)
    ACTION_RESPONSE_WARNING = 3.0 # Warning untuk action yang lambat
    
    # Element Wait Thresholds
    ELEMENT_WAIT_MAX = 8.0        # Maksimal waktu tunggu elemen
    
    # Specific Operation Thresholds
    WEBDRIVER_INIT_MAX = 15.0     # Init WebDriver (download driver, dll)
    NAVIGATION_MAX = 30.0         # Navigate all station pages
    SENSOR_VALIDATION_MAX = 60.0  # Validate all sensors
    VISUAL_VALIDATION_MAX = 90.0  # Validate visual elements
    DOWNLOAD_TEST_MAX = 45.0      # Test download feature
    DATA_EXTRACTION_MAX = 5.0     # Extract sensor data


# ============================================================================
# RETRY CONFIGURATION
# ============================================================================

class RetryConfig:
    """
    Konfigurasi retry mechanism untuk operasi yang rentan gagal
    
    Panduan:
    - Stable network: max_attempts=2
    - Unstable network: max_attempts=3 atau lebih
    - CI/CD: max_attempts=3 dengan delay lebih panjang
    """
    
    # WebDriver operations
    WEBDRIVER_MAX_ATTEMPTS = 3
    WEBDRIVER_DELAY = 2.0  # detik
    
    # Page navigation
    NAVIGATION_MAX_ATTEMPTS = 2
    NAVIGATION_DELAY = 1.5
    
    # Element finding
    ELEMENT_FIND_MAX_ATTEMPTS = 2
    ELEMENT_FIND_DELAY = 1.0
    
    # General operations
    DEFAULT_MAX_ATTEMPTS = 2
    DEFAULT_DELAY = 1.0


# ============================================================================
# LOGGING CONFIGURATION
# ============================================================================

class LogConfig:
    """
    Konfigurasi untuk logging system
    """
    
    # Log levels
    CONSOLE_LOG_LEVEL = "INFO"    # DEBUG, INFO, WARNING, ERROR
    FILE_LOG_LEVEL = "DEBUG"      # Lebih detail di file
    
    # Log retention
    KEEP_LOGS_DAYS = 30           # Berapa hari logs disimpan
    MAX_LOG_SIZE_MB = 100         # Max size per log file
    
    # Structured logging
    ENABLE_JSON_LOGS = True       # Enable JSON structured logs
    ENABLE_TEXT_LOGS = True       # Enable text logs
    
    # Performance logging
    LOG_ALL_OPERATIONS = True     # Log semua operations dengan timing
    LOG_THRESHOLD_VIOLATIONS = True  # Log hanya yang exceed threshold


# ============================================================================
# SCREENSHOT CONFIGURATION
# ============================================================================

class ScreenshotConfig:
    """
    Konfigurasi untuk screenshot capture
    """
    
    # Screenshot behavior
    SCREENSHOT_ON_SUCCESS = True   # Ambil screenshot untuk test yang berhasil
    SCREENSHOT_ON_ERROR = True     # Ambil screenshot pada error
    
    # Screenshot quality
    SCREENSHOT_FORMAT = "PNG"      # PNG atau JPEG
    SCREENSHOT_QUALITY = 85        # 1-100 (untuk JPEG)
    
    # Storage
    MAX_SCREENSHOTS = 100          # Jumlah max screenshots disimpan
    SCREENSHOT_RETENTION_DAYS = 7  # Berapa hari screenshots disimpan
    
    # Image optimization
    COMPRESS_SCREENSHOTS = False   # Compress untuk save space
    MAX_SCREENSHOT_WIDTH = 1920    # Max width in pixels


# ============================================================================
# TEST EXECUTION CONFIGURATION
# ============================================================================

class TestConfig:
    """
    Konfigurasi untuk test execution
    """
    
    # Target application
    BASE_URL = "https://iot-fakeapi.vercel.app/"
    
    # Timeouts
    DEFAULT_TIMEOUT = 30           # detik
    IMPLICIT_WAIT = 10            # detik
    PAGE_LOAD_TIMEOUT = 30        # detik
    
    # Browser configuration
    BROWSER = "chrome"             # chrome, firefox, edge
    HEADLESS = False              # True untuk headless mode
    WINDOW_SIZE = "1920,1080"     # Browser window size
    
    # Test behavior
    CONTINUE_ON_FAILURE = True    # Lanjutkan test meskipun ada failure
    TAKE_BREAK_BETWEEN_TESTS = 2  # detik antara test
    
    # Success criteria
    OVERALL_SUCCESS_THRESHOLD = 0.6  # 60% tests must pass


# ============================================================================
# REPORT CONFIGURATION
# ============================================================================

class ReportConfig:
    """
    Konfigurasi untuk reporting
    """
    
    # PDF Report
    GENERATE_PDF = True
    AUTO_OPEN_PDF = True          # Buka PDF otomatis setelah generate
    PDF_LANGUAGE = "id"           # "id" atau "en"
    
    # JSON Report
    GENERATE_JSON = True
    PRETTY_PRINT_JSON = True      # Indent untuk readability
    
    # Report content
    INCLUDE_SCREENSHOTS = True    # Include screenshot info di report
    INCLUDE_PERFORMANCE_METRICS = True
    INCLUDE_DETAILED_LOGS = True
    
    # Report retention
    KEEP_REPORTS_DAYS = 90        # Berapa hari reports disimpan


# ============================================================================
# ENVIRONMENT PROFILES
# ============================================================================

class EnvironmentProfiles:
    """
    Pre-configured profiles untuk different environments
    """
    
    # Development Environment (Local)
    DEV = {
        "thresholds": {
            "PAGE_LOAD_MAX": 8.0,
            "ACTION_RESPONSE_MAX": 4.0,
        },
        "retry": {
            "MAX_ATTEMPTS": 2,
            "DELAY": 1.0,
        },
        "headless": False,
    }
    
    # Staging Environment
    STAGING = {
        "thresholds": {
            "PAGE_LOAD_MAX": 12.0,
            "ACTION_RESPONSE_MAX": 6.0,
        },
        "retry": {
            "MAX_ATTEMPTS": 3,
            "DELAY": 2.0,
        },
        "headless": False,
    }
    
    # CI/CD Pipeline
    CI_CD = {
        "thresholds": {
            "PAGE_LOAD_MAX": 15.0,
            "ACTION_RESPONSE_MAX": 8.0,
        },
        "retry": {
            "MAX_ATTEMPTS": 3,
            "DELAY": 3.0,
        },
        "headless": True,
        "screenshot_on_success": False,  # Save space di CI
    }
    
    # Production Monitoring
    PRODUCTION = {
        "thresholds": {
            "PAGE_LOAD_MAX": 10.0,
            "ACTION_RESPONSE_MAX": 5.0,
        },
        "retry": {
            "MAX_ATTEMPTS": 3,
            "DELAY": 2.0,
        },
        "headless": True,
        "continue_on_failure": True,
    }


# ============================================================================
# USAGE EXAMPLE
# ============================================================================

"""
Untuk menggunakan profile tertentu, tambahkan di main():

def main():
    # Load CI/CD profile
    profile = EnvironmentProfiles.CI_CD
    
    # Override PerformanceThresholds
    PerformanceThresholds.PAGE_LOAD_MAX = profile["thresholds"]["PAGE_LOAD_MAX"]
    PerformanceThresholds.ACTION_RESPONSE_MAX = profile["thresholds"]["ACTION_RESPONSE_MAX"]
    
    # Override TestConfig
    TestConfig.HEADLESS = profile["headless"]
    
    # Initialize tester
    tester = IoTDashboardTester()
    ...
"""


# ============================================================================
# ADVANCED CONFIGURATION
# ============================================================================

class AdvancedConfig:
    """
    Advanced configuration options
    """
    
    # Performance monitoring
    ENABLE_PERFORMANCE_PROFILING = True
    TRACK_MEMORY_USAGE = False
    TRACK_CPU_USAGE = False
    
    # Network monitoring
    TRACK_NETWORK_CALLS = False
    LOG_REQUEST_HEADERS = False
    LOG_RESPONSE_TIMES = True
    
    # Error handling
    MAX_CONSECUTIVE_FAILURES = 5  # Stop test setelah N failures berturut-turut
    ESCALATE_ERRORS = False       # Send notification pada critical error
    
    # Parallel execution
    ENABLE_PARALLEL_TESTS = False  # Experimental
    MAX_PARALLEL_WORKERS = 2
    
    # Data persistence
    SAVE_SESSION_DATA = True      # Save untuk analysis nanti
    EXPORT_TO_DATABASE = False    # Export ke database
    DATABASE_URL = None           # Connection string


# ============================================================================
# VALIDATION
# ============================================================================

def validate_config():
    """
    Validate configuration values
    """
    errors = []
    
    # Validate thresholds
    if PerformanceThresholds.PAGE_LOAD_MAX < PerformanceThresholds.PAGE_LOAD_WARNING:
        errors.append("PAGE_LOAD_MAX must be >= PAGE_LOAD_WARNING")
    
    if PerformanceThresholds.ACTION_RESPONSE_MAX < PerformanceThresholds.ACTION_RESPONSE_WARNING:
        errors.append("ACTION_RESPONSE_MAX must be >= ACTION_RESPONSE_WARNING")
    
    # Validate retry config
    if RetryConfig.WEBDRIVER_MAX_ATTEMPTS < 1:
        errors.append("WEBDRIVER_MAX_ATTEMPTS must be >= 1")
    
    if RetryConfig.WEBDRIVER_DELAY < 0:
        errors.append("WEBDRIVER_DELAY must be >= 0")
    
    # Validate test config
    if TestConfig.DEFAULT_TIMEOUT < 1:
        errors.append("DEFAULT_TIMEOUT must be >= 1")
    
    if not (0 < TestConfig.OVERALL_SUCCESS_THRESHOLD <= 1):
        errors.append("OVERALL_SUCCESS_THRESHOLD must be between 0 and 1")
    
    if errors:
        print("❌ Configuration errors:")
        for error in errors:
            print(f"   - {error}")
        return False
    
    print("✅ Configuration validated successfully")
    return True


if __name__ == "__main__":
    # Test configuration validation
    validate_config()
    
    print("\n📊 Current Configuration:")
    print(f"   Page Load Max: {PerformanceThresholds.PAGE_LOAD_MAX}s")
    print(f"   Action Response Max: {PerformanceThresholds.ACTION_RESPONSE_MAX}s")
    print(f"   Retry Max Attempts: {RetryConfig.WEBDRIVER_MAX_ATTEMPTS}")
    print(f"   Base URL: {TestConfig.BASE_URL}")
    print(f"   Success Threshold: {TestConfig.OVERALL_SUCCESS_THRESHOLD * 100}%")

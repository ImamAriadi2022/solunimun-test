# 🎯 IoT Dashboard Automation Testing (UPGRADED v2.0)

Script automation testing comprehensive untuk IoT Dashboard dengan validasi sensor dan reporting PDF. **Sekarang dengan 6 fitur upgrade baru!**

---

## ✨ FITUR BARU (v2.0 - December 2025)

### 🚀 Upgrade Features

1. **⏱️ Pengukuran Waktu Eksekusi**
   - Track page load time & action response time
   - Performance metrics untuk setiap operasi
   - Automatic performance reporting

2. **📊 Logging Terstruktur**
   - Dual format: Text + JSON logs
   - Timestamp, status, dan durasi di setiap log entry
   - Machine-readable untuk analisis otomatis

3. **📸 Screenshot Otomatis pada Error**
   - Auto-capture saat exception terjadi
   - Naming yang descriptive: `ERROR_{operation}_{timestamp}.png`
   - Visual evidence untuk troubleshooting

4. **🛡️ Exception Handling yang Lebih Stabil**
   - Granular try-catch per test phase
   - Graceful degradation
   - Full traceback logging
   - Test berlanjut meskipun ada failure

5. **🔄 Retry Mechanism**
   - Automatic retry untuk reduce flaky tests
   - Configurable: max attempts & delay
   - Exponential backoff strategy
   - Default: 3 attempts untuk WebDriver ops

6. **⚡ Validasi Performa Berbasis Threshold**
   - Configurable performance thresholds
   - Warning & Fail levels
   - Automatic violation detection & logging
   - Performance summary di PDF report

**📖 Detail Lengkap**: Lihat [UPGRADE_FEATURES.md](UPGRADE_FEATURES.md)

---

## 🎯 Fitur Testing (Existing)

- **Navigation Testing**: 6 station pages (Petangoran & Kalimantan + Station 1 & 2)
- **Sensor Validation**: 10 parameter IoT (Temperature, Humidity, Wind Speed/Direction, Rain Gauge, dll)
- **Visual Elements**: Canvas/SVG charts validation
- **Download Feature**: Testing functionality download
- **PDF Reports**: Laporan lengkap dengan hasil testing dan performance metrics

---

## 📋 Struktur Directory

```
solunimun-test/
├── automation_tests/
│   ├── iot_testing.py          # Main testing script (UPGRADED)
│   ├── config_example.py       # ✨ NEW: Configuration template
│   ├── reports/                # ✨ ENHANCED: Multiple output formats
│   │   ├── laporan_pengujian_*.pdf      # PDF reports
│   │   ├── test_log_*.log               # Text logs
│   │   ├── test_log_*.json              # JSON structured logs
│   │   └── test_session_*.json          # Complete session data
│   └── screenshots/            # ✨ ENHANCED: Success + Error screenshots
│       ├── {test_name}_{timestamp}.png
│       └── ERROR_{operation}_{timestamp}.png
├── requirements.txt            # Dependencies
├── README.md                   # This file
└── UPGRADE_FEATURES.md         # ✨ NEW: Detailed upgrade documentation
```

---

## 🚀 Installation & Setup

### 1. Requirements

- Python 3.8+
- Google Chrome Browser
- Internet connection

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Dependencies:
```
selenium==4.15.2
webdriver-manager==4.0.1
fpdf==1.7.2
```

### 3. Run Testing

```bash
cd c:\programming\solunimun-test
python automation_tests\iot_testing.py
```

---

## 📊 Test Coverage

| Test Category | Description | Status |
|---------------|-------------|--------|
| **WebDriver Init** | Chrome WebDriver initialization with retry | ✅ Auto-retry (3x) |
| **Dashboard Loading** | Main dashboard accessibility | ✅ Performance tracked |
| **Station Navigation** | 6 station pages access | ✅ Individual timing |
| **Sensor Validation** | 10 IoT parameters extraction | ✅ Granular validation |
| **Visual Elements** | Canvas/SVG charts detection | ✅ Error screenshots |
| **Download Feature** | Download functionality testing | ✅ Retry mechanism |
| **PDF Generation** | Comprehensive report creation | ✅ Performance metrics |

---

## 🌡️ IoT Sensor Parameters (10 Parameters)

1. **Timestamp** - Data collection time
2. **Temperature** (Sht85Temp) - Air temperature (°C)
3. **Humidity** - Relative humidity (%)
4. **Wind Direction** - Wind direction (degrees)
5. **Wind Speed** - Wind speed (m/s)
6. **Rain Gauge** - Rainfall measurement (mm)
7. **Pyrano** - Solar radiation (W/m²)
8. **Air Pressure** - Atmospheric pressure (hPa)
9. **Watertemp** - Water temperature (°C)
10. **Validation Status** - Overall sensor data completeness

---

## ⚙️ Configuration

### Performance Thresholds (Default)

```python
PAGE_LOAD_MAX = 10.0s          # Max page load time (FAIL)
PAGE_LOAD_WARNING = 7.0s       # Page load warning
ACTION_RESPONSE_MAX = 5.0s     # Max action response
ELEMENT_WAIT_MAX = 8.0s        # Max element wait
```

### Retry Configuration (Default)

```python
WEBDRIVER_MAX_ATTEMPTS = 3     # WebDriver retry
NAVIGATION_MAX_ATTEMPTS = 2    # Navigation retry
ELEMENT_FIND_MAX_ATTEMPTS = 2  # Element find retry
```

### Custom Configuration

1. Copy `automation_tests/config_example.py` → `config.py`
2. Modify values sesuai kebutuhan
3. Import di script (optional)

**Environment Profiles** tersedia:
- `DEV` - Local development
- `STAGING` - Staging environment
- `CI_CD` - CI/CD pipeline
- `PRODUCTION` - Production monitoring

---

## 📄 Output Files

### 1. PDF Report
**File**: `reports/laporan_pengujian_YYYYMMDD_HHMMSS.pdf`

**Content**:
- Test execution summary
- ✨ **NEW**: Performance metrics section
  - Total duration
  - Average operation time
  - Threshold violations
- Detailed results table
- ✨ **NEW**: Duration column per test
- Screenshot references
- Color-coded status

### 2. Structured Logs
**Files**:
- `reports/test_log_*.log` - Human-readable text logs
- `reports/test_log_*.json` - Structured JSON logs (per entry)
- `reports/test_session_*.json` - Complete session data

**JSON Format Example**:
```json
{
  "timestamp": "2025-12-23T14:30:45.123",
  "level": "INFO",
  "message": "Dashboard loaded successfully",
  "page_load_time": "3.45s",
  "url": "https://iot-fakeapi.vercel.app/",
  "status": "✅ PASS"
}
```

### 3. Screenshots
**Location**: `automation_tests/screenshots/`

**Types**:
- Success: `{test_name}_{timestamp}.png`
- ✨ **NEW**: Error: `ERROR_{operation}_{timestamp}.png`

---

## 🎨 Output Examples

```
======================================================================
🎯 Pengujian Komprehensif Dashboard IoT (UPGRADED)
======================================================================
📋 Cakupan Pengujian:
   ✅ Navigasi 6 Halaman Stasiun
   ✅ Validasi 10 Parameter Sensor IoT
   ✅ Pengujian Elemen Visual
   ✅ Pengujian Fitur Download
   ✅ Pembuatan Laporan PDF Tabel

🚀 FITUR UPGRADE:
   ⏱️  Pengukuran Waktu Eksekusi (Page Load & Action Response)
   📊 Logging Terstruktur (Timestamp, Status, Durasi)
   📸 Screenshot Otomatis pada Error
   🔄 Retry Mechanism untuk Flaky Tests (Max 3x)
   ⚡ Validasi Performa Berbasis Threshold Waktu
   🛡️  Exception Handling yang Lebih Stabil
======================================================================

2025-12-23 14:30:42 - INFO - 🚀 Initializing Chrome WebDriver...
2025-12-23 14:30:45 - INFO - ✅ Chrome WebDriver initialized successfully
2025-12-23 14:30:45 - INFO - ⏱️ Webdriver_initialization: initialize_webdriver [duration=3.21s, status=✅ PASS]
2025-12-23 14:30:45 - INFO - 🌐 Opening URL: https://iot-fakeapi.vercel.app/
2025-12-23 14:30:48 - INFO - ✅ Dashboard loaded successfully [page_load_time=2.87s]
2025-12-23 14:30:48 - INFO - ⏱️ Page_load: open_dashboard [duration=2.87s, status=✅ PASS]
2025-12-23 14:30:48 - INFO - 🚉 Navigating to Petangoran Main...
2025-12-23 14:30:51 - INFO - ✅ Petangoran Main loaded successfully [page_load_time=2.34s]
2025-12-23 14:30:54 - INFO - 📈 Sensor data extracted [page=Petangoran_Main, sensors_found=8]

============================================================
📊 FINAL TEST RESULTS
============================================================
webdriver_init: ✅ PASS
dashboard_open: ✅ PASS
sensor_validation: ✅ PASS
visual_elements: ✅ PASS
download_feature: ✅ PASS

Success Rate: 5/5 (100.0%) [successful_tests=5, total_tests=5]
Total Operations Duration: 45.23s [total_operations=15, avg_duration=3.02s]
🎉 OVERALL: TESTING SUCCESSFUL!
============================================================

==================================================
📊 PENGUJIAN SELESAI
==================================================
Pengujian Berhasil: 5/5
Keberhasilan Keseluruhan: YA

📁 File Output:
   📄 PDF Report: laporan_pengujian_20251223_143055.pdf
   📊 JSON Logs: test_session_20251223_143055.json
   📝 Text Logs: test_log_20251223_143055.log
   📁 Lokasi: c:\programming\solunimun-test\automation_tests\reports
   📸 Screenshots: 8 file(s)
==================================================
```

---

## 🔧 Advanced Usage

### Menyesuaikan Thresholds

Edit di `iot_testing.py`:

```python
class PerformanceThresholds:
    PAGE_LOAD_MAX = 15.0  # Increase untuk slow network
    ACTION_RESPONSE_MAX = 8.0
```

### Menggunakan Environment Profile

```python
from config_example import EnvironmentProfiles

# Load CI/CD profile
profile = EnvironmentProfiles.CI_CD
PerformanceThresholds.PAGE_LOAD_MAX = profile["thresholds"]["PAGE_LOAD_MAX"]
```

### Analisis Performance Data

```bash
# Parse JSON logs untuk operations > 5s
python -c "import json; data=json.load(open('reports/test_session_*.json')); print([p for p in data['performance_data'] if p['duration'] > 5])"
```

---

## 🔍 Troubleshooting

### Issue: Page Load Timeout

**Symptom**: `TimeoutException` during page load

**Solution**:
1. Check internet connection
2. Increase `PAGE_LOAD_MAX` threshold
3. Review `ERROR_*.png` screenshots
4. Check `test_log_*.json` for details

**Handled by**: Automatic retry mechanism (up to 3 attempts)

---

### Issue: Flaky Element Finding

**Symptom**: `NoSuchElementException` intermittently

**Solution**:
- Already handled by retry mechanism
- Increase `ELEMENT_FIND_MAX_ATTEMPTS` if needed
- Check error screenshots for page state

---

### Issue: Performance Threshold Violations

**Symptom**: ⚠️ WARNING logs untuk slow operations

**Solution**:
1. Check network conditions
2. Adjust thresholds untuk environment
3. Review performance metrics di PDF
4. Use environment profiles (DEV/STAGING/PROD)

---

## 📚 Documentation

- **[UPGRADE_FEATURES.md](UPGRADE_FEATURES.md)** - Detailed upgrade documentation
- **[config_example.py](automation_tests/config_example.py)** - Configuration guide & examples
- **[README.md](README.md)** - This file (Quick start & overview)

---

## 🎓 Best Practices

### 1. Threshold Tuning
- Start dengan default values
- Monitor performance over time
- Adjust berdasarkan environment (local/staging/prod)
- Use warning thresholds untuk early detection

### 2. Log Management
- Archive old logs periodically (default: keep 30 days)
- Use JSON logs untuk automated analysis
- Review error patterns untuk improvement

### 3. Screenshot Management
- Archive old screenshots (default: keep 7 days)
- Review error screenshots untuk debugging
- Use success screenshots untuk documentation

### 4. Retry Configuration
- Balance antara reliability vs speed
- Increase retries untuk unstable environments
- Monitor retry patterns untuk root cause analysis

### 5. Performance Monitoring
- Track performance trends over time
- Set realistic thresholds untuk environment
- Use CI/CD profile untuk automated testing

---

## 📈 Version History

### v2.0 (December 2025) - MAJOR UPGRADE ✨
- ⏱️ Added: Performance measurement & tracking
- 📊 Added: Structured logging (text + JSON)
- 📸 Added: Auto error screenshots
- 🛡️ Enhanced: Stable exception handling
- 🔄 Added: Retry mechanism with exponential backoff
- ⚡ Added: Performance validation with thresholds
- 📄 Enhanced: PDF report dengan performance metrics
- 🔧 Added: Configuration system dengan environment profiles

### v1.0 (November 2025) - Initial Release
- Basic test automation
- PDF reporting
- Screenshot capture
- Sensor validation
- Visual element testing

---

## 👤 Author

**QA Automation Engineer**

Target Application: https://iot-fakeapi.vercel.app/

---

## 📄 License

Internal use only

---

## 🤝 Support

Untuk pertanyaan atau issues:

1. **Check documentation**: [UPGRADE_FEATURES.md](UPGRADE_FEATURES.md)
2. **Review logs**: `reports/test_log_*.log`
3. **Check screenshots**: `screenshots/ERROR_*.png`
4. **Analyze JSON**: `reports/test_session_*.json`
5. **Contact**: QA Team

---

**Status**: ✅ Production Ready  
**Python**: 3.8+  
**Selenium**: 4.15.2  
**Last Updated**: December 23, 2025

# IoT Dashboard Automation Testing

Script automation testing comprehensive untuk IoT Dashboard dengan validasi sensor dan reporting PDF.

## 🎯 Fitur Testing

- **Navigation Testing**: 6 station pages (Petangoran & Kalimantan + Station 1 & 2)
- **Sensor Validation**: 9 parameter IoT (Temperature, Humidity, Wind Speed/Direction, Rain Gauge, dll)
- **Visual Elements**: Canvas/SVG charts validation
- **Download Feature**: Testing functionality download
- **PDF Reports**: Laporan lengkap dengan hasil testing

## 📋 Struktur Directory

```
solunimun-test/
├── automation_tests/
│   └── iot_testing.py          # Main testing script
├── reports/                    # PDF reports (auto-generated)
│   └── iot_test_report_*.pdf   # Testing reports
└── README.md                   # Documentation
```

## 🚀 Installation & Setup

### 1. Install Dependencies

```bash
pip install selenium webdriver-manager fpdf2
```

### 2. Run Testing

```bash
cd c:\programming\solunimun-test
python automation_tests\iot_testing.py
```

## 📊 Test Coverage

| Test Category | Description | Target |
|---------------|-------------|---------|
| **WebDriver Init** | Chrome WebDriver initialization | Auto-managed ChromeDriver |
| **Dashboard Loading** | Main dashboard accessibility | https://iot-fakeapi.vercel.app/ |
| **Station Navigation** | 6 station pages access | Petangoran/Kalimantan + Station 1/2 |
| **Sensor Validation** | 9 IoT parameters extraction | Temperature, Humidity, Wind, etc. |
| **Visual Elements** | Canvas/SVG charts detection | Dashboard charts/graphs |
| **Download Feature** | Download functionality testing | Download links/buttons |
| **PDF Generation** | Comprehensive report creation | Auto-generated reports |

## 🌡️ IoT Sensor Parameters (9 Parameters)

1. **Timestamp** - Data collection time
2. **Temperature** - Air temperature (°C)
3. **Humidity** - Relative humidity (%)
4. **Wind Direction** - Wind direction (degrees)
5. **Wind Speed** - Wind speed (m/s)
6. **Rain Gauge** - Rainfall measurement (mm)
7. **Pyrano** - Solar radiation (W/m²)
8. **Air Pressure** - Atmospheric pressure (hPa)
9. **Watertemp** - Water temperature (°C)

## 📄 Report Features

- **Test Summary**: Pass/fail statistics
- **Detailed Results**: Individual test results with timestamps
- **Station Coverage**: Navigation success for each station
- **Sensor Completeness**: 9-parameter validation results
- **Visual Evidence**: Screenshots and element detection
- **Performance Metrics**: Test duration and success rates

## 🎨 Output Examples

```
🚀 Starting IoT Dashboard Comprehensive Testing...
🔧 Test 1: WebDriver Initialization
✅ Chrome WebDriver initialized successfully
🌐 Test 2: Dashboard Loading  
✅ Dashboard loaded successfully
🚉 Navigating to Petangoran Main...
✅ Petangoran Main loaded successfully
📈 Found 5 sensors in Petangoran_Main
   - Temperature: 25.5°C
   - Humidity: 65%
   - Wind Speed: 2.3 m/s
📊 Sensor completeness: 7/9 (77.8%)
📄 PDF report created: iot_test_report_20241123_143022.pdf
🎉 OVERALL: TESTING SUCCESSFUL!
```

## ⚙️ Configuration

### Chrome Options
- Disabled web security for CORS
- Window size: 1920x1080
- No sandbox mode
- Extensions disabled

### Timeouts
- Default wait: 30 seconds
- Page load: 3 seconds
- Element detection: Auto-retry

### Success Thresholds
- Sensor completeness: ≥60% (minimum 5/9 parameters)
- Overall success: ≥60% of all tests passed

## 🔧 Troubleshooting

### Common Issues

**ChromeDriver Error:**
```
Solution: webdriver-manager handles auto-download
```

**Page Loading Timeout:**
```
- Check internet connection
- Verify target URL accessibility
- Increase timeout in script if needed
```

**Sensor Data Not Found:**
```
- Script includes mock data for demonstration
- Pattern matching covers multiple formats
- Success threshold allows partial data
```

**PDF Generation Failed:**
```
- Check write permissions in reports/ directory
- Verify fpdf2 installation
- Manual directory creation if needed
```

## 📝 Technical Details

### Technology Stack
- **Python 3.7+**: Main scripting language
- **Selenium WebDriver**: Browser automation
- **webdriver-manager**: ChromeDriver management
- **FPDF2**: PDF report generation
- **Chrome Browser**: Testing target browser

### Architecture
- **Class-based Design**: IoTDashboardTester main class
- **Modular Testing**: Individual test methods
- **Error Handling**: Comprehensive exception management
- **Logging**: Detailed test execution logs
- **Reporting**: Automated PDF generation

### Performance
- **Multi-page Navigation**: 6 station pages
- **Pattern Matching**: Multiple regex patterns for sensor detection
- **Resource Management**: Automatic cleanup
- **Report Generation**: Structured PDF with charts and statistics

## 📞 Support

Untuk pertanyaan atau issues terkait testing script:

1. **Check logs**: Console output untuk debugging
2. **Verify URL**: Pastikan https://iot-fakeapi.vercel.app/ accessible
3. **Update dependencies**: `pip install --upgrade selenium webdriver-manager fpdf2`
4. **Manual testing**: Test individual functions jika diperlukan

---

**Author**: IoT Dashboard Automation Team  
**Version**: 1.0.0  
**Last Updated**: November 2024  
**Target**: https://iot-fakeapi.vercel.app/
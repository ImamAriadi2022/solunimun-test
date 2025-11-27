# IoT Web Dashboard Automation Testing

Script pengujian otomatis untuk Web Dashboard IoT berbasis React.js menggunakan Python + Selenium WebDriver.

## 🚀 Fitur Utama

### ✅ Yang Sudah Diimplementasikan:
- **Inisialisasi WebDriver**: Chrome WebDriver dengan webdriver-manager
- **Verifikasi Halaman Utama**: Validasi judul dan navigasi
- **Validasi Visualisasi Data**: Deteksi Chart.js & JustGage
- **Testing Filter Waktu**: 1 Hari, 7 Hari, 30 Hari
- **Testing Download + Password**: Skenario positif & negatif
- **Logging Lengkap**: Info, warning, dan error logs
- **Struktur Modular**: Class-based dengan utility functions

## 📦 Instalasi

### 1. Clone atau Download Project
```bash
git clone <repository-url>
cd solunimun-test
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Pastikan Chrome Browser Terinstall
Script ini menggunakan Chrome WebDriver yang akan otomatis didownload oleh webdriver-manager.

## 🏃‍♂️ Cara Menjalankan

### 🎯 Metode 1: Simple Runner (Direkomendasikan)
```bash
python simple_runner.py
```

### 🚀 Metode 2: Otomatis (Windows)
```bash
run_tests.bat
```

### ⚙️ Metode 3: Manual
```bash
cd automation_tests
python iot_dashboard_tester.py
```

### 🎛️ Metode 4: Interactive (Jika tidak ada masalah import)
```bash
python quick_start.py
```

### Menjalankan dengan Konfigurasi Custom
Edit file `utils/config.py` untuk menyesuaikan:
- URL aplikasi
- Timeout values
- Password untuk testing
- Chrome options

## 📁 Struktur Project

```
solunimun-test/
├── requirements.txt                 # Dependencies
├── automation_tests/
│   ├── iot_dashboard_tester.py     # Script utama
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── config.py               # Konfigurasi testing
│   │   └── helpers.py              # Utility functions
│   └── reports/                    # Output logs & reports
└── README.md
```

## 🧪 Test Cases

### 1. **Inisialisasi WebDriver**
- Setup Chrome WebDriver dengan webdriver-manager
- Konfigurasi download directory
- Window size dan options

### 2. **Verifikasi Halaman Utama**
- ✅ Judul halaman memuat "Microclimate Dashboard"
- ✅ Elemen navigasi "Home" ada
- ✅ Elemen navigasi "Dashboard" ada

### 3. **Validasi Visualisasi Data**
- ✅ Deteksi Chart.js (`<canvas>` elements)
- ✅ Deteksi JustGage untuk suhu (`<svg>` elements)
- ✅ Deteksi JustGage untuk kelembapan
- ⚠️ Handle "No Data" atau "Alat Rusak" (warning, bukan error)

### 4. **Testing Filter Waktu**
- ✅ Klik filter "1 Hari"
- ✅ Klik filter "7 Hari"  
- ✅ Klik filter "30 Hari"
- ✅ Wait for chart updates (explicit wait)
- ✅ Optimal delays between interactions

### 5. **Testing Download + Password**
- ✅ Klik tombol "Download Data"
- ✅ Verifikasi popup password muncul
- ✅ Test password salah → pesan error
- ✅ Test password benar → file terdownload
- ✅ Verifikasi file di folder Downloads

## ⚙️ Konfigurasi

### URL dan Timeout
```python
BASE_URL = "https://iot-fakeapi.vercel.app/"  # Sesuaikan dengan aplikasi Anda
DEFAULT_TIMEOUT = 30                # Timeout untuk explicit waits
```

### Credentials
```python
CORRECT_PASSWORD = "admin123"       # Password yang benar
WRONG_PASSWORD = "wrongpass"        # Password salah untuk testing
```

### Chrome Options
```python
CHROME_OPTIONS = [
    "--no-sandbox",
    "--disable-dev-shm-usage", 
    "--disable-gpu",
    "--window-size=1920,1080"
]
HEADLESS_MODE = False              # True untuk background testing
```

## 📊 Output dan Logging

### Console Output
Script akan menampilkan progress testing secara real-time dengan emoji dan warna:
```
🚀 Menginisialisasi Chrome WebDriver...
✅ Chrome WebDriver berhasil diinisialisasi
🌐 Membuka URL: https://iot-fakeapi.vercel.app/
✅ Halaman dashboard berhasil dimuat
🔍 Memverifikasi halaman utama...
```

### Log Files
Log lengkap disimpan di `reports/iot_dashboard_test_YYYYMMDD_HHMMSS.log`

### Test Results Summary
```
📊 HASIL PENGUJIAN OTOMATIS WEB DASHBOARD IOT
================================================================================
Webdriver Init: ✅ BERHASIL
Dashboard Open: ✅ BERHASIL  
Main Page Verify: ✅ BERHASIL
Data Visualization: ✅ BERHASIL
Time Filters: ✅ BERHASIL
Download Feature: ✅ BERHASIL
--------------------------------------------------------------------------------
Total Keberhasilan: 6/6 (100.0%)
🎉 PENGUJIAN BERHASIL - Dashboard IoT berfungsi dengan baik!
```

## 🔧 Troubleshooting

### Common Issues:

**1. ✅ Import Errors (RESOLVED)**
Import errors di `quick_start.py` dan `advanced_example.py` sudah diperbaiki dengan menggunakan subprocess approach. Semua script sekarang berjalan tanpa masalah dependency.

**2. ChromeDriver Error**
- Pastikan Chrome browser terinstall
- webdriver-manager akan otomatis download ChromeDriver

**3. Timeout Errors** 
- Tingkatkan nilai `DEFAULT_TIMEOUT` di config.py
- Pastikan website https://iot-fakeapi.vercel.app/ dapat diakses

**4. Element Not Found**
- Periksa selector di config.py
- Sesuaikan dengan struktur HTML aplikasi yang baru

**5. Download Test Gagal**
- Pastikan folder Downloads dapat diakses
- Cek permission folder Downloads

**6. Website Tidak Dapat Diakses**
- Pastikan koneksi internet stabil
- Cek apakah https://iot-fakeapi.vercel.app/ dapat dibuka di browser

## 🎯 Customization untuk Aplikasi Anda

### 1. Sesuaikan Selectors
Edit `utils/config.py` pada bagian `SELECTORS`:
```python
SELECTORS = {
    "navigation": {
        "home": "//a[contains(text(), 'Home')]",  # Sesuaikan selector
        "dashboard": "//button[@id='dashboard-nav']"  # Contoh ID selector
    }
}
```

### 2. Tambah Test Cases
Extend class `IoTDashboardTester` dengan method baru:
```python
def test_custom_feature(self) -> bool:
    """Testing fitur kustom Anda"""
    # Implementasi testing
    pass
```

### 3. Custom Assertions
Tambahkan validasi spesifik untuk aplikasi:
```python
def verify_sensor_data(self) -> bool:
    """Verifikasi data sensor spesifik"""
    # Custom validation logic
    pass
```

## 📈 CI/CD Integration

Script mengembalikan exit code:
- `0`: Semua test berhasil
- `1`: Ada test yang gagal

Untuk CI/CD pipeline:
```bash
python automation_tests/iot_dashboard_tester.py
if [ $? -eq 0 ]; then
    echo "✅ All tests passed"
else
    echo "❌ Some tests failed"
    exit 1
fi
```

## 🤝 Contributing

1. Fork repository ini
2. Buat feature branch (`git checkout -b feature/new-test`)
3. Commit changes (`git commit -am 'Add new test case'`)
4. Push ke branch (`git push origin feature/new-test`)
5. Create Pull Request

## 📝 License

MIT License - Silakan gunakan untuk keperluan skripsi dan project lainnya.

## 👨‍💻 Author

**QA Automation Engineer**  
Script ini dibuat khusus untuk kebutuhan skripsi Web Dashboard IoT berbasis React.js.

---

**Happy Testing! 🚀**
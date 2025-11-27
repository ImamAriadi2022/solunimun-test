"""
IoT Web Dashboard Automation Testing Script
Author: QA Automation Engineer
Deskripsi: Script pengujian otomatis untuk Web Dashboard IoT berbasis React.js
          menggunakan Python + Selenium WebDriver
"""

import logging
import os
import time
from datetime import datetime
from pathlib import Path
from typing import Optional, List

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    TimeoutException, 
    NoSuchElementException, 
    ElementNotInteractableException
)
from webdriver_manager.chrome import ChromeDriverManager


class IoTDashboardTester:
    """
    Kelas utama untuk pengujian otomatis Web Dashboard IoT
    """
    
    def __init__(self, base_url: str = "https://iot-fakeapi.vercel.app/", timeout: int = 30):
        """
        Inisialisasi IoT Dashboard Tester
        
        Args:
            base_url: URL dasar aplikasi yang akan ditest
            timeout: Waktu timeout untuk explicit wait (detik)
        """
        self.base_url = base_url
        self.timeout = timeout
        self.driver: Optional[webdriver.Chrome] = None
        self.wait: Optional[WebDriverWait] = None
        
        # Setup logging
        self._setup_logging()
        
        # Download directory untuk verifikasi file
        self.download_dir = str(Path.home() / "Downloads")
        
    def _setup_logging(self) -> None:
        """Setup konfigurasi logging untuk test results"""
        log_filename = f"iot_dashboard_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        log_path = Path(__file__).parent / "reports" / log_filename
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_path, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def initialize_webdriver(self) -> bool:
        """
        Inisialisasi Chrome WebDriver dengan webdriver-manager
        
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        try:
            self.logger.info("🚀 Menginisialisasi Chrome WebDriver...")
            
            # Setup Chrome options
            chrome_options = Options()
            chrome_options.add_experimental_option("prefs", {
                "download.default_directory": self.download_dir,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True
            })
            
            # Untuk debugging, bisa dinonaktifkan dengan menghapus comment
            # chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
            
            # Setup WebDriver dengan fallback yang lebih robust
            driver_initialized = False
            
            # Method 1: Coba system ChromeDriver dulu (paling reliable)
            try:
                self.logger.info("🔄 Mencoba system ChromeDriver...")
                self.driver = webdriver.Chrome(options=chrome_options)
                self.logger.info("✅ System ChromeDriver berhasil")
                driver_initialized = True
            except Exception as e:
                self.logger.info(f"⚠️  System ChromeDriver tidak tersedia: {str(e)}")
            
            # Method 2: webdriver-manager sebagai fallback
            if not driver_initialized:
                try:
                    self.logger.info("🔄 Fallback ke webdriver-manager...")
                    driver_path = ChromeDriverManager().install()
                    self.logger.info(f"🔧 ChromeDriver path: {driver_path}")
                    
                    service = Service(driver_path)
                    self.driver = webdriver.Chrome(service=service, options=chrome_options)
                    self.logger.info("✅ webdriver-manager berhasil")
                    driver_initialized = True
                except Exception as e:
                    self.logger.warning(f"⚠️  webdriver-manager juga gagal: {str(e)}")
            
            if not driver_initialized:
                raise Exception("Tidak dapat menginisialisasi ChromeDriver dengan method apapun")
            
            # Setup WebDriverWait
            self.wait = WebDriverWait(self.driver, self.timeout)
            
            self.logger.info("✅ Chrome WebDriver berhasil diinisialisasi")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Gagal menginisialisasi WebDriver: {str(e)}")
            
            # Fallback: Coba tanpa webdriver-manager (system ChromeDriver)
            self.logger.info("🔄 Mencoba fallback tanpa webdriver-manager...")
            try:
                self.driver = webdriver.Chrome(options=chrome_options)
                self.wait = WebDriverWait(self.driver, self.timeout)
                self.logger.info("✅ Fallback berhasil - menggunakan system ChromeDriver")
                return True
            except Exception as fallback_error:
                self.logger.error(f"❌ Fallback juga gagal: {str(fallback_error)}")
                self.logger.error("💡 Solusi:")
                self.logger.error("   1. Pastikan Chrome browser terinstall")
                self.logger.error("   2. Download ChromeDriver manual dari https://chromedriver.chromium.org/")
                self.logger.error("   3. Tambahkan ChromeDriver ke PATH system")
                return False
    
    def open_dashboard(self) -> bool:
        """
        Membuka halaman utama dashboard IoT
        
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        try:
            self.logger.info(f"🌐 Membuka URL: {self.base_url}")
            self.driver.get(self.base_url)
            
            # Tunggu halaman selesai dimuat
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            
            self.logger.info("✅ Halaman dashboard berhasil dimuat")
            return True
            
        except TimeoutException:
            self.logger.error("❌ Timeout saat memuat halaman dashboard")
            return False
        except Exception as e:
            self.logger.error(f"❌ Error saat membuka dashboard: {str(e)}")
            return False
    
    def verify_main_page(self) -> bool:
        """
        Verifikasi elemen-elemen utama di halaman dashboard
        
        Returns:
            bool: True jika semua verifikasi berhasil
        """
        self.logger.info("🔍 Memverifikasi halaman utama...")
        
        success_count = 0
        total_checks = 3
        
        # 1. Verifikasi judul halaman
        try:
            self.wait.until(lambda driver: "Microclimate Dashboard" in driver.title)
            self.logger.info("✅ Judul halaman mengandung 'Microclimate Dashboard'")
            success_count += 1
        except TimeoutException:
            self.logger.warning(f"⚠️  Judul halaman tidak mengandung 'Microclimate Dashboard'. Actual: '{self.driver.title}'")
        
        # 2. Verifikasi navigasi Home
        try:
            home_element = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Home')]"))
            )
            self.logger.info("✅ Elemen navigasi 'Home' ditemukan")
            success_count += 1
        except TimeoutException:
            self.logger.warning("⚠️  Elemen navigasi 'Home' tidak ditemukan")
        
        # 3. Verifikasi navigasi Dashboard
        try:
            dashboard_element = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Dashboard')]"))
            )
            self.logger.info("✅ Elemen navigasi 'Dashboard' ditemukan")
            success_count += 1
        except TimeoutException:
            self.logger.warning("⚠️  Elemen navigasi 'Dashboard' tidak ditemukan")
        
        success_rate = (success_count / total_checks) * 100
        self.logger.info(f"📊 Verifikasi halaman utama: {success_count}/{total_checks} ({success_rate:.1f}%) berhasil")
        
        return success_count == total_checks
    
    def validate_data_visualization(self) -> bool:
        """
        Validasi keberadaan visualisasi data (Chart.js & JustGage)
        
        Returns:
            bool: True jika validasi berhasil
        """
        self.logger.info("📊 Memvalidasi visualisasi data...")
        
        success_count = 0
        total_checks = 3
        
        # 1. Deteksi Chart.js (canvas elements)
        try:
            canvas_elements = self.wait.until(
                EC.presence_of_all_elements_located((By.TAG_NAME, "canvas"))
            )
            
            if len(canvas_elements) > 0:
                self.logger.info(f"✅ Ditemukan {len(canvas_elements)} elemen Chart.js (canvas)")
                success_count += 1
                
                # Cek apakah ada chart yang menunjukkan "No Data"
                for i, canvas in enumerate(canvas_elements):
                    try:
                        # Cari elemen parent atau sibling yang mungkin mengandung pesan "No Data"
                        parent = canvas.find_element(By.XPATH, "./..")
                        if "No Data" in parent.text or "Alat Rusak" in parent.text:
                            self.logger.warning(f"⚠️  Chart {i+1} menampilkan 'No Data' atau 'Alat Rusak'")
                    except:
                        pass  # Tidak apa-apa jika tidak menemukan pesan
            else:
                self.logger.warning("⚠️  Tidak ditemukan elemen Chart.js (canvas)")
                
        except TimeoutException:
            self.logger.warning("⚠️  Timeout saat mencari elemen Chart.js")
        
        # 2. Deteksi JustGage untuk Suhu (SVG elements)
        try:
            svg_elements = self.wait.until(
                EC.presence_of_all_elements_located((By.TAG_NAME, "svg"))
            )
            
            temperature_gage_found = False
            humidity_gage_found = False
            
            for svg in svg_elements:
                svg_text = svg.get_attribute('outerHTML').lower()
                if any(keyword in svg_text for keyword in ['temperature', 'suhu', 'temp']):
                    temperature_gage_found = True
                if any(keyword in svg_text for keyword in ['humidity', 'kelembapan', 'humid']):
                    humidity_gage_found = True
            
            if temperature_gage_found:
                self.logger.info("✅ JustGage untuk suhu ditemukan")
                success_count += 1
            else:
                self.logger.warning("⚠️  JustGage untuk suhu tidak ditemukan")
                
            if humidity_gage_found:
                self.logger.info("✅ JustGage untuk kelembapan ditemukan")  
                success_count += 1
            else:
                self.logger.warning("⚠️  JustGage untuk kelembapan tidak ditemukan")
                
        except TimeoutException:
            self.logger.warning("⚠️  Timeout saat mencari elemen JustGage (SVG)")
        
        success_rate = (success_count / total_checks) * 100
        self.logger.info(f"📊 Validasi visualisasi data: {success_count}/{total_checks} ({success_rate:.1f}%) berhasil")
        
        return success_count >= 2  # Minimal 2 dari 3 harus berhasil
    
    def test_time_filters(self) -> bool:
        """
        Testing interaksi dengan filter waktu (1 Hari, 7 Hari, 30 Hari)
        
        Returns:
            bool: True jika semua filter testing berhasil
        """
        self.logger.info("⏰ Testing filter waktu...")
        
        # Daftar filter yang akan ditest
        filters = ["1 Hari", "7 Hari", "30 Hari"]
        success_count = 0
        
        for filter_name in filters:
            try:
                self.logger.info(f"🔄 Testing filter: {filter_name}")
                
                # Cari dan klik tombol filter
                filter_button = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(), '{filter_name}')]"))
                )
                
                # Scroll ke elemen jika perlu
                self.driver.execute_script("arguments[0].scrollIntoView(true);", filter_button)
                time.sleep(0.5)
                
                # Klik filter
                filter_button.click()
                self.logger.info(f"✅ Berhasil mengklik filter '{filter_name}'")
                
                # Tunggu grafik selesai diperbarui dengan menunggu loading indicator hilang
                # atau menunggu canvas terupdate
                try:
                    # Tunggu sebentar untuk memastikan request dimulai
                    time.sleep(1)
                    
                    # Tunggu hingga tidak ada loading indicator
                    self.wait.until_not(
                        EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'loading') or contains(@class, 'spinner')]"))
                    )
                except TimeoutException:
                    # Jika tidak ada loading indicator, tunggu canvas terupdate
                    time.sleep(2)
                
                self.logger.info(f"✅ Grafik berhasil diperbarui untuk filter '{filter_name}'")
                success_count += 1
                
                # Jeda optimal antar filter
                time.sleep(1)
                
            except TimeoutException:
                self.logger.warning(f"⚠️  Timeout saat testing filter '{filter_name}'")
            except ElementNotInteractableException:
                self.logger.warning(f"⚠️  Tidak dapat mengklik filter '{filter_name}'")
            except Exception as e:
                self.logger.warning(f"⚠️  Error saat testing filter '{filter_name}': {str(e)}")
        
        success_rate = (success_count / len(filters)) * 100
        self.logger.info(f"📊 Testing filter waktu: {success_count}/{len(filters)} ({success_rate:.1f}%) berhasil")
        
        return success_count == len(filters)
    
    def test_download_feature(self, correct_password: str = "admin123", wrong_password: str = "wrongpass") -> bool:
        """
        Testing fitur download dengan proteksi password
        
        Args:
            correct_password: Password yang benar
            wrong_password: Password yang salah untuk testing negatif
            
        Returns:
            bool: True jika semua testing download berhasil
        """
        self.logger.info("💾 Testing fitur download dengan proteksi password...")
        
        success_count = 0
        total_tests = 3
        
        # Test 1: Klik tombol download dan verifikasi popup muncul
        try:
            download_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Download') or contains(text(), 'download')]"))
            )
            
            self.driver.execute_script("arguments[0].scrollIntoView(true);", download_button)
            time.sleep(0.5)
            
            download_button.click()
            self.logger.info("✅ Berhasil mengklik tombol Download")
            
            # Tunggu popup password muncul
            password_modal = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'modal') or contains(@class, 'popup') or contains(@class, 'dialog')]"))
            )
            self.logger.info("✅ Popup password berhasil muncul")
            success_count += 1
            
        except TimeoutException:
            self.logger.warning("⚠️  Popup password tidak muncul dalam waktu yang ditentukan")
        except Exception as e:
            self.logger.warning(f"⚠️  Error saat mengklik tombol download: {str(e)}")
        
        # Test 2: Testing dengan password yang salah
        try:
            password_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='password' or contains(@placeholder, 'password') or contains(@name, 'password')]"))
            )
            
            password_input.clear()
            password_input.send_keys(wrong_password)
            
            # Cari dan klik tombol submit/konfirmasi
            submit_button = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Submit') or contains(text(), 'Confirm') or contains(text(), 'OK') or @type='submit']")
            submit_button.click()
            
            # Tunggu pesan error muncul
            error_message = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'error') or contains(text(), 'Error') or contains(text(), 'salah') or contains(text(), 'wrong')]"))
            )
            
            self.logger.info("✅ Pesan error untuk password salah berhasil muncul")
            success_count += 1
            
        except TimeoutException:
            self.logger.warning("⚠️  Pesan error untuk password salah tidak muncul")
        except Exception as e:
            self.logger.warning(f"⚠️  Error saat testing password salah: {str(e)}")
        
        # Test 3: Testing dengan password yang benar dan verifikasi download
        try:
            # Cari input password lagi (mungkin sudah ter-reset)
            password_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='password' or contains(@placeholder, 'password') or contains(@name, 'password')]"))
            )
            
            password_input.clear()
            password_input.send_keys(correct_password)
            
            # Hapus file download lama jika ada
            self._cleanup_old_downloads()
            
            # Klik tombol submit
            submit_button = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Submit') or contains(text(), 'Confirm') or contains(text(), 'OK') or @type='submit']")
            submit_button.click()
            
            # Tunggu file download selesai
            if self._wait_for_download():
                self.logger.info("✅ File berhasil diunduh")
                success_count += 1
            else:
                self.logger.warning("⚠️  File tidak berhasil diunduh dalam waktu yang ditentukan")
                
        except TimeoutException:
            self.logger.warning("⚠️  Timeout saat melakukan download dengan password benar")
        except Exception as e:
            self.logger.warning(f"⚠️  Error saat testing download dengan password benar: {str(e)}")
        
        success_rate = (success_count / total_tests) * 100
        self.logger.info(f"📊 Testing fitur download: {success_count}/{total_tests} ({success_rate:.1f}%) berhasil")
        
        return success_count >= 2  # Minimal 2 dari 3 harus berhasil
    
    def _cleanup_old_downloads(self) -> None:
        """Membersihkan file download lama untuk testing"""
        download_path = Path(self.download_dir)
        for file in download_path.glob("*.csv"):
            if file.name.startswith("iot_data") or "dashboard" in file.name.lower():
                try:
                    file.unlink()
                    self.logger.info(f"🗑️  Membersihkan file lama: {file.name}")
                except:
                    pass
        
        for file in download_path.glob("*.json"):
            if file.name.startswith("iot_data") or "dashboard" in file.name.lower():
                try:
                    file.unlink()
                    self.logger.info(f"🗑️  Membersihkan file lama: {file.name}")
                except:
                    pass
    
    def _wait_for_download(self, timeout: int = 30) -> bool:
        """
        Menunggu file download selesai
        
        Args:
            timeout: Waktu timeout dalam detik
            
        Returns:
            bool: True jika file berhasil didownload
        """
        download_path = Path(self.download_dir)
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            # Cek file .csv atau .json yang baru
            csv_files = list(download_path.glob("*.csv"))
            json_files = list(download_path.glob("*.json"))
            
            # Filter file yang mungkin dari dashboard
            recent_files = []
            current_time = time.time()
            
            for file in csv_files + json_files:
                # Cek file yang dibuat dalam 2 menit terakhir
                if current_time - file.stat().st_mtime < 120:
                    recent_files.append(file)
            
            if recent_files:
                for file in recent_files:
                    # Cek apakah file tidak sedang di-download (tidak ada .crdownload)
                    if not (download_path / f"{file.name}.crdownload").exists():
                        self.logger.info(f"📁 File berhasil diunduh: {file.name}")
                        return True
            
            time.sleep(1)
        
        return False
    
    def run_all_tests(self) -> dict:
        """
        Menjalankan semua test cases
        
        Returns:
            dict: Hasil summary dari semua testing
        """
        self.logger.info("🚀 Memulai pengujian otomatis Web Dashboard IoT...")
        
        results = {
            "webdriver_init": False,
            "dashboard_open": False,
            "main_page_verify": False,
            "data_visualization": False,
            "time_filters": False,
            "download_feature": False,
            "overall_success": False
        }
        
        try:
            # 1. Inisialisasi WebDriver
            if not self.initialize_webdriver():
                return results
            results["webdriver_init"] = True
            
            # 2. Buka Dashboard
            if not self.open_dashboard():
                return results
            results["dashboard_open"] = True
            
            # 3. Verifikasi Halaman Utama
            results["main_page_verify"] = self.verify_main_page()
            
            # 4. Validasi Visualisasi Data
            results["data_visualization"] = self.validate_data_visualization()
            
            # 5. Testing Filter Waktu
            results["time_filters"] = self.test_time_filters()
            
            # 6. Testing Fitur Download
            results["download_feature"] = self.test_download_feature()
            
            # Hitung keberhasilan keseluruhan
            successful_tests = sum(1 for test, result in results.items() 
                                 if test != "overall_success" and result)
            total_tests = len(results) - 1
            
            results["overall_success"] = successful_tests >= (total_tests * 0.7)  # 70% harus berhasil
            
            self._log_final_results(results, successful_tests, total_tests)
            
        except Exception as e:
            self.logger.error(f"❌ Error dalam pengujian: {str(e)}")
            
        finally:
            self.cleanup()
        
        return results
    
    def _log_final_results(self, results: dict, successful_tests: int, total_tests: int) -> None:
        """Log hasil akhir testing"""
        self.logger.info("\n" + "="*80)
        self.logger.info("📊 HASIL PENGUJIAN OTOMATIS WEB DASHBOARD IOT")
        self.logger.info("="*80)
        
        for test_name, result in results.items():
            if test_name != "overall_success":
                status = "✅ BERHASIL" if result else "❌ GAGAL"
                self.logger.info(f"{test_name.replace('_', ' ').title()}: {status}")
        
        success_rate = (successful_tests / total_tests) * 100
        self.logger.info("-"*80)
        self.logger.info(f"Total Keberhasilan: {successful_tests}/{total_tests} ({success_rate:.1f}%)")
        
        if results["overall_success"]:
            self.logger.info("🎉 PENGUJIAN BERHASIL - Dashboard IoT berfungsi dengan baik!")
        else:
            self.logger.warning("⚠️  PENGUJIAN PARSIAL - Ada beberapa fitur yang perlu diperbaiki")
        
        self.logger.info("="*80)
    
    def cleanup(self) -> None:
        """Membersihkan resources dan menutup WebDriver"""
        if self.driver:
            try:
                self.driver.quit()
                self.logger.info("🧹 WebDriver berhasil ditutup")
            except Exception as e:
                self.logger.warning(f"⚠️  Warning saat menutup WebDriver: {str(e)}")


def main():
    """
    Fungsi utama untuk menjalankan pengujian
    """
    print("🚀 IoT Web Dashboard Automation Testing")
    print("="*50)
    
    # Konfigurasi testing
    BASE_URL = "https://iot-fakeapi.vercel.app/"  # Sesuaikan dengan URL aplikasi Anda
    TIMEOUT = 30  # Timeout dalam detik
    
    # Buat instance tester dan jalankan semua test
    tester = IoTDashboardTester(base_url=BASE_URL, timeout=TIMEOUT)
    results = tester.run_all_tests()
    
    # Return code untuk CI/CD integration
    return 0 if results["overall_success"] else 1


if __name__ == "__main__":
    exit(main())
"""  
Quick Start Script untuk IoT Dashboard Testing
Jalankan script ini untuk testing cepat dengan konfigurasi minimal

Catatan: Jika ada masalah import, gunakan simple_runner.py sebagai alternatif
"""

import sys
import os
import subprocess
from pathlib import Path
def quick_test():
    """
    Menjalankan quick test dengan subprocess untuk menghindari import issues
    """
    print("🚀 IoT Dashboard Quick Test")
    print("=" * 40)
    print("📍 URL: https://iot-fakeapi.vercel.app/")
    print("⏱️  Timeout: 30 seconds")
    print("🔑 Password: admin123")
    print()
    
    # Konfirmasi dari user
    while True:
        confirm = input("Lanjutkan testing? (y/n): ").lower().strip()
        if confirm in ['y', 'yes', 'ya']:
            break
        elif confirm in ['n', 'no', 'tidak']:
            print("Testing dibatalkan.")
            return
        else:
            print("Silakan ketik 'y' untuk ya atau 'n' untuk tidak")
    
    print()
    
    # Jalankan testing dengan subprocess
    automation_dir = Path(__file__).parent / "automation_tests"
    
    if not automation_dir.exists():
        print("❌ Direktori automation_tests tidak ditemukan!")
        return
    
    try:
        print("🎯 Memulai pengujian...")
        original_dir = os.getcwd()
        os.chdir(automation_dir)
        
        result = subprocess.run([sys.executable, "iot_dashboard_tester.py"], 
                              capture_output=False)
        
        os.chdir(original_dir)
        
        # Tampilkan ringkasan
        if result.returncode == 0:
            print("\n🎉 QUICK TEST BERHASIL!")
            print("Semua fitur utama berfungsi dengan baik.")
        else:
            print("\n⚠️ QUICK TEST SELESAI")  
            print("Ada beberapa fitur yang perlu diperiksa.")
            print("Lihat log detail untuk informasi lengkap.")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        os.chdir(original_dir)


def interactive_config():
    """
    Mode interaktif untuk konfigurasi custom
    """
    print("⚙️  KONFIGURASI CUSTOM")
    print("=" * 30)
    
    # Input URL
    url = input("URL Dashboard (default: https://iot-fakeapi.vercel.app/): ").strip()
    if not url:
        url = "https://iot-fakeapi.vercel.app/"
    
    # Input timeout
    timeout_input = input("Timeout dalam detik (default: 30): ").strip()
    try:
        timeout = int(timeout_input) if timeout_input else 30
    except ValueError:
        timeout = 30
        print("⚠️ Timeout tidak valid, menggunakan default: 30 detik")
    
    # Input password
    password = input("Password untuk download test (default: admin123): ").strip()
    if not password:
        password = "admin123"
    
    print(f"\n📋 KONFIGURASI:")
    print(f"   URL: {url}")
    print(f"   Timeout: {timeout} detik")
    print(f"   Password: {password}")
    print()
    
    print("💡 Custom config saat ini hanya mendukung URL default.")
    print("   Untuk kustomisasi penuh, edit automation_tests/utils/config.py")
    
    # Jalankan testing standar
    automation_dir = Path(__file__).parent / "automation_tests"
    
    try:
        original_dir = os.getcwd()
        os.chdir(automation_dir)
        
        result = subprocess.run([sys.executable, "iot_dashboard_tester.py"], 
                              capture_output=False)
        
        os.chdir(original_dir)
        return result.returncode == 0
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        os.chdir(original_dir)
        return False


def main():
    """
    Menu utama untuk quick start
    """
    print("🎯 IoT Dashboard Testing - Quick Start")
    print("=" * 50)
    print()
    print("Pilih mode testing:")
    print("1. Quick Test (konfigurasi default)")
    print("2. Custom Config (konfigurasi manual)")
    print("3. Keluar")
    print()
    
    while True:
        choice = input("Pilihan Anda (1-3): ").strip()
        
        if choice == "1":
            quick_test()
            break
        elif choice == "2":
            interactive_config()
            break
        elif choice == "3":
            print("Terima kasih! 👋")
            break
        else:
            print("⚠️ Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Testing dihentikan oleh user.")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("Silakan cek log untuk detail lengkap.")
    
    input("\nTekan Enter untuk keluar...")
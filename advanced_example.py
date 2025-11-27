"""
Contoh Penggunaan Advanced - IoT Dashboard Testing
Versi sederhana tanpa dependency import yang kompleks

Untuk menjalankan:
python advanced_example.py
"""

import sys
import os
import subprocess
from pathlib import Path


def run_main_test():
    """Jalankan test utama"""
    automation_dir = Path(__file__).parent / "automation_tests"
    
    if not automation_dir.exists():
        print("❌ Direktori automation_tests tidak ditemukan!")
        return False
    
    main_script = automation_dir / "iot_dashboard_tester.py"
    if not main_script.exists():
        print("❌ File iot_dashboard_tester.py tidak ditemukan!")
        return False
    
    try:
        print("🎯 Menjalankan test utama IoT Dashboard...")
        print("📍 URL: https://iot-fakeapi.vercel.app/")
        print("-" * 50)
        
        original_dir = os.getcwd()
        os.chdir(automation_dir)
        
        # Run main test
        result = subprocess.run([sys.executable, "iot_dashboard_tester.py"], 
                              capture_output=False)
        
        os.chdir(original_dir)
        return result.returncode == 0
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        if 'original_dir' in locals():
            os.chdir(original_dir)
        return False


def run_responsive_simulation():
    """Simulasi test responsive design dengan screenshot manual"""
    print("\n📱 SIMULASI RESPONSIVE TESTING")
    print("=" * 40)
    
    screen_sizes = [
        ("Desktop", "1920x1080"),
        ("Laptop", "1366x768"), 
        ("Tablet", "768x1024"),
        ("Mobile", "375x667")
    ]
    
    print("💡 Untuk test responsive manual:")
    print("   1. Buka https://iot-fakeapi.vercel.app/ di browser")
    print("   2. Tekan F12 untuk Developer Tools")
    print("   3. Klik icon device/responsive mode")
    print("   4. Test ukuran layar berikut:")
    print()
    
    for name, size in screen_sizes:
        print(f"   📐 {name}: {size}")
    
    print("\n✅ Pastikan navigasi dan grafik tetap dapat diakses")
    print("✅ Pastikan tidak ada elemen yang terpotong")


def run_performance_check():
    """Simulasi performance testing"""
    print("\n⚡ SIMULASI PERFORMANCE TESTING")
    print("=" * 40)
    
    print("💡 Untuk test performance manual:")
    print("   1. Buka https://iot-fakeapi.vercel.app/")
    print("   2. Tekan F12 > Network tab")
    print("   3. Refresh halaman (Ctrl+R)")
    print("   4. Cek metrics berikut:")
    print()
    
    print("   📊 Load Time: < 3 detik (good)")
    print("   📊 First Paint: < 1.5 detik (good)")
    print("   📊 DOM Content Loaded: < 2 detik (good)")
    print("   📊 Network Requests: < 50 requests (good)")
    print()
    
    print("   5. Pindah ke Console tab")
    print("   6. Pastikan tidak ada error merah")


def show_advanced_menu():
    """Menu untuk advanced testing"""
    print("\n🚀 ADVANCED IOT DASHBOARD TESTING")
    print("=" * 50)
    print("1. Jalankan Test Utama (Automation)")
    print("2. Guide Responsive Testing (Manual)")
    print("3. Guide Performance Testing (Manual)")
    print("4. Jalankan Semua (Test + Guides)")
    print("5. Kembali")
    print()


def run_all_advanced():
    """Jalankan semua test dan guide"""
    print("🎯 MENJALANKAN SEMUA ADVANCED TESTING")
    print("=" * 50)
    
    # 1. Main automated test
    success = run_main_test()
    
    # 2. Manual guides
    run_responsive_simulation()
    run_performance_check()
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 ADVANCED TESTING SUMMARY")
    print("=" * 60)
    
    print("🔧 AUTOMATED TESTS:")
    if success:
        print("   ✅ Main IoT Dashboard Test: PASSED")
    else:
        print("   ❌ Main IoT Dashboard Test: FAILED")
    
    print("\n📱 MANUAL TESTING GUIDES:")
    print("   📐 Responsive Design Guide: PROVIDED")
    print("   ⚡ Performance Testing Guide: PROVIDED")
    
    print("\n💡 NEXT STEPS:")
    print("   1. Review automated test logs")
    print("   2. Follow manual testing guides")
    print("   3. Document any issues found")
    print("=" * 60)


def main():
    """Main function untuk advanced testing"""
    while True:
        show_advanced_menu()
        
        choice = input("Pilihan Anda (1-5): ").strip()
        
        if choice == "1":
            success = run_main_test()
            if success:
                print("\n🎉 Test utama berhasil!")
            else:
                print("\n⚠️ Test utama selesai dengan peringatan.")
            input("\nTekan Enter untuk kembali...")
            
        elif choice == "2":
            run_responsive_simulation()
            input("\nTekan Enter untuk kembali...")
            
        elif choice == "3":
            run_performance_check()
            input("\nTekan Enter untuk kembali...")
            
        elif choice == "4":
            run_all_advanced()
            input("\nTekan Enter untuk kembali...")
            
        elif choice == "5":
            print("\nKembali ke menu utama...")
            break
            
        else:
            print("⚠️ Pilihan tidak valid. Silakan pilih 1-5.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Program dihentikan oleh user.")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        input("\nTekan Enter untuk keluar...")
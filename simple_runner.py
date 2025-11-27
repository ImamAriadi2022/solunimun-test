"""
Simple Test Runner untuk IoT Dashboard Testing
Script runner sederhana tanpa dependency kompleks
"""

import os
import sys
import subprocess
from pathlib import Path


def run_main_test():
    """Jalankan test utama langsung"""
    print("🚀 IoT Dashboard Test - Simple Runner")
    print("=" * 50)
    
    # Navigate to automation_tests directory
    automation_dir = Path(__file__).parent / "automation_tests"
    
    if not automation_dir.exists():
        print("❌ Direktori automation_tests tidak ditemukan!")
        return False
    
    main_script = automation_dir / "iot_dashboard_tester.py"
    
    if not main_script.exists():
        print("❌ File iot_dashboard_tester.py tidak ditemukan!")
        return False
    
    print(f"📍 URL Target: https://iot-fakeapi.vercel.app/")
    print("⏱️  Timeout: 30 detik")
    print()
    
    # Konfirmasi
    confirm = input("Mulai testing? (y/n): ").lower().strip()
    if confirm not in ['y', 'yes', 'ya']:
        print("Testing dibatalkan.")
        return False
    
    print("\n🎯 Memulai pengujian...")
    print("-" * 40)
    
    # Jalankan script dengan subprocess
    try:
        # Change to automation_tests directory
        original_dir = os.getcwd()
        os.chdir(automation_dir)
        
        # Run the script
        result = subprocess.run([sys.executable, "iot_dashboard_tester.py"], 
                              capture_output=False, 
                              text=True)
        
        # Return to original directory
        os.chdir(original_dir)
        
        return result.returncode == 0
        
    except Exception as e:
        print(f"❌ Error menjalankan test: {str(e)}")
        os.chdir(original_dir)  # Make sure we return to original dir
        return False


def show_menu():
    """Tampilkan menu utama"""
    print("\n" + "=" * 50)
    print("🎯 IoT Dashboard Testing Menu")
    print("=" * 50)
    print("1. Jalankan Test Utama")
    print("2. Lihat Struktur Project") 
    print("3. Keluar")
    print()


def show_project_structure():
    """Tampilkan struktur project"""
    print("\n📁 Struktur Project:")
    print("=" * 30)
    
    base_dir = Path(__file__).parent
    
    def print_tree(directory, prefix="", max_depth=3, current_depth=0):
        if current_depth >= max_depth:
            return
            
        items = sorted(directory.iterdir(), key=lambda x: (x.is_file(), x.name))
        
        for i, item in enumerate(items):
            if item.name.startswith('.'):
                continue
                
            is_last = i == len(items) - 1
            current_prefix = "└── " if is_last else "├── "
            print(f"{prefix}{current_prefix}{item.name}")
            
            if item.is_dir() and current_depth < max_depth - 1:
                next_prefix = prefix + ("    " if is_last else "│   ")
                print_tree(item, next_prefix, max_depth, current_depth + 1)
    
    print_tree(base_dir)
    print("\n📋 File Utama:")
    print("   • iot_dashboard_tester.py - Script pengujian utama")
    print("   • quick_start.py - Interactive runner") 
    print("   • simple_runner.py - Runner sederhana (file ini)")
    print("   • run_tests.bat - Windows batch runner")


def main():
    """Fungsi utama"""
    while True:
        show_menu()
        
        choice = input("Pilihan Anda (1-3): ").strip()
        
        if choice == "1":
            success = run_main_test()
            if success:
                print("\n🎉 Testing selesai dengan sukses!")
            else:
                print("\n⚠️ Testing selesai dengan peringatan.")
            
            input("\nTekan Enter untuk kembali ke menu...")
            
        elif choice == "2":
            show_project_structure()
            input("\nTekan Enter untuk kembali ke menu...")
            
        elif choice == "3":
            print("\nTerima kasih! 👋")
            break
            
        else:
            print("⚠️ Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Program dihentikan oleh user.")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        input("\nTekan Enter untuk keluar...")
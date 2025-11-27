"""
Utility functions untuk IoT Dashboard Testing
"""

import os
import time
from pathlib import Path
from typing import List, Optional
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestUtils:
    """Utility class dengan helper methods untuk testing"""
    
    @staticmethod
    def safe_click(driver, element: WebElement, scroll_first: bool = True) -> bool:
        """
        Safely click an element with optional scrolling
        
        Args:
            driver: WebDriver instance
            element: WebElement to click
            scroll_first: Whether to scroll to element first
            
        Returns:
            bool: True if click successful
        """
        try:
            if scroll_first:
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(0.5)
            
            element.click()
            return True
        except Exception as e:
            print(f"Error clicking element: {str(e)}")
            return False
    
    @staticmethod
    def wait_for_element_text_change(driver, element: WebElement, 
                                   original_text: str, timeout: int = 10) -> bool:
        """
        Wait for an element's text to change from original text
        
        Args:
            driver: WebDriver instance
            element: WebElement to monitor
            original_text: Original text to compare against
            timeout: Timeout in seconds
            
        Returns:
            bool: True if text changed within timeout
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                current_text = element.text
                if current_text != original_text:
                    return True
                time.sleep(0.5)
            except:
                pass
        return False
    
    @staticmethod
    def find_elements_by_partial_text(driver, text: str, 
                                    tag: str = "*") -> List[WebElement]:
        """
        Find elements containing partial text
        
        Args:
            driver: WebDriver instance
            text: Partial text to search for
            tag: HTML tag to search within (default: any tag)
            
        Returns:
            List[WebElement]: List of matching elements
        """
        try:
            xpath = f"//{tag}[contains(text(), '{text}')]"
            return driver.find_elements(By.XPATH, xpath)
        except:
            return []
    
    @staticmethod
    def is_element_visible(driver, locator: tuple, timeout: int = 5) -> bool:
        """
        Check if element is visible within timeout
        
        Args:
            driver: WebDriver instance
            locator: Tuple of (By type, selector)
            timeout: Timeout in seconds
            
        Returns:
            bool: True if element is visible
        """
        try:
            wait = WebDriverWait(driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
    
    @staticmethod
    def get_download_directory() -> str:
        """Get the default download directory"""
        return str(Path.home() / "Downloads")
    
    @staticmethod
    def clean_old_downloads(patterns: List[str], max_age_minutes: int = 60) -> int:
        """
        Clean old download files matching patterns
        
        Args:
            patterns: List of file patterns (e.g., ['*.csv', '*.json'])
            max_age_minutes: Maximum age of files to keep in minutes
            
        Returns:
            int: Number of files cleaned
        """
        download_dir = Path(TestUtils.get_download_directory())
        cleaned_count = 0
        cutoff_time = time.time() - (max_age_minutes * 60)
        
        for pattern in patterns:
            for file_path in download_dir.glob(pattern):
                try:
                    if file_path.stat().st_mtime < cutoff_time:
                        file_path.unlink()
                        cleaned_count += 1
                except:
                    pass
                    
        return cleaned_count
    
    @staticmethod
    def wait_for_file_download(patterns: List[str], timeout: int = 30) -> Optional[Path]:
        """
        Wait for a file matching patterns to be downloaded
        
        Args:
            patterns: List of file patterns to look for
            timeout: Timeout in seconds
            
        Returns:
            Optional[Path]: Path to downloaded file or None if timeout
        """
        download_dir = Path(TestUtils.get_download_directory())
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            for pattern in patterns:
                files = list(download_dir.glob(pattern))
                for file_path in files:
                    # Check if file is recent (created within last 2 minutes)
                    if time.time() - file_path.stat().st_mtime < 120:
                        # Check if file is not being downloaded (.crdownload)
                        if not (download_dir / f"{file_path.name}.crdownload").exists():
                            return file_path
            
            time.sleep(1)
        
        return None
    
    @staticmethod
    def take_screenshot(driver, filename: str, directory: str = "reports") -> bool:
        """
        Take a screenshot and save it
        
        Args:
            driver: WebDriver instance
            filename: Name of the screenshot file
            directory: Directory to save screenshot
            
        Returns:
            bool: True if screenshot saved successfully
        """
        try:
            screenshot_dir = Path(__file__).parent.parent / directory
            screenshot_dir.mkdir(exist_ok=True)
            
            filepath = screenshot_dir / f"{filename}.png"
            driver.save_screenshot(str(filepath))
            return True
        except Exception as e:
            print(f"Error taking screenshot: {str(e)}")
            return False
    
    @staticmethod
    def log_browser_console(driver) -> List[dict]:
        """
        Get browser console logs
        
        Args:
            driver: WebDriver instance
            
        Returns:
            List[dict]: List of console log entries
        """
        try:
            return driver.get_log('browser')
        except:
            return []
    
    @staticmethod
    def wait_for_page_load(driver, timeout: int = 30) -> bool:
        """
        Wait for page to fully load
        
        Args:
            driver: WebDriver instance
            timeout: Timeout in seconds
            
        Returns:
            bool: True if page loaded successfully
        """
        try:
            WebDriverWait(driver, timeout).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            return True
        except:
            return False


class TestReporter:
    """Class untuk generating test reports"""
    
    @staticmethod
    def generate_html_report(results: dict, output_file: str = "test_report.html") -> bool:
        """
        Generate HTML test report
        
        Args:
            results: Test results dictionary
            output_file: Output HTML file name
            
        Returns:
            bool: True if report generated successfully
        """
        try:
            html_content = TestReporter._create_html_content(results)
            
            report_dir = Path(__file__).parent.parent / "reports"
            report_dir.mkdir(exist_ok=True)
            
            with open(report_dir / output_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            return True
        except Exception as e:
            print(f"Error generating HTML report: {str(e)}")
            return False
    
    @staticmethod
    def _create_html_content(results: dict) -> str:
        """Create HTML content for test report"""
        
        # Calculate statistics
        total_tests = len(results) - 1  # Exclude 'overall_success'
        passed_tests = sum(1 for k, v in results.items() if k != 'overall_success' and v)
        success_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>IoT Dashboard Test Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .header {{ background: #2196F3; color: white; padding: 20px; border-radius: 5px; }}
                .summary {{ background: #f5f5f5; padding: 15px; margin: 20px 0; border-radius: 5px; }}
                .test-case {{ margin: 10px 0; padding: 10px; border-left: 4px solid #ddd; }}
                .passed {{ border-left-color: #4CAF50; background: #f9fff9; }}
                .failed {{ border-left-color: #f44336; background: #fff9f9; }}
                .status {{ font-weight: bold; }}
                .passed .status {{ color: #4CAF50; }}
                .failed .status {{ color: #f44336; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>IoT Dashboard Automation Test Report</h1>
                <p>Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
            
            <div class="summary">
                <h2>Test Summary</h2>
                <p><strong>Total Tests:</strong> {total_tests}</p>
                <p><strong>Passed:</strong> {passed_tests}</p>
                <p><strong>Failed:</strong> {total_tests - passed_tests}</p>
                <p><strong>Success Rate:</strong> {success_rate:.1f}%</p>
                <p><strong>Overall Status:</strong> {'PASSED' if results.get('overall_success', False) else 'FAILED'}</p>
            </div>
            
            <div class="test-details">
                <h2>Test Details</h2>
        """
        
        # Add test case details
        test_names = {
            'webdriver_init': 'WebDriver Initialization',
            'dashboard_open': 'Dashboard Loading',
            'main_page_verify': 'Main Page Verification',
            'data_visualization': 'Data Visualization Validation',
            'time_filters': 'Time Filter Testing',
            'download_feature': 'Download Feature Testing'
        }
        
        for key, name in test_names.items():
            status = results.get(key, False)
            status_class = 'passed' if status else 'failed'
            status_text = 'PASSED' if status else 'FAILED'
            
            html += f"""
                <div class="test-case {status_class}">
                    <h3>{name}</h3>
                    <p class="status">Status: {status_text}</p>
                </div>
            """
        
        html += """
            </div>
        </body>
        </html>
        """
        
        return html
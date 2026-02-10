# src/open_flipkart.py
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
 
def main():
    # Headless options (works in GitHub Actions CI)
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")      # Chrome's new headless
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
 
    # Start Chrome via webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
 
    try:
        url = "https://www.flipkart.com/"
        print(f"Opening: {url}")
        driver.get(url)
        # Simple sanity check: wait and print page title
        time.sleep(3)
        print("Page title:", driver.title)
 
        # (Optional) Take a screenshot artifact
        driver.save_screenshot("flipkart_home.png")
        print("Saved screenshot: flipkart_home.png")
 
    finally:
        driver.quit()
 
if __name__ == "__main__":
    main()
 
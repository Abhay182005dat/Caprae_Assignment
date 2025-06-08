from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

def setup_driver():
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-blink-features=AutomationControlled")
    opts.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/114.0.0.0 Safari/537.36"
    )
    opts.add_experimental_option('excludeSwitches', ['enable-logging'])
    return webdriver.Chrome(service=Service("C:/webdrivers/chromedriver.exe"), options=opts)

def test_print_company_cards():
    driver = setup_driver()
    companies_data = []
    
    try:
        driver.get("https://clutch.co/web-developers")

        # wait until at least one card is present
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "provider-list-item"))
        )
        time.sleep(2)  # let any lazy-load settle

        # grab all cards by their class name
        company_cards = driver.find_elements(By.CLASS_NAME, "provider-list-item")
        
        for card in company_cards:
            try:
                company_info = {}
                
                # Company name
                company_info['Company Name'] = card.find_element(
                    By.CLASS_NAME, "provider__title").text.strip()
                
                # Website
                try:
                    website = card.find_element(
                        By.CSS_SELECTOR, "a.website-link__item").get_attribute('href')
                    company_info['Website'] = website
                except:
                    company_info['Website'] = "N/A"
                
                # LinkedIn
                try:
                    linkedin = card.find_element(
                        By.CSS_SELECTOR, "a[href*='linkedin.com']").get_attribute('href')
                    company_info['LinkedIn'] = linkedin
                except:
                    company_info['LinkedIn'] = "N/A"
                
                # Employee Range
                try:
                    employees = card.find_element(By.CLASS_NAME, "fp-employees").text
                    company_info['Employee Range'] = employees
                except:
                    company_info['Employee Range'] = "N/A"
                
                # Hourly Rate
                try:
                    rate = card.find_element(By.CLASS_NAME, "hourly-rate").text
                    company_info['Hourly Rate'] = rate
                except:
                    company_info['Hourly Rate'] = "N/A"
                
                # Location
                try:
                    location = card.find_element(By.CLASS_NAME, "location").text
                    company_info['Location'] = location
                except:
                    company_info['Location'] = "N/A"
                
                companies_data.append(company_info)
                
            except Exception as e:
                print(f"Error processing card: {str(e)}")
                continue
        
        # Save to CSV
        if companies_data:
            fieldnames = ['Company Name', 'Website', 'LinkedIn', 
                         'Employee Range', 'Hourly Rate', 'Location']
            
            with open('scraped_leads.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(companies_data)
            
            print(f"Successfully scraped {len(companies_data)} companies")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_print_company_cards()

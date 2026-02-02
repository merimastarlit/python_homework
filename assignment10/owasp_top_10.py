
# Task 6: Scraping OWASP Top 10 vulnerabilities from the OWASP website and saving them into a CSV file.

# Importing necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


# Setting up the webdriver
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
wait = WebDriverWait(driver, 20)

driver.get("https://owasp.org/Top10/2025/")

# Waiting for page content
wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a")))


results = []

# XPath for OWASP Top 10 (A01–A10)
owasp_10 = driver.find_elements(
    By.XPATH,
    "//a[starts-with(normalize-space(.), 'A0') or starts-with(normalize-space(.), 'A10')]"
)

# Extracting vulnerability titles and links
for each in owasp_10:
    title = each.text.strip()
    if not title:
        continue

    results.append({
        "Vulnerability": title,
        "Link": each.get_attribute("href")
    })


# Verify output
for r in results:
    print(r)

# Writing CSV
df = pd.DataFrame(results)
df.to_csv("./owasp_top_10.csv", index=False)

driver.quit()

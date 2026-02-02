
# Task 1, Task 2, Task 3: Web Scraping with Selenium

# importing necessary libraries
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

# setting up the webdriver
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

# navigating to the library search page
driver.get(
    "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")


# waiting for the page to load and the search results to be present
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_all_elements_located(
    (By.CSS_SELECTOR, 'li[data-test-id="searchResultItem"]')
))

# extracting book information
results = []
list_books = driver.find_elements(
    By.CSS_SELECTOR, 'li[data-test-id="searchResultItem"]')

# iterating through each book and extracting details
for book in list_books:
    # Title
    try:
        title = book.find_element(
            By.CSS_SELECTOR, "span.title-content").text.strip()
    except NoSuchElementException:
        title = ""

    # Authors (handle multiple)
    author_elements = book.find_elements(By.CLASS_NAME, "author-link")
    authors = [a.text.strip() for a in author_elements if a.text.strip()]
    author = "; ".join(authors)

    print(author)

    # Format + Year
    try:
        format_year = book.find_element(
            By.CLASS_NAME, "manifestation-item-link").text.strip()
    except NoSuchElementException:
        format_year = ""

    results.append({
        "Title": title,
        "Author": author,
        "Format-Year": format_year
    })

# Creating a DataFrame to display the results
df = pd.DataFrame(results)
print(df.head(10))

driver.quit()


# Task 4: Save the data into a CSV file

# Saving to CSV
df.to_csv("./get_books.csv", index=False)


# saving results list in json format
with open("./get_books.json", "w") as json_file:
    json.dump(results, json_file, indent=4)



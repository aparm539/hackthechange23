from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Set up the webdriver
driver.get("https://www.dellrefurbished.ca/laptops")

# Wait for the page to load
wait = WebDriverWait(driver, 5)
laptops = driver.find_elements(By.CSS_SELECTOR, ".thumb-grid")

# List to hold laptop data
laptop_data = []

for laptop in laptops:
    # Extracting laptop details
    name = laptop.find_element(By.CSS_SELECTOR, ".name").text
    price = laptop.find_element(By.CSS_SELECTOR, ".prices-wrap .price").text
    memory = laptop.find_element(By.XPATH, ".//label[text()='Memory']/following-sibling::div").text
    storage = laptop.find_element(By.XPATH, ".//label[text()='HDD']/following-sibling::div").text
    display = laptop.find_element(By.XPATH, ".//label[text()='Display']/following-sibling::div").text

    laptop_data.append({
        "Name": name,
        "Price": price,
        "Memory": memory,
        "Storage": storage,
        "Display": display

    })

# Close the WebDriver
driver.quit()

# Print the scraped data
for data in laptop_data:
    print(data)


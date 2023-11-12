
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Set up the webdriver
driver.get("https://www.amazon.ca/s?bbn=8929975011&rh=n:8929975011,n:667823011,n:!677211011,n:2404990011,n:677252011&pf_rd_i=8929975011&pf_rd_m=A3DWYIK6Y9EEQB&pf_rd_p=00b50a20-35f7-426f-be7f-df3ecdb0b123&pf_rd_r=CH7S5VXGMH87DARR7EVC&pf_rd_s=merchandised-search-6&pf_rd_t=101")

wait = WebDriverWait(driver, 5)

# Wait for the laptops to load
laptops = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")))
all_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".a-color-base")))

prices = []
for element in all_elements:
    text = element.text
    if "$" in text and "." in text:
        prices.append(element)

# Extract only every third element from all_elements as these are the prices


with open('laptop_details.txt', 'w') as file:
    ## write the laptop name and price to the file
    for laptop, price in zip(laptops, prices):
        try:
            full_name = laptop.text
            price_text = price.text
            file.write(f"{full_name}, {price_text}\n")
        except Exception as e:
            print("Error in extracting data for a laptop", e)

driver.quit()
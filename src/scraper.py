from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()

# Indispensable dans GitHub Codespaces
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

driver.get("https://data.inpi.fr")

print(driver.title)

driver.quit()

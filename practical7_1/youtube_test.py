from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys  # Needed for pressing Enter
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. Open the Chrome browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # 2. Navigate to YouTube
    driver.get("https://www.youtube.com")

    # 3. Wait for the page to load
    time.sleep(2)

    # 4. Maximize the browser window
    driver.maximize_window()

    # 5. Locate the YouTube search box
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(
        EC.presence_of_element_located((By.NAME, "search_query"))
    )

    # 6. Enter text and press ENTER
    search_box.send_keys("open source software")
    search_box.send_keys(Keys.ENTER)

    # 7. Wait to view the search results
    print("Search performed successfully on YouTube!")
    time.sleep(5)

except Exception as e:
    print("An error occurred:", e)

finally:
    # 8. Close the browser
    driver.quit()
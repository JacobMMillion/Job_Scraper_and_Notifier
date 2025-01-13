"""
This program scrapes the Teach For America leaning stream to find
available tutoring positions. It uses the 'send_email_driver'
function from the 'send_message' program to send an email if a
new position is added
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from send_message import send_email_driver

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument("--disable-gpu")

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open the webpage
url = "https://reg.learningstream.com/view/cal4a.aspx?ek=&ref=0&aa=0&sid1=0&sid2=0&as=70&wp=796&tz=0&ms=0&nav=0&cc=0&cat1=0&cat2=0&cat3=0&aid=TFA&rf=&pn=0"

maxRows = 0

# Loop that runs every 10 minutes
while True:
    try:
        # Open the webpage
        driver.get(url)

        # Wait for the page to load completely (adjust the sleep time if needed)
        time.sleep(5)

        # Check if page is loaded and print page source for debugging
        page_source = driver.page_source
        # print(page_source)

        # Locate the container element
        container = driver.find_element(By.ID, "container")
        print("Container found!")
        
        # Try to locate the table headers inside the container
        table_header = container.find_element(By.CLASS_NAME, "table_header_cal_list")
        print("Table header found!")
        
        # Extract the table items (rows)
        rows = container.find_elements(By.CSS_SELECTOR, '.table_item_cal_list')

        # Iterate through the rows and print their HTML for debugging
        # for row in rows:
        #     print(row.get_attribute('outerHTML'))  # Prints the full HTML of the row
        #     columns = row.find_elements(By.TAG_NAME, 'div')
        #     print(f"Number of columns in this row: {len(columns)}")

        #     for col in columns:
        #         print(f"Column text: {col.text.strip()}")  # Print the text of each column

        print("Row length:", len(rows))

        # if additional entries and greater len than prev max
        if len(rows) > 5 and maxRows < len(rows):
            print("Row added!")
            send_email_driver()
            maxRows = len(rows)
        # if an entry was removed, update maxRows accordingly
        elif len(rows) < maxRows:
            print("Row removed!")
            maxRows = len(rows)
        else:
            print("No change since last check")

    except Exception as e:
        print(f"FAIL - Error: {str(e)}")  # Print specific error if exception occurs

    # Sleep for 5 minutes (300 seconds) before repeating
    print("---------------------------------")
    time.sleep(300)

# Close the driver after scraping (this line will never be reached unless the loop is broken manually)
driver.quit()
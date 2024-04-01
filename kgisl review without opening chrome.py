from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import time

chrome_options = ChromeOptions()
chrome_options.add_argument("executable_path=C:/Users/CHARAN/Documents/KGiSL/cd/chromedriver-win64/chromedriver.exe")

driver = Chrome(options=chrome_options)
driver.get("https://www.glassdoor.co.in/Reviews/KGISL-Reviews-E404925.htm")
time.sleep(1)

# Create and open a text file for writing
#with open("glassdoor_reviews.txt", "w", encoding="utf-8") as file:

    # Loop through the review elements
for i in range(1, 11):  # Assuming you want to extract 10 reviews
    review_element = driver.find_element(By.XPATH, f'/html/body/div[2]/div[1]/div[2]/main/div[5]/div/ol/li[{i}]/div/div/div[2]')
    review_text = review_element.text
    print(review_text)
#        file.write(f"Review {i}:\n{review_text}\n\n")

# Close the browser
driver.quit()

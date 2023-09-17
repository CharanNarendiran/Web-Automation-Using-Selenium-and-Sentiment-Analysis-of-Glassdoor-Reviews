from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import time

def extract_reviews(url):
    driver = Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(1)

    reviews = []

    for i in range(1, 10):
        review_element = driver.find_element(By.XPATH, f'/html/body/div[2]/div[1]/div[2]/main/div[5]/div/ol/li[{i}]/div/div/div[2]')
        review_text = review_element.text
        reviews.append(review_text)
        print(review_text)

    driver.quit()

    return reviews

chrome_options = ChromeOptions()
chrome_options.add_argument("executable_path=C:/Users/CHARAN/Documents/KGiSL/cd/chromedriver-win64/chromedriver.exe")

all_reviews = []


# Loop through the pages (assuming there are 3 pages)
for page_num in range(1, 40):
    url = f"https://www.glassdoor.co.in/Reviews/KGISL-Reviews-E404925_P{page_num}.htm?filter.iso3Language=eng"
    page_reviews = extract_reviews(url)
    all_reviews.extend(page_reviews)

# Save the reviews to a file
output_filepath = "C:/Users/CHARAN/KGiSL/kgisl glassdoor final reviews.txt"

try:
    with open(output_filepath, "w", encoding="utf-8") as file:
        for i, review in enumerate(all_reviews, start=1):
            file.write(f"Review {i}:\n{review}\n\n")
    print(f"Reviews saved to '{output_filepath}'.")
except Exception as e:
    print(f"An error occurred while saving the reviews: {e}")
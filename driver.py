from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

def downloadTorrent():
    pass

def processCatalogResult():
    pass

browser = webdriver.Firefox()

browser.get('https://librivox.org/search?primary_key=0&search_category=title&search_page=1&search_form=get_results')

#time.sleep(5)

#bookList = browser.find_elements(By.CLASS_NAME, "catalog-result")

bookList = WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".result-data a [href]")))

for book in bookList:
    print(book.get_attribute('href'))

browser.quit()
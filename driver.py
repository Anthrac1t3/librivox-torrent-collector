from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options

downloadLocation = r"\\10.28.28.4\Torrents\AudioBooks"

options = Options()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", downloadLocation)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

browser = webdriver.Firefox(options=options)

currentPage = 1

browser.get(f"https://librivox.org/search?primary_key=0&search_category=title&search_page={currentPage}&search_form=get_results")

lastPage = int(WebDriverWait(browser, 30).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'page-number')))[-1].get_attribute('data-page_number'))

while True:
    #Create a list for holding the URLs of the books on the page
    bookList = []

    #Grab a list of all the catalog result objects on the page load. These object represent the books, their links and info
    resultList = WebDriverWait(browser, 30).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'catalog-result')))

    #Grab the book URLs from each one of those objects and append it to the bookList
    for result in resultList:
        bookList.append(result.find_element(By.TAG_NAME, 'a').get_attribute('href'))

    #Now process the book list
    for book in bookList:
        #Get the load the book's URL into the browser
        browser.get(book)
        #When the "Torrent" button loads, click it and start the download
        WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Torrent']"))).click()

    #If we are on the last page of the catalog then we can drop out of the main loop
    if currentPage == lastPage:
        break

    #Increment the page count when we are done with each page
    currentPage += 1

    #Get the next page of the catalog
    browser.get(f"https://librivox.org/search?primary_key=0&search_category=title&search_page={currentPage}&search_form=get_results")

#Close up the browser
browser.quit()
from bs4 import BeautifulSoup
from selenium import webdriver
import requests


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}

chrome_driver = r'C:\Users\Aldyk\Desktop\oreh\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=chrome_driver, options=options)

def currency(query):

    target = 'https://coinmarketcap.com/currencies/' + query + '/news/'
    driver.get(target)

    soup = BeautifulSoup(driver.page_source, 'lxml')

    for links in soup.find_all('a', class_="svowul-0 jMBbOf cmc-link"):
        if links['href'][0] != 'h':       
            print('Title: ' + links.h3.text)
            page_link = 'https://coinmarketcap.com' + links['href']
            #print(page_link)
        else:
            print('Title: ' + links.h3.text)
            page_link = links['href']
            #print(page_link)
        print('______________________________________________________________________________________________________')
        print('')
        r = requests.get(page_link).text
        soup_links = BeautifulSoup(r, 'lxml')
        for data in soup_links.find_all('p', class_=None):
            print(data.text)   
        print('______________________________________________________________________________________________________')
        print('')
        



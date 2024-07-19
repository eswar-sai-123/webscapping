#Import these libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time 

#initialize the webdriver
driver = webdriver.Chrome('c:\Windows\chromedriver.exe')

#Load the url, give the time for the website to load
url = 'https://in.indeed.com/'
driver.get(url)
time.sleep(6)

#Search bar, write the requried data
search_box = driver.find_element_by_xpath('//*[@id="text-input-what"]')
search_box.send_keys("Data Analyst")
time.sleep(4)

#Clicking the search button    
search_button = driver.find_element_by_xpath('//*[@id="jobsearch"]/div/div[2]')
search_button.click()
time.sleep(5)

#function where webscarpping is done.
def web_scrapping():
    
    source = driver.page_source #You can go through each use case of soup from its documentaion
    soup = BeautifulSoup(source, "lxml")
    #Loop over each table as available in the html;
    for article in soup.find_all("table"):
        job = article.h2.a.span.text
        
        company = article.find("span",class_="css-63koeb eu4oa1w0").text
        

        link = article.find("a",class_="jcs-JobTitle css-jspxzf eu4oa1w0")["href"]

        link1 = f"https://in.indeed.com{link}"
        

        csv_writer.writerow([job,company,link1])

#Open the csv file to write the required;
csv_file = open("jobs.csv","w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Job","Companyname","link"])

#Ensuring the loop doesn't go through the whole pages, in these the code goes to 2 tab only.
c =0
while c < 2:
    c += 1 
    try:
        #code for going to the next page.
        web_scrapping()
        time.sleep(10) 
        next_button = driver.find_element_by_xpath('//*[@id="jobsearch-JapanPage"]/div/div[5]/div/div[1]/nav/ul/li[6]/a')
        next_button.click()
        time.sleep(7)
    except:
        print("An error ocuured")
        break 
csv_file.close()




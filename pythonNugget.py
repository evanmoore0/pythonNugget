from selenium import webdriver
from selenium.webdriver.remote import command
from webdriver_manager.chrome import ChromeDriverManager

#Initiate the browser
browser  = webdriver.Chrome(ChromeDriverManager().install())

#Open Yahoo Finance
browser.get("https://finance.yahoo.com")

#Get company user is looking for
company = input("What company are you looking for? \n")

#Find the search bar and send it user input
searchBar = browser.find_element_by_id("yfin-usr-qry")
searchBar.send_keys(company)
searchBar.submit()


#Python 3.6.8
#author Karan Joshi



from bs4 import BeautifulSoup
import pandas
from selenium import webdriver # Use https://github.com/mozilla/geckodriver/releases to install geckodriver on your python console 
import time
driver=webdriver.Firefox() # Instantiating browser object
page=driver.get("https://yourstory.com/companies/search?page=1&sortBy=EmployeeCountASC&hitsPerPage=1000")
time.sleep(10)  # Waiting for automated browser to get the page downloaded
all_table=driver.find_element_by_tag_name("table") # searching the table tag in the html code
soup=BeautifulSoup(all_table.get_attribute("innerHTML"),"html.parser") # get the inner html code of tables as a Beautiful soup object
x=soup.find_all("div")# get all divs from the table html code
df=pandas.DataFrame()# start a pandas dataframe 
table_text=[i.text for i in x] # for each element in the list x transfer its text to each element of table_text list
df["name"]=table_text[::5] # transfer to each row corresponding to the attributes into the dataframe
df["sectors"]=table_text[1::5]
df["headquaters"]=table_text[2::5]
df["funding"]=table_text[3::5]
df["employee count"]=table_text[4::5]
df.to_csv("your_story_full_page_type1.csv")# transfer dataframe to csv



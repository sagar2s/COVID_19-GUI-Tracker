
import requests
import bs4
import notifiers
import time
import datetime
import tkinter as tk

#url passing function
def get_covid_details(url):
    value = requests.get(url)
    return value


#Web scraping function 
# Worldwide

def formatted_output_data_wordwide():
    wb_site='https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1'
    data=get_covid_details(wb_site)
    formatted = bs4.BeautifulSoup(data.text, 'html.parser')
    info=formatted.find_all(id="maincounter-wrap")
    print("Worldwide Covid19 Data:")
    for id in info:
        all_text=id.find("h1").get_text()
        all_data=id.find("span").get_text()
        print(all_text+" "+all_data)
            



#Search by country

def formatted_output_data_country():
    searchdata=input("Enter a country you want to search\n")
    wb_site_country="https://www.worldometers.info/coronavirus/country/"+searchdata
    data_country=get_covid_details(wb_site_country)
    formatted_country = bs4.BeautifulSoup(data_country.text, 'html.parser')
    info=formatted_country.find_all(id="maincounter-wrap")
    print(searchdata.capitalize()+"'s COVID 19 DATA :")
    formdat=""
    for id in info:
        all_text=id.find("h1").get_text()
        all_data=id.find("span").get_text()
        data=all_text+" "+all_data+"\n"
        formdat=formdat+data
    print(formdat)
    
formatted_output_data_country()
print("\n")
formatted_output_data_wordwide()







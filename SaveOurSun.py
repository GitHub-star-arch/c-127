from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import csv

start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('./chromedriver')

browser.get(start_url)

time.sleep(10)

def scrap():
    bsoup = BeautifulSoup(browser.page_source, 'html.parser')
    table_tags = bsoup.find('table', attrs={'class':"wikitable sortable jquery-tablesorter"})
    temp_list=[]
    row_tags = table_tags.find_all('tr')
    for tr in row_tags:
        data_tags = tr.find_all('td')
        r = [i.text.rstrip( ) for i in data_tags]
        temp_list.append(r)
    print(temp_list[1])
    name_list=[]
    dist_list=[]
    mass_list=[]
    radius_list=[]
    lumen_list=[]
    for i in range(1, len(temp_list)):
        name_list.append(temp_list[i][1])
        dist_list.append(temp_list[i][3])
        mass_list.append(temp_list[i][5])
        radius_list.append(temp_list[i][6])
        lumen_list.append(temp_list[i][7])
    #print(name_list)
    #with open('stars.csv', "w") as f:
    #    cw = csv.writer(f)   
    #    cw.writerow(['names','distance','mass','radius','luminosity'])
    #    cw.writerows(name_list)
    #    cw.writerows(dist_list)
    #    cw.writerows(mass_list)
    #    cw.writerows(radius_list)
    #    cw.writerows(lumen_list)
    df = pd.DataFrame(list(zip(name_list,dist_list,mass_list,radius_list,lumen_list)), columns=['names','distance','mass','radius','luminosity'])
    print(df)
    df.to_csv('brightestars.csv')
        

scrap()
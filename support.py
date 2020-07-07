from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webbrowser
import requests
import time 
import datetime
from bs4 import BeautifulSoup 
import re
from googlesearch import search
import requests, json 


def search_2(subject,phrase):
	ext="https://www.google.com/search?q="
	for s in subject:
		 	new_='"'+s+'"'
		 	n=phrase.replace(s,new_)
	msg=n.replace(" ","+")
	url=ext+msg
	webbrowser.open(url,new=1)

def play(message,subject):
    result=message
    ext="https://www.youtube.com/results?search_query="
    messg=result.replace(" ","+")
    msg=ext+messg

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 3)
    presence = EC.presence_of_element_located
    visible = EC.visibility_of_element_located

    driver.get(msg)
    wait.until(visible((By.ID, "video-title")))
    names=driver.find_elements_by_id("video-title")
    i=0
    for name in names:
        print(name.text)
        if len(subject)==2:
        	s=subject[1]
        else:
        	s=subject[0]
        if s not in name.text.lower():
            i+=1
            continue
        else:
            break

        #driver.quit()
    print(i)
    driver.find_elements_by_id("video-title")[i].click()
    url = driver.current_url
    time_prev= int(round(time.time()))
    #video=pafy.new(url)
    #print((driver.find_elements_by_xpath("//span[@class='ytp-time-duration']")[0]).text)
    s=driver.find_elements_by_xpath("//html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/div[1]/ytd-thumbnail-overlay-time-status-renderer/span")[0].text
    #s="10:00"
    time_k=int(s.split(':')[0])*60+int(s.split(':')[1])
    boo=True
    while boo:
        time_now=int(round(time.time()))
        if time_now-time_prev==int(time_k+2):
            driver.quit()
            boo=False
    

def book(message):
        if "hotel" in message:
            
            ext="https://www.google.com/search?q="
            print("Can u please specify the palce where you want to book")
            detail_place=input()
            print("can u please specify the on the date of stay")
            detail_date=input()
            msg="hotel booking at "+str(detail_place)+" on "+str(detail_date)
            url=ext+msg
            
            
            count=0
#import requests
            links=search(msg, num=5, stop=5, pause=2)
            
            for link in links:
                #print(link)
                
                    webbrowser.open(link)
                    #webbrowser.open(re.split(":(?=http)",link["href"].replace("/url?q=",""))[0],new=1)
            webbrowser.open(url,new=1)
            time.sleep(5)
            res="Here are the options"
        elif "bus" in message:
            ext="https://www.google.com/search?q="
            print("Can u please specify your destination")
            detail_dest=input()
            print("Can u please specify your source")
            detail_source=input()
            print("can u please specify the on the date of journey")
            detail_date=input()
            print("can u please approx time of journey")

            detail_time=input()
            print("AC or NON AC")
            choice=input()
            msg=choice+ " bus booking from "+str(detail_source)+" to "+str(detail_dest)+" on "+str(detail_date)+" at "+str(detail_time)
            url=ext+msg
            
            links=search(msg, num=5, stop=5, pause=2)
            
            for link in links:
                #print(link)
                
                    webbrowser.open(link)
                    #webbrowser.open(re.split(":(?=http)",link["href"].replace("/url?q=",""))[0],new=1)
            webbrowser.open(url,new=1)
            time.sleep(5)
            res="Here are the options"
        elif "room" in message:
            ext="https://www.google.com/search?q="
            print("Can u please specify your place")
            detail_dest=input()
            #print("Can u please specify your source")
            #detail_source=input()
            print("can u please specify the on the date of stay")
            detail_date=input()
            print("3 star or 5 star")
            detail_desc=input()

            #detail_time=input()
            print("AC or NON AC")
            AC=input()
            print("any particular hotel u want")
            choice=input()
            if re.search(r"\b(no|none|nothing)\b",choice) is not None:
                choice=""
            mesg=AC+" room " +choice+" "+detail_desc+" hotel booking in "+str(detail_dest)+" from "+str(detail_date)
            msg=mesg.replace(" ","+")
            url=ext+msg
            
            links=search(msg, num=5, stop=5, pause=2)
            #links=search(msg, tld="co.in", num=5, stop=5, pause=2)
            
            for link in links:
                #print(link)
                
                    webbrowser.open(link)
                    #webbrowser.open(re.split(":(?=http)",link["href"].replace("/url?q=",""))[0],new=1)
            webbrowser.open(url,new=1)
            time.sleep(5)
            res="Here are the options"
        elif "train" in message:
            ext="https://www.google.com/search?q="
            print("Can u please specify your destination")
            detail_dest=input()
            print("Can u please specify your source")
            detail_source=input()
            print("can u please specify the on the date of journey")
            detail_date=input()
            print("can u please approx time of journey")

            detail_time=input()
            print("AC or NON AC")
            choice=input()
            msg=choice+ " train booking from "+str(detail_source)+" to "+str(detail_dest)+" on "+str(detail_date)+" at "+str(detail_time)
            url=ext+msg
            
            links=search(msg,  num=5, stop=5, pause=2)
            for link in links:
                #print(link)
                
                    webbrowser.open(link)
                    #webbrowser.open(re.split(":(?=http)",link["href"].replace("/url?q=",""))[0],new=1)
            webbrowser.open(url,new=1)
            time.sleep(5)
            res="Here are the options"
        elif "flight" in message:
            ext="https://www.google.com/search?q="
            print("Can u please specify your destination")
            detail_dest=input()
            print("Can u please specify your source")
            detail_source=input()
            print("can u please specify the on the date of journey")
            detail_date=input()
            print("can u please approx time of journey")

            detail_time=input()
            print("Choice of Flight Service")
            choice=input()
            msg=choice+ " flight booking from "+str(detail_source)+" to "+str(detail_dest)+" on "+str(detail_date)+" at "+str(detail_time)
            url=ext+msg
            
            links=search(msg, num=5, stop=5, pause=2)
            for link in links:
                #print(link)
                
                    webbrowser.open(link)
                    #webbrowser.open(re.split(":(?=http)",link["href"].replace("/url?q=",""))[0],new=1)
            webbrowser.open(url,new=1)
            time.sleep(5)
            res="Here are the options"
        elif "movie" in message:
            ext="https://www.google.com/search?q="
            print("Can u please tell the movie")
            detail_movie=input()
            print("Can u please specify the timing")
            detail_timing=input()
            print("can u please specify the region or city")
            detail_region=input()
            #print("can u please approx time of journey")

           # detail_time=input()
            #print("Choice of Flight Service")
            #choice=input()
            msg=detail_movie+" movie booking at "+str(detail_timing)+" in "+str(detail_region)
            url=ext+msg
            
            links=search(msg, num=5, stop=5, pause=2)
            for link in links:
                #print(link)
                
                    webbrowser.open(link)
                    #webbrowser.open(re.split(":(?=http)",link["href"].replace("/url?q=",""))[0],new=1)
            webbrowser.open(url,new=1)
            time.sleep(5)
            res="Here are the options"
        else:
            res="I dont properly understand but i will try to help"
            ext="https://www.google.com/search?q="
            url=ext+message
            webbrowser.open(url,new=1)

def get_weather():
	api_key = "3fde248dfc251d2e2770c78bfee66975"
	base_url = "http://api.openweathermap.org/data/2.5/weather?"

	print("Enter the city please")

	city_name=input()
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
	response = requests.get(complete_url)
	x = response.json()
	if x["cod"] != "404": 
		y = x["main"]
		current_temperature = y["temp"]
		current_pressure = y["pressure"] 
		current_humidiy = y["humidity"]
		z = x["weather"] 
		weather_description = z[0]["description"] 
		print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description)) 
	else: 
		print(" City Not Found ") 

def get_news_update():
    url="https://www.telegraphindia.com/"
    news = requests.get(url)
    news_c = news.content
    soup = BeautifulSoup(news_c, 'html5lib')
    headline_1 = soup.find_all('h2', class_="fs-32 uk-text-1D noto-bold uk-margin-small-bottom ellipsis_data_2 firstWord")

    headline_2 = soup.find_all('h2',class_="fs-20 pd-top-5 noto-bold uk-text-1D uk-margin-small-bottom ellipsis_data_2")

    headlines=[]
    for i in headline_1:
        h=i.get_text()[1:]
        headlines.append(h)
    for i in headline_2:
        h=i.get_text()[1:]
        headlines.append(h)
    for i in headlines:
        l=i.split()
        new_string = " ".join(l)
        print(new_string)

def scrape(phrase):
    flag=0
    ext="https://www.google.com/search?q="
    links=search(phrase, num=5, stop=5, pause=2)
    msg=phrase.replace(" ","+")
    url=ext+msg
    i=0
    for link in links:
        i+=1
        if 'wikipedia' in link:
            flag=1
            l=link
            break
    

    if flag==1:
        wiki = requests.get(l)

        wiki_c = wiki.content
        soup = BeautifulSoup(wiki_c, 'html.parser')
        data=soup.find_all('p')
        print("Source:wikipedia")

        print(data[0].get_text())

        print(data[1].get_text())
        print(data[2].get_text())
        print(data[3].get_text())
        
    else:
        print("wikipedia Source not available")
    print("Providing search results")
    webbrowser.open(url,new=1)
    time.sleep(3)

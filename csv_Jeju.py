from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import numpy as np


data = []
High_Low_Precipitation = ['08','10','21']


for year_to_2020 in range(1970,2020):
    for element in High_Low_Precipitation:
        html="https://www.weather.go.kr/w/obs-climate/land/past-obs/obs-by-element.do?stn=184&yy=%d&obs=%s" % (year_to_2020,element)
        driver = webdriver.Chrome(ChromeDriverManager().install())
        #ChromeDriverManager().install()로 자동으로 하려고 했지만 코드를 짜던중에 사용자이름을 바꿔 오류가 떠서 절대경로로 해주었다.
        driver.implicitly_wait(3)
        driver.get(html)
        #selenium 을 사용한 웹 크롤링을 했습니다.
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for i in range(2,14):
            row = soup.select("#weather_table > tbody > tr:nth-child(32) > td:nth-child(%d) > span" % i)
            #반복문을 이용해 불필요한 것을 제거합니다.
            data.append(row)

print(data)
value = []
csv_data = []
for i in data:
    for j in i:
        value.append(j.get_text()) #원하는값만 추출합니다.
for i in value:
    csv_data.append([i])

df = pd.DataFrame(np.array(csv_data))
df.to_csv("C:\\Users\\leesa\\PycharmProjects\\JejuIsland\\jeju.csv",sep=',',encoding = 'utf-8-sig') #한글방지로 utf-8-sig를 사용합니다.

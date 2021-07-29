import csv
import re

from bs4 import BeautifulSoup 
from selenium import webdriver 


# 음료
# filename = "starbucks_drink_영양정보.csv"
# 푸드
filename = "starbucks_food_영양정보.csv"
csv_open = open(filename, "w+", encoding="utf-8-sig")
csv_writer = csv.writer(csv_open)

# webdriver 실행 
dr = webdriver.Chrome('E:/chromedriver_win32/chromedriver.exe') 

# target page 접근 
# dr.get("https://www.starbucks.co.kr/menu/drink_list.do")
dr.get("https://www.starbucks.co.kr/menu/food_list.do") 
# dr.get("https://www.starbucks.co.kr/menu/product_list.do") 

# html source 추출 
html_source = dr.page_source 

# BS로 html parsing 
soup = BeautifulSoup(html_source, 'html.parser') 
# 원하는 항목의 데이터만 추출 
target = soup.findAll('table', {'class': re.compile("coffeeInfo mb60")})
#print(target)
# 결과 확인 
# for drink in drinks:
#     image_tag = drink.find("img")
#     image_url = image_tag['src']
#     title = image_tag['alt']
#     csv_writer.writerow((title, image_url))
# csv_open.close()



for t in target:
    tbody = t.find("tbody")
    trData = tbody.find_all('tr')
    for tr in trData:
        tdData = tr.find_all('td')
        print(tdData[0].text)
        csv_writer.writerow((tdData[0].text, tdData[1].text, tdData[2].text, tdData[3].text, tdData[4].text, tdData[5].text))
csv_open.close()


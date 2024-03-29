import csv
import re

from bs4 import BeautifulSoup 
from selenium import webdriver 

# 음료
# filename = "starbucks_drink.csv"
# 푸드
# filename = "starbucks_food.csv"
# 상품
filename = "starbucks_product.csv"
# 커피
# filename = "starbucks_coffee.csv"
csv_open = open(filename, "w+", encoding="utf-8-sig")
csv_writer = csv.writer(csv_open)

# webdriver 실행 
dr = webdriver.Chrome('E:/chromedriver_win32/chromedriver.exe') 

# target page 접근 
# dr.get("https://www.starbucks.co.kr/menu/drink_list.do")
# dr.get("https://www.starbucks.co.kr/menu/food_list.do") 
dr.get("https://www.starbucks.co.kr/menu/product_list.do") 
# dr.get("https://www.starbucks.co.kr/coffee/product_list.do") 

# html source 추출 
html_source = dr.page_source 

# BS로 html parsing 
soup = BeautifulSoup(html_source, 'html.parser') 

# 원하는 항목의 데이터만 추출 
drinks = soup.findAll("li", {"class": re.compile("menuDataSet")})

# 결과 확인 
for drink in drinks:
    image_tag = drink.find("img")
    image_url = image_tag['src']
    title = image_tag['alt']
    csv_writer.writerow((title, image_url))
csv_open.close()



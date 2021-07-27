import urllib.request
url = 'https://image.istarbucks.co.kr/upload/store/skuimg/2021/06/[9200000003643]_20210623101238720.jpg'
urllib.request.urlretrieve(url, 'jpg/test.jpg')

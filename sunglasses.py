#dynamic scrapping 
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

url = 'https://www.glasses.com/gl-us/sunglasses'
all_products = []

data = driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
products = soup.find_all('div', class_='product-info')

for product in products:
    #finding and pulling the needed columns
    brand_tag = product.find('div', class_='product-brand')
    code_tag = product.find('div', class_='product-code')
    offerprice_tag = product.find('div', class_='product-offer-price')
    actualprice_tag = product.find('div', class_='product-list-price')

    #Standardizing and pulling the needed data safely to avoid the code breaking
    brand_name = brand_tag.get_text(strip=True) if brand_tag else "N/A"
    code = code_tag.get_text(strip=True) if code_tag else "N/A"
    offer_price = offerprice_tag.get_text(strip=True) if offerprice_tag else "N/A"
    actual_price = actualprice_tag.get_text(strip=True) if actualprice_tag else "N/A"

    #Passing it into the created list
    all_products.append({
        'brand': brand_name,
        'code': code,
        'offer': offer_price,
        'price' : actual_price
    })


print(f"Total product generate: {len(all_products)}")
print(all_products)
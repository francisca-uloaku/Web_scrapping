#dynamic scrapping 
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
#options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

url = 'https://www.glasses.com/gl-us/eyeglasses'
all_products = []

data = driver.get(url)
#driver.get(url)
#time.sleep(5)

#max_clicks = 5
#click_count = 0

#while True:
 #   try:
 #       more_page = driver.find_element("xpath", "//button[contains(text(), 'MORE')]")
  #      driver.execute_script("argument[0].scrollIntoView({behavior: 'smooth', block: 'center'});", more_page)
  #      time.sleep(1.5)
        
   #     more_page.click()
   #     click_count += 1
    #    print("Successfully clicked")

    #    time.sleep(4)

   # except Exception:
   #     print("All product loaded successfully")
    #    break

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
#driver.quit()

print(f"Total product generate: {len(all_products)}")
print(all_products)
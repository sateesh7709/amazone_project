from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

app = Flask(__name__)

@app.route('/amz_search/<product_name>' , methods = ['GET'])
def search(product_name: str):
    if product_name == ' ':
        return 'Product name not provided'

    product_name = product_name.replace(' ', '+')
    url = f'https://www.amazon.in/s?k={product_name}&crid=2MUVVRNCECQG9&sprefix={product_name}%2Caps%2C360&ref=nb_sb_noss_1'


    current_dir = os.getcwd()
    driver_path = os.path.join(current_dir, 'chromedriver.exe')
    driver = webdriver.Chrome(driver_path)
    driver.get(url)
    elements = driver.find_elements(By.XPATH, '//span[@class="a-size-base-plus a-color-base a-text-normal"]')
    pro_list = []
    for element in elements:
        pro_list.append(element.text)

    driver.quit()
    return {'products': pro_list, "url": url}

if __name__ == '__main__':
    app.run(debug=True)




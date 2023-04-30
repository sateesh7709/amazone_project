I have tried using Two methods I will prefer to cheak on - Method 1.  - file (method_web_scraping.py)  - WEB SCRAPING

Method 1.  - file (method_web_scraping.py)  - WEB SCRAPING

#postman collection attached with the file's in the repo.

Prerequisites:-

- To run the project we need to crome driver (one is attached with the project for crome version 112) - chromedriver.exe
- also need to install requirements.txt file (attached with project).

Amazon Product Search API:- 

This project is a simple API for fetching product names from the Amazon website. The API is built using Flask and uses Selenium for web scraping.

Usage: - 
The API can be accessed by sending a GET request to the endpoint /amz_search/<product_name>. The product_name parameter specifies the search keyword for which products need to be fetched.

The API returns a JSON response containing a list of product names and the URL of the Amazon search page.


Note: 
-In some case the url might be genereated wrong in that case can try to replace url.
-In case api return blank list and url is correct try rehit api

Example
Sending a GET request to http://localhost:5000/amz_search/'laptop'


Method 2 - file (method_amz_api.py)  - CALLING AMAZONE API.

- This api calls AmazonAPI to get data 
- This will required to have following data
    -aws_access_key_id 
    -aws_secret_access_key 
    -aws_associate_tag 


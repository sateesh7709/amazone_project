from amazon.api import AmazonAPI

aws_access_key_id = ''
aws_secret_access_key = ''
aws_associate_tag = ''


amazon = AmazonAPI(aws_access_key_id, aws_secret_access_key, aws_associate_tag)
products = amazon.search(Keywords='kindle', SearchIndex='All')
for product in products:
    print(product)

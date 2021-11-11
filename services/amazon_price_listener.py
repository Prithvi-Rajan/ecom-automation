from services.mail_server import MailServer
import requests
from bs4 import BeautifulSoup
from decouple import config


class AmazonPriceListener:
    @staticmethod
    def check(product_link: str, price_threshold: int):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }

        # send a request to fetch HTML of the page
        response = requests.get(product_link, headers=headers)

        # create the soup object
        soup = BeautifulSoup(response.content, 'html.parser')
        try:
            # change the encoding to utf-8
            soup.encode('utf-8')
            title = soup.find(id="productTitle").get_text().strip()
            price = soup.find(id="priceblock_ourprice").get_text().replace(
                ',', '').replace('₹', '').replace(' ', '').strip()
        except:
            print('Captcha requested...Retrying in 2 minutes...')
            return 120

        # converting the string amount to float
        converted_price = float(price[0:5])
        print(converted_price)
        if(converted_price < price_threshold):
            MailServer.send_mail(to=config('TO'),
                                 subject=f'Price drop on {title}!',
                                 body=f'Price dropped to ₹ {price}.\n Click the link to view product: {product_link}'
                                 )
        return 60 * 60

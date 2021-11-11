import time

from services.amazon_price_listener import AmazonPriceListener
import sys
sys.path.append('/services')


def main():
    products = {
        'axor_venomous_dull_black': 'https://www.amazon.in/Apex-Venomous-Dull-Black-Helmet-M/dp/B07Y5KCSWM/'
    }

    while(True):
        sleep_for = AmazonPriceListener.check(
            products['axor_venomous_dull_black'], price_threshold=5700)
        time.sleep(sleep_for)


if __name__ == '__main__':
    main()

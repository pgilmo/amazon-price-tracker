import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

url = 'https://www.amazon.es/UBUNTU-25-10-Memoria-Bootable-Linux/dp/B0FZBN1B1H/ref=sr_1_1?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&sr=8-1'
desired_price = 10
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

def extract_price(url):
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')

        price_whole = soup.find('span', class_='a-price-whole').getText().replace(',', '').strip()
        price_fraction = soup.find('span', class_='a-price-fraction').getText().replace(',', '').strip()

        price = float(price_whole + '.' + price_fraction)

        return price
    except Exception as e:
        return None
    
def main():
    while True:

        current_price = extract_price(url)
        timestamp = datetime.now()

        if current_price is not None:
            if current_price <= desired_price:
                print(f'Checking price at {timestamp}')
                print('The price is cheap! Buy it!')
                print(f'Desired price: {desired_price}€ | Current price: {current_price}\n')
            else:
                print(f'Checking price at {timestamp}')
                print('The price is too expensive...')
                print(f'Desired price: {desired_price}€ | Current price: {current_price}\n')
        else:
            print('There was an error. Trying again in 1 min.')
            time.sleep(60)
            continue

        time.sleep(3600)

if __name__ == '__main__':
    main()
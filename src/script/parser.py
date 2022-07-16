import csv
import os
from typing import Dict, List, Optional

import requests

from data import get_cookies, get_headers


def create_path() -> str:
    """ Create path for saving path. """

    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(parent_dir, 'result', 'products.csv')


def save_file(items: Dict[str, Optional[str]]) -> None:
    """ Save data in .csv file. """

    with open(create_path(), 'w', encoding='utf-16', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(
            [
                'ID товара',
                'Наименование',
                'Цена, руб',
                'Город',
                'Промоцена, руб',
                'Ссылка',
            ]
        )

        for item in items:
            writer.writerow(
                [
                    item.get('id'),
                    item.get('title'),
                    item.get('price'),
                    item.get('city'),
                    item.get('promo_price'),
                    item.get('link'),
                ]
            )


def get_data(cities: List[str]) -> None:
    """ Get data from Api. """

    clean_products: Dict[str, Optional[str]] = []

    for city in cities:
        products = requests.get(
            f'https://api.detmir.ru/v2/products?filter=categories.alias:lego;'
            f'placement:web_listing_popular;region.iso:RU-{city}&limit=500',
            cookies=get_cookies(city),
            headers=get_headers(),
        ).json()

        for product in products:
            promo_price = False if product['old_price'] is None else True
            price = ''
            if promo_price:
                price = product.get('old_price').get('price')
            else:
                price = product.get('price').get('price')
            promo_price = (
                product.get('price').get('price') if promo_price else None
            )
            clean_products.append(
                {
                    'id': product.get('id'),
                    'title': product.get('title'),
                    'price': price,
                    'city': cities[city],
                    'promo_price': promo_price,
                    'link': product.get('link').get('web_url'),
                }
            )

    save_file(clean_products)


def main() -> None:
    """ Main function. """

    cities = {
        'MOW': 'Москва',
        'SPE': 'Санкт-Петербург',
    }
    get_data(cities)


if __name__ == '__main__':
    main()

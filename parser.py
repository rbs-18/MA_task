import requests
import json


def get_data(cities):
    """ Get data from Api. """

    clean_products = {}

    for city in cities:
        cookies = {
            'ab2_90': 'ab2_90old90',
            'ab2_33': 'ab2_33old34',
            'ab2_50': '33',
            'ab3_75': 'ab3_75old75',
            'ab3_33': 'ab3_33new33',
            'ab3_20': 'ab3_20_20_3',
            'cc': '0',
            'uid': 'X6NyEmLQHewuPbe0A+HRAg==',
            '_gaexp': 'GAX1.2.8MwGXf_UQwWf1g2n0sBLCw.19243.x90!rF6aGfQwQPiBEWNbZr-EZQ.19193.2',
            'is_shop_pos': '1',
            'JSESSIONID': 'f8ade7e2-1354-40e2-9508-e3262e25a195',
            'detmir-cart': 'badcc269-8872-48ac-9016-9917f00b240a',
            'auid': '6926bb3d-536a-4113-a07f-a4a96626ffea',
            'srv_id': 'cubic-front08-prod',
            '_ga': 'GA1.2.183838861.1657806319',
            '_gid': 'GA1.2.1596867625.1657806319',
            '_gcl_au': '1.1.1359377107.1657806319',
            '_ym_uid': '1657806319655416033',
            '_ym_d': '1657806319',
            'advcake_track_id': 'a745d62d-0901-201d-2cde-821f7404c83a',
            'advcake_session_id': 'bbbc69e0-7aff-d1e9-4c7f-0fa2659a1625',
            'tmr_lvid': '2da186de2173ce5c8a0f6d7f2a536eb8',
            'tmr_lvidTS': '1657806320120',
            '_ym_isad': '2',
            'dm_s': 'L-f8ade7e2-1354-40e2-9508-e3262e25a195|kHbadcc269-8872-48ac-9016-9917f00b240a|Vj6926bb3d-536a-4113-a07f-a4a96626ffea|gqcubic-front08-prod|qa604fc531-b354-4a1c-94f4-0106ba5e1c3a|RK1657807359231|11cbf932b7-d5b8-4f5b-b285-206dfdf768e6#BWnBkcL89a021pgDykDNcDKEjzNWwIdyM4X0bF5dlIA',
            'tmr_reqNum': '13',
            '_sp_ses.2b21': '*',
            '_ym_visorc': 'w',
            'qrator_msid': '1657813919.268.fuS69P7npegNuNLl-gbf4e9e8d1rhle61d6qos4ta7setb19s',
            'geoCityDM': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%20%D0%B8%20%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C',
            'geoCityDMIso': f'RU-{city}',
            'geoCityDMCode': '7700000000000',
            '_sp_id.2b21': '8f960979-dd84-40c4-8814-2999b5815f64.1657806318.2.1657815398.1657807492.dc5db757-a334-49e5-9bfa-eeee145395db',
            '_gat': '1',
            'mindboxDeviceUUID': 'a021240e-48f4-4674-bf44-500b9bca8c4d',
            'directCrm-session': '%7B%22deviceGuid%22%3A%22a021240e-48f4-4674-bf44-500b9bca8c4d%22%7D',
            'cto_bundle': 'hPNekl82MHRYbmx0JTJGUVNIbHRWbndiWkt0MFVCd2RFbjBad0ZTRW5FZ29ydVlObXJoZnQ0VDFKbE5LRHk5MVlSNXZXaFdqOTMyQ0hIcSUyQk1Yazg2NzhyMlYlMkJnb1hUT3FtOE1iM2VRQ2dlQ3dZUm92dU81VmxHUnJWJTJGVFhMTHNGblZVb3Z3JTJGVjRISG94QXhIOVVBbTNzYXBWNzBRJTNEJTNE',
        }

        headers = {
            'authority': 'api.detmir.ru',
            'accept': '*/*',
            'accept-language': 'en,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7',
            'content-type': 'application/json',
            'cache-control': 'no-cache, no-store, must-revalidate',
            'expires': '0',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'ab2_90=ab2_90old90; ab2_33=ab2_33old34; ab2_50=33; ab3_75=ab3_75old75; ab3_33=ab3_33new33; ab3_20=ab3_20_20_3; cc=0; uid=X6NyEmLQHewuPbe0A+HRAg==; _gaexp=GAX1.2.8MwGXf_UQwWf1g2n0sBLCw.19243.x90!rF6aGfQwQPiBEWNbZr-EZQ.19193.2; is_shop_pos=1; JSESSIONID=f8ade7e2-1354-40e2-9508-e3262e25a195; detmir-cart=badcc269-8872-48ac-9016-9917f00b240a; auid=6926bb3d-536a-4113-a07f-a4a96626ffea; srv_id=cubic-front08-prod; _ga=GA1.2.183838861.1657806319; _gid=GA1.2.1596867625.1657806319; _gcl_au=1.1.1359377107.1657806319; _ym_uid=1657806319655416033; _ym_d=1657806319; advcake_track_id=a745d62d-0901-201d-2cde-821f7404c83a; advcake_session_id=bbbc69e0-7aff-d1e9-4c7f-0fa2659a1625; tmr_lvid=2da186de2173ce5c8a0f6d7f2a536eb8; tmr_lvidTS=1657806320120; _ym_isad=2; dm_s=L-f8ade7e2-1354-40e2-9508-e3262e25a195|kHbadcc269-8872-48ac-9016-9917f00b240a|Vj6926bb3d-536a-4113-a07f-a4a96626ffea|gqcubic-front08-prod|qa604fc531-b354-4a1c-94f4-0106ba5e1c3a|RK1657807359231|11cbf932b7-d5b8-4f5b-b285-206dfdf768e6#BWnBkcL89a021pgDykDNcDKEjzNWwIdyM4X0bF5dlIA; tmr_reqNum=13; _sp_ses.2b21=*; _ym_visorc=w; qrator_msid=1657813919.268.fuS69P7npegNuNLl-gbf4e9e8d1rhle61d6qos4ta7setb19s; geoCityDM=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%20%D0%B8%20%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C; geoCityDMIso=RU-MOW; geoCityDMCode=7700000000000; _sp_id.2b21=8f960979-dd84-40c4-8814-2999b5815f64.1657806318.2.1657815398.1657807492.dc5db757-a334-49e5-9bfa-eeee145395db; _gat=1; mindboxDeviceUUID=a021240e-48f4-4674-bf44-500b9bca8c4d; directCrm-session=%7B%22deviceGuid%22%3A%22a021240e-48f4-4674-bf44-500b9bca8c4d%22%7D; cto_bundle=hPNekl82MHRYbmx0JTJGUVNIbHRWbndiWkt0MFVCd2RFbjBad0ZTRW5FZ29ydVlObXJoZnQ0VDFKbE5LRHk5MVlSNXZXaFdqOTMyQ0hIcSUyQk1Yazg2NzhyMlYlMkJnb1hUT3FtOE1iM2VRQ2dlQ3dZUm92dU81VmxHUnJWJTJGVFhMTHNGblZVb3Z3JTJGVjRISG94QXhIOVVBbTNzYXBWNzBRJTNEJTNE',
            'if-none-match': 'W/"58349-fOIuiLax6eCem9OaUwL5f++mh+E"',
            'origin': 'https://www.detmir.ru',
            'pragma': 'no-cache',
            'referer': 'https://www.detmir.ru/',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'x-requested-with': 'detmir-ui',
        }

        response = requests.get(
            f'https://api.detmir.ru/v2/recommendation/products?filter=category.'
            f'id:40;placement:web_listing_popular;region.iso:RU-{city}&limit=30',
            cookies=cookies,
            headers=headers
        ).json()
        products = response.get('products')
        # print(response)

        # with open('products.json', 'w') as file:
        #     json.dump(products, file, indent=4, ensure_ascii=False)

        clean_products[city] = []
        for product in products:
            promo_price = False if product['old_price'] is None else True
            clean_products[city].append(
                {
                    'id': product['id'],
                    'title': product['title'],
                    'price': (
                        product['old_price'] if promo_price
                        else product['price']
                    ),
                    # 'city': city,
                    'promo-price': product['price'] if promo_price else None,
                    'link': product['link']['web_url'],
                }
            )

    print(len(clean_products['MOW']), len(clean_products['SPE']))
    with open('clean_products.json', 'w') as file:
        json.dump(clean_products, file, indent=4, ensure_ascii=False)
    # print(clean_products)


if __name__ == '__main__':
    cities = ['MOW', 'SPE']
    get_data(cities)

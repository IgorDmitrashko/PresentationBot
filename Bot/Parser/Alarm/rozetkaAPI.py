import requests


class RozetkaAPI:
    def __init__(self):
        self.url = "https://xl-catalog-api.rozetka.com.ua/v4/goods/getDetails"
        self.url_alarm = "https://map.ukrainealarm.com/"

        self.headers = {
            "cookie": "cart-modal=old; ab-auto-portal=old; promo-horizontal-filters=verticalFilters; ab_tile_filter=old; xab_segment=3; slang=ru; _uss-csrf=Z0/P1DMUc7LMTM+tMqMnrRMxxhO+3sPjbD4XHIpOshEfr1J0; ussapp=TZ8e9jil9KH9piBJrtMADUz0qjMS9CHhbAa0WZs1; city_id=b205dde2-2e2e-4eb9-aef2-a67c82bbdf27; login=chiara3333%40ukr.net; popup18=%5B%7B%22user_detail_id%22%3A6%2C%22timestamp%22%3A1713719998%7D%5D; social-auth=new; tile_view=small; ab_test_search=1; uid=Cgo9D2dHwfco60rCZ31HAg==; __cf_bm=9J6wqQOxKcv3yI78oQVlxGK74eAygTXdiS4XCQ8EcSg-1732755959-1.0.1.1-xABTmB.EOCffFj_P.x6pEYZP0BO_4yZPyo4daWJP9kAGHO7bC2OYYjvCIzWrZM_WD_vgcY68nfobHyzZo9eHEQ; cf_clearance=TRaX4nRgQG846a6bpqFeukFoc3shDlCo96nNijIg4pw-1732755960-1.2.1.1-AXxFRh9Xc6uHFLdG7.iP7VT1w7HaZoSYmnhxeAXfSkbKRGqAtQA_euhM.EvJiD.ttE0f2e.6Ex.gFNungcyryKFZEL2rEGJcdgraU9Lc2HwYsDIi.J.q7DMTDlNNTNH5ZvPdvfT6g8YEzsmeQQ11fvyaeEhcrjWkNio2wVN2VySBuCphhk1abimF6sQ60oJzMC22fBJGURpspOfcAd0Mvc.bjyqZStuIKsQ_23BfZhDi2EeYvRKLGLojpP6ol_ZKgYT8GKnIrE8mf9xXSMVmSzGOGBvOzIsgHXA10pJVYvSz.Nt2KWwDoye6RKNg76aQ9EfnOHfAanMtuQkFv6tkcoVFF8UeT2B7gMV0jFsEPSOR7KuzE9wOs1tvNEcYPs0r",
            "accept": "application/json, text/plain, */*",
            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "dnt": "1",
            "origin": "https://rozetka.com.ua",
            "priority": "u=1, i",
            "referer": "https://rozetka.com.ua/notebooks/c80004/preset=game/",
            "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        }


    def get_product_details(self):
        querystring = {"country":"UA",
                       "lang":"ru",
                       "with_groups":"1",
                       "with_docket":"1",
                       "with_extra_info":"1",
                       "goods_group_href":"1",
                       "product_ids":"318463663,318463900,365714604,395460909,395460924,395461038,395461101,"
                                     "396809853,402336147,412864716,412922958,412954668,412955499,412955562,"
                                     "412955592,412955628,412955646,412955673,412955679,412955775,412955898,"
                                     "413011932,413045109,413045154,413045265,416017110,416023140,418345779,"
                                     "418347795,419349936,421984884,422876082,422894847,422904585,424932888,"
                                     "426585036,431112035,432388181,435347423,436841171,438235844,438280412,"
                                     "440054705,440068034,440071568,440385008,441294716,445010363,448413080,"
                                     "448428584,448428614,448428623,448428626,449721614,450350987,451802720,"
                                     "452354030,453866576,454034585,459688984"}

        response = requests.get(self.url, headers=self.headers, params=querystring)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Request failed", "status_code": response.status_code}


rozetka_api = RozetkaAPI()
print(rozetka_api.get_product_details())




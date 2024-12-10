import requests

url = "https://xl-catalog-api.rozetka.com.ua/v4/goods/getDetails"

querystring = {"country":"UA","lang":"ru","with_groups":"1","with_docket":"1","with_extra_info":"1","goods_group_href":"1","product_ids":"350834451,350834907,361212276,361220004,369852381,369914403,369933759,382590996,386457897,392205942,393033699,397735722,397739883,397751439,397754205,397755174,397755177,412056807,412064382,412077987,412078731,412084374,412085157,413134788,413154423,414036066,414043806,415384107,415384581,415386489,422783499,424933791,424940313,426858695,427232105,431601752,431613392,431613476,431613500,431615897,431616197,431617397,431617403,431619185,431619341,433676459,433681940,435037076,435069248,435073478,435074639,440530241,441989375,442019831,446555051,446556851,449051765,460809419"}

payload = ""
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cookie": "cart-modal=old; ab-auto-portal=old; promo-horizontal-filters=verticalFilters; ab_tile_filter=old; xab_segment=3; slang=ru; _uss-csrf=Z0/P1DMUc7LMTM+tMqMnrRMxxhO+3sPjbD4XHIpOshEfr1J0; ussapp=TZ8e9jil9KH9piBJrtMADUz0qjMS9CHhbAa0WZs1; city_id=b205dde2-2e2e-4eb9-aef2-a67c82bbdf27; login=chiara3333%40ukr.net; popup18=%5B%7B%22user_detail_id%22%3A6%2C%22timestamp%22%3A1713719998%7D%5D; social-auth=new; tile_view=small; ab_test_search=1; uid=Cgo9D2dHwfco60rCZ31HAg==; cf_clearance=r9fcYj8hzR7UDJ7llSYidgobbYxKVYTSmt7yXkvw4TQ-1732892279-1.2.1.1-UDYZxMR7CUDCDZwdyVdFjjnsRTseNa9KDDQ_pGvq198xvdW2NyLxbZQBObXWVrMmdkMi5rywAoPqIri5jSYTvTzOE4fLEK6H4awp6BB93AC7MEOiEVNAP3ZTWFPD3wwGiIH53f_QrW34JlSmBHZHrbt.5rSDrUs5TDAXfIhwWqND32qVr8.YDF7heweOKHkNvGnnZw3yWq93vFCbwYs3rcD96AqYBQLllyvI_P6.isRsawH_B9Tp..BpiH02Ly5TtuWUyfxuLqlLUJRioKRzuvJWP5UvOSPy.xDM_OMUmUsc2WobZlOcZmNieAWXR_57udV.sP_k7IXVomKTgWah2GiFTMvfkyhTuOMjmjzI6sq7v_rwB_YuZkgJ8hQud.r5; __cf_bm=nRk0FPxPQJOOSI8umeR4_VxoXZMA47qJCqeoApRyZmw-1732892622-1.0.1.1-fzzyASNXBm1sOoMarWYwzv0QFcsSpujFUHdDK6hGmAYEdwMgkJBeklvTjdMntwyUN2745zsY1BQQgHQT.pxqlg",
    "dnt": "1",
    "origin": "https://rozetka.com.ua",
    "priority": "u=1, i",
    "referer": "https://rozetka.com.ua/mobile-phones/c80003/",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}


response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)

import requests

BOT_TOKEN = '6503718678:AAEUjWh8jz1cklX_r8O_xcXH-1MnveEHJ2o'
WEATHER_TOKEN = '883ce8e32c9731721a8c6aeaaee11eb4'
API_KEY_NASA = '2M3J5egWX8kVhdGnU9N0vQ1spK3siVttzvcI6roE'

host = "localhost"
user = "root"
password = "password"
db_name = "mydb"


classes_yabko = {
    'catalog': 'product_catalog_',
    'item': 'catalog-product-item',
    'product_name': 'catalog-product-item--title',
    'special_price': 'current',
    'old_price': 'old'
}

classes_eStore = {
    'catalog': 'products-grid category-products-grid itemgrid itemgrid-adaptive itemgrid-2col single-line-name centered',
    'item': 'item',
    'product_name': 'product-name',
    'special_price': 'special-price',
    'old_price': 'old-price'
}


####### Апи тревог ####################
alarm_url = "https://map.ukrainealarm.com/api/data/getStatesHistory"
alarm_payload = ""
alarm_headers = {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE3MzI3NTAwODIsImV4cCI6MTczMjc1MzY4MiwiaXNzIjoidWtyYWluZS1hbGFybS1tYXAiLCJhdWQiOiJ1a3JhaW5lLWFsYXJtLW1hcCJ9.JVMe2zMUN4XflcLU1j13VuIFuyxAvXVRy0d4kXvlsoY",
    "cache-control": "max-age=0",
    "cookie": "_ga=GA1.1.1185894806.1728299565; _ga_9QLR0Q6YVH=GS1.1.1728299565.1.0.1728299566.0.0.0; cf_clearance=VDD34Ei0KoBHPUrDLhqRe3uGq3W9qfN524CMUJE2jqE-1732750080-1.2.1.1-S1Wo8WT6kEvqB3hYGCtz8Uo4_SSgy5qUZ7SxXAdkvgC7Uj_gyQY0CWirNlbcflPWBbtDbfEDEG0CcI1SZfql4jEiw9yvVVLyfpPjVUW.nGPKqckM.x35zxNyRmCXjkKiitqD0jVOxgIZNk71mfpGh2B4hvrgGM2ql6UbmL7Ej2OXtP4.X_tGCIgxgD_ScvxbauW6gvuyOIcdk8xBWCzQY1JoSkB5gFlD3.nrYY03hJQSUEvmznzvEyPNC56SUUtqVilrIu1rKJWnwH3tihsQfQdQjjU9zlYLG297dFMilC5dltgbnSvB6QN4QZHxb6QXamlyt7UOa.qm7VAnDPa0IYd3iC0UJ_u53L1PRbLZEaY32sCg81lO5DzWhJCBpxHoWUbkGMvnMMOF4sdmZRzZJmctPcOMCBiRAEgM0AitcpR_Dby52IHbpD1X9YUw_Z90",
    "dnt": "1",
    "priority": "u=1, i",
    "referer": "https://map.ukrainealarm.com/",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version": '"131.0.6778.86"',
    "sec-ch-ua-full-version-list": '"Google Chrome";v="131.0.6778.86", "Chromium";v="131.0.6778.86", "Not_A Brand";v="24.0.0.0"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '',
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"15.0.0"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
#response = requests.request("GET", alarm_url, data=payload, headers=headers)
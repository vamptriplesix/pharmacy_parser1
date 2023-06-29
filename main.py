import os.path
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from geopy import distance
from yandex_geocoder import Client
import pandas as pd
from PyQt5.QtWidgets import *
from subprocess import CREATE_NO_WINDOW
from selenium_stealth import stealth

# service = Service(ChromeDriverManager().install())
# # driver = webdriver.Chrome(service=service)
#
#
# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
#
# # options.add_argument("--headless")
#
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# driver = webdriver.Chrome(options=options, service=service)
#
# stealth(driver,
#         languages=["ru-RU", "ru"],
#         vendor="Google Inc.",
#         platform="Win64",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
#         )


CSV = 'meds.csv'

service = Service(ChromeDriverManager().install())
service.creation_flags = CREATE_NO_WINDOW
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options, service=service)



# def parse_1():
#
#     # urls
#     urls = ['https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/protivoallergicheskie_preparaty/',
#             'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/krov_i_krovoobrashchenie/',
#             'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/vitaminy_1/',
#             'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/ot_vrednykh_privychek/',
#             'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/preparaty_dlya_lecheniya_gemorroya/',
#             'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/dykhatelnaya_sistema/',
#             'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/pishchevaritelnaya_sistema/',
#             'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/organy_chuvstv_zrenie_slukh/',
#             'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/preparaty_povyshayushchie_immunitet/',
#             'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/antibakterialnye_preparaty/',
#             'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/mochepolovaya_sistema/',
#             'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/obezbolivayushchie_preparaty/',
#             'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/toniziruyushchie_preparaty/',
#             'https://apteka22.ru/catalog/prochie_tovary/sredstva_ot_nasekomykh/',
#             'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/dermatologicheskie_preparaty/',
#             'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/protivovirusnye_preparaty/',
#             'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/nervnaya_sistema/',
#             'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/serdechno_sosudistye_preparaty/',
#             'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/obmennye_protsessy/']
#
#     # categories
#     categories = ['Аллергия',
#                   'Кровь, кровообращение',
#                   'Витамины и микроэлементы',
#                   'Вредные привычки',
#                   'Геморрой',
#                   'Дыхательная система',
#                   'Пищеварительная система',
#                   'Заболевания глаз',
#                   'Иммунитет',
#                   'Инфекционные заболевания',
#                   'Мочеполовая система',
#                   'Обезболивающие',
#                   'Общеукрепляющие и тонизирующие',
#                   'От насекомых',
#                   'Поражения кожи',
#                   'Простуда, грипп',
#                   'Психические расстройства',
#                   'Сердце и сосуды',
#                   'Эндокринная система']
#
#     i = 0
#
#     urls = ['https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/ot_vrednykh_privychek/']
#
#     for url in urls:
#
#         driver.get(url)
#         if (urls[0] == url):
#             driver.find_element(By.XPATH, '//*[@id="a22_header"]/div[4]/div/div[1]/button').click()
#
#         meds = []
#
#         time.sleep(10)
#
#         num = driver.find_element(By.CLASS_NAME, "el-pager").find_elements(By.TAG_NAME, ('li'))
#
#         num = int(num[-1].text)
#
#         while num != 0:
#
#             blocks = driver.find_element(By.XPATH, '//*[@id="a22_app"]/div[1]/div[1]/div[3]/div[4]')
#             elements = blocks.find_elements(By.CLASS_NAME, "product-element")
#
#             for element in elements:
#                 title = element.find_element(By.CLASS_NAME, "info__name").find_element(By.TAG_NAME, "span").text
#                 title_url = element.find_element(By.CLASS_NAME, "info__name").find_element(By.TAG_NAME,
#                                                                                            "a").get_attribute("href")
#                 manufacturer = element.find_element(By.CLASS_NAME, "info__manufacturer").text
#                 price = element.find_element(By.CLASS_NAME, 'price__price').text.replace(' ', '')
#                 price = price[:-7]
#
#                 meds.append({
#                     'pharmacy': 'apteka22',
#                     'category': categories[i],
#                     'title': title,
#                     'manufacturer': manufacturer,
#                     'price': price,
#                     'url': title_url
#                 })
#
#             time.sleep(10)
#
#             driver.find_element(By.CLASS_NAME, "btn-next").click()
#
#             time.sleep(10)
#             print(num)
#
#             num -= 1
#
#         safe_in_csv(meds, CSV)
#
#         i += 1

# def parse_2():
#
#     urls = ['https://farmakopeika.ru/catalog/2613',
#             'https://farmakopeika.ru/catalog/2503',
#             'https://farmakopeika.ru/catalog/2455',
#             'https://farmakopeika.ru/catalog/2443',
#             'https://farmakopeika.ru/catalog/2450',
#             'https://farmakopeika.ru/catalog/2479',
#             'https://farmakopeika.ru/catalog/2539',
#             'https://farmakopeika.ru/catalog/2568',
#             'https://farmakopeika.ru/catalog/2536',
#             'https://farmakopeika.ru/catalog/2497',
#             'https://farmakopeika.ru/catalog/2441',
#             'https://farmakopeika.ru/catalog/2512',
#             'https://farmakopeika.ru/catalog/2545',
#             'https://farmakopeika.ru/catalog/2474',
#             'https://farmakopeika.ru/catalog/2337',
#             'https://farmakopeika.ru/catalog/2487',
#             'https://farmakopeika.ru/catalog/2555',
#             'https://farmakopeika.ru/catalog/2510',
#             'https://farmakopeika.ru/catalog/2566']
#
#     # categories
#     categories = ['Аллергия',
#                   'Кровь, кровообращение',
#                   'Витамины и микроэлементы',
#                   'Вредные привычки',
#                   'Геморрой',
#                   'Гинекология',
#                   'Дыхательная система',
#                   'Пищеварительная система',
#                   'Заболевания глаз',
#                   'Иммунитет',
#                   'Инфекционные заболевания',
#                   'Мочеполовая система',
#                   'Обезболивающие',
#                   'Общеукрепляющие и тонизирующие',
#                   'От насекомых',
#                   'Поражения кожи',
#                   'Психические расстройства',
#                   'Сердце и сосуды',
#                   'Успокаивающие']
#
#
#     i = 0
#
#     for url in urls:
#
#         driver.get(url)
#
#         meds = []
#
#         time.sleep(10)
#
#         num = driver.find_elements(By.CLASS_NAME, "pagination__item")
#
#         num = int(num[-1].text)
#
#         print(num)
#
#         p1 = 1
#         p2 = 6
#
#         print(i)
#
#         while num != 0:
#
#             blocks = driver.find_element(By.CLASS_NAME, 'subcat__content-box')
#             elements = blocks.find_elements(By.CLASS_NAME, "product__body")
#
#             for element in elements:
#                 title = element.find_element(By.CLASS_NAME, "product__title").text
#                 title_url = element.find_element(By.TAG_NAME, "a").get_attribute("href")
#                 price = element.find_element(By.CLASS_NAME, 'product__price-text').text.replace(' ', '').replace('.', '')
#                 price = price[2:-2]
#
#                 meds.append({
#                     'pharmacy': 'farmakopeika',
#                     'category': categories[i],
#                     'title': title,
#                     'manufacturer': '-',
#                     'price': price,
#                     'url': title_url
#                 })
#
#             time.sleep(10)
#
#             if p1 < 8 and num != 1:
#                 driver.find_element(By.XPATH, f'/html/body/div[2]/main/section[4]/div/div/div/div/a[{p1}]').click()
#                 p1 += 1
#             elif num <= 7 and p2 != 12 and num != 1:
#                 driver.find_element(By.XPATH, f'/html/body/div[2]/main/section[4]/div/div/div/div/a[{p2}]').click()
#                 p2 += 1
#             elif num > 7 and p1 >= 8:
#                 driver.find_element(By.XPATH, f'/html/body/div[2]/main/section[4]/div/div/div/div/a[6]').click()
#
#             time.sleep(10)
#
#             print('\t' + str(num))
#             num -= 1
#
#         safe_in_csv(meds, CSV)
#
#         i += 1

# def parse_3():
#
#     # urls
#     urls = ['https://melzdrav.ru/catalog/1354/',
#             'https://melzdrav.ru/catalog/1020/',
#             'https://melzdrav.ru/catalog/968/',
#             'https://melzdrav.ru/catalog/1369/',
#             'https://melzdrav.ru/catalog/1102/',
#             'https://melzdrav.ru/catalog/991/',
#             'https://melzdrav.ru/catalog/997/',
#             'https://melzdrav.ru/catalog/1440/',
#             'https://melzdrav.ru/catalog/1003/',
#             'https://melzdrav.ru/catalog/1006/',
#             'https://melzdrav.ru/catalog/966/',
#             'https://melzdrav.ru/catalog/1034/',
#             'https://melzdrav.ru/catalog/1361/',
#             'https://melzdrav.ru/catalog/986/',
#             'https://melzdrav.ru/catalog/1012/',
#             'https://melzdrav.ru/catalog/1091/',
#             'https://melzdrav.ru/catalog/1360/',
#             'https://melzdrav.ru/catalog/1097/',
#             'https://melzdrav.ru/catalog/1374/',
#             'https://melzdrav.ru/catalog/1108/']
#
#     # categories
#     categories = ['Аллергия',
#                   'Кровь, кровообращение',
#                   'Витамины и микроэлементы',
#                   'Вредные привычки',
#                   'Геморрой',
#                   'Гинекология',
#                   'Дыхательная система',
#                   'Пищеварительная система',
#                   'Заболевания глаз',
#                   'Иммунитет',
#                   'Инфекционные заболевания',
#                   'Мочеполовая система',
#                   'Обезболивающие',
#                   'Общеукрепляющие и тонизирующие',
#                   'Поражения кожи',
#                   'Простуда, грипп',
#                   'Психические расстройства',
#                   'Сердце и сосуды',
#                   'Успокаивающие',
#                   'Эндокринная система']
#
#     i = 0
#
#     for url in urls:
#
#         driver.get(url)
#
#         meds = []
#
#         time.sleep(5)
#
#         num = driver.find_element(By.CLASS_NAME, "styled-nav").find_elements(By.CLASS_NAME, 'styled-nav__item')
#
#         num = int(num[-1].text)
#
#         print(i)
#
#         while num != 0:
#
#             blocks = driver.find_element(By.CLASS_NAME, 'catalog-list')
#             elements = blocks.find_elements(By.CLASS_NAME, "catalog__item")
#
#             for element in elements:
#                 title = element.find_element(By.CLASS_NAME, "catalog__item__name").find_element(By.TAG_NAME, "a").text
#                 title_url = element.find_element(By.CLASS_NAME, "catalog__item__name").find_element(By.TAG_NAME,
#                                                                                                "a").get_attribute("href")
#                 manufacturer = element.find_element(By.CLASS_NAME, "catalog__item__producer").text
#                 try:
#                     price = element.find_element(By.CLASS_NAME, 'catalog__item__basket__price').text.replace(' ', '')
#                     price = price[2:-4]
#                 except:
#                     price = "Нет в наличии"
#
#                 meds.append({
#                     'pharmacy': 'melzdrav',
#                     'category': categories[i],
#                     'title': title,
#                     'manufacturer': manufacturer,
#                     'price': price,
#                     'url': title_url
#                 })
#
#             time.sleep(5)
#
#             if num != 1:
#                 driver.find_element(By.CSS_SELECTOR, '.styled-nav__arrow.right').click()
#
#             time.sleep(5)
#
#             print('\t' + str(num))
#             num -= 1
#
#         safe_in_csv(meds, CSV)
#
#         i += 1

def geo(user_location, apteka_number):

    apteka22 = ['пр-кт Строителей, д. 25, Барнаул',
                'тр.Павловский, 275, Барнаул',
                'ул Матросова, д.12, Барнаул',
                'ул Энтузиастов, 14а, Барнаул',
                'ул. 40 лет Октября, д.3а, Барнаул',
                'ул.Антона Петрова, 237б, Барнаул',
                'ул.Балтийская, 65, Барнаул',
                'ул.Германа Титова, д.20, Барнаул',
                'ул.Ленина, 10, Барнаул',
                'ул.Малахова, 142, Барнаул',
                'ул.Панфиловцев, 35, Барнаул',
                'ул.Попова, 139, Барнаул',
                'ул.Попова, 72, Барнаул',
                'ул.Северо - Западная, 230б, Барнаул',
                'ул.Советская, 5, Барнаул',
                'ул.Титова, 6, Барнаул',
                'ул.Эмилии Алексеевой, 10, Барнаул',
                'ул.Эмилии Алексеевой, 61, Барнаул',
                'ул.Ядринцева, 95, Барнаул',
                'ул.Молодежная, 56, Барнаул'
    ]
    farmakopeika = ['г Барнаул, пр-кт Ленина, д 22',
                    'г Барнаул, ул Бабуркина, д 5',
                    'г Барнаул, Социалистический пр-кт, д 61',
                    'г Барнаул, ул Балтийская, д 93',
                    'г Барнаул, рп Южный, ул Чайковского, д 29',
                    'г Барнаул, ул Попова, д 70Д',
                    'г Барнаул, ул Новгородская, д 26',
                    'г Барнаул, рп Южный, пр-кт Дзержинского, д 17',
                    'г Барнаул, ул Эмилии Алексеевой, д 76',
                    'г Барнаул, ул Малахова, д 44',
                    'г Барнаул, ул Антона Петрова, д 136',
                    'г Барнаул, ул Сергея Семенова, д 1',
                    'г Барнаул, пр-кт Ленина, д 113',
                    'г Барнаул, пр-кт Ленина, д 93',
                    'г Барнаул, пр-кт Ленина, д 71',
                    'г Барнаул, ул Воровского, д 108в',
                    'г Барнаул, Красноармейский пр-кт, д 101',
                    'г Барнаул, ул Антона Петрова, д 176',
                    'г Барнаул, ул Пушкина, д 74',
                    'г Барнаул, ул Попова, д 72',
                    'г Барнаул, ул Новосибирская/Фестивальная, д 11б/1б',
                    'г Барнаул, Павловский тракт, д 283',
                    'г Барнаул, ул Попова, д 48',
                    'г Барнаул, ул Германа Титова, д 21',
                    'г Барнаул, пр-кт Ленина, д 45А',
                    'г Барнаул, ул Партизанская, д 126',
                    'г Барнаул, ул Георгиева, д 57',
                    'г Барнаул, ул Малахова, д 55',
                    'г Барнаул, ул Новосибирская, д 24',
                    'г Барнаул, ул Советская, д 3',
                    'г Барнаул, ул Балтийская, д 12',
                    'г Барнаул, б-р 9 Января, д 92',
                    'г Барнаул, ул Шевченко, д 52А',
                    'г Барнаул, ул Георгия Исакова, д 174',
                    'г Барнаул, ул Шукшина, д 28',
                    'г Барнаул, рп Южный, ул Чайковского, д 24',
                    'г Барнаул, ул. Солнечная Поляна, д.94, корп.1',
                    'г Барнаул, пер Ядринцева, д 95',
                    'г Барнаул, ул Юрина, д 199',
                    'г Барнаул, ул Власихинская, д 103',
                    'г Барнаул, ул Сергея Семенова, д 14',
                    'г Барнаул, ул Балтийская, д 103',
                    'г Барнаул, пр-кт Ленина, д 155А',
                    'г Барнаул, ул Власихинская, д 97',
                    'г Барнаул, ул Взлетная, зд 43б',
                    'г Барнаул, ул Георгия Исакова, д 243',
                    'г Барнаул, поселок Научный Городок, д 39',
                    'г Барнаул, ул 280-летия Барнаула, зд 17',
                    'г Барнаул, ул Попова, д 76',
                    'г Барнаул, ул 50 лет СССР, д 4'
    ]
    melzdrav = ['Барнаул, 65 лет Победы ул, дом № 1',
                'Барнаул, 80 Гвардейской Дивизии ул, дом № 40',
                'Барнаул, Антона Петрова ул, дом № 213',
                'Барнаул, Антона Петрова ул, дом № 120',
                'Барнаул, Антона Петрова ул, дом № 219Б',
                'Барнаул, Антона Петрова ул, дом № 219Б',
                'Барнаул, Балтийская ул, дом № 96',
                'Барнаул, Балтийская ул, дом № 53',
                'Барнаул, Южный рп, Белинского ул, дом № 12',
                'Барнаул, Веры Кащеевой ул, дом № 12',
                'Барнаул, Взлетная ул, дом № 2л',
                'Барнаул, Власихинская ул, дом № 65',
                'Барнаул, Георгиева ул, дом № 35',
                'Барнаул, Георгия Исакова ул, дом № 215',
                'Барнаул, Гущина ул, дом № 154д',
                'Барнаул, Змеиногорский тракт, дом № 104П/1',
                'Барнаул, Змеиногорский тракт, дом № 104м/5',
                'Барнаул, Космонавтов пр-кт, дом № 6В',
                'Барнаул, Красноармейский пр-кт, дом № 108',
                'Барнаул, Красноармейский пр-кт, дом № 4',
                'Барнаул, Красноармейский пр-кт, дом № 58',
                'Барнаул, Лазурная ул, владение № 57',
                'Барнаул, Ленина пр-кт, дом № 55',
                'Барнаул, Ленина пр-кт, дом № 63А',
                'Барнаул, Ленина пр-кт, дом № 26',
                'Барнаул, Малахова ул, дом № 156',
                'Барнаул, Мало-Тобольская ул, дом № 23',
                'Барнаул, Матросова ул, дом № 5',
                'Барнаул, Маяковского ул, дом № 4Б',
                'Барнаул, Молодежная ул, дом № 111',
                'Барнаул, Новосибирская ул, здание № 11А',
                'Барнаул, Павловский тракт, дом № 251',
                'Барнаул, Павловский тракт, дом № 78',
                'Барнаул, Павловский тракт, дом № 223',
                'Барнаул, Павловский тракт, дом № 251в',
                'Барнаул, Павловский тракт, дом № 188',
                'Барнаул, Панфиловцев ул, дом № 22',
                'Барнаул, Панфиловцев ул, дом № 22',
                'Барнаул, Папанинцев ул, дом № 129А',
                'Барнаул, Партизанская ул, дом № 203',
                'Барнаул, Пионеров ул, дом № 7б',
                'Барнаул, Попова ул, дом № 24Б',
                'Барнаул, Попова ул, дом № 88',
                'Барнаул, Попова ул, дом № 86',
                'Барнаул, Пролетарская ул, дом № 160',
                'Барнаул, Северо-Западная ул, дом № 58',
                'Барнаул, Сергея Ускова ул, дом № 3',
                'Барнаул, Смирнова ул, дом № 92',
                'Барнаул, Советской Армии ул, дом № 36А',
                'Барнаул, Солнечная Поляна ул, дом № 29',
                'Барнаул, Южный рп, Чайковского ул, дом № 15',
                'Барнаул, Челюскинцев ул, дом № 69',
                'Барнаул, Чкалова ул, дом № 57',
                'Барнаул, Чудненко ул, дом № 110',
                'Барнаул, Шумакова ул, дом № 50',
                'Барнаул, Шумакова ул, дом № 46',
                'Барнаул, Энергетиков пр-кт, дом № 4',
                'Барнаул, Энтузиастов ул, дом № 13',
                'Барнаул, Юрина ул, дом № 118'
    ]

    apteka_data = []

    n = 0

    # 0 - 19
    # 20 - 69
    # 70 - 128

    try:
        if apteka_number == 0:
            apteka_data.extend(apteka22)
            apteka_data.extend(farmakopeika)
            apteka_data.extend(melzdrav)
        elif apteka_number == 1:
            apteka_data.extend(apteka22)
        elif apteka_number == 2:
            apteka_data.extend(farmakopeika)
        elif apteka_number == 3:
            apteka_data.extend(melzdrav)

        client = Client("91d7262c-bf73-407f-adaf-054acad906e2")

        user_coordinates = client.coordinates(user_location)

        for apteka in apteka_data:

            apteka_coordinates = client.coordinates(apteka)
            apteka_address = client.address(apteka_coordinates[0], apteka_coordinates[1])


            if apteka_data[0] == apteka:
                nearby_apteka_coordinates = apteka_coordinates
                nearby_apteka_address = apteka_address
                n = apteka_data.index(apteka)
            elif distance.distance(user_coordinates, nearby_apteka_coordinates).km > distance.distance(user_coordinates,
                                                                                                       apteka_coordinates).km:
                nearby_apteka_coordinates = apteka_coordinates
                nearby_apteka_address = apteka_address
                n = apteka_data.index(apteka)

        coordinates = 'Расстояние: ' + str(
            round(distance.distance(user_coordinates, nearby_apteka_coordinates).km, 2)) + ' км'

        if n >= 0 and n <= 19:
            apteka_name = 'Аптека22: '
        elif n >= 20 and n <= 69:
            apteka_name = 'Фармакопейка: '
        elif n >= 70 and n <= 128:
            apteka_name = 'Мелодия здоровья: '

        return nearby_apteka_address, coordinates, apteka_name
    except:
        nearby_apteka_address = "Произошла ошибка"
        coordinates = "Попробуйте снова"
        apteka_name = " "
        return nearby_apteka_address, coordinates, apteka_name

def safe_in_csv(items, path):

    if os.path.exists(CSV) == False:
        with open(path, 'w', newline='',  encoding="utf-8-sig") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Название аптеки', 'Категория', 'Название товара','Цена (руб.)', 'Производитель', 'Ссылка на товар'])
            for item in items:
                writer.writerow([item['pharmacy'], item['category'], item['title'], item['price'], item['manufacturer'], item['url']])

    elif os.path.exists(CSV) == True:
        with open(path, 'a', newline='',  encoding="utf-8-sig") as file:
            writer = csv.writer(file, delimiter=';')
            for item in items:
                writer.writerow([item['pharmacy'], item['category'], item['title'], item['price'], item['manufacturer'], item['url']])


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import resources


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 800))
        MainWindow.setStyleSheet("background-color: #eef2ef;")
        MainWindow.setIconSize(QtCore.QSize(50, 50))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget QWidget {\n"
                                    "    background-color: #eef2ef\n"
                                    "}\n"
                                    "QTabWidget::pane {\n"
                                    "}\n"
                                    "QTabWidget:tab-bar{\n"
                                    "    alignment: centr;\n"
                                    "}\n"
                                    "QTabBar:tab{\n"
                                    "    border-radius: 10px;\n"
                                    "    padding: 8.5px 50px;\n"
                                    "    color: white;\n"
                                    "    background: #86bb9a;\n"
                                    "    margin: 10px;\n"
                                    "    width:180;\n"
                                    "    height:60;    \n"
                                    "}\n"
                                    "QTabBar:tab:selected{\n"
                                    "    background: #659577;\n"
                                    "}\n"
                                    "QTabBar:tab:hover{\n"
                                    "    background: #659577;\n"
                                    "}")
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.main = QtWidgets.QWidget()
        self.main.setStyleSheet("")
        self.main.setObjectName("main")
        self.label_9 = QtWidgets.QLabel(self.main)
        self.label_9.setGeometry(QtCore.QRect(19, 0, 971, 671))
        self.label_9.setStyleSheet("border-radius: 10px;\n"
                                    "padding: 8.5px 200px;\n"
                                    "color: white;\n"
                                    "background: rgba(134, 187,154, 200);\n"
                                    "margin: 10px;\n"
                                    "width:160;\n"
                                    "height:60;")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.pushButton_3 = QtWidgets.QPushButton(self.main)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 10, 200, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "    border-radius: 10px;\n"
                                        "    padding: 8.5px 15px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "    margin: 10px;\n"
                                        "    width:160;\n"
                                        "    height:60;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/magnifier.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(self.main)
        self.tableWidget.setGeometry(QtCore.QRect(320, 80, 641, 551))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.comboBox_2 = QtWidgets.QComboBox(self.main)
        self.comboBox_2.setGeometry(QtCore.QRect(320, 20, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("QComboBox{\n"
                                        "    border: 0px;\n"
                                        "    border-radius: 15px;\n"
                                        "    padding: 4.5px 20px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "    margin: 10px;\n"
                                        "    width:160;\n"
                                        "    height:60;\n"
                                        "}\n"
                                        "QComboBox::hover{\n"
                                        "    background: #659577;\n"
                                        "}\n"
                                        "QComboBox::drop-down{\n"
                                        "    border: 0px;\n"
                                        "}\n"
                                        "QComboBox::down-arrow{\n"
                                        "    image: url(:/icons/icons/arrow.png);\n"
                                        "    width: 20 px;\n"
                                        "    height: 20 px;\n"
                                        "    margin-right: 35px;\n"
                                        "}\n"
                                        "QComboBox QListView{\n"
                                        "    border: 0px;\n"
                                        "    border-radius: 5px;\n"
                                        "    padding: 8.5px 20px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "    selection-background-color: #659577;\n"
                                        "    margin: 10px;\n"
                                        "    width:160;\n"
                                        "    height:60;\n"
                                        "}\n"
                                        "\n"
                                        "")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setDuplicatesEnabled(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.toolBox = QtWidgets.QToolBox(self.main)
        self.toolBox.setGeometry(QtCore.QRect(40, 20, 271, 611))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet("QToolBox::tab {\n"
                                    "        background: rgba(134, 187,154, 200);    \n"
                                    "     color: white;\n"
                                    " }\n"
                                    "\n"
                                    "QToolBox::tab:hover {\n"
                                    "       background: #659577; \n"
                                    " }\n"
                                    "\n"
                                    " QToolBox::tab:selected { \n"
                                    "    color: white;\n"
                                    "    background: #659577;  \n"
                                    " }\n"
                                    "\n"
                                    "QWidget#page\n"
                                    "{\n"
                                    "  background: rgba(134, 187,154, 200);\n"
                                    "}\n"
                                    "QWidget#page_2\n"
                                    "{\n"
                                    "  background: rgba(134, 187,154, 200);\n"
                                    "}\n"
                                    "QWidget#page_3\n"
                                    "{\n"
                                    "  background: rgba(134, 187,154, 200);\n"
                                    "}\n"
                                    "")
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 271, 533))
        self.page.setObjectName("page")
        self.verticalWidget = QtWidgets.QWidget(self.page)
        self.verticalWidget.setGeometry(QtCore.QRect(0, 0, 271, 531))
        self.verticalWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.verticalWidget.setStyleSheet("background: rgba(134, 187,154, 200);")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_27 = QtWidgets.QCheckBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_27.setFont(font)
        self.checkBox_27.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_27.setObjectName("checkBox_27")
        self.verticalLayout.addWidget(self.checkBox_27)
        self.checkBox_29 = QtWidgets.QCheckBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_29.setFont(font)
        self.checkBox_29.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_29.setObjectName("checkBox_29")
        self.verticalLayout.addWidget(self.checkBox_29)
        self.checkBox_25 = QtWidgets.QCheckBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_25.setFont(font)
        self.checkBox_25.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_25.setObjectName("checkBox_25")
        self.verticalLayout.addWidget(self.checkBox_25)
        self.checkBox_30 = QtWidgets.QCheckBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_30.setFont(font)
        self.checkBox_30.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_30.setObjectName("checkBox_30")
        self.verticalLayout.addWidget(self.checkBox_30)
        self.checkBox_31 = QtWidgets.QCheckBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_31.setFont(font)
        self.checkBox_31.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_31.setObjectName("checkBox_31")
        self.verticalLayout.addWidget(self.checkBox_31)
        self.checkBox_32 = QtWidgets.QCheckBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_32.setFont(font)
        self.checkBox_32.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_32.setObjectName("checkBox_32")
        self.verticalLayout.addWidget(self.checkBox_32)
        self.checkBox_44 = QtWidgets.QCheckBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_44.setFont(font)
        self.checkBox_44.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_44.setObjectName("checkBox_44")
        self.verticalLayout.addWidget(self.checkBox_44)
        self.checkBox_43 = QtWidgets.QCheckBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_43.setFont(font)
        self.checkBox_43.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_43.setObjectName("checkBox_43")
        self.verticalLayout.addWidget(self.checkBox_43)
        self.checkBox_41 = QtWidgets.QCheckBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_41.setFont(font)
        self.checkBox_41.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_41.setObjectName("checkBox_41")
        self.verticalLayout.addWidget(self.checkBox_41)
        self.checkBox_42 = QtWidgets.QCheckBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_42.setFont(font)
        self.checkBox_42.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_42.setObjectName("checkBox_42")
        self.verticalLayout.addWidget(self.checkBox_42)
        self.checkBox_33 = QtWidgets.QCheckBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_33.setFont(font)
        self.checkBox_33.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_33.setObjectName("checkBox_33")
        self.verticalLayout.addWidget(self.checkBox_33)
        self.checkBox_35 = QtWidgets.QCheckBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_35.setFont(font)
        self.checkBox_35.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_35.setObjectName("checkBox_35")
        self.verticalLayout.addWidget(self.checkBox_35)
        self.checkBox_34 = QtWidgets.QCheckBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_34.setFont(font)
        self.checkBox_34.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_34.setObjectName("checkBox_34")
        self.verticalLayout.addWidget(self.checkBox_34)
        self.checkBox_37 = QtWidgets.QCheckBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_37.setFont(font)
        self.checkBox_37.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_37.setObjectName("checkBox_37")
        self.verticalLayout.addWidget(self.checkBox_37)
        self.checkBox_39 = QtWidgets.QCheckBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_39.setFont(font)
        self.checkBox_39.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_39.setObjectName("checkBox_39")
        self.verticalLayout.addWidget(self.checkBox_39)
        self.checkBox_38 = QtWidgets.QCheckBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_38.setFont(font)
        self.checkBox_38.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_38.setObjectName("checkBox_38")
        self.verticalLayout.addWidget(self.checkBox_38)
        self.checkBox_36 = QtWidgets.QCheckBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_36.setFont(font)
        self.checkBox_36.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_36.setObjectName("checkBox_36")
        self.verticalLayout.addWidget(self.checkBox_36)
        self.checkBox_40 = QtWidgets.QCheckBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_40.setFont(font)
        self.checkBox_40.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_40.setObjectName("checkBox_40")
        self.verticalLayout.addWidget(self.checkBox_40)
        self.checkBox_26 = QtWidgets.QCheckBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_26.setFont(font)
        self.checkBox_26.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_26.setObjectName("checkBox_26")
        self.verticalLayout.addWidget(self.checkBox_26)
        self.checkBox_28 = QtWidgets.QCheckBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_28.setFont(font)
        self.checkBox_28.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_28.setObjectName("checkBox_28")
        self.verticalLayout.addWidget(self.checkBox_28)
        self.checkBox_24 = QtWidgets.QCheckBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_24.setFont(font)
        self.checkBox_24.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_24.setObjectName("checkBox_24")
        self.verticalLayout.addWidget(self.checkBox_24)
        self.checkBox_23 = QtWidgets.QCheckBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_23.setFont(font)
        self.checkBox_23.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_23.setObjectName("checkBox_23")
        self.verticalLayout.addWidget(self.checkBox_23)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 271, 533))
        self.page_2.setObjectName("page_2")
        self.checkBox_47 = QtWidgets.QCheckBox(self.page_2)
        self.checkBox_47.setGeometry(QtCore.QRect(0, 10, 269, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_47.setFont(font)
        self.checkBox_47.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_47.setObjectName("checkBox_47")
        self.checkBox_48 = QtWidgets.QCheckBox(self.page_2)
        self.checkBox_48.setGeometry(QtCore.QRect(0, 50, 269, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_48.setFont(font)
        self.checkBox_48.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_48.setObjectName("checkBox_48")
        self.checkBox_49 = QtWidgets.QCheckBox(self.page_2)
        self.checkBox_49.setGeometry(QtCore.QRect(0, 90, 269, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_49.setFont(font)
        self.checkBox_49.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_49.setObjectName("checkBox_49")
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 271, 533))
        self.page_3.setObjectName("page_3")
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("border-radius: 10px;\n"
                                    "padding: 8.5px 15px;\n"
                                    "color: white;\n"
                                    "background: rgba(134, 187,154, 200);\n"
                                    "margin: 10px;\n"
                                    "width:160;\n"
                                    "height:60;")
        self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_10.setScaledContents(False)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.page_3)
        self.label_11.setGeometry(QtCore.QRect(0, 110, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border-radius: 10px;\n"
                                    "padding: 8.5px 15px;\n"
                                    "color: white;\n"
                                    "background: rgba(134, 187,154, 200);\n"
                                    "margin: 10px;\n"
                                    "width:160;\n"
                                    "height:60;")
        self.label_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_11.setScaledContents(False)
        self.label_11.setObjectName("label_11")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 50, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius: 10px;\n"
                                        "padding: 8.5px 10px;\n"
                                        "background: white;\n"
                                        "margin: 10px;\n"
                                        "width:160;\n"
                                        "height:60;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(0, 160, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-radius: 10px;\n"
                                        "padding: 8.5px 10px;\n"
                                        "background: white;\n"
                                        "margin: 10px;\n"
                                        "width:160;\n"
                                        "height:60;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(0, 260, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border-radius: 10px;\n"
                                        "padding: 8.5px 10px;\n"
                                        "background: white;\n"
                                        "margin: 10px;\n"
                                        "width:160;\n"
                                        "height:60;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(0, 370, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border-radius: 10px;\n"
                                        "padding: 8.5px 10px;\n"
                                        "background: white;\n"
                                        "margin: 10px;\n"
                                        "width:160;\n"
                                        "height:60;")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_13 = QtWidgets.QLabel(self.page_3)
        self.label_13.setGeometry(QtCore.QRect(0, 220, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("border-radius: 10px;\n"
                                    "padding: 8.5px 15px;\n"
                                    "color: white;\n"
                                    "background: rgba(134, 187,154, 200);\n"
                                    "margin: 10px;\n"
                                    "width:160;\n"
                                    "height:60;")
        self.label_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_13.setScaledContents(False)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page_3)
        self.label_14.setGeometry(QtCore.QRect(0, 320, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("border-radius: 10px;\n"
                                    "padding: 8.5px 15px;\n"
                                    "color: white;\n"
                                    "background: rgba(134, 187,154, 200);\n"
                                    "margin: 10px;\n"
                                    "width:160;\n"
                                    "height:60;")
        self.label_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_14.setScaledContents(False)
        self.label_14.setObjectName("label_14")
        self.toolBox.addItem(self.page_3, "")
        self.pushButton_4 = QtWidgets.QPushButton(self.main)
        self.pushButton_4.setGeometry(QtCore.QRect(760, 10, 200, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
                                        "    border-radius: 10px;\n"
                                        "    padding: 8.5px 15px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "    margin: 10px;\n"
                                        "    width:160;\n"
                                        "    height:60;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.main, "")
        self.geo = QtWidgets.QWidget()
        self.geo.setObjectName("geo")
        self.label_2 = QtWidgets.QLabel(self.geo)
        self.label_2.setGeometry(QtCore.QRect(50, 0, 900, 671))
        self.label_2.setStyleSheet("border-radius: 10px;\n"
                                    "padding: 8.5px 200px;\n"
                                    "color: white;\n"
                                    "background: rgba(134, 187,154, 200);\n"
                                    "margin: 10px;\n"
                                    "width:160;\n"
                                    "height:60;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.geo)
        self.label_3.setGeometry(QtCore.QRect(150, 20, 700, 71))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-radius: 10px;\n"
                                    "padding: 8.5px 200px;\n"
                                    "color: white;\n"
                                    "background: rgba(134, 187,154, 200);\n"
                                    "margin: 10px;\n"
                                    "width:160;\n"
                                    "height:60;")
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.geo)
        self.label_4.setGeometry(QtCore.QRect(150, 80, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border-radius: 10px;\n"
                                    "padding: 8.5px 15px;\n"
                                    "color: white;\n"
                                    "background: rgba(134, 187,154, 200);\n"
                                    "margin: 10px;\n"
                                    "width:160;\n"
                                    "height:60;")
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.geo)
        self.lineEdit.setGeometry(QtCore.QRect(150, 140, 700, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius: 10px;\n"
                                    "padding: 8.5px 10px;\n"
                                    "background: white;\n"
                                    "margin: 10px;\n"
                                    "width:160;\n"
                                    "height:60;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.geo)
        self.comboBox.setGeometry(QtCore.QRect(150, 200, 701, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox{\n"
                                    "    border: 0px;\n"
                                    "    border-radius: 15px;\n"
                                    "    padding: 8.5px 20px;\n"
                                    "    color: white;\n"
                                    "    background: rgba(134, 187,154, 200);\n"
                                    "    margin: 10px;\n"
                                    "    width:160;\n"
                                    "    height:60;\n"
                                    "}\n"
                                    "QComboBox::hover{\n"
                                    "    background: #659577;\n"
                                    "}\n"
                                    "QComboBox::drop-down{\n"
                                    "    border: 0px;\n"
                                    "}\n"
                                    "QComboBox::down-arrow{\n"
                                    "    image: url(:/icons/icons/arrow.png);\n"
                                    "    width: 20 px;\n"
                                    "    height: 20 px;\n"
                                    "    margin-right: 35px;\n"
                                    "}\n"
                                    "QComboBox QListView{\n"
                                    "    border: 0px;\n"
                                    "    border-radius: 5px;\n"
                                    "    padding: 8.5px 20px;\n"
                                    "    color: white;\n"
                                    "    background: rgba(134, 187,154, 200);\n"
                                    "    selection-background-color: #659577;\n"
                                    "    margin: 10px;\n"
                                    "    width:160;\n"
                                    "    height:60;\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.comboBox.setEditable(False)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.geo)
        self.pushButton.setGeometry(QtCore.QRect(400, 550, 200, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                        "    border-radius: 10px;\n"
                                        "    padding: 8.5px 15px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "    margin: 10px;\n"
                                        "    width:160;\n"
                                        "    height:60;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.geo)
        self.label_5.setGeometry(QtCore.QRect(150, 300, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border-radius: 10px;\n"
                                    "padding: 8.5px 15px;\n"
                                    "color: white;\n"
                                    "background: rgba(134, 187,154, 200);\n"
                                    "margin: 10px;\n"
                                    "width:160;\n"
                                    "height:60;")
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.geo)
        self.label_6.setGeometry(QtCore.QRect(150, 360, 700, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border-radius: 10px;\n"
                                    "padding: 8.5px 20px;\n"
                                    "color: white;\n"
                                    "background: rgba(134, 187,154, 200);\n"
                                    "margin: 10px;\n"
                                    "width:160;\n"
                                    "height:60;")
        self.label_6.setText("")
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setScaledContents(False)
        self.label_6.setObjectName("label_6")
        self.label_12 = QtWidgets.QLabel(self.geo)
        self.label_12.setGeometry(QtCore.QRect(150, 420, 700, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border-radius: 10px;\n"
                                    "padding: 8.5px 20px;\n"
                                    "color: white;\n"
                                    "background: rgba(134, 187,154, 200);\n"
                                    "margin: 10px;\n"
                                    "width:160;\n"
                                    "height:60;")
        self.label_12.setText("")
        self.label_12.setTextFormat(QtCore.Qt.AutoText)
        self.label_12.setScaledContents(False)
        self.label_12.setObjectName("label_12")
        self.tabWidget.addTab(self.geo, "")
        self.parser = QtWidgets.QWidget()
        self.parser.setObjectName("parser")
        self.label_7 = QtWidgets.QLabel(self.parser)
        self.label_7.setGeometry(QtCore.QRect(50, 0, 900, 671))
        self.label_7.setStyleSheet("border-radius: 10px;\n"
                                    "padding: 8.5px 200px;\n"
                                    "color: white;\n"
                                    "background: rgba(134, 187,154, 200);\n"
                                    "margin: 10px;\n"
                                    "width:160;\n"
                                    "height:60;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.progressBar = QtWidgets.QProgressBar(self.parser)
        self.progressBar.setGeometry(QtCore.QRect(250, 430, 521, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar{\n"
                                        "    border-radius: 10px;\n"
                                        "    color: #141414\n"
                                        "}\n"
                                        "QProgressBar::chunk{\n"
                                        "    border-radius: 10px;\n"
                                        "    background: #659577;\n"
                                        "}\n"
                                        "    ")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.checkBox = QtWidgets.QCheckBox(self.parser)
        self.checkBox.setGeometry(QtCore.QRect(370, 90, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("QCheckBox{\n"
                                    "    border-radius: 10px;\n"
                                    "    padding: 8.5px 15px;\n"
                                    "    color: white;\n"
                                    "    background: rgba(134, 187,154, 200);\n"
                                    "    margin: 10px;\n"
                                    "    width:160;\n"
                                    "    height:60;\n"
                                    "}\n"
                                    "QCheckBox:hover{\n"
                                    "    background: #659577;\n"
                                    "}\n"
                                    "")
        self.checkBox.setObjectName("checkBox")
        self.label_8 = QtWidgets.QLabel(self.parser)
        self.label_8.setGeometry(QtCore.QRect(150, 20, 700, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border-radius: 10px;\n"
                                    "    padding: 8.5px 200px;\n"
                                    "    color: white;\n"
                                    "    background: rgba(134, 187,154, 200);\n"
                                    "    margin: 10px;\n"
                                    "    width:160;\n"
                                    "    height:60;")
        self.label_8.setScaledContents(False)
        self.label_8.setObjectName("label_8")
        self.checkBox_2 = QtWidgets.QCheckBox(self.parser)
        self.checkBox_2.setGeometry(QtCore.QRect(370, 150, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    padding: 8.5px 15px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "    margin: 10px;\n"
                                        "    width:160;\n"
                                        "    height:60;\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.parser)
        self.checkBox_3.setGeometry(QtCore.QRect(370, 210, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setStyleSheet("QCheckBox{\n"
                                        "    border-radius: 10px;\n"
                                        "    padding: 8.5px 15px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "    margin: 10px;\n"
                                        "    width:160;\n"
                                        "    height:60;\n"
                                        "}\n"
                                        "QCheckBox:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        self.checkBox_3.setObjectName("checkBox_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.parser)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 330, 200, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    border-radius: 10px;\n"
                                        "    padding: 8.5px 15px;\n"
                                        "    color: white;\n"
                                        "    background: rgba(134, 187,154, 200);\n"
                                        "    margin: 10px;\n"
                                        "    width:160;\n"
                                        "    height:60;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background: #659577;\n"
                                        "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/parsing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.parser, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.toolBox.setCurrentIndex(2)
        self.toolBox.layout().setSpacing(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_function()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pharmacy Parser"))
        self.pushButton_3.setText(_translate("MainWindow", " Поиск"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Фильтр"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Сначала дорогие"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Сначала недорогие"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "От А до Я"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "От Я до А"))
        self.checkBox_27.setText(_translate("MainWindow", "Аллергия"))
        self.checkBox_29.setText(_translate("MainWindow", "Кровь, кровообращение"))
        self.checkBox_25.setText(_translate("MainWindow", "Витамины и микроэлементы"))
        self.checkBox_30.setText(_translate("MainWindow", "Вредные привычки"))
        self.checkBox_31.setText(_translate("MainWindow", "Гинекология"))
        self.checkBox_32.setText(_translate("MainWindow", "Геморрой"))
        self.checkBox_44.setText(_translate("MainWindow", "Дыхательная система"))
        self.checkBox_43.setText(_translate("MainWindow", "Пищеварительная система"))
        self.checkBox_41.setText(_translate("MainWindow", "Заболевания глаз"))
        self.checkBox_42.setText(_translate("MainWindow", "Иммунитет"))
        self.checkBox_33.setText(_translate("MainWindow", "Инфекционные заболевания"))
        self.checkBox_35.setText(_translate("MainWindow", "Мочеполовая система"))
        self.checkBox_34.setText(_translate("MainWindow", "Обезболивающие"))
        self.checkBox_37.setText(_translate("MainWindow", "Общеукрепляющие и тонизирующие"))
        self.checkBox_39.setText(_translate("MainWindow", "От насекомых"))
        self.checkBox_38.setText(_translate("MainWindow", "Поражения кожи"))
        self.checkBox_36.setText(_translate("MainWindow", "Простуда, грипп"))
        self.checkBox_40.setText(_translate("MainWindow", "Психические расстройства"))
        self.checkBox_26.setText(_translate("MainWindow", "Сердце и сосуды"))
        self.checkBox_28.setText(_translate("MainWindow", "Эндокринная система"))
        self.checkBox_24.setText(_translate("MainWindow", "Простуда, грипп"))
        self.checkBox_23.setText(_translate("MainWindow", "Успокаивающие"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Категория"))
        self.checkBox_47.setText(_translate("MainWindow", " Аптека 22"))
        self.checkBox_48.setText(_translate("MainWindow", " Фармакопейка"))
        self.checkBox_49.setText(_translate("MainWindow", " Мелодия здоровья"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Аптека"))
        self.label_10.setText(_translate("MainWindow", "Название:"))
        self.label_11.setText(_translate("MainWindow", "Производитель:"))
        self.label_13.setText(_translate("MainWindow", "Цена от:"))
        self.label_14.setText(_translate("MainWindow", "Цена до:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Название, цена, производитель"))
        self.pushButton_4.setText(_translate("MainWindow", " Загрузить данные"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), _translate("MainWindow", "Каталог"))
        self.label_3.setText(_translate("MainWindow", "Поиск ближайшей аптеки"))
        self.label_4.setText(_translate("MainWindow", "Введите ваш адрес:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Все аптеки"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Аптека22"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Фармакопейка"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Мелодия здоровья"))
        self.pushButton.setText(_translate("MainWindow", " Поиск"))
        self.label_5.setText(_translate("MainWindow", "Ближайшая аптека:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.geo), _translate("MainWindow", "Поиск аптеки"))
        self.checkBox.setText(_translate("MainWindow", " Аптека22"))
        self.label_8.setText(_translate("MainWindow", "Какие сайты парсить?"))
        self.checkBox_2.setText(_translate("MainWindow", " Фармакопейка"))
        self.checkBox_3.setText(_translate("MainWindow", " Мелодия здоровья"))
        self.pushButton_2.setText(_translate("MainWindow", "  Начать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.parser), _translate("MainWindow", "Парсер"))


    def add_function(self):
        self.pushButton.clicked.connect(self.search_geo)
        self.pushButton_2.clicked.connect(self.parser_selection)
        self.pushButton_4.clicked.connect(self.download_csv)
        self.pushButton_3.clicked.connect(self.sorting_data)


    def search_geo(self):
        _translate = QtCore.QCoreApplication.translate

        user_address = self.lineEdit.text()

        if self.comboBox.currentIndex() == 0:

            address, distance, n = geo(user_address, 0)
            address = n + address

        elif self.comboBox.currentIndex() == 1:

            address, distance, n = geo(user_address, 1)

        elif self.comboBox.currentIndex() == 2:

            address, distance, n = geo(user_address, 2)

        elif self.comboBox.currentIndex() == 3:

            address, distance, n = geo(user_address, 3)

        address = address.replace('Россия, Алтайский край, ', '')

        self.label_6.setText(_translate("MainWindow", address))
        self.label_12.setText(_translate("MainWindow", distance))

    def parse_1(self):

        urls = [
            'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/protivoallergicheskie_preparaty/',
            'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/krov_i_krovoobrashchenie/',
            'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/vitaminy_1/',
            'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/ot_vrednykh_privychek/',
            'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/preparaty_dlya_lecheniya_gemorroya/',
            'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/dykhatelnaya_sistema/',
            'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/pishchevaritelnaya_sistema/',
            'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/organy_chuvstv_zrenie_slukh/',
            'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/preparaty_povyshayushchie_immunitet/',
            'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/antibakterialnye_preparaty/',
            'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/mochepolovaya_sistema/',
            'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/obezbolivayushchie_preparaty/',
            'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/toniziruyushchie_preparaty/',
            'https://apteka22.ru/catalog/prochie_tovary/sredstva_ot_nasekomykh/',
            'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/dermatologicheskie_preparaty/',
            'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/protivovirusnye_preparaty/',
            'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/nervnaya_sistema/',
            'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/serdechno_sosudistye_preparaty/',
            'https://apteka22.ru/catalog/lekarstvennye_sredstva_i_bady/lekarstvennye_sredstva/obmennye_protsessy/']

        categories = ['Аллергия',
                      'Кровь, кровообращение',
                      'Витамины и микроэлементы',
                      'Вредные привычки',
                      'Геморрой',
                      'Дыхательная система',
                      'Пищеварительная система',
                      'Заболевания глаз',
                      'Иммунитет',
                      'Инфекционные заболевания',
                      'Мочеполовая система',
                      'Обезболивающие',
                      'Общеукрепляющие и тонизирующие',
                      'От насекомых',
                      'Поражения кожи',
                      'Простуда, грипп',
                      'Психические расстройства',
                      'Сердце и сосуды',
                      'Эндокринная система']

        i = 0

        m = 100
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(m)

        n = len(urls)
        t = m/n
        n = 0


        for url in urls:

            n += t
            self.progressBar.setValue(int(n))

            driver.get(url)

            if (urls[0] == url):
                driver.find_element(By.XPATH, '//*[@id="a22_header"]/div[4]/div/div[1]/button').click()

            meds = []

            time.sleep(10)

            num = driver.find_element(By.CLASS_NAME, "el-pager").find_elements(By.TAG_NAME, ('li'))

            num = int(num[-1].text)


            while num != 0:

                blocks = driver.find_element(By.XPATH, '//*[@id="a22_app"]/div[1]/div[1]/div[3]/div[4]')
                elements = blocks.find_elements(By.CLASS_NAME, "product-element")

                for element in elements:
                    title = element.find_element(By.CLASS_NAME, "info__name").find_element(By.TAG_NAME, "span").text
                    title_url = element.find_element(By.CLASS_NAME, "info__name").find_element(By.TAG_NAME,
                                                                                               "a").get_attribute(
                        "href")
                    manufacturer = element.find_element(By.CLASS_NAME, "info__manufacturer").text
                    price = element.find_element(By.CLASS_NAME, 'price__price').text.replace(' ', '')
                    price = price[:-7]

                    meds.append({
                        'pharmacy': 'apteka22',
                        'category': categories[i],
                        'title': title,
                        'manufacturer': manufacturer,
                        'price': price,
                        'url': title_url
                    })

                time.sleep(10)

                driver.find_element(By.CLASS_NAME, "btn-next").click()

                time.sleep(10)
                # print(num)

                num -= 1

            safe_in_csv(meds, CSV)

            i += 1

    def parse_2(self):

        urls = ['https://farmakopeika.ru/catalog/2613',
                'https://farmakopeika.ru/catalog/2503',
                'https://farmakopeika.ru/catalog/2455',
                'https://farmakopeika.ru/catalog/2443',
                'https://farmakopeika.ru/catalog/2450',
                'https://farmakopeika.ru/catalog/2479',
                'https://farmakopeika.ru/catalog/2539',
                'https://farmakopeika.ru/catalog/2568',
                'https://farmakopeika.ru/catalog/2536',
                'https://farmakopeika.ru/catalog/2497',
                'https://farmakopeika.ru/catalog/2441',
                'https://farmakopeika.ru/catalog/2512',
                'https://farmakopeika.ru/catalog/2545',
                'https://farmakopeika.ru/catalog/2474',
                'https://farmakopeika.ru/catalog/2337',
                'https://farmakopeika.ru/catalog/2487',
                'https://farmakopeika.ru/catalog/2555',
                'https://farmakopeika.ru/catalog/2510',
                'https://farmakopeika.ru/catalog/2566']

        # categories
        categories = ['Аллергия',
                      'Кровь, кровообращение',
                      'Витамины и микроэлементы',
                      'Вредные привычки',
                      'Геморрой',
                      'Гинекология',
                      'Дыхательная система',
                      'Пищеварительная система',
                      'Заболевания глаз',
                      'Иммунитет',
                      'Инфекционные заболевания',
                      'Мочеполовая система',
                      'Обезболивающие',
                      'Общеукрепляющие и тонизирующие',
                      'От насекомых',
                      'Поражения кожи',
                      'Психические расстройства',
                      'Сердце и сосуды',
                      'Успокаивающие']

        i = 0

        m = 100
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(m)

        n = len(urls)
        t = m / n
        n = 0

        for url in urls:

            n += t
            self.progressBar.setValue(int(n))

            driver.get(url)

            meds = []

            time.sleep(10)

            num = driver.find_elements(By.CLASS_NAME, "pagination__item")

            num = int(num[-1].text)

            # print(num)

            p1 = 1
            p2 = 6

            # print(i)

            while num != 0:

                blocks = driver.find_element(By.CLASS_NAME, 'subcat__content-box')
                elements = blocks.find_elements(By.CLASS_NAME, "product__body")

                for element in elements:
                    title = element.find_element(By.CLASS_NAME, "product__title").text
                    title_url = element.find_element(By.TAG_NAME, "a").get_attribute("href")
                    price = element.find_element(By.CLASS_NAME, 'product__price-text').text.replace(' ', '').replace(
                        '.', '')
                    price = price[2:-2]

                    meds.append({
                        'pharmacy': 'farmakopeika',
                        'category': categories[i],
                        'title': title,
                        'manufacturer': '-',
                        'price': price,
                        'url': title_url
                    })

                time.sleep(10)

                if p1 < 8 and num != 1:
                    driver.find_element(By.XPATH, f'/html/body/div[2]/main/section[4]/div/div/div/div/a[{p1}]').click()
                    p1 += 1
                elif num <= 7 and p2 != 12 and num != 1:
                    driver.find_element(By.XPATH, f'/html/body/div[2]/main/section[4]/div/div/div/div/a[{p2}]').click()
                    p2 += 1
                elif num > 7 and p1 >= 8:
                    driver.find_element(By.XPATH, f'/html/body/div[2]/main/section[4]/div/div/div/div/a[6]').click()

                time.sleep(10)

                # print('\t' + str(num))
                num -= 1

            safe_in_csv(meds, CSV)

            i += 1

    def parse_3(self):

        # urls
        urls = ['https://melzdrav.ru/catalog/1354/',
                'https://melzdrav.ru/catalog/1020/',
                'https://melzdrav.ru/catalog/968/',
                'https://melzdrav.ru/catalog/1369/',
                'https://melzdrav.ru/catalog/1102/',
                'https://melzdrav.ru/catalog/991/',
                'https://melzdrav.ru/catalog/997/',
                'https://melzdrav.ru/catalog/1440/',
                'https://melzdrav.ru/catalog/1003/',
                'https://melzdrav.ru/catalog/1006/',
                'https://melzdrav.ru/catalog/966/',
                'https://melzdrav.ru/catalog/1034/',
                'https://melzdrav.ru/catalog/1361/',
                'https://melzdrav.ru/catalog/986/',
                'https://melzdrav.ru/catalog/1012/',
                'https://melzdrav.ru/catalog/1091/',
                'https://melzdrav.ru/catalog/1360/',
                'https://melzdrav.ru/catalog/1097/',
                'https://melzdrav.ru/catalog/1374/',
                'https://melzdrav.ru/catalog/1108/']

        # categories
        categories = ['Аллергия',
                      'Кровь, кровообращение',
                      'Витамины и микроэлементы',
                      'Вредные привычки',
                      'Геморрой',
                      'Гинекология',
                      'Дыхательная система',
                      'Пищеварительная система',
                      'Заболевания глаз',
                      'Иммунитет',
                      'Инфекционные заболевания',
                      'Мочеполовая система',
                      'Обезболивающие',
                      'Общеукрепляющие и тонизирующие',
                      'Поражения кожи',
                      'Простуда, грипп',
                      'Психические расстройства',
                      'Сердце и сосуды',
                      'Успокаивающие',
                      'Эндокринная система']

        i = 0

        m = 100
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(m)

        n = len(urls)
        t = m / n
        n = 0

        for url in urls:

            n += t
            self.progressBar.setValue(int(n))

            driver.get(url)

            meds = []

            time.sleep(5)

            num = driver.find_element(By.CLASS_NAME, "styled-nav").find_elements(By.CLASS_NAME, 'styled-nav__item')

            num = int(num[-1].text)

            # print(i)

            while num != 0:

                blocks = driver.find_element(By.CLASS_NAME, 'catalog-list')
                elements = blocks.find_elements(By.CLASS_NAME, "catalog__item")

                for element in elements:
                    title = element.find_element(By.CLASS_NAME, "catalog__item__name").find_element(By.TAG_NAME,
                                                                                                    "a").text
                    title_url = element.find_element(By.CLASS_NAME, "catalog__item__name").find_element(By.TAG_NAME,
                                                                                                        "a").get_attribute(
                        "href")
                    manufacturer = element.find_element(By.CLASS_NAME, "catalog__item__producer").text
                    try:
                        price = element.find_element(By.CLASS_NAME, 'catalog__item__basket__price').text.replace(' ',
                                                                                                                 '')
                        price = price[2:-4]
                    except:
                        price = "Нет в наличии"

                    meds.append({
                        'pharmacy': 'melzdrav',
                        'category': categories[i],
                        'title': title,
                        'manufacturer': manufacturer,
                        'price': price,
                        'url': title_url
                    })

                time.sleep(5)

                if num != 1:
                    driver.find_element(By.CSS_SELECTOR, '.styled-nav__arrow.right').click()

                time.sleep(5)

                # print('\t' + str(num))
                num -= 1

            safe_in_csv(meds, CSV)

            i += 1

    def parser_selection(self):

        if self.checkBox.isChecked() == True:
            self.parse_1()
        if self.checkBox_2.isChecked() == True:
            self.parse_2()
        if self.checkBox_3.isChecked() == True:
            self.parse_3()

    def download_csv(self):

        self.tableWidget.setRowCount(0)

        df = pd.read_csv('meds.csv', on_bad_lines='skip', sep=';', na_values=['-'])
        df['Производитель'] = df['Производитель'].fillna('Неизвестен')

        headers = df.columns.values.tolist()

        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)

        for i, row in df.iterrows():
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)

            for j in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(row[j])))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def sorting_data(self):

        self.tableWidget.setRowCount(0)

        df = pd.read_csv('meds.csv', on_bad_lines='skip', sep=';', na_values=['-'])
        df['Производитель'] = df['Производитель'].fillna('Неизвестен')
        headers = df.columns.values.tolist()

        if self.comboBox_2.currentIndex() == 0:
            pass
        elif self.comboBox_2.currentIndex() == 1:
            df = df.sort_values(by='Цена (руб.)', ascending=False).reset_index(drop=True)
        elif self.comboBox_2.currentIndex() == 2:
            df = df.sort_values(by='Цена (руб.)', ascending=True).reset_index(drop=True)
        elif self.comboBox_2.currentIndex() == 3:
            df = df.sort_values(by='Название товара', ascending=True).reset_index(drop=True)
        elif self.comboBox_2.currentIndex() == 4:
            df = df.sort_values(by='Название товара', ascending=False).reset_index(drop=True)

        a = ''

        if self.checkBox_47.isChecked() == True:
            a += 'apteka22|'
        if self.checkBox_48.isChecked() == True:
            a += 'farmakopeika|'
        if self.checkBox_49.isChecked() == True:
            a += 'melzdrav|'

        a = a[:-1]

        mask = df["Название аптеки"].str.contains(a)
        df = df.loc[mask].reset_index(drop=True)

        c = ''
        if self.checkBox_23.isChecked() == True:
            c += 'Успокаивающие|'
        if self.checkBox_24.isChecked() == True:
            c += 'Простуда, грипп|'
        if self.checkBox_25.isChecked() == True:
            c += 'Витамины и микроэлементы|'
        if self.checkBox_26.isChecked() == True:
            c += 'Сердце и сосуды|'
        if self.checkBox_27.isChecked() == True:
            c += 'Аллергия|'
        if self.checkBox_28.isChecked() == True:
            c += 'Эндокринная система|'
        if self.checkBox_29.isChecked() == True:
            c += 'Кровь, кровообращение|'
        if self.checkBox_30.isChecked() == True:
            c += 'Вредные привычки|'
        if self.checkBox_31.isChecked() == True:
            c += 'Гинекология|'
        if self.checkBox_32.isChecked() == True:
            c += 'Геморрой|'
        if self.checkBox_33.isChecked() == True:
            c += 'Инфекционные заболевания|'
        if self.checkBox_34.isChecked() == True:
            c += 'Обезболивающие|'
        if self.checkBox_35.isChecked() == True:
            c += 'Мочеполовая система|'
        if self.checkBox_36.isChecked() == True:
            c += 'Простуда, грипп|'
        if self.checkBox_37.isChecked() == True:
            c += 'Общеукрепляющие и тонизирующие|'
        if self.checkBox_38.isChecked() == True:
            c += 'Поражения кожи|'
        if self.checkBox_39.isChecked() == True:
            c += 'От насекомых|'
        if self.checkBox_40.isChecked() == True:
            c += 'Психические расстройства|'
        if self.checkBox_41.isChecked() == True:
            c += 'Заболевания глаз|'
        if self.checkBox_42.isChecked() == True:
            c += 'Иммунитет|'
        if self.checkBox_43.isChecked() == True:
            c += 'Пищеварительная система|'
        if self.checkBox_44.isChecked() == True:
            c += 'Дыхательная система|'

        c = c[:-1]

        mask = df["Категория"].str.contains(c)
        df = df.loc[mask].reset_index(drop=True)

        if self.lineEdit_2.text() == '':
            pass
        else:
            mask = df["Название товара"].str.contains(self.lineEdit_2.text(), case=False)
            df = df.loc[mask].reset_index(drop=True)

        if self.lineEdit_3.text() == '':
            pass
        else:
            mask = df["Производитель"].str.contains(self.lineEdit_3.text(), case=False)
            df = df.loc[mask].reset_index(drop=True)

        if self.lineEdit_4.text() == '':
            pass
        else:
            df = df[df['Цена (руб.)'] > int(self.lineEdit_4.text())].reset_index(drop=True)

        if self.lineEdit_5.text() == '':
            pass
        else:
            df = df[df['Цена (руб.)'] < int(self.lineEdit_5.text())].reset_index(drop=True)


        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)

        for i, row in df.iterrows():
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)

            for j in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(row[j])))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


import datetime
from requests_html import HTML
from random import randint
import requests_html
from bs4 import BeautifulSoup

import requests
import re
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'deflate, br',  # choice(encoding_box),
    'Server': 'nginx/1.15.12',
    'access-control-allow-origin': '1',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'X-Forwarded-For': '.'.join([str(randint(0, 255)) for x in range(4)])
}
def get_price_tax_history(url):
    r = requests.get("https://www.zillow.com/homedetails/5-N-Meteor-Ave-Clearwater-FL-33765/47065349_zpid/", headers=headers)
    # urls = re.findall(re.escape('AjaxRender.htm?'), r.content.decode('utf-8'))

    import json

    ggg = r.content.decode('utf-8')
    ggg = str(ggg)
    print(ggg)
    print(ggg.index("priceHistory"), ggg.index("zoMarketName"), "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    # print(ggg[ggg.index("zoMarketName"):])
    ppp = ggg[ggg.index('"priceHistory'): ggg.index('zoMarketName')].replace("\\", "")[16:-3]
    ppp = ppp.replace("},{", "};{").split(";")

    ttt = ggg[ggg.index('"taxHistory'): ggg.index('homeValues')].replace("\\", "")[14:-3]
    ttt = ttt.replace("},{", "};{").split(";")
    print(ttt)

    for j in ttt:
        j = json.loads(j)
        print(j["taxPaid"])

    for i in ppp:
        i = json.loads(i)
        print(i["event"])





    # list_o_lines = ggg.find("script#hdpApolloPreloadedData", first=False)
    # for i in list_o_lines:
    #
    #     if "apiCache" in i.text:
    #         line = i.text.replace('\\', '').replace('true', '"True"').replace('false', '"False"')
    #         print(line)
    #
    #         print(6)
    #
    #         hope_object = '{"' + line[line.index("streetAddress"):line.index(',"listing_sub_type')] + '}'
    #
    #         print(hope_object)
    #
    #         d = json.loads(hope_object)
    #         print(d)
    #
    #         lat, lon = d["latitude"], d["longitude"]
    #         NULL = "NAN"
    #         d.update({"latLong": {"latitude": lat, "longitude": lon},
    #                   "time_stamp": datetime.datetime.now(),
    #                   "address": f'{d["streetAddress"]}, {d["city"]}, {d["state"]} {d["zipcode"]}',
    #                   "addressStreet": d["streetAddress"],
    #                   "addressCity": d["city"],
    #                   "addressZipcode": d["zipcode"],
    #                   "main_call_id": -1,
    #                   "detailUrl": r.url,
    #                   "addressState": d["state"],
    #                   "beds": d["bedrooms"] if "bedrooms" in d.keys() else NULL,
    #                   "baths": d["bathrooms"] if "bathrooms" in d.keys() else NULL,
    #                   "hdpData": {"homeInfo": {"homeType": d["homeType"] if "homeType" in d.keys() else 'null',
    #                                            "homeStatus": d["homeStatus"] if "homeStatus" in d.keys() else 'null',
    #                                            "daysOnZillow": d[
    #                                                "daysOnZillow"] if "daysOnZillow" in d.keys() else NULL,
    #                                            "zestimate": d["zestimate"] if "zestimate" in d.keys() else NULL,
    #                                            "livingArea": d["livingArea"] if "livingArea" in d.keys() else NULL,
    #                                            "lotSize": d["lotSize"] if "lotSize" in d.keys() else NULL,
    #                                            "yearBuilt": d["yearBuilt"] if "yearBuilt" in d.keys() else NULL,
    #                                            "price": d["price"] if "price" in d.keys() else NULL,
    #                                            "rentZestimate": d[
    #                                                "rentZestimate"] if "rentZestimate" in d.keys() else NULL}}})
    #         print(d)

#
#
# jjj = ggg[ggg.index("priceHistory"): ggg.index("zoMarketName")].replace("\\", "")[16:-3]
#
# jjj = "[" + jjj + "]"
#
# jjj = json.loads(f'priceHistory: {jjj}')
# print(jjj)
# print(r.content[r.content.index("priceHistory"),r.content.index('"zoMarketName"')])
#
# url = "https://www.zillow.com/AjaxRender.htm?{}".format(urls[4])
# r = requests.get(url, headers=headers)
# soup = BeautifulSoup(r.content.replace('\\', ''), "html.parser")
# data = []
#
# for tr in soup.find_all('tr'):
#     data.append([td.text for td in tr.find_all('td')])
#
# for row in data[:5]:        # Show first 5 entries
#     print(row)
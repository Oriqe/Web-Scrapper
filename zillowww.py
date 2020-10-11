from packet_app.realtytrac import trying, inserting_realtytrac
from random import randint
from packet_app.zillow_addresses import zillow_funcs, newesr_zillow_upgrade
import asyncio
from requests_html import HTML
from datetime import datetime
import time
from playwright import async_playwright
now = datetime.now()

optional = [
            '--autoplay-policy=user-gesture-required',
            '--disable-background-networking',
            '--disable-background-timer-throttling',
            '--disable-backgrounding-occluded-windows',
            '--disable-breakpad',
            '--disable-client-side-phishing-detection',
            '--disable-component-update',
            '--disable-default-apps',
            '--disable-dev-shm-usage',
            '--disable-domain-reliability',
            '--disable-extensions',
            '--disable-features=AudioServiceOutOfProcess',
            '--disable-hang-monitor',
            '--disable-ipc-flooding-protection',
            '--disable-notifications',
            '--disable-offer-store-unmasked-wallet-cards',
            '--disable-popup-blocking',
            '--disable-print-preview',
            '--disable-prompt-on-repost',
            '--disable-renderer-backgrounding',
            '--disable-setuid-sandbox',
            '--disable-speech-api',
            '--disable-sync',
            '--disk-cache-size=33554432',
            '--hide-scrollbars',
            '--ignore-gpu-blacklist',
            '--metrics-recording-only',
            '--mute-audio',
            '--no-default-browser-check',
            '--no-first-run',
            '--no-pings',
            '--no-sandbox',
            '--no-zygote',
            '--password-store=basic',
            '--use-mock-keychain',
            '--disable-gl-drawing-for-tests']


req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'X-Forwarded-For': '.'.join([str(randint(0, 255)) for x in range(4)])
}

# # ********************************************** OPERATIONAL
# street_address = input("enter street address: ")
# city = input("enter street city: ")
# state = input("enter street state: ")
# zip_code = input("enter street zip code: ")
# # **********************************************
#
# # ********************************************** TESTING LEASURE

street_address = "17209 Indian Ln".lower()
city = "vancleave"
state = "ms"
zip_code = "39565"

# for v in range(1):
line_of_dicts = zillow_funcs.get_zillow(city, state, zip_code)


lat, lon, line_of_dicts = zillow_funcs.get_zillow_info(line_of_dicts, street_address, city, state, zip_code)
print(line_of_dicts[0])
remove_list = []
for u in line_of_dicts:
    print(u['latLong'])
    if u['latLong'] == {}:
        print(u)
        remove_list.append(u)
for i in remove_list:
    print(i)
    line_of_dicts.remove(i)
print(line_of_dicts[0])
line_of_dicts.sort(key=lambda line: pow(pow(line["latLong"]["latitude"] - lat, 2) + pow(line["latLong"]["longitude"] - lon, 2), 0.5))

from copy import deepcopy
remaining_houses = deepcopy(line_of_dicts)
group_number = 0
checked_houses = []
new_list = []
while remaining_houses != []:

    current_group = []
    current_group.append(remaining_houses.pop(0))
    temp_remaining = remaining_houses
    current_group[0]["group_number"] = group_number

    for i in temp_remaining:
        if 0.005 > pow(pow(current_group[0]["latLong"]["latitude"] - i["latLong"]["latitude"], 2) + pow(current_group[0]["latLong"]["longitude"] - i["latLong"]["longitude"], 2), 0.5):
            i["group_number"] = group_number
            current_group.append(i)
            remaining_houses.remove(i)
    group_copy = current_group
    for j in group_copy[1:]:
        for k in remaining_houses:
            if 0.005 > pow(pow(j["latLong"]["latitude"] - k["latLong"]["latitude"], 2) + pow(j["latLong"]["longitude"] - k["latLong"]["longitude"], 2), 0.5) and k not in group_copy:
                k["group_number"] = j["group_number"]
                group_copy.append(k)
                temp_remaining.remove(k)

    group_number += 1
    new_list.extend(group_copy)
# for i in line_of_dicts:
#     print(i)

for b in new_list:
    print(b["group_number"])

# raise ImportError
# raise ImportError
zillow_funcs.insert_zillow(line_of_dicts)

for i in line_of_dicts:
    print(i["address"])
print("""*************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************
*****************************************************************************""")


for i in line_of_dicts:
    print(i["address"], pow(pow(i["latLong"]["latitude"] - lat, 2) + pow(i["latLong"]["longitude"] - lon, 2), 0.5))

print("WEIRDDDDDDDDD")
print(line_of_dicts[0])
print(len(line_of_dicts))

    # browser = asyncio.get_event_loop().run_until_complete(newesr_zillow_upgrade.trying_something_different())


async def final_one(line_of_dicts, loop):
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=optional, headless=True)
        for index in range(0, 40, 20):
            # ans = asyncio.get_event_loop().run_until_complete(zillow_funcs.async_requesting_part(line_of_dicts[index+1]["detailUrl"]))
            # print(line_of_dicts[index+1]["detailUrl"])
            # html_ans = HTML(html=ans.text)
            # print(html_ans.text)
            # for i in html_ans.find("tr", first=False):
            #     print(i.html)
            # raise ImportError
            number = 1



            ph1, ph2, ph3, ph4, ph5, ph6, ph7, ph8, ph9, ph10, ph11, ph12, ph13, ph14, ph15, ph16, ph17, ph18, ph19, ph20 = \
            await zillow_funcs.async_middle_func([(line_of_dicts[index]["detailUrl"], line_of_dicts[index]),
                                                  (line_of_dicts[index+1]["detailUrl"], line_of_dicts[index+1]),
                                                  (line_of_dicts[index+2]["detailUrl"], line_of_dicts[index+2]),
                                                  (line_of_dicts[index+3]["detailUrl"], line_of_dicts[index+3]),
                                                  (line_of_dicts[index+4]["detailUrl"], line_of_dicts[index+4]),
                                                  (line_of_dicts[index+5]["detailUrl"], line_of_dicts[index+5]),
                                                  (line_of_dicts[index+6]["detailUrl"], line_of_dicts[index+6]),
                                                  (line_of_dicts[index+7]["detailUrl"], line_of_dicts[index+7]),
                                                  (line_of_dicts[index+8]["detailUrl"], line_of_dicts[index+8]),
                                                  (line_of_dicts[index+9]["detailUrl"], line_of_dicts[index+9]),
                                                  (line_of_dicts[index + 10]["detailUrl"], line_of_dicts[index + 10]),
                                                  (line_of_dicts[index + 11]["detailUrl"], line_of_dicts[index + 11]),
                                                  (line_of_dicts[index + 12]["detailUrl"], line_of_dicts[index + 12]),
                                                  (line_of_dicts[index + 13]["detailUrl"], line_of_dicts[index + 13]),
                                                  (line_of_dicts[index + 14]["detailUrl"], line_of_dicts[index + 14]),
                                                  (line_of_dicts[index + 15]["detailUrl"], line_of_dicts[index + 15]),
                                                  (line_of_dicts[index + 16]["detailUrl"], line_of_dicts[index + 16]),
                                                  (line_of_dicts[index + 17]["detailUrl"], line_of_dicts[index + 17]),
                                                  (line_of_dicts[index + 18]["detailUrl"], line_of_dicts[index + 18]),
                                                  (line_of_dicts[index + 19]["detailUrl"], line_of_dicts[index + 19])], browser)
            number += 1
            print("got imidiattley to here, and i shouldnt")
            zillow_funcs.insert_zillow_price_table(ph1[0], ph1[1])
            zillow_funcs.insert_zillow_price_table(ph2[0], ph2[1])
            zillow_funcs.insert_zillow_price_table(ph3[0], ph3[1])
            zillow_funcs.insert_zillow_price_table(ph4[0], ph4[1])
            zillow_funcs.insert_zillow_price_table(ph5[0], ph5[1])
            zillow_funcs.insert_zillow_price_table(ph6[0], ph6[1])
            zillow_funcs.insert_zillow_price_table(ph7[0], ph7[1])
            zillow_funcs.insert_zillow_price_table(ph8[0], ph8[1])
            zillow_funcs.insert_zillow_price_table(ph9[0], ph9[1])
            zillow_funcs.insert_zillow_price_table(ph10[0], ph10[1])
            zillow_funcs.insert_zillow_price_table(ph11[0], ph11[1])
            zillow_funcs.insert_zillow_price_table(ph12[0], ph12[1])
            zillow_funcs.insert_zillow_price_table(ph13[0], ph13[1])
            zillow_funcs.insert_zillow_price_table(ph14[0], ph14[1])
            zillow_funcs.insert_zillow_price_table(ph15[0], ph15[1])
            zillow_funcs.insert_zillow_price_table(ph16[0], ph16[1])
            zillow_funcs.insert_zillow_price_table(ph17[0], ph17[1])
            zillow_funcs.insert_zillow_price_table(ph18[0], ph18[1])
            zillow_funcs.insert_zillow_price_table(ph19[0], ph19[1])
            zillow_funcs.insert_zillow_price_table(ph20[0], ph20[1])

        nower = datetime.now()
        ans = nower - now
        print("timestamp =", ans)
        raise ImportError

async def semi_final_one(line_of_dicts, loop):
    await final_one(line_of_dicts, loop)


loop = asyncio.get_event_loop()
loop.run_until_complete(semi_final_one(line_of_dicts, loop))
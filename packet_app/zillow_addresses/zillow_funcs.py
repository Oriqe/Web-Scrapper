import time
import random
import math
import json
import asyncio

from .newesr_zillow_upgrade import deeper_zillow
from random import randint
import datetime


user_agents = ['Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
              'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
              'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41',
              'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1',
              'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)']

req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': random.choice(user_agents),
    'X-Forwarded-For': '.'.join([str(randint(0, 255)) for x in range(4)])
}


def get_zillow_addresses(page):

    addresses_list = []
    # print(page.html)
    for i in page.html.split("\n"):


        if "#mobile-hdp .zsg-footer" in i:
            # print(len(i))
            for index, g in enumerate(i.split("},{")):

                if "/homedetails/" in g and g[:6] == '"zpid"':

                    if '"hasListResults"' in g:
                        g = g[:g.index('}],"hasListResults"')]

                    elif '}],"relaxedResultsHash"' in g:
                        g = g[:g.index('}],"relaxedResultsHash"')]

                    elif '"relaxed":false}]' in g:
                        g = g[:g.index('"relaxed":false') + len('"relaxed":false')]


                    print(g)
                    g = "{" + g + "}"
                    d = None
                    # d = json.loads(g)
                    while not d:
                        try:
                            d = json.loads(g)
                        except json.decoder.JSONDecodeError as e:
                            print(e)
                            print(g)
                            time.sleep(5)
                            continue

                    time.sleep(0.001)
                    d["time_stamp"] = datetime.datetime.now()
                    # print(type(d))
                    addresses_list.append(d)
                else:
                    continue

                continue
            # raise ImportError

    return addresses_list


def insert_zillow_price_table(price_list, adrs_dict):
    import psycopg2.errors
    from psycopg2.errorcodes import DUPLICATE_TABLE
    connection = psycopg2.connect(database="real_estate", user="postgres", password="Testing321",
                                  host="localhost")
    cursor = connection.cursor()
    NULL = "NAN"
    # print(adrs_dict)
    try:
        for record in price_list:

            record['DATE'] = record['DATE'].replace("/", "-")
            print(record)
            cursor.execute(
            f"""INSERT INTO price_list VALUES ((SELECT call_id FROM first_list
                                                        WHERE house_address = '{adrs_dict["address"].lower()}' AND time_stamp = '{adrs_dict["time_stamp"]}'),
                                                        '{adrs_dict["main_call_id"]}',
                                                        '{record['EVENT']}',
                                                        '{record['PRICE'].split(' ')[0].replace('/mo', '').replace('$', '').replace(",", "") if record['PRICE']!="N/A" and record['PRICE']!="--" else NULL}',  
                                                        '{record['source'][8:] if "source" in record.keys() else 'NULL'}',
                                                        '{adrs_dict["addressStreet"]}',
                                                        '{adrs_dict["addressCity"]}',
                                                        '{adrs_dict["addressState"]}',
                                                        '{adrs_dict["addressZipcode"]}',
                                                        '{record['DATE'] if len(record['DATE'].split("-")[0])==2 else f"0{record['DATE']}"}');""")

            connection.commit()
        cursor.close()
        print(adrs_dict["detailUrl"])
        print("FINISHED ENTERINGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")

    except psycopg2.errors.lookup(DUPLICATE_TABLE) as e:
        print(e)
        cursor.close()


def insert_zillow(line_of_dicts):
    import psycopg2

    connection = psycopg2.connect(database="real_estate", user="postgres", password="Testing321",
                                  host="localhost")
    cursor = connection.cursor()

    for index, i in enumerate(line_of_dicts):
        print(i["address"], i["time_stamp"])
        print(line_of_dicts[0]["address"].lower())

        if index == 1:
            cursor.execute(f"""SELECT call_id FROM first_list WHERE house_address = '{line_of_dicts[0]["address"].lower()}' AND time_stamp = '{line_of_dicts[0]["time_stamp"]}'""")
            serial = cursor.fetchone()[0]
            print(serial)
            for k in line_of_dicts[1:]:
                k["main_call_id"] = serial

        print(i)
        NULL = 'NAN'
        cursor.execute(
            # f"""INSERT INTO half_extracted_list VALUES ('{datetime.datetime.date(datetime.datetime.now())}');""")
            f"""INSERT INTO first_list VALUES (DEFAULT,
                                            '{i["hdpData"]["homeInfo"]["homeType"]}',
                                            '{i["address"].lower().replace("'", "`")}',
                                            '{i["addressCity"]}',
                                            '{i["addressState"]}',
                                            '{i["addressZipcode"] if i["addressZipcode"]!=' ' else NULL}',
                                            '{i["latLong"]["longitude"]}',
                                            '{i["latLong"]["latitude"]}',
                                            '{i["hdpData"]["homeInfo"]["homeStatus"]}',
                                            '{i["hdpData"]["homeInfo"]["daysOnZillow"]}',
                                            '{i["hdpData"]["homeInfo"]["zestimate"] if "zestimate" in i["hdpData"]["homeInfo"].keys() else NULL}',
                                            '{i["hdpData"]["homeInfo"]["livingArea"] if "livingArea" in i["hdpData"]["homeInfo"].keys() else NULL}',
                                            '{i["hdpData"]["homeInfo"]["lotSize"] if "lotSize" in i["hdpData"]["homeInfo"].keys() else NULL}',
                                            '{i["hdpData"]["homeInfo"]["yearBuilt"] if "yearBuilt" in i["hdpData"]["homeInfo"].keys() else NULL}',
                                            '{i["hdpData"]["homeInfo"]["price"] if "price" in i["hdpData"]["homeInfo"].keys() and i["hdpData"]["homeInfo"]["price"] != 'null' else NULL}',
                                            '{i["beds"] if i["beds"] != None else NULL}',
                                            '{i["baths"] if i["baths"] != None else NULL}',
                                            '{i["detailUrl"].replace("'", "`")}',
                                            '{i["hdpData"]["homeInfo"]["rentZestimate"] if "rentZestimate" in i["hdpData"]["homeInfo"].keys() and i["hdpData"]["homeInfo"]["rentZestimate"] != 'null' else NULL}',
                                            '{i["hdpData"]["homeInfo"]["priceReduction"] if "priceReduction" in i["hdpData"]["homeInfo"].keys() else 'NULL'}',
                                            '{i["hdpData"]["homeInfo"]["isPreforeclosureAuction"] if "isPreforeclosureAuction" in i["hdpData"]["homeInfo"].keys() else 'NULL'}',
                                            '{i["hdpData"]["homeInfo"]["taxAssessedValue"] if "taxAssessedValue" in i["hdpData"]["homeInfo"].keys() else NULL}',
                                            '{i["variableData"]["text"] if "variableData" in i.keys() else 'NULL'}',
                                            '{i["time_stamp"]}',
                                            '{i["main_call_id"]}',
                                            'NULL',
                                            'NULL',
                                            'NULL',
                                            'NULL',
                                            '{i["hasOpenHouse"] if "hasOpenHouse" in i.keys() else 'NULL'}');""")

        connection.commit()
    cursor.close()


from requests.exceptions import ContentDecodingError
from requests_html import HTML
import requests_html
from random import randint


def the_requesting_part(url):
    try:
        with requests_html.HTMLSession() as s:
            for k, v in req_headers.items():
                s.headers[k] = v

        return s.get(url)

    except ContentDecodingError as e:
        print(e)
        s.close()
    except AttributeError as e:
        print(e)
        s.close()

# ans = the_requesting_part("https://www.zillow.com/browse/homes/ca/los-angeles-county/90034/21/")
# ans_html = HTML(html=ans.text)
# print(ans_html.html)
# print("https://www.zillow.com/homes/st.-louis-hills-saint-louis-mo/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-90.37218470633476%2C%22east%22%3A-90.23680629366524%2C%22south%22%3A38.549964665249476%2C%22north%22%3A38.60626672938819%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A276586%2C%22regionType%22%3A8%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22mapZoom%22%3A13%2C%22filterState%22%3A%7B%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D".replace("%22", " ").replace("%7B", "{").replace("%7D", "}").replace("%3A", ":").replace("%2C", ",").replace("%5B", "[").replace("%5D", "]"))

def adding_the_page_number(page_number, url):
    page_number += 1
    if page_number > 1:
        if page_number == 2:
            url = url + f"/{page_number}_p/"
        else:
            url = url.replace(f"/{page_number - 1}_p/", f"/{page_number}_p/")

    return url, page_number


def adding_the_beds_number(url, bed_number):
    bed_number += 1
    if bed_number == 0:
        url = url + f"/-{bed_number}_beds"
        # bed_number += 1
    elif bed_number == 1:
        url = url[:url.index("_beds") + 5]
        url = url.replace(f"/-{bed_number-1}_beds", f"/{bed_number}-{bed_number}_beds")
    elif 1 < bed_number < 6:
        url = url[:url.index("_beds")+5]
        url = url.replace(f"/{bed_number - 1}-{bed_number - 1}_beds", f"/{bed_number}-{bed_number}_beds")
    elif bed_number == 6:
        url = url[:url.index("_beds") + 5]
        url = url.replace(f"/{bed_number - 1}-{bed_number - 1}_beds", f"/{bed_number}-_beds")
    return url, bed_number





async def async_requesting_part(url):
    try:
        with requests_html.AsyncHTMLSession() as s:
            for k, v in req_headers.items():
                s.headers[k] = v

        # time.sleep(randint(0, 10) / 5)
        await asyncio.sleep(randint(0, 10) / 5)
        ans = await s.get(url)
        await s.close()
        return ans


    except ContentDecodingError as e:
        print(e)
        await s.close()
    except AttributeError as e:
        print(e)
        await s.close()


async def async_gatherer_addresses(base_url, special_number): # the spec_num is  ((resuly_num - 40) / 40)
    if special_number >= 19:
        special_number = 19
    if special_number < 1:
        ans = the_requesting_part(base_url)
        ans_html = HTML(html=ans.text)
        temp_list = get_zillow_addresses(ans_html)
        return temp_list


    urls = []
    print(special_number)
    for num in range(2, special_number + 2, 1):
        # print(f"page num {num}")
        urls.append(base_url + f"/{num}_p/")
    urls.append(base_url)
    print(urls)
    # raise ImportError
    ans = await asyncio.gather(*[async_requesting_part(i) for i in urls])

    print("inside the async_gatherer_addresses")
    print(ans)
    print("exiting async_gatherer_addresses")
    mega_ans = []
    for i in ans:
        i_html = HTML(html=i.text)
        temp_list = get_zillow_addresses(i_html)
        for h in temp_list:
            print(h)
        print("ENDINGGGGGGGGGGGGGGGGGGGGGGGG")
        for j in temp_list:
            mega_ans.append(j)
    return mega_ans




def get_zillow(city, state, zip_code):
    print("?????????????????????????????/")
    print("aaa")
    stage = 1
    bed_number = -1
    p_counter, p, rent_counter = 0, 0, 0

    url_to_scrape = f"https://www.zillow.com/{city}-{state}-{zip_code}/sold"

    line_of_dicts = []

    while stage <= 3:
        print("restarting outer loop")
        if stage == 1:
            url_to_scrape = f"https://www.zillow.com/{city}-{state}-{zip_code}/sold"
        elif stage == 2:
            url_to_scrape = f"https://www.zillow.com/{city}-{state}-{zip_code}"
        elif stage == 3:
            url_to_scrape = f"https://www.zillow.com/{city}-{state}-{zip_code}/rent"
        elif stage > 3:
            break

        while True:
            # if bed_number > 0:
            #     stage = 4
            #     break
            print("restarting inner loop")
            r = the_requesting_part(url_to_scrape)
            print(bed_number, p_counter, r.url)

            r_html = HTML(html=r.text)
            if not r_html.find("span.result-count", first=True):
                if "_beds" in r.url:
                    if bed_number <= 6:
                        url_to_scrape, bed_number = adding_the_beds_number(url_to_scrape, bed_number)
                        continue
                    else:
                        bed_number = -1
                        stage += 1
                        break
                else:
                    stage += 1
                    break
            result_number = int(r_html.find("span.result-count", first=True).text.split(" ")[0].replace(",", ""))
            print(result_number)
            if "_beds" in r.url:
                """I want it to run through all the pages till max 20, increase the bed_number, and restart
                the inner loop, and break the outer loop if bed_number > 6"""
                print("_beds in r.url")
                spec_num = math.ceil((result_number - 40) / 40)
                many_lists = asyncio.get_event_loop().run_until_complete(async_gatherer_addresses(url_to_scrape, spec_num))
                line_of_dicts.extend(many_lists)
                # print(many_lists)
                url_to_scrape, bed_number = adding_the_beds_number(url_to_scrape, bed_number)
                if bed_number > 6:
                    bed_number = -1
                    stage += 1
                    break
                continue

            elif "_beds" not in r.url and result_number < 800:
                """run through all the pages till max 20, and restart the outer loop"""
                print("_beds not in r.url and result_number < 800")
                spec_num = math.ceil((result_number-40)/40)
                many_lists = asyncio.get_event_loop().run_until_complete(async_gatherer_addresses(url_to_scrape, spec_num))
                # print(many_lists)

                line_of_dicts.extend(many_lists)
                stage += 1
                break


            elif "beds" not in r.url and result_number > 800:
                """increase the bed_number, and restart the inner loop"""
                print("_beds not in r.url and result_number > 800")
                url_to_scrape, bed_number = adding_the_beds_number(url_to_scrape, bed_number)
                continue

    return line_of_dicts





# def get_zillow(city, state, zip_code):
#     print("?????????????????????????????/")
#     bed_number = -1
#     p_counter, p, rent_counter = 0, 0, 0
#
#     url_to_scrape = f"https://www.zillow.com/{city}-{state}-{zip_code}/sold"
#
#     line_of_dicts = []
#
#     while True:
#         # temporaryyyyyyyyyy
#         if p_counter > 0:
#             break
#         # temporaryyyyyyyyyy
#         url_to_scrape, p_counter = adding_the_page_number(p_counter, url_to_scrape)
#
#         r = the_requesting_part(url_to_scrape)
#
#         print(bed_number, p_counter, r.url)
#
#         r_html = HTML(html=r.text)
#
#         result_number = int(r_html.find("span.result-count", first=True).text.split(" ")[0].replace(",", ""))
#
#         if result_number > 800 and "_beds" not in url_to_scrape:
#             if "_beds" not in url_to_scrape or (bed_number > 0 and "_baths" not in url_to_scrape):
#                 # bed_number = 0
#                 p_counter = 0
#                 url_to_scrape, bed_number = adding_the_beds_number(url_to_scrape, bed_number)
#                 continue
#
#         if "_beds" in r.url and p_counter > 1 and "_p" not in r.url and bed_number <= 5:
#             url_to_scrape, bed_number = adding_the_beds_number(url_to_scrape, bed_number)
#             p_counter = 0
#             print("this at list!!!")
#             continue
#
#         if "_p/" not in r.url and p_counter > 1:  # NO OVERRFLOW checking if finished available houses or passed 20
#
#             if "sold" in r.url:  # finished the sold section, going into the for sale section
#                 url_to_scrape = f"https://www.zillow.com/{city}-{state}-{zip_code}"
#                 p_counter = 0
#                 bed_number = 0
#                 continue
#             elif "sold" not in r.url and rent_counter == 0:  # NO OVERFLOW finished the for sale section, going into the rent section
#                 url_to_scrape = f"https://www.zillow.com/{city}-{state}-{zip_code}/rent"
#                 p_counter = 0
#                 bed_number = 0
#                 rent_counter += 1
#                 continue
#             break
#
#         if "_p/" not in r.url and p_counter > 1 and "_beds" in r.url:  # OVERFLOW checking if finished filtered section
#             if bed_number > 5:
#                 break
#             url_to_scrape, bed_number = adding_the_beds_number(url_to_scrape, bed_number)
#             continue
#
#         temp_list = get_zillow_addresses(r_html)
#
#         line_of_dicts.extend(temp_list)
#
#     return line_of_dicts
#
#
async def async_middle_func(urls, browser):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!3")
    price_history1, price_history2, price_history3, price_history4, price_history5,\
        price_history6, price_history7, price_history8, price_history9, price_history10,\
        price_history11, price_history12, price_history13, price_history14, price_history15,\
        price_history16, price_history17, price_history18, price_history19, price_history20 = \
        await asyncio.gather(deeper_zillow(urls[0][0], urls[0][1], browser),
                             deeper_zillow(urls[1][0], urls[1][1], browser),
                             deeper_zillow(urls[2][0], urls[2][1], browser),
                             deeper_zillow(urls[3][0], urls[3][1], browser),
                             deeper_zillow(urls[4][0], urls[4][1], browser),
                             deeper_zillow(urls[5][0], urls[5][1], browser),
                             deeper_zillow(urls[6][0], urls[6][1], browser),
                             deeper_zillow(urls[7][0], urls[7][1], browser),
                             deeper_zillow(urls[8][0], urls[8][1], browser),
                             deeper_zillow(urls[9][0], urls[9][1], browser),
                             deeper_zillow(urls[10][0], urls[10][1], browser),
                             deeper_zillow(urls[11][0], urls[11][1], browser),
                             deeper_zillow(urls[12][0], urls[12][1], browser),
                             deeper_zillow(urls[13][0], urls[13][1], browser),
                             deeper_zillow(urls[14][0], urls[14][1], browser),
                             deeper_zillow(urls[15][0], urls[15][1], browser),
                             deeper_zillow(urls[16][0], urls[16][1], browser),
                             deeper_zillow(urls[17][0], urls[17][1], browser),
                             deeper_zillow(urls[18][0], urls[18][1], browser),
                             deeper_zillow(urls[19][0], urls[19][1], browser))

    print(price_history1)
    print(price_history2)
    print(price_history3)
    print(price_history4)
    print(price_history5)
    return price_history1, price_history2, price_history3, price_history4, price_history5, price_history6, price_history7, price_history8, price_history9, price_history10, price_history11, price_history12, price_history13, price_history14, price_history15, price_history16, price_history17, price_history18, price_history19, price_history20


def get_zillow_info(line_of_dicts, street_address, city, state, zip_code):
    from requests_html import HTML
    import requests_html
    failed = True
    # for t in line_of_dicts:
    #     print(type(t))


    for t in line_of_dicts:
        print(f"{street_address}   :::  {t['addressStreet']}")
        if street_address in t["addressStreet"].lower():
            lat = t["latLong"]["latitude"]
            lon = t["latLong"]["longitude"]
            failed = False
            t.update({"main_call_id": -1, "time_stamp": datetime.datetime.now()})
            print(line_of_dicts[0])
            line_of_dicts.remove(t)
            line_of_dicts.insert(0, t)
            return lat, lon, line_of_dicts

    print("Failed: ", failed)
    if failed:
        import json
        with requests_html.HTMLSession() as s:
            for k, v in req_headers.items():
                s.headers[k] = v

            url = f"https://www.zillow.com/homes/{street_address.replace(' ', '-')}-{city.replace(' ', '-')},-{state.upper()},-{zip_code}_rb"
            r = s.get(url)
            r_html = HTML(html=r.text)
            print("till here")

            list_o_lines = r_html.find("script#hdpApolloPreloadedData", first=False)
            if not list_o_lines:
                list_o_lines = r_html.html.split("\n")
                for i in list_o_lines:

                    if "#mobile-hdp" in i:
                        line = i.replace('\\', '').replace('true', '"True"').replace('false', '"False"')
            else:
                for i in list_o_lines:

                    if "apiCache" in i.html:
                        line = i.html.replace('\\', '').replace('true', '"True"').replace('false', '"False"')


            print(url)
            print(r_html.html)
            print(f"actual url {r.url}")
            print("supposed to stop")

            print(line)

            print(6)

            hope_object = '{"' + line[line.index("streetAddress"):line.index(',"listing_sub_type')] + '}'

            print(hope_object)

            d = json.loads(hope_object)
            print(d)

            lat, lon = d["latitude"], d["longitude"]
            NULL = "NAN"
            d.update({"latLong": {"latitude": lat, "longitude": lon},
                      "time_stamp": datetime.datetime.now(),
                      "address": f'{d["streetAddress"]}, {d["city"]}, {d["state"]} {d["zipcode"]}',
                      "addressStreet": d["streetAddress"],
                      "addressCity": d["city"],
                      "addressZipcode": d["zipcode"],
                      "main_call_id": -1,
                      "detailUrl": url,
                      "addressState": d["state"],
                      "beds": d["bedrooms"] if "bedrooms" in d.keys() else NULL,
                      "baths": d["bathrooms"] if "bathrooms" in d.keys() else NULL,
                      "hdpData": {"homeInfo": {"homeType": d["homeType"] if "homeType" in d.keys() else 'null',
                                               "homeStatus": d["homeStatus"] if "homeStatus" in d.keys() else 'null',
                                               "daysOnZillow": d["daysOnZillow"] if "daysOnZillow" in d.keys() else NULL,
                                               "zestimate": d["zestimate"] if "zestimate" in d.keys() else NULL,
                                               "livingArea": d["livingArea"] if "livingArea" in d.keys() else NULL,
                                               "lotSize": d["lotSize"] if "lotSize" in d.keys() else NULL,
                                               "yearBuilt": d["yearBuilt"] if "yearBuilt" in d.keys() else NULL,
                                               "price": d["price"] if "price" in d.keys() else NULL,
                                               "rentZestimate": d["rentZestimate"] if "rentZestimate" in d.keys() else NULL}}})
            print(d)

            line_of_dicts.insert(0, d)

            return lat, lon, line_of_dicts

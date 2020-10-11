# ********************************************** OPERATIONAL
# street_address = input("enter street address")
# city = input("enter street city")
# state = input("enter street state")
# zip_code = input("enter street zip code")
# **********************************************

# ********************************************** TESTING LEASURE
# street_address = "2836 eagle run cir e"
# city = "clearwater"
# state = "fl"
# zip_code = "33760"
# **********************************************
# my_neighborhood = "2836 eagle run FL 33760"
# area = "FL 33760"
# geolocator = Nominatim(user_agent="Heyy im nick")
#
# my_neighborhood = geolocator.geocode(my_neighborhood)


#####################################################################################################

# maybe good practice request headers

# #
# # encoding_box = ['gzip, deflate, br', 'deflate, br', 'br', 'gzip, deflate', 'deflate', 'gzip br',]
# # req_headers = {
# #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# #     'accept-encoding': choice(encoding_box),
# #     'Server': 'nginx/1.15.12',
# #     'accept-language': 'en-US,en;q=0.8',
# #     'upgrade-insecure-requests': '1',
# #     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
# #     #'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
# #     'X-Forwarded-For': '.'.join([str(randint(0, 255)) for x in range(4)])
# # }
#



#####################################################################################################




#####################################################################################################
#!!!!!!!!!!!!!!!!!!!!!!!!!!!from zillowww.py
# failed = True
# for t in line_of_dicts:
#     if street_address in t["addressStreet"].lower():
#         lat = t["latLong"]["latitude"]
#         lon = t["latLong"]["longitude"]
#         failed = False
# if failed:
#     import json
#     with requests_html.HTMLSession() as s:
#         for k, v in req_headers.items():
#             s.headers[k] = v
#
#
#         "https://www.zillow.com/homes/2836-Eagle-Run-Cir-E-Clearwater,-FL,-33760_rb"
#         url = f"https://www.zillow.com/homes/{street_address.replace(' ', '-')}-{city},-{state.upper()},-{zip_code}_rb"
#         print(url)
#         r = s.get(url)
#         r_html = HTML(html=r.text)
#         print(r_html.html)
#         list_o_lines = r_html.find("script#hdpApolloPreloadedData", first=False)
#         for i in list_o_lines:
#             if "apiCache" in i.text:
#                 line = i.text.replace('\\', '').replace('true', '"True"').replace('false', '"False"')
#                 print(line)
#                 print(line[line.index("streetAddress"):])
#                 hope_object = '{"' + line[line.index("streetAddress"):line.index(',"listing_sub_type')] + '}'
#                 print(hope_object)
#                 d = json.loads(hope_object)
#                 print(d)
#                 print(d["zestimate"])
#                 lat, lon = d["latitude"], d["longitude"]
#                 d.update({"latLong": {"latitude": lat, "longitude": lon}})
#                 line_of_dicts.append(d)
#####################################################################################################
#!!!!!!!!!!!!!!!!!!!!!!!!!!!from zillowww.py
# # **********************************************
# # my_neighborhood = "2836 eagle run FL 33760"
# # area = "FL 33760"
# # geolocator = Nominatim(user_agent="Heyy im nick")
# #
# # my_neighborhood = geolocator.geocode(my_neighborhood)
#
# p_counter = 0
#
#
# guide = [f"https://www.zillow.com/{city}-{state}-{zip_code}/sold"]
# # guide = ["https://www.zillow.com/clearwater-fl-33760/sold/"]
# line_of_dicts = []
# p = 0
# print(len(guide))
# mega_list = []
#
# print(guide)
# while True:
#     if p_counter >= 1:   # testing only
#         break
#     with requests_html.HTMLSession() as s:
#         for k, v in req_headers.items():
#             s.headers[k] = v
#         print(s.headers)
#         print(1)
#         try:
#             print("STREP ONE")
#             time.sleep(3)
#             print("STREP TWO")
#             p_counter += 1
#             if p_counter == 1:
#                 guide[0] = guide[0]
#             elif p_counter > 1:
#                 guide[0] = guide[0] + f"/{p_counter}_p/"
#
#
#             r = s.get(guide[0])
#             print(p_counter, r.url)
#             if "_p/" not in r.url and p_counter > 1:
#                 break
#             print(2)
#
#
#             r_html = HTML(html=r.text)
#
#             print(len(r_html.html))
#             # print(r_html.html)
#             # print(r_html.links)
#             print()
#             print()
#             print("start of change")
#             temp_list = zillow_funcs.get_zillow_addresses(r_html)
#             print("end of function change")
#             line_of_dicts.extend(temp_list)
#             print("end of line of dicts partial extension")
#             print(len(line_of_dicts))
#
#         except ContentDecodingError as e:
#             print(e)
#             s.close()
#             #continue
#         except AttributeError as e:
#             print(e)
#             s.close()
#             #continue
#######################################################################

import time
import asyncio
from geopy.distance import geodesic
import json
from geopy.geocoders import Nominatim
from packet_app.realtytrac import trying, gathering_realtytrac, inserting_realtytrac
from packet_app.zillow_addresses import zillow_funcs
from requests.exceptions import ContentDecodingError
from googlesearch import search
from requests_html import HTML
import requests_html
import os
from random import random, randint, choice
import proxyscrape



req_headers = {
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

with requests_html.HTMLSession() as s:
    r = s.get(
        "https://www.redfin.com/FL/Clearwater/2836-Eagle-Run-Cir-E-33760/home/48198149", headers=req_headers)

    # print(r.html.render(
    #     timeout=30, wait=3, reload=True))
    print(r.url)
    print(1)

    r_html = HTML(html=r.text)
    print(r_html.html)





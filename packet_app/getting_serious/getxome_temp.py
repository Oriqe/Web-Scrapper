from requests_html import AsyncHTMLSession, HTML
from requests_html import HTMLSession
from random import randint
import psycopg2
import datetime

from lat_lon import geolocate
from gathering_xome import gathering_similar_homes, gathering_home_details, gathering_price_details, gathering_tax_details
from inserting import insert_into_xome_table
from slugifying import slug_xome_comp_sold, slug_xome_comp_listed, slug_xome_prop_facts, slug_xome_price_history, slug_xome_tax_history
from inserting import insert_into_xome_table

req_headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.8',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
                'X-Forwarded-For': '.'.join([str(randint(0, 255)) for x in range(4)])
            }


from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="Heyy im nick")
location = geolocator.geocode("2836 Eagle Run Circle E FL 33760")



""


async def get_xome(address, zip, slug, gather): #address, zip, gather_method, slug_method):
    asession = AsyncHTMLSession()

    r = await asession.get(slug(address, zip), headers=req_headers)
    print(r.url)
    # r = await asession.get(slug_method(address, zip), headers=req_headers)
    await r.html.arender(timeout=30, wait=3, reload=True)
    resp = r.html.html

    resp = HTML(html=resp)

    #dicto = gather_method(resp)
    dicto = gather(resp)

    return dicto


def replacing(str):
    return str.replace("Lane", "Ln").replace("Street", "St").replace("Road", "Rd").replace("Drive", "Dr")





asession = AsyncHTMLSession()



# xome = sorted(asession.run(
#                     lambda: get_xome("293 Spring St", "07860", slug_xome_comp_sold, gathering_similar_homes),
#                     lambda: get_xome("293 Spring St", "07860", slug_xome_prop_facts, gathering_home_details),
#                     lambda: get_xome("293 Spring St", "07860", slug_xome_tax_history, gathering_tax_details),
#                     lambda: get_xome("293 Spring St", "07860", slug_xome_price_history, gathering_price_details)),
#                     key=lambda x: x[1]
# )

xome = sorted(asession.run(
                    lambda: get_xome("1505 chew rd", "44902", slug_xome_comp_sold, gathering_similar_homes),
                    lambda: get_xome("1505 chew rd", "44902", slug_xome_prop_facts, gathering_home_details),
                    lambda: get_xome("1505 chew rd", "44902", slug_xome_tax_history, gathering_tax_details),
                    lambda: get_xome("1505 chew rd", "44902", slug_xome_price_history, gathering_price_details)),
                    key=lambda x: x[1]
)



# asession.loop.run_until_complete(asession.close())

xome[1][0].update(xome[0][0][1])


for i in xome:
    print(i)

insert_into_xome_table(xome[1][0], xome[2][0][0])

# main_coordinate = geolocator.geocode("5361 Doverton Dr 92649")
# sorted_by_distance = []
# not_sorted = []
# for i in xome[0][0][0]:
#     if not geolocator.geocode(f'{i.split(",")[0]+i.split(",")[2]}'):
#         continue
#     coordinate = [geolocator.geocode(f'{i.split(",")[0]+i.split(",")[2]}').latitude, geolocator.geocode(f'{i.split(",")[0]+i.split(",")[2]}').longitude, i]
#     coordinate[0] -= main_coordinate.latitude
#     coordinate[1] -= main_coordinate.longitude
#     not_sorted.append(coordinate)
#     print(coordinate)
# sorted_by_distance = sorted(not_sorted, key=lambda distance: pow(pow(round(distance[0], 3), 2) + pow(round(distance[1], 3), 2), 0.5))
# print(sorted_by_distance)
#
import asyncio

ioloop = asyncio.get_event_loop()
addresses_to_visit = ioloop.run_until_complete(geolocate(xome[0][0][0], "1505 chew rd 44902"))
#




rest_addresses = []

new_counter = 0
for i in addresses_to_visit:
    asession = AsyncHTMLSession()
    new = i.split(",")
    print(new[0], new[-1].split(" ")[-1])
    count = 0


    while True:
        try:
            xome = sorted(asession.run(
                lambda: get_xome(replacing(new[0]), new[-1].split(" ")[-1].zfill(5), slug_xome_comp_sold, gathering_similar_homes),
                lambda: get_xome(replacing(new[0]), new[-1].split(" ")[-1].zfill(5), slug_xome_prop_facts, gathering_home_details),
                lambda: get_xome(replacing(new[0]), new[-1].split(" ")[-1].zfill(5), slug_xome_tax_history, gathering_tax_details),
                lambda: get_xome(replacing(new[0]), new[-1].split(" ")[-1].zfill(5), slug_xome_price_history, gathering_price_details)),
                key=lambda x: x[1]
            )
            xome[1][0].update(xome[0][0][1])
            if new_counter < 9:
                print(rest_addresses, addresses_to_visit)
                print("pre start")
                # addresses_to_visit.extend(rest_addresses)



                ioloop = asyncio.get_event_loop()

                more_addresses_to_visit = ioloop.run_until_complete(geolocate(xome[0][0][0], "1505 chew rd 44902", addresses_to_visit))
                addresses_to_visit.extend(more_addresses_to_visit)
                print("start")
                print(addresses_to_visit)
                print("end")
                # addresses_to_visit.extends(more_addresses_to_visit)
                # more_addresses = geolocate(xome[0][0][0], f'{xome[1][0]["address"]} {xome[1][0]["zip"]}')
                # addresses_to_visit.extends(more_addresses)
                new_counter += 1
                # if i == addresses_to_visit[-1]:
                #     addresses_to_visit = rest_addresses
            for i in xome:
                print(i)
            insert_into_xome_table(xome[1][0], xome[2][0][0])
            break
        except IndexError as e:
            print(e)
            count += 1
            if count >= 2:
                break
            pass
        except ConnectionResetError as e:
            print(e)
            asession.close()
            pass
        except asyncio.exceptions.IncompleteReadError as e:
            print(e)
            count += 1
            if count >= 2:
                break
            pass
        except AttributeError as e:
            print(e)
            pass
        except OSError:
            print("IIIIIIIIIIIIIIIIII cought it")
            asession.close()
            continue
        # finally:
        #     asession.close()
        #     continue

# for i in rest_addresses:
#     asession = AsyncHTMLSession()
#     new = i.split(",")
#     print(new[0], new[-1].split(" ")[-1])
#     count = 0
#     while True:
#         try:
#             xome = sorted(asession.run(
#                 lambda: get_xome(replacing(new[0]), new[-1].split(" ")[-1].zfill(5), slug_xome_comp_sold,
#                                  gathering_similar_homes),
#                 lambda: get_xome(replacing(new[0]), new[-1].split(" ")[-1].zfill(5), slug_xome_prop_facts,
#                                  gathering_home_details),
#                 lambda: get_xome(replacing(new[0]), new[-1].split(" ")[-1].zfill(5), slug_xome_tax_history,
#                                  gathering_tax_details),
#                 lambda: get_xome(replacing(new[0]), new[-1].split(" ")[-1].zfill(5), slug_xome_price_history,
#                                  gathering_price_details)),
#                 key=lambda x: x[1]
#             )
#             xome[1][0].update(xome[0][0][1])
#
#             for i in xome:
#                 print(i)
#             insert_into_xome_table(xome[1][0], xome[2][0][0])
#             break
#         except IndexError:
#             count += 1
#             if count >= 2:
#                 break
#             pass
#         except ConnectionResetError:
#             asession.close()
#             pass
#         except AttributeError:
#             pass
#         except OSError:
#             print("IIIIIIIIIIIIIIIIII cought it")
#             asession.close()
#             continue
    # asession.loop.run_until_complete(asession.close())








# for i in xome[0][0][0][15:]:
#     asession = AsyncHTMLSession()
#     new = i.split(",")
#     print(new[0], new[-1].split(" ")[-1])
#     count = 0
#     while True:
#         try:
#             xome = sorted(asession.run(
#                 lambda: get_xome(replacing(new[0]), new[-1].split(" ")[-1].zfill(5), slug_xome_comp_sold, gathering_similar_homes),
#                 lambda: get_xome(replacing(new[0]), new[-1].split(" ")[-1].zfill(5), slug_xome_prop_facts, gathering_home_details),
#                 lambda: get_xome(replacing(new[0]), new[-1].split(" ")[-1].zfill(5), slug_xome_tax_history, gathering_tax_details),
#                 lambda: get_xome(replacing(new[0]), new[-1].split(" ")[-1].zfill(5), slug_xome_price_history, gathering_price_details)),
#                 key=lambda x: x[1]
#             )
#             xome[1][0].update(xome[0][0][1])
#
#
#             for i in xome:
#                 print(i)
#             insert_into_xome_table(xome[1][0], xome[2][0][0])
#             break
#         except IndexError:
#             count += 1
#             if count >= 2:
#                 break
#             pass
#         except ConnectionResetError:
#             asession.close()
#             pass
#         except AttributeError:
#             pass
#         except OSError:
#             print("IIIIIIIIIIIIIIIIII cought it")
#             asession.close()
#             continue
#     # asession.loop.run_until_complete(asession.close())
#
#
#
#
#



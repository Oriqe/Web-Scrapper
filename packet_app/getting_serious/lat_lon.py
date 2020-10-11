# from geopy.geocoders import Nominatim
# import asyncio
#
# address_list = ['5341 Doverton Drive, Huntington Beach, CA 92649', '5312 Doverton Drive, Huntington Beach, CA 92649', '5322 Doverton Drive, Huntington Beach, CA 92649', '5335 Charlotta Drive, Huntington Beach, CA 92649', '16836 Barclay Lane, Huntington Beach, CA 92649', '6252 FARINELLA Drive, Huntington Beach, CA 92647', '6202 Point Loma Drive, Huntington Beach, CA 92647', '16441 Kohala Lane, Huntington Beach, CA 92649', '6122 Gumm Drive, Huntington Beach, CA 92647', '5375 Charlotta Drive, Huntington Beach, CA 92649', '5326 Charlotta Drive, Huntington Beach, CA 92649', '6121 Kelley Circle, Huntington Beach, CA 92647', '16865 Pembrook Lane, Huntington Beach, CA 92649', '16818 Barracuda Ln 88, Huntington Beach, CA 92649', '16292 ANGLER Lane, Huntington Beach, CA 92647', '5142 Warner Avenue UNIT 105, Huntington Beach, CA 92649', '4845 Coveview Drive, Huntington Beach, CA 92649', '5142 Warner Ave 105, Huntington Beach, CA 92649', '5252 Chadwick Dr, Huntington Beach, CA 92649', '17691 Amberton Lane, Huntington Beach, CA 92649', '16891 Saybrook Lane, Huntington Beach, CA 92649', '17301 Wareham Lane, Huntington Beach, CA 92649', '4411 Waimea, Huntington Beach, CA 92649', '5311 Glenstone Drive, Huntington Beach, CA 92649', '17291 Wareham Lane, Huntington Beach, CA 92649', '17532 Bates Circle, Huntington Beach, CA 92649', '5376 Wishfield Circle, Huntington Beach, CA 92649', '16861 Primrose, Huntington Beach, CA 92649', '4831 Los Patos Ave, Huntington Beach, CA 92649', '17211 Twain Lane, Huntington Beach, CA 92649', '16232 Fairway Lane, Huntington Beach, CA 92649', '4561 Warner Ave 203, Huntington Beach, CA 92649', '5142 Warner Ave 302, Huntington Beach, CA 92649', '16836 Pembrook Lane, Huntington Beach, CA 92649', '4622 Minuet Dr, Huntington Beach, CA 92649', '5502 Wendy Circle, Huntington Beach, CA 92649', '16362 Gentry Lane, Huntington Beach, CA 92647', '5471 Meadow Circle, Huntington Beach, CA 92649', '4466 Alderport Dr 56, Huntington Beach, CA 92649', '5382 Barwood Drive, Huntington Beach, CA 92649', '17152 Sandra Lee Lane, Huntington Beach, CA 92649', '16752 Westfield Lane, Huntington Beach, CA 92649', '5266 Acorn Drive, Huntington Beach, CA 92649', '17432 Almelo Lane, Huntington Beach, CA 92649', '17321 Coronado Lane, Huntington Beach, CA 92647', '6051 Point Loma Drive, Huntington Beach, CA 92647', '17192 Lynn Ln, Huntington Beach, CA 92649', '17221 Apel Ln, Huntington Beach, CA 92649', '17491 Bellport Circle, Huntington Beach, CA 92649', '16351 Gentry Lane, Huntington Beach, CA 92647']
# # geolocator = Nominatim(user_agent="Heyy im nick")
# # main_coordinate = geolocator.geocode("5361 Doverton Dr 92649")
# # sorted_by_distance = []
# # not_sorted = []
# # for i in xome[0][0][0]:
# #     if not geolocator.geocode(f'{i.split(",")[0]+i.split(",")[2]}'):
# #         continue
# #     coordinate = [geolocator.geocode(f'{i.split(",")[0]+i.split(",")[2]}').latitude, geolocator.geocode(f'{i.split(",")[0]+i.split(",")[2]}').longitude, i]
# #     coordinate[0] -= main_coordinate.latitude
# #     coordinate[1] -= main_coordinate.longitude
# #     not_sorted.append(coordinate)
# #     print(coordinate)
# # sorted_by_distance = sorted(not_sorted, key=lambda distance: pow(pow(round(distance[0], 3), 2) + pow(round(distance[1], 3), 2), 0.5))
# # print(sorted_by_distance)
#
# #
# # import asyncio
# # import time
# # async def main():
# #     task1 = asyncio.create_task(
# #         say_after(1, 'hello'))
# #
# #     task2 = asyncio.create_task(
# #         say_after(2, 'world'))
# #
# #     print(f"started at {time.strftime('%X')}")
# #
# #     # Wait until both tasks are completed (should take
# #     # around 2 seconds.)
# #     await task1
# #     await task2
# #
# #
#
#
#
# async def changing(address, geolocator):
#     ans = geolocator.geocode(f'{address.split(",")[0]+address.split(",")[2]}', timeout=2)
#     return ans, address
#
#
# async def geolocate(specific_addresses, original_address, addresses_to_visit=[]):
#     geolocator = Nominatim(user_agent="Heyy im nick")
#     main_coordinate = geolocator.geocode(original_address)
#     not_sorted, sorted_by_distance = [], []
#     for i in range(0, len(specific_addresses), 10):
#         #coordinate = await geolocator.geocode(f'{i.split(",")[0]+i.split(",")[2]}')
#
#         task1 = asyncio.create_task(
#             changing(specific_addresses[i], geolocator))
#
#         task2 = asyncio.create_task(
#             changing(specific_addresses[i+1], geolocator))
#
#         task3 = asyncio.create_task(
#             changing(specific_addresses[i+2], geolocator))
#
#         task4 = asyncio.create_task(
#             changing(specific_addresses[i+3], geolocator))
#
#         task5 = asyncio.create_task(
#             changing(specific_addresses[i+4], geolocator))
#
#         task6 = asyncio.create_task(
#             changing(specific_addresses[i+5], geolocator))
#
#         task7 = asyncio.create_task(
#             changing(specific_addresses[i+6], geolocator))
#
#         task8 = asyncio.create_task(
#             changing(specific_addresses[i+7], geolocator))
#
#         task9 = asyncio.create_task(
#             changing(specific_addresses[i+8], geolocator))
#
#         task10 = asyncio.create_task(
#             changing(specific_addresses[i+9], geolocator))
#
#         await task1, task2, task3, task4, task5, task6, task7, task8, task9, task10
#
#         not_sorted.extend([task1.result(),
#                            task2.result(),
#                            task3.result(),
#                            task4.result(),
#                            task5.result(),
#                            task6.result(),
#                            task7.result(),
#                            task8.result(),
#                            task9.result(),
#                            task10.result()
#                            ])
#         print(task1.result(),
#                task2.result(),
#                task3.result(),
#                task4.result(),
#                task5.result(),
#                task6.result(),
#                task7.result(),
#                task8.result(),
#                task9.result(),
#                task10.result())
#
#
#     for i in not_sorted:
#
#         if not i[0]:
#             continue
#         if i[1] in addresses_to_visit:
#             continue
#         # print(i)
#         i = [(i[0].latitude, i[0].longitude), i[1]]
#         print(f'i[0] = {pow((pow(i[0][0]-main_coordinate.latitude, 2) + pow(i[0][1]-main_coordinate.longitude, 2)), 0.5)}')
#         i[0] = pow((pow(i[0][0]-(27.9211), 2) + pow(i[0][1]-(-82.719842), 2)), 0.5)
#         if not i[0]:
#             continue
#         sorted_by_distance.append(i)
#
#
#     while True:
#         try:
#             sorted_by_distance = [i[1] for i in sorted(sorted_by_distance, key=lambda i: i[0])][:10]
#
#             break
#         except TypeError:
#             pass
#     # print(sorted_by_distance)
#     return sorted_by_distance
#
# if __name__ == "__main__":
#
#
#     asyncio.run(geolocate(address_list, "5341 Doverton Drive, Huntington Beach, CA 92649"))
#
#
#
#
#
#
#
#
#
#
#
#
#
#     #
#     #     coordinate = task1.result()
#     #     #
#     #     # coordinate = await changing(i, geolocator)
#     #     # print(coordinate)
#     #     if not coordinate:
#     #         continue
#     #     coordinate = [(coordinate.latitude, coordinate.longitude), i]
#     #     coordinate[0] = pow((pow(coordinate[0][0]-main_coordinate.latitude, 2) + pow(coordinate[0][1]-main_coordinate.longitude, 2)), 0.5)
#     #     not_sorted.append(coordinate)
#     # print(not_sorted)
#
# #asyncio.run(geolocate(address_list, "5341 Doverton Drive, Huntington Beach, CA 92649"))




from geopy.geocoders import Nominatim
import asyncio

address_list = ['5341 Doverton Drive, Huntington Beach, CA 92649', '5312 Doverton Drive, Huntington Beach, CA 92649', '5322 Doverton Drive, Huntington Beach, CA 92649', '5335 Charlotta Drive, Huntington Beach, CA 92649', '16836 Barclay Lane, Huntington Beach, CA 92649', '6252 FARINELLA Drive, Huntington Beach, CA 92647', '6202 Point Loma Drive, Huntington Beach, CA 92647', '16441 Kohala Lane, Huntington Beach, CA 92649', '6122 Gumm Drive, Huntington Beach, CA 92647', '5375 Charlotta Drive, Huntington Beach, CA 92649', '5326 Charlotta Drive, Huntington Beach, CA 92649', '6121 Kelley Circle, Huntington Beach, CA 92647', '16865 Pembrook Lane, Huntington Beach, CA 92649', '16818 Barracuda Ln 88, Huntington Beach, CA 92649', '16292 ANGLER Lane, Huntington Beach, CA 92647', '5142 Warner Avenue UNIT 105, Huntington Beach, CA 92649', '4845 Coveview Drive, Huntington Beach, CA 92649', '5142 Warner Ave 105, Huntington Beach, CA 92649', '5252 Chadwick Dr, Huntington Beach, CA 92649', '17691 Amberton Lane, Huntington Beach, CA 92649', '16891 Saybrook Lane, Huntington Beach, CA 92649', '17301 Wareham Lane, Huntington Beach, CA 92649', '4411 Waimea, Huntington Beach, CA 92649', '5311 Glenstone Drive, Huntington Beach, CA 92649', '17291 Wareham Lane, Huntington Beach, CA 92649', '17532 Bates Circle, Huntington Beach, CA 92649', '5376 Wishfield Circle, Huntington Beach, CA 92649', '16861 Primrose, Huntington Beach, CA 92649', '4831 Los Patos Ave, Huntington Beach, CA 92649', '17211 Twain Lane, Huntington Beach, CA 92649', '16232 Fairway Lane, Huntington Beach, CA 92649', '4561 Warner Ave 203, Huntington Beach, CA 92649', '5142 Warner Ave 302, Huntington Beach, CA 92649', '16836 Pembrook Lane, Huntington Beach, CA 92649', '4622 Minuet Dr, Huntington Beach, CA 92649', '5502 Wendy Circle, Huntington Beach, CA 92649', '16362 Gentry Lane, Huntington Beach, CA 92647', '5471 Meadow Circle, Huntington Beach, CA 92649', '4466 Alderport Dr 56, Huntington Beach, CA 92649', '5382 Barwood Drive, Huntington Beach, CA 92649', '17152 Sandra Lee Lane, Huntington Beach, CA 92649', '16752 Westfield Lane, Huntington Beach, CA 92649', '5266 Acorn Drive, Huntington Beach, CA 92649', '17432 Almelo Lane, Huntington Beach, CA 92649', '17321 Coronado Lane, Huntington Beach, CA 92647', '6051 Point Loma Drive, Huntington Beach, CA 92647', '17192 Lynn Ln, Huntington Beach, CA 92649', '17221 Apel Ln, Huntington Beach, CA 92649', '17491 Bellport Circle, Huntington Beach, CA 92649', '16351 Gentry Lane, Huntington Beach, CA 92647']
# geolocator = Nominatim(user_agent="Heyy im nick")
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
# import asyncio
# import time
# async def main():
#     task1 = asyncio.create_task(
#         say_after(1, 'hello'))
#
#     task2 = asyncio.create_task(
#         say_after(2, 'world'))
#
#     print(f"started at {time.strftime('%X')}")
#
#     # Wait until both tasks are completed (should take
#     # around 2 seconds.)
#     await task1
#     await task2
#
#

from googlesearch import search

def changing(address):
    # ioloop = asyncio.get_event_loop()


    results = search(f"{address} trulia", tld="co.in", num=3, stop=3, pause=2.0)
    # ioloop.close()
    for i in results:
        print(i)
        return i

#
# async def geolocate(address_list):

    # for i in range(0, len(address_list), 5):
    #     #coordinate = await geolocator.geocode(f'{i.split(",")[0]+i.split(",")[2]}')
    #
    #     task1 = asyncio.create_task(
    #         changing(address_list[i]))
    #
    #     task2 = asyncio.create_task(
    #         changing(address_list[i+1]))
    #
    #     task3 = asyncio.create_task(
    #         changing(address_list[i+2]))
    #
    #     task4 = asyncio.create_task(
    #         changing(address_list[i+3]))
    #
    #     task5 = asyncio.create_task(
    #         changing(address_list[i+4]))
    #
    #
    #
    #     await task1, task2, task3, task4, task5
    #
    #     print(task1.result(),
    #            task2.result(),
    #            task3.result(),
    #            task4.result(),
    #            task5.result())
    #
    # async def main(five_urls):
    #     # Schedule three calls *concurrently*:
    #     await asyncio.gather(
    #         changing(five_urls[0]),
    #         changing(five_urls[1]),
    #         changing(five_urls[2]),
    #         changing(five_urls[3]),
    #         changing(five_urls[4])
    #     )
    # for j in range(0, len(address_list), 5):
    #     print(1)
    #     asyncio.run(main(address_list))
    #     print(2)








#
# async def main(five_urls):
#     # Schedule three calls *concurrently*:
#     await asyncio.gather(
#         changing(five_urls[0]),
#         changing(five_urls[1]),
#         changing(five_urls[2]),
#         changing(five_urls[3]),
#         changing(five_urls[4])
#     )
#
#
# import asyncio
# asyncio.run(main(address_list))
# asyncio.run()

# ioloop = asyncio.get_event_loop()
# addresses_to_visit = ioloop.run_until_complete(geolocate(address_list))
# #
# asyncio.run(geolocate(address_list))

import threading

t0 = threading.Thread(target=changing, args=(address_list[0],))
t1 = threading.Thread(target=changing, args=(address_list[1],))
t2 = threading.Thread(target=changing, args=(address_list[2],))
t3 = threading.Thread(target=changing, args=(address_list[3],))
t4 = threading.Thread(target=changing, args=(address_list[4],))

# starting thread 1

# starting thread 2
t0.start(), t1.start(), t2.start(), t3.start(), t4.start()

# wait until thread 1 is completely executed
t0.join(), t1.join(), t2.join(), t3.join(), t4.join()
# wait until thread 2 is completely executed


# both threads completely executed
print("Done!")



    #
    #     coordinate = task1.result()
    #     #
    #     # coordinate = await changing(i, geolocator)
    #     # print(coordinate)
    #     if not coordinate:
    #         continue
    #     coordinate = [(coordinate.latitude, coordinate.longitude), i]
    #     coordinate[0] = pow((pow(coordinate[0][0]-main_coordinate.latitude, 2) + pow(coordinate[0][1]-main_coordinate.longitude, 2)), 0.5)
    #     not_sorted.append(coordinate)
    # print(not_sorted)

#asyncio.run(geolocate(address_list, "5341 Doverton Drive, Huntington Beach, CA 92649"))

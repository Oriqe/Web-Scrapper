import threading
from googlesearch import search






def changing(address, empty_list):
    # ioloop = asyncio.get_event_loop()


    results = search(f"{address} trulia", tld="co.in", num=1, stop=1)
    # ioloop.close()
    for i in results:
        print(i)
        empty_list.append(i)
        return i



def find_trulia_urls(address_list):
    empty_list = []

    t0 = threading.Thread(target=changing, args=(address_list[0], empty_list))
    t1 = threading.Thread(target=changing, args=(address_list[1], empty_list))
    t2 = threading.Thread(target=changing, args=(address_list[2], empty_list))
    t3 = threading.Thread(target=changing, args=(address_list[3], empty_list))
    t4 = threading.Thread(target=changing, args=(address_list[4], empty_list))



    t0.start(), t1.start(), t2.start(), t3.start(), t4.start()


    t0.join(), t1.join(), t2.join(), t3.join(), t4.join()
    return empty_list


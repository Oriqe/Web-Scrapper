from requests_html import HTML, HTMLSession, AsyncHTMLSession
from random import randint
#
# def text_extracter(url):
#
#     with HTMLSession() as s:
#         r = s.get(url, headers=req_headers)
#         r_html = HTML(html=r.text)
#         return r_html.text
#

from googlesearch import search
def google_address_direct(address):
    results = search(f"{address} trulia", tld="co.in", num=3, stop=3)
    for i in results:
        print(i)
        return i


#
# from requests_html import HTML, HTMLSession, AsyncHTMLSession
# from random import randint
# import asyncio
#
# async def text_extracter(url):
#     req_headers = {
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#         'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'en-US,en;q=0.8',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
#         'X-Forwarded-For': '.'.join([str(randint(0, 255)) for x in range(4)])
#     }
#     async with AsyncHTMLSession() as s:
#         async with s.get(url, headers=req_headers) as response:
#             await print(response.status)
#
#         # r = s.get(url, headers=req_headers)
#         # r_html = HTML(html=r.text)
#         # return r_html.text
#
# HTMLSession
# (text_extracter("https://www.zillow.com/homedetails/1651-Sand-Key-Estates-Ct-APT-36-Clearwater-FL-33767/47221746_zpid/"))
#


#
# class Gregory():
#     async def get_somthing(self, url, text=True):
#         req_headers = {
#             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#             'accept-encoding': 'gzip, deflate, br',
#             'accept-language': 'en-US,en;q=0.8',
#             'upgrade-insecure-requests': '1',
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
#             'X-Forwarded-For': '.'.join([str(randint(0, 255)) for x in range(4)])
#         }
#
#         asession = AsyncHTMLSession()
#
#
#         r = await asession.get(url, headers=req_headers)
#         r_html = HTML(html=r.text)
#         return r_html.text, "zillow"
import requests
import asyncio
from requests_html import AsyncHTMLSession, HTML
from requests_html import HTMLSession
from random import randint


def text_extracter(list):#url_zillow, url_trulia):
    req_headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.8',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
                'X-Forwarded-For': '.'.join([str(randint(0, 255)) for x in range(4)])
            }

    asession = AsyncHTMLSession()


    async def get_zillow():
        with requests.Session() as asession:
            r = await asession.get("https://www.trulia.com/p/fl/clearwater/1430-gulf-blvd-502-clearwater-fl-33767--2035884841", headers=req_headers)
            r_html = HTML(html=r.text)
            print(r_html.text)
            await r.html.arender(timeout=30, wait=3, reload=True)
            print("********************************************************")
            print("********************************************************")
            print("********************************************************")
            print("********************************************************")
            print("********************************************************")

            resp = r.html.html
            print(resp)

            resp = HTML(html=resp)




            return r_html, "zillow"

    async def get_realtor():
        r = await asession.get("https://www.realtor.com/realestateandhomes-detail/2077-59th-Way-N_Clearwater_FL_33760_M55258-77544", headers=req_headers)
        r_html = HTML(html=r.text)
        # print(r_html.text)
        # return r_html, "zillow"

    with AsyncHTMLSession() as s:

        async def get_trulia(address):
            url = await google_address_direct(address)
            r = await s.get(url, headers=req_headers)
            r_html = HTML(html=r.text)
            print("trulia finished")
            ggg = r_html.find("table", first=True)
            return r_html.text


            # for i in ggg:
            #     print(i.text)
        async def urlocator():
            import asyncio
            task0 = asyncio.create_task(
                google_address_direct(list[0]))
            # task1 = asyncio.create_task(
            #     google_address_direct(list[1]))
            # task2 = asyncio.create_task(
            #     google_address_direct(list[2]))
            # task3 = asyncio.create_task(
            #     google_address_direct(list[3]))
            # task4 = asyncio.create_task(
            #     google_address_direct(list[4]))
            # print(task0)
            await task0  #, task1, task2, task3, task4
            print(task0)
            await s.close()
    urlocator()

    # ggg = r_html.find("div", containing="See Virtual Tour", first=True)

    #
    # for i in ggg.find("li"):
    #     print(i.full_text)


    # maybe = r_html.find("div", containing="Baths" ,first=True)
    # maybe1 = r_html.find("div", containing="Beds", first=True)
    # maybe2 = r_html.find("div", containing="sqft", first=True)
    # maybe3 = r_html.find("table", containing="Date", first=True)
    # #
    # # print(maybe.full_text, maybe1.full_text, maybe2.full_text)

    # list1 = []
    # for j in maybe3.find("tbody"):
    #     for k in j.find("tr"):
    #         history = []
    #         if len(k.find("td")) == 1:
    #             list1[-1].append(k.find("td")[0].full_text)
    #         else:
    #             for g in k.find("td"):
    #                 history.append(g.full_text)
    #             list1.append(history)
    #
    # for h in list1:
    #     print(h)
    #
    #



        # lambda: get_xome("1505 chew rd", "44902", slug_xome_comp_sold, gathering_similar_homes),
        # lambda: get_xome("1505 chew rd", "44902", slug_xome_prop_facts, gathering_home_details),
        # lambda: get_xome("1505 chew rd", "44902", slug_xome_tax_history, gathering_tax_details),
        # lambda: get_xome("1505 chew rd", "44902", slug_xome_price_history, gathering_price_details)),
        #

        # ggg = asyncio.run(
        #     lambda: get_trulia(list[0]),
        #     lambda: get_trulia(list[1]),
        #     lambda: get_trulia(list[2]),
        #     lambda: get_trulia(list[3]),
        #     lambda: get_trulia(list[4])
        # )



        # ans = s.run(
        #     lambda: get_trulia(list[0]),
        #     lambda: get_trulia(list[1]),
        #     lambda: get_trulia(list[2]),
        #     lambda: get_trulia(list[3]),
        #     lambda: get_trulia(list[4])
        # )
        # return ans




test_address_list = ["1972 Whitney Oaks Blvd #6 clearwater florida 33760",
                    "1963 Whitney Oaks Blvd #18 clearwater florida 33760",
                    "1976 Levine Ln clearwater florida 33760",
                    "1840 Allendale Dr clearwater florida 33760",
                    "3200 Cove Cay Dr Unit 6B clearwater florida 33760"]



ioloop = asyncio.get_event_loop()

more_addresses_to_visit = ioloop.run_until_complete(text_extracter(test_address_list))

# url_list = []
# for i in test_address_list:
#     url_list.append(google_address_direct(i))

# r = text_extracter(test_address_list)
# print(r)
    #
    # print("before running the async")
    # zillow_and_trulia = asession.run(get_zillow, get_trulia, get_realtor)
    # for i in zillow_and_trulia:
    #     if i == None:
    #         zillow_and_trulia.remove(i)
    # if zillow_and_trulia[0][1] == "zillow":
    #     zillow = zillow_and_trulia[0][0]
    #     trulia = zillow_and_trulia[1][0]
    # else:
    #     zillow = zillow_and_trulia[1][0]
    #     trulia = zillow_and_trulia[0][0]
    # print("after running the async")
    #
    # return zillow, trulia





from bs4 import BeautifulSoup
import requests

req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}






req_headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.8',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
                'X-Forwarded-For': '.'.join([str(randint(0, 255)) for x in range(4)])
            }


async def zillow(url_zillow):
    # with AsyncHTMLSession() as s:
    #     url = "https://www.zillow.com/homedetails/2618-Cove-Cay-Dr-UNIT-406-Clearwater-FL-33760/47211992_zpid/"
    #     r = await s.get(url, headers=req_headers)
    #     print(r.text)
    #
        # await r.html.arender(timeout=30, wait=3, reload=True)
        # print(r.text)




    with AsyncHTMLSession() as asession:
        # r = await asession.get(url_zillow, headers=req_headers)
        print(1)



        print(2)


        r = await asession.get(url_zillow, headers=req_headers)
        print(3)

        #r = AsyncHTMLSession(r.html)
        # r = HTML(html=r.text)
        r = HTML(html=r.text)



        print(r.links)
        print("SFAAFSAFSAASFSAFA")
        print(r.full_text)

        print(3.5)
        await r.arender(timeout=30, wait=3, reload=True)
        print()

        #loop.create_task(await r.arender(timeout=30, wait=3, reload=True))
        #print(r.html.html)
        print(4)
        #loop.run_until_complete(r.html.arender(timeout=30, wait=3, reload=True))
        print(5)

        print(r.text)
        print(6666666666666666666666666666666666666666666666666666666666666666666666)
        # print(r.content)
        print(r.links)
        #print(r_html.text)
        print(77777777777777777777777777777777777777777777777777777777777777777777777)
        asession.close()

    return


        #await r.html.arender(timeout=30, wait=3, reload=True)
        #await task10

        #print(r.text)
        # await asyncio.wait_for(r.html, timeout=30)




#
#
# guess = asyncio.run(zillow("https://www.zillow.com/homedetails/2618-Cove-Cay-Dr-UNIT-406-Clearwater-FL-33760/47211992_zpid/"))
# #
# guess.close()

#text_extracter("https://www.zillow.com/homedetails/2618-Cove-Cay-Dr-UNIT-406-Clearwater-FL-33760/47211992_zpid/", "https://www.zillow.com/homedetails/2618-Cove-Cay-Dr-UNIT-406-Clearwater-FL-33760/47211992_zpid/")
# for i in j:
#     print(i.text)


#
# loop.run_until_complete()
#
# asession = AsyncHTMLSession()
#
# >>> r = await asession.get('https://python.org/')
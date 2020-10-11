# from requests_html import HTML, HTMLSession, AsyncHTMLSession
# from random import randint
#
# def text_extracter(url):
#
#     with HTMLSession() as s:
#         r = s.get(url, headers=req_headers)
#         r_html = HTML(html=r.text)
#         return r_html.text
#




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


from requests_html import AsyncHTMLSession, HTML
from requests_html import HTMLSession
from random import randint
import time



def gathering_similar_homes(page, address_list=[]):

    table_cells = page.find(".xw-widget-comparables-comp-property-row", first=False)

    similar_local_homes = []
    for i in table_cells:

        full_address = i.text.split("\n")[0]
        similar_local_homes.append(full_address)

    print(similar_local_homes)
    return similar_local_homes



def gathering_price_details(page):
    price_history = page.find(".js-xw-price-history-table-row", first=False)
    print(price_history)
    price_list = []
    for i in price_history:
        print(i.html)
        temp = i.text.split("\n")
        if temp[0] == "price":
            temp[0] = "price changed"
        temp_dict = {"event": temp[0], "date": temp[1], "price": temp[2]}
        price_list.append(temp_dict)
    return price_list


def gathering_tax_details(page):
    tax_history = page.find(".js-xw-tax-history-table-row", first=False)
    net = [i.text.split("$") for i in tax_history]
    tax_list = []

    for k in net:
        new_k = []
        for t in k:
            t = t.replace("\n", "")
            if "+" in t:
                t = t[:t.index("+")]
            if "-" in t:
                t = t[:t.index("-")]
            new_k.append(t)

        tax_dict = {"year": new_k[0], "property_taxes": new_k[1], "tax_assessment": new_k[2]}

        tax_list.append(tax_dict)

    return tax_list


def gather_home_details(page):
    page_dict = {}

    page_dict["state"] = page.find("#txtState", first=True).attrs.get("value")
    page_dict["city"] = page.find("#txtCity", first=True).attrs.get("value")
    page_dict["zip"] = page.find("#txtZip", first=True).attrs.get("value")
    page_dict["address"] = page.find("#txtAddress", first=True).attrs.get("value")

    property_fact = page.find(".xw-pf-table-cell", first=False)

    counter = 0

    while counter < len(property_fact):
        page_dict[property_fact[counter].text] = property_fact[counter + 1].text
        counter += 2

    return page_dict



def text_extracter(url_xome):
    req_headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.8',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
                'X-Forwarded-For': '.'.join([str(randint(0, 255)) for x in range(4)])
            }

    asession = AsyncHTMLSession()
    print(asession.headers)


    async def get_xome():
        r = await asession.get(url_xome, headers=req_headers)  #render(timeout=30, wait=3)#.html.arender(timeout=30, wait=3)

        r_html = HTML(html=r.text)
        print(len(r_html.html))

        await r.html.arender(timeout=30, wait=3)



        resp = r.html.html

        r = HTML(html=r.text)

        print(len(resp))


        print("****************************************")
        print("****************************************")
        print("****************************************")
        print("****************************************")
        print("****************************************")

        return resp

    async def get_another_xome():
        r = await asession.get(url_xome, headers=req_headers)  #render(timeout=30, wait=3)#.html.arender(timeout=30, wait=3)

        r_html = HTML(html=r.text)
        print(len(r_html.html))
        await r.html.arender(timeout=30, wait=3)
        resp = r.html.html
        print(len(resp))
        resp = HTML(html=resp)
        dicto = gathering_tax_details(resp)
        print(dicto)





        print("****************************************")
        print("****************************************")
        print("****************************************")
        print("****************************************")
        print("****************************************")

        return resp


    xome, xome2 = asession.run(get_xome, get_another_xome)
    return xome, xome2



xome_page, xome_page2 = text_extracter('https://x-api.xome.com/xda/web/widgets/SampleWidget?widget=TaxHistory&streetAddress="293SpringSt"&zip=07860')
# xome_page = text_extracter("https://x-api.xome.com/xda/web/widgets/SampleWidget?widget=PriceHistory")
# "https://x-api.xome.com/xda/web/widgets/SampleWidget?widget=TaxHistory"
print("?????????")
# print(xome_page)
# print(xome_page2)
#
# xome_page = xome_page[0].find("span#listing-info")
# listing_dict = {}
# j = ""
# j += str(xome_page[0])
# j = j.replace("<Element 'span' ", "")
#
# j = j.replace("'", "").split("data-")
# for i in j:
#     print(i)
#     key, value = i.split("=", 1)
#     if value != "" and value != " ":
#         listing_dict[key] = value.strip()
#
#
# print(listing_dict)
# for i in another_thing:
#     print(i)





# for kwarg in j:
#     key, value = kwarg.split("=")
#     listing_dict[key] = value
# #
# # listing_dict
# print(j)
# xome_page[0].remove("<Element 'span' ")


    #
    # async def get_trulia():
    #     r = await asession.get(url_trulia, headers=req_headers)
    #     r_html = HTML(html=r.text)

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

        # return r_html.text, "trulia"
        #
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
    #

# for i in j:
#     print(i.text)


#
# loop.run_until_complete()
#
# asession = AsyncHTMLSession()
#
# >>> r = await asession.get('https://python.org/')
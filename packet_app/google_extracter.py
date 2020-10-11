from googlesearch import search
from random import randint
req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    #'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'X-Forwarded-For': '.'.join([str(randint(0, 255)) for x in range(4)])
}



def google_address_direct(address):
    results = search(f"{address} trulia", tld="co.in", num=3, stop=3)
    for i in results:
        return i


test_address_list = ["1972 Whitney Oaks Blvd #6 clearwater florida 33760",
                    "1963 Whitney Oaks Blvd #18 clearwater florida 33760",
                    "1976 Levine Ln clearwater florida 33760",
                    "1840 Allendale Dr clearwater florida 33760",
                    "3200 Cove Cay Dr Unit 6B clearwater florida 33760"]

def getting_realtytrac(addresses):
    from requests.exceptions import ContentDecodingError


    from googlesearch import search
    from requests_html import HTML
    import requests_html
    import os
    from random import random, randint, choice
    req_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
        # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'X-Forwarded-For': '.'.join([str(randint(0, 255)) for x in range(4)])
    }
    ans = ""

    while True:

        with requests_html.AsyncHTMLSession() as s:
            for k, v in req_headers.items():
                s.headers[k] = v
            print(f"addresses:    {addresses}")
            print(1)
            try:

                async def getting_realtytrac_async():
                    print("******************")
                    ans = google_address_direct(addresses[0])
                    print(ans)
                    print("oneloha")
                    return ans
                    # return ans.html

                async def getting_realtytrac_async1():
                    print("******************")
                    ans = google_address_direct(addresses[1])
                    print(ans)
                    print("twoloha")

                async def getting_realtytrac_async2():
                    print("******************")
                    ans = google_address_direct(addresses[2])
                    print(ans)
                    print("treeloha")

                async def getting_realtytrac_async3():
                    print("******************")
                    ans = google_address_direct(addresses[3])
                    print(ans)
                    print("forloha")

                async def getting_realtytrac_asyns4():
                    print("******************")
                    ans = google_address_direct(addresses[4])
                    print(ans)
                    print("fivloha")

                if len(addresses) < 5:
                    dispatcher = {0: getting_realtytrac_async,
                                  1: getting_realtytrac_async1,
                                  2: getting_realtytrac_async2,
                                  3: getting_realtytrac_async3}
                    new_urls = []
                    for url in range(0, len(addresses) - 1):
                        new_urls.append(dispatcher[url])
                    print(*new_urls)
                    r = s.run(
                        *new_urls
                    )
                # import asyncio
                # getting_realtytrac_async()
                # getting_realtytrac_async1()
                # getting_realtytrac_async2()
                # getting_realtytrac_async3()
                # getting_realtytrac_asyns4()
                elif len(addresses) == 5:
                    r = s.run(getting_realtytrac_async,
                              getting_realtytrac_async1,
                              getting_realtytrac_async2,
                              getting_realtytrac_async3,
                              getting_realtytrac_asyns4)
                    print(f"this is R:  {r}")





            except UnboundLocalError as e:
                print(e)
                pass
            except Exception as e:
                print(10)
                print(e)
                home_details_dict = ""
            finally:
                print(11)
                s.close()
                break


from requests_html import HTML
import requests_html

with requests_html.HTMLSession() as s:
    for i in test_address_list:
        url = google_address_direct(i)
        print(url)

        r = s.get(url, headers=req_headers)
        if r.status_code != 200:
            continue
#
        r_html = HTML(html=r.text)

        print(r_html.text)
        ggg = r_html.find("div", containing="See Virtual Tour", first=True)


        # for i in ggg.find("li"):
        #     print(i.full_text)


        maybe = r_html.find("div", containing="Baths" ,first=True)
        maybe1 = r_html.find("div", containing="Beds", first=True)
        maybe2 = r_html.find("div", containing="sqft", first=True)
        maybe3 = r_html.find("table", containing="Date", first=True)
        #
        # print(maybe.full_text, maybe1.full_text, maybe2.full_text)

        list1 = []
        for j in maybe3.find("tbody"):
            for k in j.find("tr"):
                history = []
                if len(k.find("td")) == 1:
                    list1[-1].append(k.find("td")[0].full_text)
                else:
                    for g in k.find("td"):
                        history.append(g.full_text)
                    list1.append(history)

        for h in list1:
            print(h)

#
# ggg = getting_realtytrac(test_address_list)
# for i in ggg[0]:
#     print(i)

    #
    # new_results, address, new_link = [], address.lower().replace(" apt", "").replace(",", "").split(" "), ""
    #
    # for link in results:
    #     for letter in link:
    #         new_link += letter
    #
    #     new_link, counter = new_link.lower(), len(address)
    #
    #     for word in address:
    #         if word not in new_link:
    #             break
    #         counter -= 1
    #     if counter == 0:
    #         new_results.append(link)
    #
    # result_zillow, result_trulia = "", ""
    # for i in new_results:
    #     if result_zillow == "":
    #         if "zillow" in i:
    #             result_zillow = i
    #     if result_trulia == "":
    #         if "trulia" in i:
    #             result_trulia = i
    #     if result_trulia != "" and result_zillow != "":
    #         break
    #
    # return result_zillow, result_trulia


#
# for i in range(30):
#     print()
#     print()
#     print()
#     for j in google_address_direct("2836 eagle run cir e clearwater florida 33760"):
#         print(j)

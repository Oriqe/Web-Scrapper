from playwright import sync_playwright, async_playwright
from random import choice, randint
from requests_html import HTML
import requests_html
from requests.exceptions import ContentDecodingError
import asyncio
import requests


import aiohttp
import asyncio

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# #chrome_options.add_argument("--disable-extensions")
# #chrome_options.add_argument("--disable-gpu")
# #chrome_options.add_argument("--no-sandbox") # linux only
# chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works

# browser = webdriver.Chrome(options=chrome_options, executable_path=r"C:\Users\orikl\Desktop\Playground\chromedriver")
#
# browser.get("https://www.zillow.com/homedetails/689-Luis-Munoz-Marin-Blvd-APT-508-Jersey-City-NJ-07310/108625724_zpid/")
# # table = wait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="hdp-price-history"]//table')))
#
# print(browser.page_source)






def get_headers():
    user_agents = [
        # 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
        #            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
                   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41']

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'accept-encoding': 'gzip',
        'accept-language': 'en-GB,en;q=0.8,en-US;q=0.6,ml;q=0.4',
        'upgrade-insecure-requests': '*',
        'user-agent': choice(user_agents),
        'referer': 'https://google.com',
        'X-Forwarded-For': '.'.join([str(randint(0, 255)) for x in range(4)])
    }
    return headers








certain_url = 'https://www.zillow.com/homedetails/16608-Lake-Dr-W-Vancleave-MS-39565/78015814_zpid/'

#
# async def fetch(session, url):
#     async with session.get(url, headers=get_headers()) as response:
#         return await response.text()
#
# async def main():
#
#     async with aiohttp.ClientSession() as session:
#
#         html = await fetch(session, certain_url)
#         print(html)
#
# # if __name__ == '__main__':
# #     loop = asyncio.get_event_loop()
# #     loop.run_until_complete(main())
#
#
#
# from bs4 import BeautifulSoup
# import requests
# import re
#
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0"}
# r = requests.get("https://www.zillow.com/homes/recently_sold/Culver-City-CA/house,condo,apartment_duplex,townhouse_type/20432063_zpid/51617_rid/12m_days/globalrelevanceex_sort/34.048605,-118.340178,33.963223,-118.47785_rect/12_zm/", headers=get_headers())
# r_html = HTML(html=r.text)
# print(r_html.html)
# for i in r_html.html.split("\n"):
#     if 'AjaxRender.htm?' in i:
#         print(i)
# # urls = re.findall(re.escape('AjaxRender.htm?') + '(.*?)"', r_html.html)
# # print(urls)
# # url = "https://www.zillow.com/AjaxRender.htm?{}".format(urls[4])
# # r = requests.get(url, headers=headers)
# # print(r.text)
# # # ImportError
# # soup = BeautifulSoup(r.content.replace('\\', ''), "html.parser")
#
# data = []
# print(1)
# for tr in soup.find_all('tr'):
#     data.append([td.text for td in tr.find_all('td')])
#
# print(2)
#
# for row in data[:5]:        # Show first 5 entries
#     print(row)
#
#



# async def read_website():
#     async with aiohttp.ClientSession() as session:
#         async with session.get(certain_url) as resp:
#             await resp.read()
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(read_website())
# # Zero-sleep to allow underlying connections to close
# loop.run_until_complete(asyncio.sleep(0.25))
# loop.close()





import pandas as pd

url = 'https://www.trulia.com/p/fl/clearwater-beach/1430-gulf-blvd-502-clearwater-beach-fl-33767--2035884841?rd=1'
# d = pd.read_html(url)
#
# print(d)





# gg = requests.session()
# for k, v in get_headers().items():
#     gg.headers[k] = v
# a = gg.get(url)
# print(a.html)

options = {
            # 'executablePath': 'C:\\Users\\orikl\\Downloads\\chrome-win\\chrome.exe',
            'headless': True,
            'ignoreHTTPSErrors': True,
            'dumpio': True,
            # 'userDataDir': './tmp',
            'args': [
                # '--proxy-server=http://144.217.101.245:3129'
                # "--proxy-server='direct://'",
                # '--proxy-bypass-list=*',
                # '--enable-features=NetworkService',
                # NEW ONESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
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
                '--disable-gl-drawing-for-tests'
                # ORIGINAL ONESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
                # '--user-data-dir',
                # '--no-sandbox',
                # '--disable-setuid-sandbox',
                # '--disable-infobars',
                # '--window-position=0,0',
                # '--ignore-certifcate-errors',
                # '--ignore-certifcate-errors-spki-list',
                # END OF ORIGINAL ONESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
            ]
        }


def the_requesting_part(url):
    try:
        with requests_html.HTMLSession(browser_args=options) as s:
            for k, v in get_headers().items():
                s.headers[k] = v



            # g.html.render(timeout=50000)
            # # g = HTML(html=g.text)



            return s.get(url)

    except ContentDecodingError as e:
        print(e)
        s.close()
    except AttributeError as e:
        print(e)
        s.close()




print(the_requesting_part("https://www.zillow.com/homedetails/525-527-Wyoming-Ave-Scranton-PA-18509/239873937_zpid/").text)
raise ImportError
url = "https://www.realtor.com/realestateandhomes-detail/29141-Us-Hwy-19-N-Unit-161_Clearwater_FL_33761_M91937-10656?view=qv"
#
# for y in range(10):
#     page = the_requesting_part(url)
#     print(page)
#     # page.
#     page_html = HTML(html=page.text)
#     print(page_html.html)
#     for i in page_html.find("table", first=False):
#         print(i.text)
#     print(y)
# print(page_html.html)



optional = [
            '--proxy-server=http://82.81.169.142:80',
            # "--proxy-server='direct://'",
            # '--proxy-bypass-list=*',
            # '--enable-features=NetworkService',
            # NEW ONESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
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





#
# with sync_playwright() as p:


async def going_async():
    async with async_playwright() as p:

        print("START")


        browser = await p.chromium.launch(args=optional, headless=True)

        print(1)



        page = await browser.newPage()
        print(1.5)
        await page.setExtraHTTPHeaders(headers=get_headers())
        print(2)
        await page.goto('https://www.myip.com/', timeout=200000)
        print("https://www.myip.com/")
        print(page.url)
        current_page = await page.content()
        print(current_page)


            # raise ImportError
            # # print(current_page)
            # # print("""*************************************************************************************************
            # # *************************************************************************************************
            # # *************************************************************************************************
            # # *************************************************************************************************
            # # *************************************************************************************************
            # # *************************************************************************************************
            # # *************************************************************************************************
            # # *************************************************************************************************
            # # *************************************************************************************************""")
            # import time
            # print(2.5)
            # buttons = await page.querySelectorAll('div[display="flex"] button.ds-text-button')
            # print(3)
            # for btn in buttons:
            #
            #
            #     print(btn)
            #     print(3.1)
            #     await btn.click()
            #     print(await btn.textContent())
            #
            #     print(3.2)
            #     time.sleep(0.5)
            #     print(3.3)
            # time.sleep(1)
            # # current_page = HTML(html=await page.content())
            # # for i in current_page.find("tbody", first=False):
            # #     print(i.html)
            # #
            # #
            # #
            # #
            # # for i in ans.find("tr", first=False):
            # #     table_row = i.find("td", first=False)
            # #
            # #     if len(table_row) > 2:
            # #         row_data = {"DATE": table_row[0].text, "EVENT": table_row[1].text, "PRICE": table_row[2].text}
            # #         print(row_data)
            # #         if num == 2 or "Source" in row_data.keys():
            # #             history_data.append(row_data)
            #         num = 2
            #
            #         continue
            #     else:
            #         row_data["SOURCE"] = table_row[0].text
            #         print(row_data)
            #         history_data.append(row_data)
            #         num = 0
            #
            #     if num == 2:
            #         history_data.append(row_data)
            # print(url, history_data)
            #
            #
            # await page.close()


        # await browser.close()


# async def going_async11():
#     async with async_playwright() as p:
#         aa = await p.chromium.launch()


async def initiator():
    await going_async()




asyncio.get_event_loop().run_until_complete(initiator())

#
# import asyncio
# asyncio.get_event_loop().run_until_complete(going_async())




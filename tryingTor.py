from torrequest import TorRequest
from random import choice, randint


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



from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary("C:\\Users\\orikl\\Desktop\\Tor Browser\\Browser\\firefox.exe")
import tbselenium.common as cm
from tbselenium.tbdriver import TorBrowserDriver
from tbselenium.utils import launch_tbb_tor_with_stem


from selenium import webdriver

from stem import Signal
from stem.control import Controller
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

# signal TOR for a new connection
# def switchIP():
#     with Controller.from_port(port = 9051) as controller:
#         controller.authenticate()
#         controller.signal(Signal.NEWNYM)
#
# # get a new selenium webdriver with tor as the proxy
# def my_proxy(PROXY_HOST,PROXY_PORT):
#     fp = webdriver.FirefoxProfile()
#     # Direct = 0, Manual = 1, PAC = 2, AUTODETECT = 4, SYSTEM = 5
#     fp.set_preference("network.proxy.type", 1)
#     fp.set_preference("network.proxy.socks",PROXY_HOST)
#     fp.set_preference("network.proxy.socks_port",int(PROXY_PORT))
#     fp.update_preferences()
#
#     options = Options()
#     options.headless = True
#     return webdriver.Firefox(options=options, firefox_profile=fp, executable_path=r"C:\Users\orikl\Desktop\geckodriver")
#
# for x in range(10):
#     proxy = my_proxy("127.0.0.1", 9050)
#     proxy.get("https://whatsmyip.com/")
#     html = proxy.page_source
#     soup = BeautifulSoup(html, 'lxml')
#     print(soup.find("span", {"id": "ipv4"}))
#     print(soup.find("span", {"id": "ipv6"}))
#     switchIP()
import asyncio
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from requests_html import HTML
binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
options = Options()

options.binary = binary

options.headless = True



import asyncio
from concurrent.futures.thread import ThreadPoolExecutor

from selenium import webdriver

executor = ThreadPoolExecutor(10)

cap = DesiredCapabilities().FIREFOX.copy()
cap["marionette"] = True #optional
cap["headless"] = True




def scrape(url, *, loop):
    loop.run_in_executor(executor, scraper, url)


def scraper(url):
    try:
        driver = webdriver.Firefox(options=options, capabilities=cap, executable_path=r"C:\Users\orikl\Desktop\geckodriver")
        # driver = webdriver.Chrome("./chromedriver")
        driver.get(url)
        # print(driver.page_source)
        # for i in driver.page_source[0].split("\n"):
        #     if "history" in i:
        #         print(i)
        # print(driver.page_source[:1000])

        print("*************************************************************")
        print("*************************************************************")
        print("*************************************************************")
        print("*************************11111111111111111111*****************")
        print("continued")



    finally:
        found = False
        htmlified = HTML(html=driver.page_source)
        driver.quit()


        for i in htmlified.html.split("\n"):
            if "See complete tax history" in i:
                print(i[:1000])
                found = True
        if not found:
            print("didnt find it")
            for i in htmlified.html.split("\n"):
                if "human" in i or "Human" in i:
                    print(i)

        print("FFFFFFFFFFFFFFFFFIINISHED")
            # print(driver.page_source)
            # print(driver.page_source)


loop = asyncio.get_event_loop()
for url in ["https://www.zillow.com/homedetails/525-527-Wyoming-Ave-Scranton-PA-18509/239873937_zpid/"] * 20:
    scrape(url, loop=loop)

loop.run_until_complete(asyncio.gather(*asyncio.all_tasks(loop)))




# webdriver.Firefox
# cap = DesiredCapabilities().FIREFOX.copy()
# cap["marionette"] = True #optional
# cap["headless"] = True
# print(cap)
# print(binary)
# async def tor_async():
#     driver = webdriver.Firefox(options=options, capabilities=cap, executable_path=r"C:\Users\orikl\Desktop\geckodriver")
#     # driver.se
#     driver.get("https://www.zillow.com/homedetails/525-527-Wyoming-Ave-Scranton-PA-18509/239873937_zpid/")
#     print("Firefox Initialized")
#     print(driver.page_source[:100])
#     driver.quit()

#
# async def gatherer():
#     asyncio.gather(await tor_async())
# #

#
# asyncio.get_event_loop().run_until_complete.([tor_async() for i in range(5)])

#



















# profile = webdriver.FirefoxProfile()
# profile.set_preference("network.proxy.type", 1)
# profile.set_preference("network.proxy.socks", "127.0.0.1")
# profile.set_preference("network.proxy.socks_port", 9050)
# profile.set_preference("network.proxy.socks_version", 5)
#
#
# profile.update_preferences()
#
# driver = webdriver.Firefox(firefox_profile=profile, executable_path="C:\\Users\\orikl\\Desktop\\Tor Browser\\Browser\\firefox.exe")
# import time
# time.sleep(10)
# driver.get("http://whatismyip.com")
# print(driver.page_source)
# tbb_dir =  "C:\\Users\\orikl\\Desktop\\Tor Browser\\Browser\\firefox.exe"
# profile = webdriver.FirefoxProfile()
# profile.set_preference("network.proxy.type", 1)
# profile.set_preference("network.proxy.socks", "127.0.0.1")
# profile.set_preference("network.proxy.socks_port", 9050)
# profile.set_preference("network.proxy.socks_version", 5)
# profile.update_preferences()
# driver = webdriver.Firefox(firefox_profile=profile)
# tor_process = launch_tbb_tor_with_stem(tbb_path=tbb_dir)
# with TorBrowserDriver(tbb_dir, tor_cfg=cm.USE_STEM) as driver:
#     driver.load_url("https://check.torproject.org")
#     print(driver.page_source)
# tor_process.kill()

#
# with TorRequest() as tr:
#     tr.session.headers = get_headers()
#     # response = tr.session.get('https://www.zillow.com/137-Orchard-St-White-Plains-NY-1060,4/32975063_zpid/')
#     # # response = tr.get('https://www.zillow.com/137-Orchard-St-White-Plains-NY-10604/32975063_zpid/')
#     #
#     # print(response.content)
#
#     response = tr.get('https://www.zillow.com/homedetails/15-Garretson-Rd-White-Plains-NY-10604/32975103_zpid/')
#
#
#     'HDP_ZESTIMATE_LIST_PRICE'
#
#     print(response.content)
#

# from pytor import pytor
# tor = pytor()
# html = tor.get('http://bradheath.org')
# print(html)
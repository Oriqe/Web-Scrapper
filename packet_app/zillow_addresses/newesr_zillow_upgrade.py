from requests_html import HTML
from random import randint, choice
import pyppeteer
from pyppeteer_stealth import stealth
# from ..zillow_addresses.zillow_funcs import async_requesting_part
# from .zillow_funcs import async_requesting_part
import time
import asyncio



def get_headers():
    user_agents = ['Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
                   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
                   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41']

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'accept-encoding': 'gzip , vary',
        'accept-language': 'en-GB,en;q=0.8,en-US;q=0.6,ml;q=0.4',
        'upgrade-insecure-requests': '*',
        'user-agent': choice(user_agents),
        'referer': 'https://google.com',
        'X-Forwarded-For': '.'.join([str(randint(0, 255)) for x in range(4)])
    }
    return headers






# async def helper_func():
#     page = await asyncio.gather(trying_something_different())
#     return page
async def trying_something_different():
    # browser = await pyppeteer.launch({
    #     'executablePath': 'C:\\Users\\orikl\\Downloads\\chrome-win\\chrome.exe',
    #     'headless': True,
    #     'ignoreHTTPSErrors': True,
    #     'dumpio': True,
    #     # 'userDataDir': './tmp',
    #     'args': [
    #         # '--proxy-server=http://144.217.101.245:3129'
    #         # "--proxy-server='direct://'",
    #         # '--proxy-bypass-list=*',
    #         # '--enable-features=NetworkService',
    #         # NEW ONESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
    #         '--autoplay-policy=user-gesture-required',
    #         '--disable-background-networking',
    #         '--disable-background-timer-throttling',
    #         '--disable-backgrounding-occluded-windows',
    #         '--disable-breakpad',
    #         '--disable-client-side-phishing-detection',
    #         '--disable-component-update',
    #         '--disable-default-apps',
    #         '--disable-dev-shm-usage',
    #         '--disable-domain-reliability',
    #         '--disable-extensions',
    #         '--disable-features=AudioServiceOutOfProcess',
    #         '--disable-hang-monitor',
    #         '--disable-ipc-flooding-protection',
    #         '--disable-notifications',
    #         '--disable-offer-store-unmasked-wallet-cards',
    #         '--disable-popup-blocking',
    #         '--disable-print-preview',
    #         '--disable-prompt-on-repost',
    #         '--disable-renderer-backgrounding',
    #         '--disable-setuid-sandbox',
    #         '--disable-speech-api',
    #         '--disable-sync',
    #         '--disk-cache-size=33554432',
    #         '--hide-scrollbars',
    #         '--ignore-gpu-blacklist',
    #         '--metrics-recording-only',
    #         '--mute-audio',
    #         '--no-default-browser-check',
    #         '--no-first-run',
    #         '--no-pings',
    #         '--no-sandbox',
    #         '--no-zygote',
    #         '--password-store=basic',
    #         '--use-mock-keychain',
    #         '--disable-gl-drawing-for-tests'
    #         # ORIGINAL ONESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
    #         # '--user-data-dir',
    #         # '--no-sandbox',
    #         # '--disable-setuid-sandbox',
    #         # '--disable-infobars',
    #         # '--window-position=0,0',
    #         # '--ignore-certifcate-errors',
    #         # '--ignore-certifcate-errors-spki-list',
    #         # END OF ORIGINAL ONESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
    #     ]
    # })

    optional = [
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
        '--disable-gl-drawing-for-tests',
        '--blink-settings=imagesEnabled=false']
    from playwright import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=optional, headless=True) 
        return browser


async def deeper_zillow(url, info, browser):

    ############################################################# first stage


    ############################################################# end of first stage
    # browser = await trying_something_different()
    content_flag = True
    repeat_count = 0
    while content_flag:
        content_flag = False
        print("this is what supposed to come next")
        print(pyppeteer.version_info)

        # browser = await pyppeteer.launch({
        #     'executablePath': 'C:\\Users\\orikl\\Downloads\\chrome-win\\chrome.exe',
        #     'headless': True,
        #     'ignoreHTTPSErrors': True,
        #     'dumpio': True,
        #     # 'userDataDir': './tmp',
        #     'args': [
        #         # '--proxy-server=http://144.217.101.245:3129'
        #         # "--proxy-server='direct://'",
        #         # '--proxy-bypass-list=*',
        #         # '--enable-features=NetworkService',
        #         # NEW ONESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
        #         '--autoplay-policy=user-gesture-required',
        #         '--disable-background-networking',
        #         '--disable-background-timer-throttling',
        #         '--disable-backgrounding-occluded-windows',
        #         '--disable-breakpad',
        #         '--disable-client-side-phishing-detection',
        #         '--disable-component-update',
        #         '--disable-default-apps',
        #         '--disable-dev-shm-usage',
        #         '--disable-domain-reliability',
        #         '--disable-extensions',
        #         '--disable-features=AudioServiceOutOfProcess',
        #         '--disable-hang-monitor',
        #         '--disable-ipc-flooding-protection',
        #         '--disable-notifications',
        #         '--disable-offer-store-unmasked-wallet-cards',
        #         '--disable-popup-blocking',
        #         '--disable-print-preview',
        #         '--disable-prompt-on-repost',
        #         '--disable-renderer-backgrounding',
        #         '--disable-setuid-sandbox',
        #         '--disable-speech-api',
        #         '--disable-sync',
        #         '--disk-cache-size=33554432',
        #         '--hide-scrollbars',
        #         '--ignore-gpu-blacklist',
        #         '--metrics-recording-only',
        #         '--mute-audio',
        #         '--no-default-browser-check',
        #         '--no-first-run',
        #         '--no-pings',
        #         '--no-sandbox',
        #         '--no-zygote',
        #         '--password-store=basic',
        #         '--use-mock-keychain',
        #         '--disable-gl-drawing-for-tests'
        #         # ORIGINAL ONESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
        #         # '--user-data-dir',
        #         # '--no-sandbox',
        #         # '--disable-setuid-sandbox',
        #         # '--disable-infobars',
        #         # '--window-position=0,0',
        #         # '--ignore-certifcate-errors',
        #         # '--ignore-certifcate-errors-spki-list',
        #         # END OF ORIGINAL ONESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
        #     ]
        # })
        import random
        # time.sleep(randint(1, 10) / 10)
        await asyncio.sleep(randint(1, 10) / 10)
        ###################################################################
        # Create a new incognito browser context.
        print("alpha")
        # context = await browser.createIncognitoBrowserContext()
        # Create a new page in a pristine context.
        print("beta")

        page = await browser.newPage()

        # await stealth(page)
        # await page.setViewport({'width': 800, 'height': 600})
        # await page.setRequestInterception(True)
        # page.on('request', """(req) => {
        # if(req.resourceType() === 'image'){
        #     req.abort();
        # }
        # else {
        #     req.continue();
        # }""")
        print("gamma?")
        # Do stuff
        ##########################################################################



        print("a")
        # page = await browser.newPage()
        print("b")

        await page.setExtraHTTPHeaders(headers=get_headers())
        print("c")
        # time.sleep(randint(0, 10)/10)
        await asyncio.sleep(randint(5, 15) / randint(10, 20) * random.random())
        await page.goto(url, timeout=200000)
        print("d")


        # await page.waitFor('section#price-and-tax-history')
        temp_content = await page.content()
        print("d-----------------------------------")
        temp_c = HTML(html=temp_content)
        print("d+++++++++++++++++++++++++++++++++++")



        ###################################################################################
        # print("d.5")
        # element = await page.querySelector('section#price-and-tax-history')
        # print("e")
        if len(temp_c.html) < 10000:
            print("found a SHORT ONE")
            print(page)
            print(temp_c.html)
            print("ANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNOTHERR RETRY")

            content_flag = True
            time.sleep(20)
            continue
        found = False
        for h in temp_c.find("th", first=False):
            if "EVENT" in h.html:
                found = True




        if not found:
            if "Price history is unavailable." not in temp_c.html:



                print(temp_c.html)
                print("MAJOR FUCKER")
                print("ANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNOTHERR RETRY")

                content_flag = True
                # time.sleep(5)
                # await asyncio.sleep(5)
                continue

        # new_element = temp_c.find("section#price-and-tax-history", first=True)
        #
        # if new_element:
        #     print("ELEMENT IS TRUE")
        # else:
        #     print("ELEMENT IS FALSEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        # if not new_element:

        c = temp_c



        if "See complete price history" in c.html:


            print("almost f", url)
            # btn = await page.Jx('//button[text()="See complete price history"]')
            # button = await page.querySelector('text="See complete price history"')
            # button = await page.waitForSelector('text="See complete price history"')
            # print(button)

            print("hello")
            # time.sleep(1)
            # await page.waitForSelector(btn)

            await page.click('text="See complete price history"', timeout=200000)
            # time.sleep(0.5)
            await asyncio.sleep(0.5)

            print("BYE")
            # time.sleep(0.3)
            await asyncio.sleep(0.3)
            print("g")
            repeater = False

            while not repeater:

                content = await page.content()
                c = HTML(html=content)
                for k in c.find("button.ds-text-button", first=False):
                    print(k.html)
                    print("SAAAAAAAAAAAAAAPAAAAAAAARAAAAAAAAAAAAAAAAAAAAAATOOOOOOOOOOOOOOOOR")
                    print(k.text)
                    if "price history" in k.text:
                        if "See less price history" in k.text:
                            print("found it!! ain't repeating shit")
                            repeater = True
                            break
                        elif "See complete price history" in k.text:
                            print("didnt change the button at all, repeating now...")
                            # for btn in buttons:
                            await page.click('text="See complete price history"', timeout=200000)
                            # time.sleep(0.5)
                            await asyncio.sleep(0.5)
                        else:
                            print("something weird, didnt find anything, repeating now...")
                            # for btn in buttons:
                            await page.click('text="See complete price history"', timeout=200000)
                            # time.sleep(0.5)
                            await asyncio.sleep(0.5)

                        # time.sleep(1)
                        await asyncio.sleep(1)

                    # print(btn)
                    # print(btn.toString())
                    # gg = await btn.getProperties()
                    #
                    # print(gg.keys())
                    # print(gg.items())
                    # print(gg.values())


                    # await btn.click()
                # print(button)
                # print("let's start clicking")
                # await button.click()
                # print("finished my click duty")

                #
                # print(button)
                # for i in btn:
                #     print("let's start clicking")
                #     await i.click()
                #     # time.sleep(1)
                #     print("finished my click duty")



            # else:
            #     print(c.html, url)
            #     print("RETRYYYYYYYYYYYYYYYYYYYIIIIIIINNNNNNNNNNNGGGGGGGGGGGG")
            #     content_flag = True
            #     continue

        print("f")


        print("h")
        # content = await page.evaluate('() => document.body.innerHTML')



        print("ds button view")


        print(len(c.html))
        gg = c.find("tbody", first=False)
        history_data = []
        print(type(gg))
        print(isinstance(gg, list))

        for i in gg:
            print(i.html)

        print(gg)
        if gg==[]:
            content_flag = True
            print("about to continue")
            repeat_count += 1
            print("IM HERERERE")
            # time.sleep(0.5)
            await asyncio.sleep(0.5)
            await page.close()
            # await browser.close()
            return [], info
            # print(repeat_count)
            # print(c.url)
            # print(url)
            # if repeat_count > 2:
            #     # await page.waitFor(3000)
            #     time.sleep(0.5)
            #     await page.close()
            #     # await browser.close()
            #     return [], info
            # continue
            # await browser.close()

        if len(gg)==1 and "Source:" not in gg[0].html:
            # time.sleep(0.5)
            await asyncio.sleep(0.5)
            await page.close()
            # await browser.close()
            return [], info
            content_flag = True
            print("about to continue")
            repeat_count += 1
            print("IM HERERERE")

            print(repeat_count)
            print(c.url)
            print(url)
            if repeat_count > 2:
                # await page.waitFor(3000)
                # time.sleep(0.5)
                await asyncio.sleep(0.5)
                await page.close()
                # await browser.close()
                return [], info
            continue
        # if len(gg)==1 and "Source:" in gg[0].html:
        #     gg.append(gg[0])
        num = 0
        finder = False
        ans = None
        for k in gg:
            if "Source" in k.html:
                ans = k
                finder = True

        if not finder and len(gg)>=2:
            # await page.waitFor(3000)
            # time.sleep(0.5)
            await asyncio.sleep(0.5)
            await page.close()
            # await browser.close()
            return [], info
        if not ans:
            # time.sleep(0.5)
            await asyncio.sleep(0.5)
            await page.close()
            # await browser.close()
            return [], info
            repeat_count += 1
            print("LOL")
            print(repeat_count)
            print(url)
            print(c.url)
            if repeat_count > 2:
                # await page.waitFor(3000)
                # time.sleep(0.5)
                await asyncio.sleep(0.5)
                await page.close()
                # await browser.close()
                return [], info

            continue
        for i in ans.find("tr", first=False):
            table_row = i.find("td", first=False)

            if len(table_row) > 2:
                row_data = {"DATE": table_row[0].text, "EVENT": table_row[1].text, "PRICE": table_row[2].text}
                print(row_data)
                if num == 2 or "Source" in row_data.keys():
                    history_data.append(row_data)
                num = 2

                continue
            else:
                row_data["SOURCE"] = table_row[0].text
                print(row_data)
                history_data.append(row_data)
                num = 0

            if num == 2:
                history_data.append(row_data)
        print(url, history_data)
        # await page.waitFor(3000)
        # time.sleep(0.5)
        await asyncio.sleep(0.5)
        await page.close()
        # await browser.close()
        return history_data, info


        # if new_element:
        #
        #     print("section view")
        #     print(1)
        #     element = await page.querySelector('section#price-and-tax-history')
        #     print(element)
        #     print(1.5)
        #     # arlong = await page.evaluate(
        #     #     """() => {")
        #         # arlong.setAttribu
        #     #             #     const arlong = document.getElementById('price-and-tax-history')
        #     #             #
        #     #             #     arlong.click()}""te('class', "home-details-collapsible-component-CollapsibleContainer', 'collapsible'")
        #         # return arlong}""")
        #     # arlong.setAttribute('class', "home-details-collapsible-component-CollapsibleContainer collapsible")
        #     # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        #     # print(arlong)
        #     # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        #     # print(element)
        #     # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        #     # await element.getProperties()
        #     # print(element.getProperties())
        #     # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        #     # await element.__setattr__("class", ('home-details-collapsible-component-CollapsibleContainer', 'collapsible'))
        #     # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        #     # await element.getProperties()
        #     # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        #     # print(element.getProperties())
        #     # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        #     # # await element.press(key="Enter")
        #     await element.click()
        #
        #     print(2)
        #     # time.sleep(1)
        #     await asyncio.sleep(1)
        #     print(3)
        #     # await page.waitFor("body")
        #     print(3.5)
        #     content = await page.content()
        #
        #     # content = await page.evaluate('() => document.body.innerHTML')
        #     print(4)
        #     print("7/2/1999" in content)
        #     c = HTML(html=content)
        #     print(5)
        #
        #     price_his = c.find("section#price-and-tax-history", first=True)
        #     if price_his:
        #         print(price_his)
        #         print("PRICE HIST")
        #     else:
        #         print(c.html)
        #         print("c.html")
        #     print(c.url)
        #     print(url)
        #     print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
        #
        #
        #     price_history = price_his.find("tbody", first=False)
        #     if not price_history:
        #
        #         print(f"price_history: {price_his.html}")
        #         content_flag = True
        #         continue
        #     print("niether am i supposed to be next")
        #     history_data = []
        #     for i in price_history:
        #         for j in i.find("tr", first=False):
        #
        #             row_data = {}
        #             table_row = j.find("td", first=False)
        #             row_data["DATE"] = table_row[0].text
        #             row_data["EVENT"] = table_row[1].text
        #             row_data["PRICE"] = table_row[2].text
        #             history_data.append(row_data)
        #     print(url, history_data)
        #     print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
        #
        #
        #     print(len(c.html))
        #     print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        #     # await page.waitFor(3000)
        #     # time.sleep(1.5)
        #     await asyncio.sleep(1.5)
        #     await page.close()
        #     # await browser.close()
        #     return history_data, info




# asyncio.get_event_loop().run_until_complete(deeper_zillow('https://www.zillow.com/homes/25486390_zpid/'))




        #
        #
        # print("d.5")
        # element = await page.querySelector('section#price-and-tax-history')
        # print("e")
        # if element:
        #     print("ELEMENT IS TRUE")
        # else:
        #     print("ELEMENT IS FALSEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        # if not element:
        #     content = await page.content()
        #     c = HTML(html=content)
        #
        #     if "See complete price history" in c.html:
        #         print("almost f", url)
        #         btn = await page.Jx('//button[text()="See complete price history"]')
        #         print(btn)
        #         for i in btn:
        #             print("let's start clicking")
        #             await i.press(key="Enter")
        #             # time.sleep(1)
        #             print("finished my click duty")
        #         time.sleep(1)
        #         print("g")
        #
        #     if len(c.html) < 10000:
        #         print("found a SHORT ONE")
        #         print(c.html)
        #         print("ANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNOTHERR RETRY")
        #
        #         content_flag = True
        #         continue
        #
        #     # else:
        #     #     print(c.html, url)
        #     #     print("RETRYYYYYYYYYYYYYYYYYYYIIIIIIINNNNNNNNNNNGGGGGGGGGGGG")
        #     #     content_flag = True
        #     #     continue
        #
        #     print("f")
        #
        #
        #     print("h")
        #     # content = await page.evaluate('() => document.body.innerHTML')
        #
        #
        #
        #
        #     print("ds button view")
        #
        #     print("7/2/1999" in content)
        #     print(len(c.html))
        #     gg = c.find("tbody", first=False)
        #     history_data = []
        #     print(type(gg))
        #     print(isinstance(gg, list))
        #
        #     for i in gg:
        #         print(i.html)
        #
        #     if len(gg)==1:
        #         content_flag = True
        #         print("about to continue")
        #         continue
        #
        #     for i in gg[1].find("tr", first=False):
        #         table_row = i.find("td", first=False)
        #         if len(table_row) > 2:
        #             row_data = {"DATE": table_row[0].text, "EVENT": table_row[1].text, "PRICE": table_row[2].text}
        #         else:
        #             row_data["SOURCE"] = table_row[0].text
        #             history_data.append(row_data)
        #     print(url ,history_data)
        #     return history_data, info
        #
        #
        # if element:
        #     print("section view")
        #     print(1)
        #     await element.click()
        #     print(2)
        #     time.sleep(2)
        #     print(3)
        #     content = await page.content()
        #
        #     # content = await page.evaluate('() => document.body.innerHTML')
        #     print(4)
        #     print("7/2/1999" in content)
        #     c = HTML(html=content)
        #     print(5)
        #
        #     price_history = c.find("section#price-and-tax-history", first=True)
        #     print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
        #     price_history = price_history.find("tbody", first=False)
        #     if not price_history:
        #         content_flag = True
        #         continue
        #     print("niether am i supposed to be next")
        #     history_data = []
        #     for i in price_history:
        #         for j in i.find("tr", first=False):
        #
        #             row_data = {}
        #             table_row = j.find("td", first=False)
        #             row_data["DATE"] = table_row[0].text
        #             row_data["EVENT"] = table_row[1].text
        #             row_data["PRICE"] = table_row[2].text
        #             history_data.append(row_data)
        #     print(history_data)
        #     print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
        #
        #
        #     print(len(c.html))
        #     print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        #     return history_data, info
        #
        #

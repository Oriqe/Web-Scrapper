from random import random, randint, choice
import requests_html
from requests_html import HTML
from packet_app.trulia.get_trulia_address_via_google import find_trulia_urls
from packet_app.trulia.gathering_trulia import gathering_price_history_trulia

s = requests_html.AsyncHTMLSession()


req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'X-Forwarded-For': '.'.join([str(randint(0, 255)) for x in range(4)])
}


async def getting_realtytrac_async(url):


    for k, v in req_headers.items():
        s.headers[k] = v

    ans = await s.get(url)

    ans = HTML(html=ans.text)
    history_list = gathering_price_history_trulia(ans)
    return history_list


def main(addresses):
    s = requests_html.AsyncHTMLSession()
    urls = find_trulia_urls(addresses)

    g = s.run(lambda: getting_realtytrac_async(urls[0]),
              lambda: getting_realtytrac_async(urls[1]),
              lambda: getting_realtytrac_async(urls[2]),
              lambda: getting_realtytrac_async(urls[3]),
              lambda: getting_realtytrac_async(urls[4]))
    print(g)


if __name__ == "__main__":
    main()


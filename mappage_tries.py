from requests.exceptions import ContentDecodingError
from requests_html import HTML
import requests_html
from random import randint


def the_requesting_part(url):
    req_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
        'X-Forwarded-For': '.'.join([str(randint(0, 255)) for x in range(4)])
    }

    with requests_html.HTMLSession() as s:
        for k, v in req_headers.items():
            s.headers[k] = v

        return s.get(url)


def adding_the_page_number(page_number, url):
    page_number += 1
    if page_number > 1:
        if page_number == 2:
            url = url + f"/{page_number}_p/"
        else:
            url = url.replace(f"/{page_number-1}_p/", f"/{page_number}_p/")
        # url = url + f"/{page_number}_p/"
    return url, page_number


def adding_the_beds_number(url, bed_number):
    if bed_number == 1:
        url = url + f"{bed_number}-{bed_number}_beds"
        bed_number += 1
    elif bed_number > 1:
        url = url.replace(f"{bed_number-1}-{bed_number-1}_beds", f"{bed_number}-{bed_number}_beds")
        bed_number += 1
    return url, bed_number


def get_zillow(city, state, zip_code):


    print("?????????????????????????????/")
    bed_number = 0
    p_counter, p, rent_counter = 0, 0, 0

    url_to_scrape = f"https://www.zillow.com/{city}-{state}-{zip_code}/sold"

    line_of_dicts = []

    while True:
        try:

            url_to_scrape, p_counter = adding_the_page_number(p_counter, url_to_scrape)

            r = the_requesting_part(url_to_scrape)

            print(p_counter, r.url)

            r_html = HTML(html=r.text)
            
            result_number = int(r_html.find("span.result-count", first=True).text.split(" ")[0].replace(",", ""))



            if result_number > 800 and "_beds" not in url_to_scrape:
                if "_beds" not in url_to_scrape or bed_number > 0 and "_baths" not in url_to_scrape:
                    url_to_scrape, bed_number = adding_the_beds_number(url_to_scrape, bed_number)
                    continue

            if not result_number and "_beds" in url_to_scrape:
                url_to_scrape, bed_number = adding_the_beds_number(url_to_scrape, bed_number)
                continue


            if "_p/" not in r.url and p_counter > 1 and "_beds" not in r.url:  # NO OVERRFLOW checking if finished available houses or passed 20

                if "sold" in r.url:  # finished the sold section, going into the for sale section
                    url_to_scrape = f"https://www.zillow.com/{city}-{state}-{zip_code}"
                    p_counter = 0
                    continue
                elif "sold" not in r.url and rent_counter == 0:  # NO OVERFLOW finished the for sale section, going into the rent section
                    url_to_scrape = f"https://www.zillow.com/{city}-{state}-{zip_code}/rent"
                    p_counter = 0
                    rent_counter += 1
                    continue
                break

            if "_p/" not in r.url and p_counter > 1 and "_beds" in r.url: # OVERFLOW checking if finished filtered section
                if bed_number > 5:
                    break
                url_to_scrape, bed_number = adding_the_beds_number(url_to_scrape, bed_number)
                continue



            print("start of change")
            temp_list = get_zillow_addresses(r_html)
            print("end of function change")
            line_of_dicts.extend(temp_list)
            print("end of line of dicts partial extension")
            print(len(line_of_dicts))

        except ContentDecodingError as e:
            print(e)
            s.close()
        except AttributeError as e:
            print(e)
            s.close()

    for k in line_of_dicts:
        print(k)
    return line_of_dicts



def gathering_price_history_trulia(page):
    price_history = []
    tables = page.find("tbody", first=False)

    for i in tables:
        if 'data-testid' in i.attrs.keys():
            if 'price-history-event' in i.attrs['data-testid']:
                temp_dict = {}
                price_info = i.find("tr", first=True).find("td", first=False)
                temp_dict["date"] = price_info[0].text
                temp_dict["price"] = price_info[1].text
                temp_dict["event"] = price_info[2].text

                price_history.append(temp_dict)
    for i in page.find("ul", first=False):
        if "home-features" in i.attrs.values():
            print(19000)
            for j in i.find("li", first=False):
                print(j.text)
                if "Days" in j.text:
                    print("&&&&&&&&&&&&&&&&&&&&&&")
                    print(j.text)
    #         # for j in i.find("li", first=False):
            #     if "Days on Trulia" in j.text:
            #         print(j.text)
    print(price_history)
    return price_history

def gathering_comparable_homes(page):
    table_rows = page.find(".nearby-homevalues-properties", first=True).find("li", first=False)
    comparable_homes = []
    counter = 0
    for i in table_rows[1:]:
        page_dict = {}
        link = i.find("a", first=True).links.pop()
        mini_list = i.text.split("\n")
        page_dict[f"address{counter}"] = mini_list[0]
        page_dict[f"estimate{counter}"] = mini_list[1]
        page_dict[f"link{counter}"] = link
        comparable_homes.append(page_dict)
        counter += 1
    print(comparable_homes)


def gathering_tax_history(page):
    table_rows = page.find("#ldp-history-taxes", first=True).find("tr", first=False)
    price_history_list = []

    for i in range(1, len(table_rows)):
        price_history_dict = {}
        table_data = table_rows[i].text.split("\n")
        price_history_dict[f"date{i}"] = table_data[0]
        price_history_dict[f"taxes{i}"] = table_data[1]
        price_history_dict[f"land{i}"] = table_data[2]
        price_history_dict[f"addition{i}"] = table_data[4]
        price_history_dict[f"total_assessment{i}"] = table_data[6]

        price_history_list.append(price_history_dict)

def gathering_price_history_realator(page):
    table_rows = page.find("#ldp-history-price", first=True).find("tr", first=False)
    price_history_list = []
    indexer = 1
    price_history_dict = {}
    for i in range(len(table_rows)):
        table_data = table_rows[i].text.split("\n")
        price_history_dict[f"date{i}"] = table_data[0]
        price_history_dict[f"event{i}"] = table_data[1]
        price_history_dict[f"price{i}"] = table_data[2]
        if len(table_data) > 3:
            price_history_dict[f"price/sqft{i}"] = table_data[3]
        if len(table_data) > 4:
            price_history_dict[f"source{i}"] = table_data[4]
        price_history_list.append(price_history_dict)
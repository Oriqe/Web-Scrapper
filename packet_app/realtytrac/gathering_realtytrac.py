

def gathering_price_history(page):
    try:
        price_table = page.find("table.history-table", first=False)
        for table in price_table:

            if table.attrs["class"] == ('sales-table', 'history-table'):

                price_table = table
                break

        dict_list = []
        for report in price_table.find("tr", first=False)[1:]:
            report_dict = {}
            splitted_report = report.text.split("\n")

            report_dict["date"] = splitted_report[0]
            report_dict["event"] = splitted_report[1]
            report_dict["price"] = splitted_report[2]
            report_dict["price/sqft"] = splitted_report[3]
            report_dict["source"] = splitted_report[4]

            dict_list.append(report_dict)

        print(dict_list)
        return dict_list
    except AttributeError as e:
        print(e)
        return None

def gathering_tax_history(page):
    price_table = page.find("section#taxHistoryContainer", first=True)

    dict_list = []
    for report in price_table.find("tr", first=False)[1:]:
        report_dict = {}
        splitted_report = report.text.split("\n")

        report_dict["year"] = splitted_report[0]
        report_dict["taxes"] = splitted_report[1]
        report_dict["land"] = splitted_report[2]
        report_dict["improvement"] = splitted_report[3]
        report_dict["assessment"] = splitted_report[4]

        dict_list.append(report_dict)

    print(dict_list)
    return dict_list



def gathering_home_details(page):

    detail_dict = {"estimate": page.find("strong", first=True).text,
                   "state": page.find("input#StateCode", first=True).attrs["value"],
                   "address": page.find("input#Address", first=True).attrs["value"],
                   "city": page.find("input#City", first=True).attrs["value"],
                   "zip": page.find("input#Zip", first=True).attrs["value"], "url": page.url}

    price_table = page.find("section#propertyDetailsContainer", first=True)

    for detail in price_table.find("li", first=False)[1:]:
        for i in detail.text.split("\n"):
            if ":" in i:
                key, value = i.split(":")
                key = key.lower().strip().replace(" ", "_")
                detail_dict[key] = value

    print(detail_dict)
    return detail_dict

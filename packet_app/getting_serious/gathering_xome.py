def gathering_similar_homes(page):

    ggg = page.find("#xw-compPropertyKeyAddress", first=True)


    print(ggg.text)
    ggg = ggg.text[1:].split(", ")
    print(ggg)


    adding_page_dict = {"state": ggg[-1].split(" ")[0],
                 "city": ggg[1],
                 "zip": ggg[-1].split(" ")[-1],
                 "address": ggg[0].replace('"', "")}


    table_cells = page.find(".xw-widget-comparables-comp-property-row", first=False)
    similar_local_homes = []
    for i in table_cells:
        full_address = i.text.split("\n")[0]
        similar_local_homes.append(full_address)

    return (similar_local_homes, adding_page_dict), 1


def gathering_home_details(page):

    page_dict = {}

    property_fact = page.find(".xw-pf-table-cell", first=False)
    counter = 0
    while counter < len(property_fact):
        page_dict[property_fact[counter].text] = property_fact[counter + 1].text
        counter += 2

    return page_dict, 2


def gathering_price_details(page):
    price_history = page.find(".js-xw-price-history-table-row", first=False)
    price_list = []

    for i in price_history:
        temp = i.text.split("\n")
        if temp[0] == "price":
            temp[0] = "price changed"
        temp_dict = {"event": temp[0], "date": temp[1], "price": temp[2]}
        price_list.append(temp_dict)

    return price_list, 3


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
        if len(new_k) > 2:
            tax_dict = {"year": new_k[0], "property_taxes": new_k[1], "tax_assessment": new_k[2]}

            tax_list.append(tax_dict)

    return tax_list, 4

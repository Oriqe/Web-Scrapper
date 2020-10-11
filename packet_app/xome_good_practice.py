


def gather_home_details(page):
    page_dict = {}

    page_dict["state"] = page.find("#txtState", first=True).attrs.get("value")
    page_dict["city"] = page.find("#txtCity", first=True).attrs.get("value")
    page_dict["zip"] = page.find("#txtZip", first=True).attrs.get("value")
    page_dict["address"] = page.find("#txtAddress", first=True).attrs.get("value")

    property_fact = page.find(".xw-pf-table-cell", first=False)

    counter = 0

    while counter < len(property_fact):
        page_dict[property_fact[counter].text] = property_fact[counter + 1].text
        counter += 2

    return page_dict



def gathering_similar_homes(page, address_list=[]):

    table_cells = page.find(".xw-widget-comparables-comp-property-row", first=False)

    similar_local_homes = []
    for i in table_cells:

        full_address = i.text.split("\n")[0]
        similar_local_homes.append(full_address)

    print(similar_local_homes)
    return similar_local_homes




async def get_another_xome():
    r = await asession.get(
        f"https://x-api.xome.com/xda/web/widgets/SampleWidget?widget=PropertyFacts&hideMap=true&streetAddress={address}&zip={zip}",
        headers=req_headers)

    await r.html.arender(timeout=30, wait=3)
    resp = r.html.html

    resp = HTML(html=resp)
    # dicto = gathering_similar_homes(resp)
    return resp
from new_zillow.packet_app import google_extracter, text_extracter
from requests_html import AsyncHTMLSession, HTML
import asyncio
import psycopg2



def text_ext():
    print("started")
    zillow_url, truila_url = google_extracter.google_address_direct("1429 Fairmont St, Clearwater, FL 33755")
    print("finished with google")
    print("will start trying to extract from zillow")
    text_zillow, text_trulia = text_extracter.text_extracter(zillow_url, truila_url)

    return text_zillow, text_trulia






zillow, trulia = text_ext()

# for i in zillow.split("\n"):
#     print(i)


# async def get_zillow():
#     asession = AsyncHTMLSession()
#     r = await asession.get(url_zillow, headers=req_headers)
#     r_html = HTML(html=r.text)
#     r_html.find()
#     return r_html

import ast

counter = 0
counting = 0


def find_match(one_line, phrase):
    phrase = rf"{phrase}"
    if one_line[:len(phrase)] == phrase:
        return one_line[len(phrase)+len(r'63788579}\":{\"property\":{\"'):]
import psycopg2


for line in reversed(zillow.text.split("\n")):
    # if counter == 0 and "| Zillow" in line:
    #     full_address = line[:-9]
    #     counter += 1
    #     print(f"AHHHHHHHHHHHHHHHHHHHHH {full_address}")
    #     continue



    #
    # if line[:len("Bedrooms: ")] == "Bedrooms: ":
    #     bedrooms = line[10:]
    #     print("my first great success")
    #     print(f"bedrooms: {bedrooms}")
    #
    # bedrooms = find_match(line, "Bedrooms: ")
    # if bedrooms:
    #     print(bedrooms)



        ######

    special_line = find_match(line, r'{"apiCache":"{\"VariantQuery{\\\"zpid\\\":')
    if special_line:
        if "priceHistory" in special_line:
            special_first, special_second = special_line.split("priceHistory")
            special_dict = {}
            print(special_line)
            special_line = special_first.replace(r',\"factValue\"', "").replace(r'factLabel\":', "").replace(r'\",\"value\"', "").replace(r'{\"name\":\"', "").replace('\\', "").replace('"', "").replace(r'https:', "").replace(":{", "").replace(":[", "").split("}")

            # {\"factLabel\":\"HOA\",\"factValue\":\"None\"}
            # {\"categoryName\":
            # ,\"factValue\":
            for k in special_line:
                for i in k.split(","):
                    if ":" in i:
                        if len(i.replace("{", "").split(":")) == 2:
                            k, v = i.replace("{", "").split(":")
                            counter = 0
                            while k in special_dict.keys():
                                counter += 1
                                if k + str(counter) not in special_dict.keys():
                                    k = k + str(counter)

                            special_dict[k.replace(' ', "").lower()] = v

            ######################################################

            special_second = special_second.replace(r',\"factValue\"', "").replace(r'factLabel\":', "").replace(
                r'\",\"value\"', "").replace(r'{\"name\":\"', "").replace('\\', "").replace('"', "").replace(r'https:',
                                                                                                             "").replace(
                ":{", "").replace(', ', " ").replace(":[", "").split("}")

            # {\"factLabel\":\"HOA\",\"factValue\":\"None\"}
            # {\"categoryName\":
            # ,\"factValue\":
            special_second_dict = {}
            for k in special_second:
                for i in k.split(","):
                    if ":" in i:
                        if len(i.replace("{", "").split(":")) == 2:
                            k, v = i.replace("{", "").split(":")
                            counter = 0
                            while k in special_second_dict.keys():
                                counter += 1
                                if k + str(counter) not in special_second_dict.keys():
                                    k = k + str(counter)

                            special_second_dict[k.replace(' ', "").lower()] = v

            for key in special_second_dict.keys():
                print(f"{key}  :  {special_second_dict[key]}")

            import psycopg2

            connection = psycopg2.connect(database="home_details", user="postgres", password="Testing321",
                                          host="localhost")
            cursor = connection.cursor()
            cursor.execute(
                f"""INSERT INTO direct_address_scraper VALUES ('{special_dict['streetaddress']} {special_dict['zipcode']} {special_dict['city']} {special_dict['state']}',
                                                                            '{special_dict['bedrooms']}', 
                                                                            '{special_dict['bathrooms']}',
                                                                            '{special_dict['yearbuilt']}',
                                                                            'null',
                                                                            '{special_dict['lotsize']}',
                                                                            '{special_dict['hometype']}',
                                                                            '{special_second_dict['parcelid']}',
                                                                            '{special_second_dict['zestimate']}',
                                                                            'null',
                                                                            '{special_second_dict['bathroomsthreequarter']}',
                                                                            '{special_second_dict['bathroomshalf']}',
                                                                            '{special_second_dict['bathroomsonequarter']}',
                                                                            '{special_second_dict['cooling']}',
                                                                            '{special_second_dict['heating']}',
                                                                            '{special_second_dict['flooring']}',
                                                                            '{special_second_dict['appliances']}',
                                                                            '{special_second_dict['interiorfeatures']}',
                                                                            '{special_second_dict['categoryfactsparking']}',
                                                                            '{special_second_dict['garagespaces']}',
                                                                            '{special_second_dict['coveredspaces']}',
                                                                            '{special_second_dict['hascarport']}',
                                                                            '{special_second_dict['stories']}',
                                                                            '{special_second_dict['patioandporchfeatures']}',
                                                                            '{special_second_dict['categoryfactsstructuretype']}',
                                                                            '{special_second_dict['null2']}',
                                                                            '{special_second_dict['newconstructionyn']}',
                                                                            '{special_second_dict['constructionmaterials']}',
                                                                            '{special_second_dict['foundationtype']}, {special_second_dict['foundationdetails']}',

                                                                            '{special_second_dict['roof']}',
                                                                            '{special_second_dict['windowfeatures']}',
                                                                            '{special_second_dict['greenbuildingverificationtype']} {special_second_dict['greenenergyefficient']}, {special_second_dict['greenindoorairquality']}, {special_second_dict['greensustainability']}, {special_second_dict['greenwaterconservation']}',
                                                                            '{special_second_dict['solarpotentialsunscore']}',
                                                                            '{special_second_dict['cityregion']}',
                                                                            '{special_second_dict['taxassessedvalue']}',
                                                                            '{special_second_dict['taxannualamount']}');""")
            connection.commit()
            # time\":1585911960000,\"price\":199900,\"priceChangeRate\":0.17935103,\"source\":\"ENGEL & VOELKERS TAMPA\",\"buyerAgent\":null,\"sellerAgent\":null,\"showCountyLink\":false,\"postingIsRental\":false},{\"event\":\"Sold\",\"time\":1501225200000,\"
            cursor.execute("SELECT * FROM direct_address_scraper;")
            for row in cursor:
                print(row)
            cursor.close()

            f"https://zillow.com/homedetails/{special_second_dict['zpid3']}_zpid"

        else:
            special_dict = {}
            print(special_line)
            special_line = special_line.replace(r',\"factValue\"', "").replace(r'factLabel\":', "").replace(
                r'\",\"value\"', "").replace(r'{\"name\":\"', "").replace('\\', "").replace('"', "").replace(r'https:',
                                                                                                             "").replace(
                ":{", "").replace(":[", "").split("}")

            # {\"factLabel\":\"HOA\",\"factValue\":\"None\"}
            # {\"categoryName\":
            # ,\"factValue\":
            for k in special_line:
                for i in k.split(","):
                    if ":" in i:
                        if len(i.replace("{", "").split(":")) == 2:
                            k, v = i.replace("{", "").split(":")
                            counter = 0
                            while k in special_dict.keys():
                                counter += 1
                                if k + str(counter) not in special_dict.keys():
                                    k = k + str(counter)

                            special_dict[k.replace(' ', "").lower()] = v

            for key in special_dict.keys():
                print(f"{key}  :  {special_dict[key]}")





            # import psycopg2
            #
            # connection = psycopg2.connect(database="home_details", user="postgres", password="Testing321",
            #                               host="localhost")
            # cursor = connection.cursor()
            # cursor.execute(
            #     f"""INSERT INTO direct_address_scraper VALUES ('{special_dict['streetaddress']} {special_dict['zipcode']} {special_dict['city']} {special_dict['state']}',
            #                                                                        '{special_dict['bedrooms']}',
            #                                                                        '{special_dict['bathrooms']}',
            #                                                                        '{special_dict['yearbuilt']}',
            #                                                                        'null',
            #                                                                        '{special_dict['lotsize']}',
            #                                                                        '{special_dict['hometype']}',
            #                                                                        '{special_dict['parcelid']}',
            #                                                                        '{special_dict['zestimate']}',
            #                                                                        'null',
            #                                                                        '{special_dict['bathroomsthreequarter']}',
            #                                                                        '{special_dict['bathroomshalf']}',
            #                                                                        '{special_dict['bathroomsonequarter']}',
            #                                                                        '{special_dict['cooling']}',
            #                                                                        '{special_dict['heating']}',
            #                                                                        '{special_dict['flooring']}',
            #                                                                        '{special_dict['appliances']}',
            #                                                                        '{special_dict['interiorfeatures']}',
            #                                                                        '{special_dict['categoryfactsparkingfeatures']}, {special_dict['parkingfeatures']}',
            #                                                                        '{special_dict['garagespaces']}',
            #                                                                        '{special_dict['coveredspaces']}',
            #                                                                        '{special_dict['hascarport']}',
            #                                                                        '{special_dict['stories']}',
            #                                                                        '{special_dict['patioandporchfeatures']}',
            #                                                                        '{special_dict['categoryfactsstructuretype']}',
            #                                                                        '{special_dict['null2']}',
            #                                                                        '{special_dict['newconstructionyn']}',
            #                                                                        '{special_dict['constructionmaterials']}',
            #                                                                        '{special_dict['foundationtype']}, {special_dict['foundationdetails']}',
            #
            #                                                                        '{special_dict['roof']}',
            #                                                                        '{special_dict['windowfeatures']}',
            #                                                                        '{special_dict['greenbuildingverificationtype']} {special_dict['greenenergyefficient']}, {special_dict['greenindoorairquality']}, {special_dict['greensustainability']}, {special_dict['greenwaterconservation']}',
            #                                                                        '{special_dict['solarpotentialsunscore']}',
            #                                                                        '{special_dict['cityregion']}',
            #                                                                        '{special_dict['taxassessedvalue']}',
            #                                                                        '{special_dict['taxannualamount']}');""")
            # connection.commit()
            # time\":1585911960000,\"price\":199900,\"priceChangeRate\":0.17935103,\"source\":\"ENGEL & VOELKERS TAMPA\",\"buyerAgent\":null,\"sellerAgent\":null,\"showCountyLink\":false,\"postingIsRental\":false},{\"event\":\"Sold\",\"time\":1501225200000,\"
            # cursor.execute("SELECT * FROM direct_address_scraper;")
            # for row in cursor:
            #     print(row)
            # cursor.close()

            #######################################################

        # fact_features = zillow.find("li.ds-home-fact-list")
        # print(fact_features)






print("zillow dict is a-ok")




#
# for line in trulia.split("\n"):
#     print(line)


        # for key in special_dict.keys():
        #     print(f"{key}   :   {special_dict[key]}")





        # for g in special_line.split(r',\"'):
        #     for k in g.split(r'{'):
        #         for m in k.split(r'['):
        #             for p in m.split("}"):
        #                 for h in p.split("]"):
        #                     if r'\":' in h:
        #                         k, v = m.split(r'\":')
        #                         print(k, v)
        #                     else:
        #                         print("***********************" +h)
                # for k in j.split(r'\",\"'):


                # l = l.replace(r'{', "")
                # # l = l.replace(r'[', "")
                #         if r'\":' in m:
                #             key, value = l.split(r'\":')
                #             special_dict[key] = value

            #
            #
            # print(i.split(r'\":\"'))
            # key, value = i.split(r'\":\"')
            # special_dict[key] = value

        # for key, value in special_dict:
        #     print(f"{key} : {value}")



    #
    #
    # if line[:len("Total interior livable ar
    #
    #
    # ea: ")] == "Total interior livable area: ":
    #     sqft_built = line[len("Total interior livable area: "):]
    #     print("another great success")
    #     print(sqft_built)
    #


# connection = psycopg2.connect(database="home_details", user="postgres", password="Testing321", host="localhost")
# cursor = connection.cursor()
# cursor.execute(f"INSERT INTO direct_address_scraper VALUES ('{full_address}', '{bedrooms}', '{bathrooms}');")
# connection.commit()
#
# cursor.close()




"""                      |
good practice for trulia V
"""


#counter = 0
# for line in trulia.split("\n"):
#     if counter == 0 and "branch.setBranchViewData" in line:
#         line = ast.literal_eval(line[line.index("branch.setBranchViewData")+25:-2])
#         print(line["data"])







#
# import csv
# with open('eggs.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=',',
#                             quotechar=' ', quoting=csv.QUOTE_MINIMAL)
#
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])




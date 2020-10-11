def special_line_handler(separator_string, line):
    if separator_string in line:
        import psycopg2
        special_first, special_second = line.split(separator_string)
        special_dict = {}
        print(line)
        line = special_first.replace(r',\"factValue\"', "").replace(r'factLabel\":', "").replace(r'\",\"value\"',
                                                                                                 "").replace(
            r'{\"name\":\"', "").replace('\\', "").replace('"', "").replace(r'https:', "").replace(":{", "").replace(
            ":[", "").split("}")

        # {\"factLabel\":\"HOA\",\"factValue\":\"None\"}
        # {\"categoryName\":
        # ,\"factValue\":
        for k in line:
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

    connection = psycopg2.connect(database="home_details", user="postgres", password="Testing321", host="localhost")
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
                                                                           '{special_second_dict['categoryfactsparkingfeatures']}, {special_second_dict['parkingfeatures']}',
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
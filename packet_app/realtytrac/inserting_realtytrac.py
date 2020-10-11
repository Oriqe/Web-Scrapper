
def insert_into_realytrac_table(page_dict, adrs_dict):
    import psycopg2
    import datetime
    connection = psycopg2.connect(database="real_estate", user="postgres", password="Testing321",
                                  host="localhost")
    cursor = connection.cursor()
    # print(adrs_dict)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(adrs_dict)
    print(adrs_dict["time_stamp"])
    print(adrs_dict["address"])
    print(page_dict)

    print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
    print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
    print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
    NULL = 'NAN'
    Null = 'NULL'
    if page_dict["estimate"] == "N/A":
        page_dict["estimate"] = NULL
    else:
        page_dict["estimate"] = page_dict["estimate"][1:].replace(",", "")

    cursor.execute(
        f"""INSERT INTO second_list VALUES ((SELECT call_id FROM first_list
                                                    WHERE house_address = '{adrs_dict["address"].lower()}' AND time_stamp = '{adrs_dict["time_stamp"]}'),
                                                    'NULL',
                                                    '{page_dict["address"]}',  
                                                    '{page_dict["city"]}',
                                                    '{page_dict["state"]}',
                                                    '{page_dict["zip"]}',
                                                    '{adrs_dict["latLong"]["longitude"]}',
                                                    '{adrs_dict["latLong"]["latitude"]}',
                                                    'NULL',
                                                    '{NULL}',
                                                    '{page_dict["estimate"]}',
                                                    '{page_dict["home_size"].strip().split(" ")[0].replace(",", "") if "home_size" in page_dict.keys() else NULL}',
                                                    '{page_dict["lot_size"].strip().split(" ")[0].replace(",", "") if "lot_size" in page_dict.keys() else NULL}',
                                                    '{page_dict["built_in"].strip() if "built_in" in page_dict.keys() else NULL}',
                                                    '{NULL}',
                                                    '{NULL}',
                                                    '{NULL}',
                                                    '{page_dict["url"]}',
                                                    '{NULL}',
                                                    'NULL',
                                                    'NULL',
                                                    '{NULL}',
                                                    'NULL',
                                                    '{datetime.datetime.now()}',
                                                    '{adrs_dict["main_call_id"]}',
                                                    '{page_dict["parcel_number"]}',
                                                    '{page_dict["heating_type"] if "heating_type" in page_dict.keys() else 'NULL'}',
                                                    '{page_dict["cooling_type"] if "cooling_type" in page_dict.keys() else 'NULL'}',
                                                    '{page_dict["county"]}',
                                                    'NULL');""")

    connection.commit()
    cursor.close()

def insert_realytrac_price_table(price_list, adrs_dict):
    import psycopg2.errors
    from psycopg2.errorcodes import DUPLICATE_TABLE
    connection = psycopg2.connect(database="real_estate", user="postgres", password="Testing321",
                                  host="localhost")
    cursor = connection.cursor()
    NULL = "NAN"
    print(adrs_dict)
    try:
        for record in price_list:

            record['date'] = record['date'].replace("/", "-")
            cursor.execute(
            f"""INSERT INTO price_list VALUES ((SELECT call_id FROM first_list
                                                        WHERE house_address = '{adrs_dict["address"].lower()}' AND time_stamp = '{adrs_dict["time_stamp"]}'),
                                                        '{adrs_dict["main_call_id"]}',
                                                        '{record['event']}',
                                                        '{record['price'][1:].replace(",", "") if record['price']!="N/A" else NULL}',  
                                                        '{record['source']}',
                                                        '{adrs_dict["addressStreet"]}',
                                                        '{adrs_dict["addressCity"]}',
                                                        '{adrs_dict["addressState"]}',
                                                        '{adrs_dict["addressZipcode"]}',
                                                        '{record['date'] if len(record['date'].split("-")[0])==2 else f"0{record['date']}"}');""")

            connection.commit()
        cursor.close()

    except psycopg2.errors.lookup(DUPLICATE_TABLE) as e:
        print(e)
        cursor.close()


def create_realytrac_tax_table(tax_list, adrs_dict):
    import datetime
    import psycopg2.errors
    from psycopg2.errorcodes import DUPLICATE_TABLE
    connection = psycopg2.connect(database="real_estate", user="postgres", password="Testing321",
                                  host="localhost")
    cursor = connection.cursor()

    try:
        for record in tax_list:

            cursor.execute(
            f"""INSERT INTO tax_list VALUES ((SELECT call_id FROM first_list
                                                    WHERE house_address = '{adrs_dict["address"].lower()}' AND time_stamp = '{adrs_dict["time_stamp"]}'),
                                                    '{adrs_dict["main_call_id"]}',
                                                    '{record['year']}',
                                                    '{record['taxes'].split(" ")[0][1:].replace(",", "")}',  
                                                    '{record['land'][1:].replace(",", "")}',  
                                                    '{record['improvement'][1:].replace(",", "")}',  
                                                    '{record['assessment'][1:].replace(",", "")}',
                                                    '{adrs_dict["addressStreet"]}',
                                                    '{adrs_dict["addressCity"]}',
                                                    '{adrs_dict["addressState"]}',
                                                    '{adrs_dict["addressZipcode"]}');""")

            connection.commit()
        cursor.close()

    except psycopg2.errors.lookup(DUPLICATE_TABLE) as e:
        print(e)
        cursor.close()

    except psycopg2.errors.lookup(DUPLICATE_TABLE) as e:
        print(e)
        cursor.close()

import psycopg2


connection = psycopg2.connect(database="home_details", user="postgres", password="Testing321", host="localhost")
cursor = connection.cursor()
cursor.execute(f"""INSERT INTO direct_address_scraper VALUES ('{special_dict['streetAddress']} {special_dict['zipcode']} {special_dict['city']} {special_dict['state']}',"
                                                                {special_dict['bedrooms']}, 
                                                                {special_dict['bathsrooms']},
                                                                {special_dict['homeType']},
                                                                {special_dict['lotSize']},
                                                                {special_dict['parcelId']},
                                                                {special_dict['']},
                                                                {special_dict['YearBuilt']},
                                                                {special_dict['zestimate']},
                                                                {special_dict['']},
                                                                );""")
connection.commit()



cursor.execute("SELECT * FROM direct_address_scraper;")
for row in cursor:
    print(row)
cursor.close()

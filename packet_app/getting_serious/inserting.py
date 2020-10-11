import psycopg2
import datetime
from geopy.geocoders import Nominatim


def insert_into_xome_table(page_dict, price_list):
    geolocator = Nominatim(user_agent="Heyy im nick")
    connection = psycopg2.connect(database="home_details", user="postgres", password="Testing321",
                                  host="localhost")
    cursor = connection.cursor()
    cursor.execute(
        f"""INSERT INTO xome_home_details VALUES ('{datetime.datetime.now()}',
                                                      '{price_list['event']}',
                                                      '{page_dict['address']} {page_dict['city']} {page_dict['state']} {page_dict['zip']}',
                                                      '{page_dict['address']}',
                                                      '{page_dict['city']}',
                                                      '{page_dict['County']}',
                                                      '{page_dict['state']}',
                                                      '{page_dict['zip']}',
                                                      '{page_dict['Parcel Number']}',
                                                      '{page_dict['Year Built']}',
                                                      '{page_dict['Bedrooms']}',
                                                      '{page_dict['Bathrooms']}',
                                                      '{page_dict['Living Area']}',
                                                      '{page_dict['Lot Size']}',
                                                      'null',
                                                       '{geolocator.geocode(f'{page_dict["address"]} {page_dict["state"]} {page_dict["zip"]}').latitude if geolocator.geocode(f'{page_dict["address"]} {page_dict["state"]} {page_dict["zip"]}') else 'null'}',
                                                       '{geolocator.geocode(f'{page_dict["address"]} {page_dict["state"]} {page_dict["zip"]}').longitude if geolocator.geocode(f'{page_dict["address"]} {page_dict["state"]} {page_dict["zip"]}') else 'null'}',
                                                       '{page_dict["Property Type"]}'
);""")
    connection.commit()
    cursor.close()

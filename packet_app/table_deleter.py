import psycopg2.errors
from  psycopg2.errorcodes import DUPLICATE_TABLE


connection = psycopg2.connect(database="home_details", user="postgres", password="Testing321",
                              host="localhost")
cursor = connection.cursor()

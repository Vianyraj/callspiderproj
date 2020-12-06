# import psycopg2
#
# # ENGINE= "django.db.backends.postgresql"
# # NAME= "calc"
# # USER= "postgres"
# # PASSWORD= "1234"
# # HOST= "localhost"
# #DB_PORT= "5432"
#
#
#     # conn = psycopg2.connect(database= ENGINE, user= NAME, password= PASSWORD, host= HOST)
# conn = psycopg2.connect(user="postgres",
#                               password="1234",
#                               host="127.0.0.1",
#                               port="5432",
#                               database="calc")
#
# cur = conn.cursor()
# print("database is succesful")
# #id INT NOT NULL,
# #cur.execute("""
# #
# # CREATE TABLE paperlistnew
# # (
# # ID INT NOT NULL,
# # Eventlink VARCHAR NOT NULL,
# # Eventname VARCHAR NOT NULL,
# # Dates TEXT NOT NULL,
# # wheree  TEXT NOT NULL,
# # whene TEXT NOT NULL
# #
# # )
# #
# # """)
# #
# # conn.commit()
# # print("table created successfully")
# i=1
# #inserting data
# # for i in range(1,5):
# #  ID=i
# #  Eventlink='asdf'
# #  Eventname='sdfg'
# #  Dates='dgh'
# #  where='lkj'
# #  whene='dklfjg'
# #  # cur.execute("INSERT INTO paperlistnew (ID, Eventlink, Eventname, Dates, wheree, whene) VALUES(%s,'eme1','jungle1','grimjov1','move1','move11')")
# #  # conn.commit()
# #  cur.execute("INSERT INTO calc_paperscrapying VALUES(%s,%s,%s,%s,%s,%s)", (
# #      ID,
# #      Eventlink,
# #      Eventname,
# #      Dates,
# #      where,
# #      whene
# #  ))
# #  conn.commit()
#
# #print data on console
# #cur.execute("SELECT id, movie,movie1,movie2 FROM calc_todo")
#
# # rows= cur.fetchall()
# #
# # for data in rows:
# #     print("id:" + str(data[0]))
# #     print("movie:"+ data[1])
# #     print("movie1:" + data[2])
# #     print("movie2:" + data[3])
#
# #update tables
# # cur.execute("UPDATE paperlistnew set EVENTNAME= 'gagarjack4' WHERE EVENTLINK= 'eme'")
# #
# # conn.commit()
#
#
# #delete id or row
# for j in range (1,3):
#     id=j
#     cur.execute("DELETE FROM calc_paperscrapying WHERE ID = %s", (j,))
#     conn.commit()
# print("data deleted successfully")
# print("Total row affected" + str(cur.rowcount))
# conn.close()
from django.core.management.base import BaseCommand
from scraper.spiders import TheodoSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())

        process.crawl(TheodoSpider)
        process.start()
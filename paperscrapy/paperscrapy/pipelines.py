# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2
from scrapy.loader.processors import Join
# ENGINE= "django.db.backends.postgresql"
# NAME= "calc"
# USER= "postgres"
# PASSWORD= "1234"
# HOST= "localhost"
#DB_PORT= "5432"

conn = psycopg2.connect(user="postgres",
                            password="1234",
                            host="127.0.0.1",
                            port="5432",
                            database="calc")
cur = conn.cursor()



class PaperscrapyPipeline(object):

    def process_item(self, item, spider):

                 for j in range(1, 21):
                   id = j
                   cur.execute("DELETE FROM calc_paperscrapying WHERE ID = %s", (j,))
                   conn.commit()
                 k = 0
                 p=0
                 ID_when = 1
                 ID_event = 2
                 a = len(item["when"])
                 b = len(item["Eventname"])
                 while k<=36 :
                  print('k at start is',k)
                  l=k
                  m=k+1
                  n=k+2
                  o=k+3
                  source='http://www.wikicfp.com'
                  if (ID_when<= a):
                     whenlink = source + item["whenlink"][p]
                     cur.execute("INSERT INTO calc_paperscrapying VALUES(%s,%s,%s,%s,%s,%s)", (
                         ID_when,
                         whenlink,
                         item["when"][l],
                         item["when"][m],
                         item["when"][n],
                         item["when"][o]
                     ))

                  if (ID_event<= b):
                      Eventnamelink = source + item["Eventnamelink"][p]
                      cur.execute("INSERT INTO calc_paperscrapying VALUES(%s,%s,%s,%s,%s,%s)", (
                        ID_event,
                        Eventnamelink,
                        item["Eventname"][l],
                        item["Eventname"][m],
                        item["Eventname"][n],
                        item["Eventname"][o]
                      ))
                  l = k
                  m = k + 1
                  n = k + 2
                  o = k + 3
                  p=p+1
                  ID_when = ID_when + 2
                  ID_event = ID_event +2
                  conn.commit()
                  k=k+4
                  print('k is',k)
                  if (ID_when > len(item["when"] or ID_event > len(item["Eventname"]))):
                    ID_event=1
                    ID_when=1
                    break





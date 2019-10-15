# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

## Scraped data -> Item containers -> json/csv files
## Scraped data -> Item containers -> Pipelines -> SQL/Mongo Database

## To activate pipelines uncoment the ITEM_PIPELINES code in setting.py (line 67, 68, 69)

import sqlite3
import mysql.connector
import pymongo

class ScrapykompasPipeline(object):

    ## Create init method
    def __init__(self):
        self.create_connection_sqlite()
        self.create_table_sqlite()
        self.create_connection_mysql()
        self.create_table_mysql()
        self.create_connection_mongo()
        self.create_table_mongo()

    def process_item(self, item, spider):
        self.insert_table_sqlite(item)
        self.insert_table_mysql(item)
        self.insert_table_mongo(item)
        print("SUCCESS!!!")
        return item


    ## Create a sqlite connection method
    def create_connection_sqlite(self) :
        self.sqlite_conn = sqlite3.connect('Kompas.db')
        self.sqlite_cursor = self.sqlite_conn.cursor()

    ## Create a sqlite create table method
    def create_table_sqlite(self) :
        self.sqlite_cursor.execute("""DROP TABLE IF EXISTS Kompas""")
        self.sqlite_cursor.execute("""CREATE TABLE Kompas(title TEXT, tag TEXT, link TEXT)""")

    ## Create a sqlite insert into table method
    def insert_table_sqlite(self, item) :
        self.sqlite_cursor.execute("""INSERT INTO Kompas VALUES(?, ?, ?)""", (item['title'][0], item['tag'][0], item['link'][0]))
        self.sqlite_conn.commit()


    ## Create a mysql connection method
    def create_connection_mysql(self):
        self.mysql_conn = mysql.connector.connect(host = 'localhost', user = 'amrizal', passwd = 'amrizal', database = 'Kompas')
        self.mysql_cursor = self.mysql_conn.cursor()

    ## Create a mysql create table method
    def create_table_mysql(self):
        self.mysql_cursor.execute("""DROP TABLE IF EXISTS Kompas""")
        self.mysql_cursor.execute("""CREATE TABLE Kompas(title TEXT, tag TEXT, link TEXT)""")

    ## Create a mysql insert into table method
    def insert_table_mysql(self, item):
        self.mysql_cursor.execute("INSERT INTO Kompas VALUES(%s, %s, %s)", (item['title'][0], item['tag'][0], item['link'][0]))
        self.mysql_conn.commit()
        print("('" + item['title'][0] + "', '" + item['tag'][0] + "', '" + item['link'][0] + "')")


    ## Create a mongodb connection method
    def create_connection_mongo(self):
        self.mongo_conn = pymongo.MongoClient('localhost', 27017)

    ## Create a mongodb create table method
    def create_table_mongo(self):
        db = self.mongo_conn['Kompas']
        self.collection = db['Kompas']

    ## Create a mongodb insert into table method
    def insert_table_mongo(self, item):
        self.collection.insert(dict(item))
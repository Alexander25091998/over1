import requests
import pandas
from bs4 import BeautifulSoup
import psycopg2
from psycopg2 import Error
import sqlite3
from sqlite3 import Error
from abc import ABC, abstractmethod


class DataClient(ABC):
    @abstractmethod
    def get_connection(self):
        pass

    @abstractmethod
    def create_mebel_table(self, conn):
        pass

    @abstractmethod
    def get_items(self, conn, price_from=0, price_to=100000):
        pass

    @abstractmethod
    def insert(self, conn, link, price, description):
        pass

    def run_test(self):
        conn = self.get_connection()
        self.create_mebel_table(conn)
        items = self.get_items(conn, price_from=10, price_to=30)
        for item in items:
            print(item)
        conn.close()


class PostgresClient(DataClient):
    USER = "postgres"
    PASSWORD = "postgres"
    HOST = "localhost"
    PORT = "5433"

    def get_connection(self):
        try:
            conn = psycopg2.connect(
                user=self.USER,
                password=self.PASSWORD,
                host=self.HOST,
                port=self.PORT
            )
            return conn
        except Error:
            print("Error")

    def create_mebel_table(self, connection):
        cursor_object = connection.cursor()
        cursor_object.execute(
            """
                CREATE TABLE IF NOT EXISTS mebel
                (
                    id serial PRIMARY KEY, 
                    link text, 
                    price integer, 
                    description text
                )
            """
        )
        connection.commit()

    def get_items(self, conn, price_from=0, price_to=100000):
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM mebel WHERE price >= {price_from} and price <= {price_to}')
        return cursor.fetchall()

    def insert(self, conn, link, price, description):
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO mebel (link, price, description) VALUES ('{link}', '{price}', '{description}')")
        conn.commit()


class SQLite3Client(DataClient):
    DB_Name = "kufar.db"

    def get_connection(self):
        try:
            conn = sqlite3.connect(self.DB_Name)
            return conn
        except Error:
            print("Error")

    def create_mebel_table(self, conn):
        cursor_object = conn.cursor()
        cursor_object.execute(
            """
                CREATE TABLE IF NOT EXISTS mebel
                (
                    id integer PRIMARY KEY autoincrement, 
                    link text, 
                    price integer, 
                    description text
                )
            """
        )
        conn.commit()

    def get_items(self, conn, price_from=0, price_to=100000):
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM mebel WHERE price >= {price_from} and price <= {price_to}')
        return cursor.fetchall()

    def insert(self, conn, link, price, description):
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO mebel (link, price, description) VALUES ('{link}', '{price}', '{description}')")
        conn.commit()



# data_client = PostgresClient()
# data_client = SQLite3Client()
# data_client.run_test()

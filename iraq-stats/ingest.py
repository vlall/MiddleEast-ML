#!/usr/bin/python

import psycopg2
import sys
import os
import yaml


class Iraq_Stats:


    def __init__(self):
        self.con = None
        self.connect()
        #self.load_config()
        self.set_d3()
        self.disconnect()

    def connect(self):
        con = self.con
        with open('../config.yaml', 'r') as f:
            conf = yaml.load(f)
        dbname = conf['psql']['dbname']
        user = conf['psql']['user']
        host = conf['psql']['host']
        password = conf['psql']['password']
        self.data = conf['psql']['data']
        try:
            con = psycopg2.connect("""dbname=%s
                                        user=%s
                                        host=%s
                                        password=%s""" % 
                                        (
                                            dbname,
                                            user,
                                            host,
                                            password
                                        )
                )
            cur = con.cursor()

        except psycopg2.DatabaseError, e:
            if con:
                con.rollback()
            print 'Error %s' % e
            sys.exit(1)

        finally:
            self.con = con
            self.cur = cur
            return ('Connection connected')

    def disconnect(self):
        if self.con:
            self.con.close()
            return ('Connection disconnected')

    def load_config(self):
        self.connect()
        con = self.con
        cur = self.cur

        # Set the columns.
        cur.execute("""CREATE TABLE Iraq(
                                        id SERIAL PRIMARY KEY,
                                        IBC VARCHAR,
                                        startDate DATE,
                                        endDate DATE,
                                        Time VARCHAR,
                                        Location VARCHAR,
                                        Target VARCHAR,
                                        Weapons VARCHAR,
                                        Min INT,
                                        Max INT,
                                        Sources VARCHAR)"""
        )

        # Ingest the data.
        cur.execute(("""COPY Iraq(
                                    IBC,
                                    startDate,
                                    endDate,
                                    Time,
                                    Location,
                                    Target,
                                    Weapons,
                                    Min,
                                    Max,
                                    Sources
                                ) 
                                    FROM '%s' DELIMITER ',' CSV HEADER;"""
        ) % self.data)
        con.commit()
        print('Success!')
        self.disconnect

    # Example queries on the database
    def set_d3(self):
        cur = self.cur
        cur.execute("SELECT SUM(min) FROM iraq")
        minDeaths = cur.fetchone()[0]
        cur.execute("SELECT SUM(max) FROM iraq")
        maxDeaths = cur.fetchone()[0]
        cur.execute("SELECT Weapons FROM iraq")
        weapons = cur.fetchmany(20)[0]
        print minDeaths, maxDeaths, weapons

def main():
    x = Iraq_Stats()
main()

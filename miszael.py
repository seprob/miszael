#!/usr/bin/env python

from pymongo import MongoClient
import argparse

command_line_parser = argparse.ArgumentParser("Removing all data from MongoDB databases")

command_line_parser.add_argument("-a",
                                 "--address",
                                 dest = "address",
                                 default = "localhost",
                                 required = False,
                                 help = "Database host address")

command_line_parser.add_argument("-u",
                                 "--user",
                                 dest = "user",
                                 required = False,
                                 help = "Database user name")

command_line_parser.add_argument("-p",
                                 "--password",
                                 dest = "password",
                                 required = False,
                                 help = "Database password")

command_line_parser.add_argument("-db",
                                 "--database",
                                 dest = "database",
                                 required = False,
                                 help = "Database name")

arguments = command_line_parser.parse_args()
client = MongoClient(arguments.address, 27017)

client[arguments.database].authenticate(arguments.user, arguments.password)

# For every database.

databases = client.database_names()

for database in databases:
    if database != "admin" and database != "local" and database != "graylog": # Skip following databases.
        print "[*] Database: \"" + database + "\"."

        db = client[database]

        # For every collection.

        for collection in db.collection_names():
            if "system." not in collection:
                if "capped" in db[collection].options():
                    if db[collection].options()["capped"] == True:
                        input_data = raw_input("[?] Collection \""
                                               + collection
                                               + "\" is capped. "
                                               + "Do you want to remove the collection (type \"y\" if you do)? ")

                        if input_data == "y":
                            db[collection].drop() # Remove the collection.
                    else:
                        print "[*] Removing all documents from collection: \"" + collection + "\"."

                        db[collection].remove({}) # Remove all documents form collection.
                else:
                    print "[*] Removing all documents from collection: \"" + collection + "\"."

                    db[collection].remove({}) # Remove all documents form collection.
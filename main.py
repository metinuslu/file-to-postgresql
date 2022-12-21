"""
This script is to export Raw Data (*.csv & *.xlsx) to PostgreSQL.
"""

import os
import json
import argparse
import pandas as pd
from sqlalchemy import create_engine

def get_project_config(config_file='project.json'):
    """
    This function get general project config values
    """

    with open("cfg/" + config_file, encoding='utf-8') as json_file:
        project_config = json.load(json_file)
    return project_config

def read_data(data_path, file_name, sep):
    """
    This function read data from raw file
    """

    if os.path.splitext(os.path.join(data_path, file_name))[1] == ".csv":
        df_data = pd.read_csv(os.path.join(data_path, file_name), sep=sep)
    elif os.path.splitext(os.path.join(data_path, file_name))[1] == ".xlsx":
        df_data = pd.read_excel(os.path.join(data_path, file_name))
    return df_data

def data_to_sql(db_host, db_name, db_table, db_schema, db_username, db_userpass, data):
    """
    Transfer data from pandas DataFrame to PostgreSQL table
    """

    # define connection string
    connection_string = "postgresql+psycopg2://{uid}:{pwd}@{host}:5432/{db}".format(
        uid=db_username,
        pwd=db_userpass,
        host=db_host,
        db=db_name
    )
    # create engine
    engine = create_engine(connection_string)

    # transfer data from DataFrame to PostgreSQL table
    data.to_sql(name=db_table, con=engine, schema=db_schema, if_exists="append", index=False)

def main():
    """
    Main function which transfers the data from S3 to PostgreSQL table
    """

    # if os.path.splitext(os.path.join(DATA_PATH, args["file"]))[1] == ".csv":
    #     df_data = pd.read_csv(os.path.join(DATA_PATH, args["file"]), sep=args["sep"])

    # elif os.path.splitext(os.path.join(DATA_PATH, args["file"]))[1] == ".xlsx":
    #     df_data = pd.read_excel(os.path.join(DATA_PATH, args["file"]))
    # else:
    #     print("Unknown File Format")

    df_data = read_data(data_path=DATA_PATH, file_name=args["file"], sep=args["sep"])

    try:
        data_to_sql(db_host=DB_HOST, db_name=DB_NAME, db_table=args["table"],
        db_schema=DB_SCHEMA, db_username=DB_USERNAME, db_userpass=DB_USERPASS,
        data=df_data)
    except IOError as io_err:
        print("Connection Failed", io_err)

if __name__=="__main__":

    pcfg = get_project_config(config_file='project.json')

    arg_parser = argparse.ArgumentParser(description='Data to PostgreSQL DB', usage='')

    # arg_parser.add_argument("-c", "--config", required=False, type=str,
    # default='project.json',
    # help="Please chose the Config File. Default project.json")

    arg_parser.add_argument("-", "--host", required=False, type=str,
     default=pcfg['database']['host'], help="")

    arg_parser.add_argument("-d", "--database", required=False, type=str,
     default=pcfg['database']['name'], help="")

    arg_parser.add_argument("-t", "--table", required=False, type=str, help="")

    arg_parser.add_argument("-s", "--schema", required=False, type=str,
     default=pcfg['database']['schema'], help="")

    arg_parser.add_argument("-u", "--userName", required=False, type=str,
     default=pcfg['database']['username'], help="")

    arg_parser.add_argument("-p", "--userPass", required=False, type=str,
     default=pcfg['database']['userpass'], help="")

    arg_parser.add_argument("-f", "--file", required=True, type=str,
     help="")

    arg_parser.add_argument("-b", "--sep", required=False, type=str,
     default=',', help="")

    args = vars(arg_parser.parse_args())

    ROOT_PATH = os.getcwd()
    DATA_PATH = os.path.join(ROOT_PATH, 'data')

    DB_HOST = args["host"]
    DB_NAME = args["database"]
    DB_USERNAME = args["userName"]
    DB_USERPASS = args["userPass"]
    DB_SCHEMA = args["schema"]
    # DB_TABLE = args["table"]

    main()

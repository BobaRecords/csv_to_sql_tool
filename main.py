# This is code that will be used to import csv into psql
import os
import pandas as pd
from tabulate import tabulate
import psycopg2

# user input
input_source_path = '/Desktop/Result_7.csv'
input_schema_name = 'pokemon'
input_table_name = 'Result_7'
input_host = 'localhost'
input_database = 'postgres'
input_user = 'dfang'
input_password = 'pinkpanther'

# sql table address
schema_table = input_schema_name + '.' + input_table_name

# Getting path information
root = os.path.expanduser('~')
path_to_file = root + input_source_path

# below are all the functions
def csv_to_df(path_to_file=path_to_file):
    # converts the csv to a dataframe
    df = pd.read_csv(path_to_file)
    return df


def reformat_col_names(df):
    # removes illegal header characters
    # gets all column names in a single list to be returned
    col_names = []
    for col in df.columns:
        reformat_name = col.replace(" ", "_").replace("#", "hash")
        # print(reformat_name)
        col_names.append(reformat_name)
    # print(col_names)
    return col_names


def create_sql_query_table(col_names,schema_table=schema_table):
    # create the sql query to be run for creating the table format
    query = "CREATE TABLE " + schema_table + " (\n"

    for name in col_names[:-1]:
        query = query +'"'+ name + '" text,\n'
    
    # last one does not need a comma
    query = query + '"' + col_names[-1] + '" text)'
    # print(query)
    return query


def get_col_count(df):
    col_count = 0
    for col in df.columns:
        col_count = col_count + 1
    # print('next line col count')
    # print(col_count)
    return col_count


def reformat_df_to_list(df, col_count, row_number):
    # pull the data from df column and place into list
    # this will only return 1 list at a time
    df = df.replace({"'": "''"}, regex=True)
    col_data = []
    i = 0
    while i < col_count:
        column_data = df.iloc[row_number][i]
        i += 1
        col_data.append(column_data)
    # print(col_data)
    return col_data


def create_sql_query_adding_data(col_data, schema_table=schema_table):
    # creates the SQL query for adding more data
    # this query needs to change in size depending on the .csv document
    # starting and ending are constants
    query = 'INSERT INTO ' + schema_table + "\nVALUES (\n"
    
    # loop thorugh all col_data values and add it to the query
    for data in col_data[:-1]:
        query = query + "'" + str(data) + "',\n"
    
    # last item in list is outside of loop becuase of different suffix
    query = query + "'" + str(col_data[-1]) + "')"
    
    # print(query)
    return query
    

def run_sql_in_db(query):
    # connect to the database
    con = psycopg2.connect(
        host = input_host,
        database = input_database,
        user = input_user,
        password = input_password)
    
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    con.close()


# main part executing functions
df = csv_to_df(path_to_file=path_to_file)

row_count = len(df.index)
col_count = get_col_count(df)
col_names = reformat_col_names(df)

query_table = create_sql_query_table(col_names,schema_table=schema_table)
run_sql_in_db(query_table)

row_number = 0
while row_number < row_count:
    col_data = reformat_df_to_list(df, col_count,row_number)
    query_row_data = create_sql_query_adding_data(col_data, schema_table=schema_table)
    run_sql_in_db(query_row_data)
    print("Row " + str(row_number) + " Uploaded")
    row_number += 1



# next to do
# while loop percentage completion
# graphical user interface
# improve saving creds info
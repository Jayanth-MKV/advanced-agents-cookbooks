import pandas as pd
import sqlite3

# File paths
people_file = './data/preprocessed_people_info.csv'
event_file = './data/preprocessed_event_info.csv'
company_file = './data/preprocessed_company_info.csv'

# Load data
people_df = pd.read_csv(people_file)
event_df = pd.read_csv(event_file)
company_df = pd.read_csv(company_file)

# Create a connection to the SQLite database
conn = sqlite3.connect('./event_company_people.db')
cursor = conn.cursor()

# Function to create table and insert data
def create_table(cursor, table_name, df):
    df.to_sql(table_name, conn, if_exists='replace', index=False)

# Create tables
create_table(cursor, 'people', people_df)
create_table(cursor, 'events', event_df)
create_table(cursor, 'companies', company_df)

# Commit and close the connection
conn.commit()
conn.close()
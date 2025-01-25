from langchain_community.utilities import SQLDatabase
def connectToDB(uri:str):
    db = SQLDatabase.from_uri(uri)
    # print(db.dialect)
    # print(db.get_usable_table_names())
    # print(db.get_context())
    table_names = db.get_usable_table_names()
    columns_data = db.get_table_info(table_names)
    # print(columns_data)
    return db,columns_data

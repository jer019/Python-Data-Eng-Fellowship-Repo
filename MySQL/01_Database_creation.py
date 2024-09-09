import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('E:\\Bytewise\\First Month ETL project\\Bank_Rankings.csv')

db = mysql.connector.connect(
    host='localhost',
    user="Rangar",
    passwd="rangar019",
    database="Banks_DB"
)

cursor = db.cursor()

create_table_query = """
CREATE TABLE Banks_Rankings (
    `Rank` INT PRIMARY KEY,
    `Bank_Name` VARCHAR(255),
    `Total_Assets` DECIMAL(20,2)
)
"""

cursor.execute(create_table_query)
db.commit()


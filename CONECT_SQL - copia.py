import pandas as pd
import janitor
from sqlalchemy import create_engine
import urllib.parse

df = pd.read_csv("PROYECTOS/Online_Retail_LIMPIO.csv")

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate']) 
df['TotalRevenue'] = df['Quantity'] * df['UnitPrice']
df['DateOnly'] = df['InvoiceDate'].dt.date
df['Year'] = df['InvoiceDate'].dt.year
df['Month'] = df['InvoiceDate'].dt.month
df['Hour'] = df['InvoiceDate'].dt.hour

print(df.head())

servidor = r'.\SQLEXPRESS'
base_de_datos = 'BASED'


params = urllib.parse.quote_plus(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={servidor};'
    f'DATABASE={base_de_datos};'
    f'Trusted_Connection=yes;'
    f'TrustServerCertificate=yes;'
)
engine = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')

try:
    df.to_sql('ventas_retail_master', con=engine, if_exists='replace', index=False)
    print("🔱 ¡ÉPICO! Los datos ya están en tu SQL Express.")
except Exception as e:
    print(f"❌ Error al conectar: {e}")
import pandas as pd
import janitor
from sqlalchemy import create_engine
import urllib.parse

df = pd.read_csv("PROYECTOS/MOCK_DATA_SQL.csv")
 
df["Promedio de antiguedad"] = df["antiguedad_meses"].mean()
df["Categoria de antiguedad"] = df["antiguedad_meses"].apply(lambda x: "Alta" if x > df["antiguedad_meses"].mean() else "Baja")
df["Promedio de salario"] = df["mon"].mean()
df["Categoria de salario"] = df["mon"].apply(lambda x: "Alto" if x > df["mon"].mean() else "Bajo")

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
    df.to_sql('analisis_empleados', con=engine, if_exists='replace', index=False)
    print("🔱 ¡ÉPICO! Los datos ya están en tu SQL Express.")
except Exception as e:
    print(f"❌ Error al conectar: {e}")
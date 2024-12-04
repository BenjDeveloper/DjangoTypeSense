# src/wait_for_db.py
import time
import psycopg2
from psycopg2 import OperationalError

def wait_for_db():
    print("Esperando la base de datos...")
    while True:
        try:
            conn = psycopg2.connect(
                dbname="ecommerce",
                user="user",
                password="password",
                host="db",
                port="5432"
            )
            conn.close()
            print("Base de datos disponible.")
            break
        except OperationalError:
            print("Base de datos no disponible, reintentando en 1 segundo...")
            time.sleep(1)

if __name__ == "__main__":
    wait_for_db()

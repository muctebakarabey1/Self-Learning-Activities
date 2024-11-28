import mysql.connector as con
import pandas as pd

# Veritabanı bağlantısını oluştur
db_connection = con.connect(
    host="localhost",
    user="root",
    password="355355",
    database="new_schema",
)

# Bağlantı başarılıysa mesaj ver
if db_connection.is_connected():
    print("Bağlantı başarılı!")

# Cursor oluştur
cursor = db_connection.cursor()

# INSERT sorgusu
sql_query = """
    INSERT INTO employees (EmployeeID, FirstName, LastName, Department, Salary, Email)
    VALUES
        (11, 'Muhammed', 'Elci', 'IT', 2344, 'kara34@hotmail.com'),
        (13, 'Ali', 'Kara', 'Marketing', 232344, 'kar3445534@hotmail.com')
"""

try:
    # Veriyi ekle
    cursor.execute(sql_query)
    # Değişiklikleri kaydet
    db_connection.commit()

    print("Veriler başarıyla eklendi.")
except Exception as e:
    # Hata durumunda rollback yap
    db_connection.rollback()
    print(f"Hata oluştu: {e}")

# Verileri sorgulama
try:
    cursor.execute("SELECT FirstName FROM employees")
    data = cursor.fetchall()  # Verileri al

    print("Veriler:")
    for row in data:
        print(row)

except Exception as e:
    print(f"Sorgu hatası: {e}")

# Bağlantıyı kapat
db_connection.close()
cursor.close()

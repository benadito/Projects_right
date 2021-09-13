import psycopg2
conn = psycopg2.connect("host=localhost port=5433 user=postgres password=1234")
cursor = conn.cursor()

# cursor.execute("""
 #    INSERT INTO hw_200 VALUES (0, 1.1, 2.2);

# """)
# conn.commit()


cursor.execute("""
    select * from hw_200;
""")
result = cursor.fetchall()


for register in result:
    print(register)


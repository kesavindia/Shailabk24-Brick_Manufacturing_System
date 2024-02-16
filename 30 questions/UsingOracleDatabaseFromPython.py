import cx_Oracle

# Connect to the Oracle database
conn = cx_Oracle.connect('kesavindia/password1@localhost')
cursor = conn.cursor()

# Execute the query
cursor.execute("SELECT * FROM emp")

# Fetch all rows
rows = cursor.fetchall()

# print(rows)
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()

def update_rows(empno):
    conn = cx_Oracle.connect('kesavindia/password1@localhost')
    cursor = conn.cursor()

    # Use a bind variable for the parameter in the SQL statement
    sql = "UPDATE emp SET sal = sal + 1000 WHERE empno = empno"

    args = {'empno': empno}  # Create a dictionary with the parameter value

    try:
        cursor.execute(sql,args)
        conn.commit()
        print("1 row updated...")
    except:
        print("error")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


# Get empno from user input
x = int(input("Enter empno: "))

# Call the function
update_rows(x)

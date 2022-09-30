import sqlite3

con = sqlite3.connect('mycompany2.db')
cObj = con.cursor()

# If table is not created than only create a table
cObj.execute("CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY, name TEXT, salary REAL, department TEXT, position TEXT)")
con.commit()

# Creating functions to insert values


def insert_value(id, name, salary, department, position):
    cObj.execute("INSERT INTO employees VALUES(?, ?, ?, ?, ?)",
                 (id, name, salary, department, position))
    con.commit()

# Updating a department


def update_department(department, id):
    cObj.execute("UPDATE employees SET deparment = ? WHERE id = ?",
                 (department, id))
    con.commit()

# fetching data here selecting everything from the table


def sql_fetch():
    cObj.execute("SELECT * FROM employees")
    con.commit()

# Deleting from the table


def delete_all():
    cObj.execute("DELETE FROM employees")
    con.commit()


def delete_with_id(id):
    cObj.execute("DELETE FROM employees WHERE id = ?", (id))
    con.commit()


# executing the functions
insert_value(1, "Ashish", 80000, "Physics", "Scientist")
insert_value(2, "Amit", 90000, "Army", "Captain")


cObj.close()
con.close()

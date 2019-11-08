import sqlite3
from Employee import Employee

conn = sqlite3.connect('employee.db')  #memory

c = conn.cursor()

# c.execute("""CREATE TABLE employees('
#             first text,
#             last text,
#             pay integer
#             ) """)


emp_1 = Employee('Lrae', 'Sexy', 60000)
emp_2 = Employee('Rizza', 'Yang', 65000)


# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
# conn.commit()

# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
# conn.commit()


c.execute("SELECT * FROM employees WHERE last=?", ('Pogi', ))
print(c.fetchall())

c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Sexy'})
print(c.fetchall())



# c.fetchmany(3)
# c.fetchone()


conn.commit()
conn.close()

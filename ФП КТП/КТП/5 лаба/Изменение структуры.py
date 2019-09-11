import sqlite3
c = sqlite3.connect("myDataBase.db")
cu = c.cursor()
sql = """ALTER TABLE Score
         ADD COLUMN Phone VARCHAR(12); """
cu.execute(sql)
c.commit()
cu.execute("SELECT * FROM Score")
row2 = cu.fetchmany(20)
print(row2)

c.close()

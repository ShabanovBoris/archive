import sqlite3
c = sqlite3.connect("myDataBase.db")
cu = c.cursor()
sql = """
UPDATE Score 
SET Shop_assistant  = 'Меньшиков В.А' 
WHERE NumBuy = '1'
"""
 
cu.execute(sql)
c.commit()
cu.execute("SELECT * FROM Score")
row2 = cu.fetchmany(20)
print(row2)

c.close()

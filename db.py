import sqlite3
conn = sqlite3.connect('test.db')
sql = ''' CREATE TABLE epl_table(
 
  team TEXT,
  week INTEGER, 
  win INTEGER,
  draw INTEGER,
  loss INTEGER,
  f INTEGER,
  a INTEGER,
  gd INTEGER,
  pts INTEGER
)'''
c = conn.cursor()
c.execute('SELECT * FROM epl_table')

for row in c:
  print row
# c = conn.cursor()
# c.execute(sql)
# conn.commit()
'''
Database for tracking some sensors.
'''

import sqlite3
connection = sqlite3.connect('my_project.db')
c = connection.cursor()

#Table creation
#c.execute('CREATE TABLE sensors (sensor_id integer PRIMARY KEY, sensor_type text NOT NULL, \
#sensor_name text NOT NULL UNIQUE, installation_date datetime)')

#c.execute('DELETE FROM sensors')
#c.execute('DROP TABLE sensors')

#INSERTs
#c.execute('\
#INSERT INTO sensors\
#(sensor_id, sensor_type, sensor_name, installation_date)\
#VALUES (2, "soil", "Charlie", 10-3-2018)')

#Printing SELECT query
c.execute('SELECT * FROM sensors')
all_rows = c.fetchall()
print('1):', all_rows)

connection.commit()


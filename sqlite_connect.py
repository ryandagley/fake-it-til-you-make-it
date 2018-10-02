'''
Database for tracking some sensors.
'''

import sqlite3
connection = sqlite3.connect('my_project.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE sensors (sensor_id integer PRIMARY KEY, sensor_type text NOT NULL, \
sensor_name text NOT NULL UNIQUE, installation_date datetime)')

#cursor.execute('DELETE FROM sensors')
#cursor.execute('DROP TABLE sensors')
connection.commit()
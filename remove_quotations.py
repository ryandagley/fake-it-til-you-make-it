#I had a .csv with many double-quotes in it.  I didn't want them.
#This opens the file, reads it, replaces double quotes with nothing,
#then writes it to a different file.

with open(r'c:\Download.csv', 'r') as in_file, open(r'c:\Download_no_quote.csv', 'w') as out_file:
    data = in_file.read()
    data = data.replace('"', '')
    out_file.write(data)
